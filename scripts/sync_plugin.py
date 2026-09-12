"""Apply a GitHub-verified UTF-8 repository snapshot to a local Codex plugin.

Network access belongs to the authenticated GitHub connector. No token is read
or stored here. Snapshot schema and the heartbeat runbook are in SYNC.md.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tempfile

REPOSITORY = 'zhiqiangliu0920/collart-ai-knowledge'
PLUGIN = 'plugins/collart-data-assistant/'
MANIFEST = PLUGIN + '.codex-plugin/plugin.json'
SKIP = {'.git', '__pycache__', 'node_modules', '.venv'}


def digest(content):
    return hashlib.sha256(content.encode('utf-8')).hexdigest()


def safe_path(root, name):
    parts = PurePosixPath(name).parts
    if not parts or name.startswith('/') or '\\' in name or ':' in name or any(p in {'.', '..', '.git'} for p in parts):
        raise ValueError(f'Unsafe repository path: {name}')
    current = root
    for part in parts:
        current = current / part
        if current.is_symlink() or (hasattr(current, 'is_junction') and current.is_junction()):
            raise ValueError(f'Linked path is not a sync target: {name}')
    resolved = current.resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError(f'Path escaped target: {name}')
    return current


def file_text(path):
    return path.read_text(encoding='utf-8-sig')


def inventory(root):
    result = {}
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if any(part in SKIP for part in rel.parts) or p.suffix in {'.pyc', '.zip'} or not p.is_file():
            continue
        safe_path(root, rel.as_posix())
        result[rel.as_posix()] = digest(file_text(p))
    return result


def changes(expected, actual):
    return sorted(k for k in expected.keys() | actual.keys() if expected.get(k) != actual.get(k))


def load_snapshot(path):
    data = json.loads(path.read_text(encoding='utf-8'))
    if data.get('repository') != REPOSITORY or not re.fullmatch(r'[0-9a-f]{40}', data.get('commit', '')):
        raise ValueError('Unexpected repository or commit')
    files = {}
    for item in data['files']:
        name, content = item['path'], item['content']
        safe_path(Path.cwd(), name)
        if name in files or not isinstance(content, str):
            raise ValueError(f'Duplicate path or non-text content: {name}')
        blob = content.encode('utf-8')
        actual = hashlib.sha1(b'blob ' + str(len(blob)).encode() + b'\0' + blob).hexdigest()
        if actual != item['sha']:
            raise ValueError(f'Git blob hash mismatch: {name}')
        if Path(name).name.startswith('.env') or Path(name).suffix in {'.pem', '.key', '.p12', '.pfx'} or 'service-accounts' in PurePosixPath(name).parts:
            raise ValueError(f'Credential file rejected: {name}')
        if re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{30,}|\bAIza[0-9A-Za-z_-]{30,}', content):
            raise ValueError(f'Credential pattern rejected: {name}')
        files[name] = content
    for required in [MANIFEST, '.agents/plugins/marketplace.json', PLUGIN+'scripts/kb.py', PLUGIN+'knowledge/INDEX.md']:
        if required not in files:
            raise ValueError(f'Required file missing: {required}')
    if json.loads(files[MANIFEST]).get('name') != 'collart-data-assistant':
        raise ValueError('Plugin identity changed')
    return data['commit'], files


def run(command):
    proc = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=90)
    if proc.returncode:
        raise RuntimeError(f'Command failed ({proc.returncode}): {command[0]}: {proc.stderr[-1500:]} {proc.stdout[-1500:]}')
    return proc.stdout


def configured_plugin(root):
    payload = json.loads(run(['codex', 'plugin', 'list', '--json']))
    entries = [p for p in payload['installed'] if p['pluginId'] == 'collart-data-assistant@personal']
    if len(entries) != 1 or not entries[0].get('enabled'):
        raise RuntimeError('Expected plugin is missing or disabled; do not reinstall automatically')
    entry = entries[0]
    expected = (root / PLUGIN).resolve()
    if entry.get('source', {}).get('source') != 'local' or Path(entry['source']['path']).resolve() != expected:
        raise RuntimeError('Configured plugin source differs from the sync target')
    return entry


def check_cache(root, state_root, version):
    codex_root = Path(os.environ.get('CODEX_HOME') or Path.home()/'.codex')
    cache = codex_root/'plugins/cache/personal/collart-data-assistant'/version
    if not cache.is_dir():
        raise RuntimeError('Installed plugin cache does not exist')
    mismatch = changes(inventory(root/PLUGIN), inventory(cache))
    if mismatch:
        raise RuntimeError(f'Installed cache differs from source: {mismatch}')
    return str(cache)


def write_json(path, value):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    temp.replace(path)


def status(root, state_root):
    state = json.loads((state_root/'state.json').read_text(encoding='utf-8'))
    dirty = changes(state['files'], inventory(root))
    result = {'commit': state.get('commit'), 'local_changes': dirty, 'version': state.get('version')}
    if not dirty and state.get('version'):
        entry = configured_plugin(root)
        if entry['version'] != state['version']:
            raise RuntimeError('Installed version differs from the last synchronized version')
        result['cache'] = check_cache(root, state_root, state['version'])
    return result


def apply_snapshot(root, state_root, snapshot_path, helpers):
    commit, files = load_snapshot(snapshot_path)
    previous = json.loads((state_root/'state.json').read_text(encoding='utf-8'))
    dirty = changes(previous['files'], inventory(root))
    if dirty:
        raise RuntimeError(f'Unpublished local changes preserved; publish or reconcile them first: {dirty}')
    configured_plugin(root)
    if previous.get('commit') == commit:
        result = status(root, state_root)
        return {'status': 'unchanged', **result}
    # A changed marketplace needs explicit source reconciliation, not a silent rewrite.
    if json.loads(files['.agents/plugins/marketplace.json']) != json.loads(file_text(root/'.agents/plugins/marketplace.json')):
        raise RuntimeError('Marketplace definition changed; inspect and configure it with Codex CLI first')
    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    backup = state_root/'backups'/stamp
    backup.mkdir(parents=True)
    old_content = {name: safe_path(root, name).read_bytes() for name in previous['files']}
    for name, content in old_content.items():
        dest = safe_path(backup, name)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(content)
    old_state = (state_root/'state.json').read_bytes()
    (backup/'sync-state.json').write_bytes(old_state)
    mutated = False
    with tempfile.TemporaryDirectory(prefix='stage-', dir=state_root) as temp:
        stage = Path(temp)
        if not stage.resolve().is_relative_to(state_root.resolve()):
            raise ValueError('Staging directory escaped the local sync state directory')
        for name, content in files.items():
            dest = safe_path(stage, name)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding='utf-8', newline='\n')
        check = json.loads(run([sys.executable, '-B', str(stage/(PLUGIN+'scripts/kb.py')), 'check']))
        if check.get('errors'):
            raise RuntimeError('Knowledge structure validation failed')
        # Use the supported helper, then reinstall through Codex; never edit cache files.
        marketplace = run([sys.executable, '-B', str(helpers/'read_marketplace_name.py'), '--marketplace-path', str(root/'.agents/plugins/marketplace.json')]).strip()
        if marketplace != 'personal':
            raise RuntimeError('Unexpected marketplace')
        run([sys.executable, '-B', str(helpers/'update_plugin_cachebuster.py'), str(stage/PLUGIN)])
        run([sys.executable, '-B', str(helpers/'validate_plugin.py'), str(stage/PLUGIN)])
        try:
            # Repeat the conflict check immediately before changing any tracked file.
            if changes(previous['files'], inventory(root)):
                raise RuntimeError('Local content changed during validation')
            mutated = True
            for name in files:
                dest = safe_path(root, name)
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(stage/name, dest)
            for name in previous['files'].keys()-files.keys():
                safe_path(root, name).unlink()
            version = json.loads(file_text(root/MANIFEST))['version']
            run(['codex', 'plugin', 'add', 'collart-data-assistant@personal', '--json'])
            entry = configured_plugin(root)
            if entry['version'] != version:
                raise RuntimeError('Plugin installation did not advance to the expected version')
            cache = check_cache(root, state_root, version)
            next_state = {'repository':REPOSITORY, 'commit':commit, 'version':version, 'files':inventory(root), 'remote_files':{p:digest(c) for p,c in files.items()}, 'cache':cache, 'updated_at':stamp, 'backup':str(backup), 'knowledge_check':check}
            write_json(state_root/'state.json', next_state)
            return {'status':'updated', 'commit':commit, 'version':version, 'cache':cache, 'files':len(files), 'backup':str(backup), 'knowledge_check':check}
        except Exception as original:
            if mutated:
                for name in files.keys()-old_content.keys():
                    dest = safe_path(root, name)
                    if dest.is_file():
                        dest.unlink()
                for name, content in old_content.items():
                    dest = safe_path(root, name)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(content)
                (state_root/'state.json').write_bytes(old_state)
                try:
                    # The install command can update config before returning an error.
                    run(['codex', 'plugin', 'add', 'collart-data-assistant@personal', '--json'])
                except Exception as rollback:
                    raise RuntimeError(f'Source restored; reinstall rollback failed: {rollback}; original failure: {original}') from original
            raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['init', 'status', 'apply'])
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--state-root', type=Path, default=Path.home()/'.codex/collart-knowledge-sync')
    parser.add_argument('--snapshot', type=Path)
    parser.add_argument('--helpers', type=Path, default=Path.home()/'.codex/skills/.system/plugin-creator/scripts')
    args = parser.parse_args()
    root, state_root = args.root.resolve(), args.state_root.resolve()
    if not (root/MANIFEST).is_file() or state_root.is_relative_to(root):
        raise ValueError('Expected a plugin distribution root and separate local state directory')
    state_root.mkdir(parents=True, exist_ok=True)
    lock = state_root/'sync.lock'
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.close(descriptor)
    try:
        if args.command == 'init':
            if (state_root/'state.json').exists():
                raise RuntimeError('Sync state already exists; do not overwrite its baseline')
            entry = configured_plugin(root)
            write_json(state_root/'state.json', {'repository':REPOSITORY, 'commit':None, 'version':entry['version'], 'files':inventory(root)})
            result = {'status':'initialized', 'files':len(inventory(root))}
        elif args.command == 'status':
            result = status(root, state_root)
        else:
            if not args.snapshot:
                raise ValueError('--snapshot is required for apply')
            result = apply_snapshot(root, state_root, args.snapshot, args.helpers)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    finally:
        lock.unlink()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(json.dumps({'status':'blocked', 'error':str(error)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1)
