"""Track publication separately from installation. No network and no credentials."""
import argparse,hashlib,json
from pathlib import Path
from source_pipeline import prepare_changes,write_json
from sync_plugin import load_snapshot,inventory,changes

def prepare(state_root,stage,remote_snapshot,fingerprint):
    state=json.loads((state_root/'state.json').read_text(encoding='utf-8'))
    remote_commit,remote=load_snapshot(remote_snapshot)
    baseline=state.get('remote_files',state['files'])
    publication=state_root/'release-status.json'
    if publication.exists():
        release=json.loads(publication.read_text(encoding='utf-8'))
        if release['published_commit']!=state.get('commit'):
            _,published_files=load_snapshot(Path(release['snapshot']))
            baseline={p:hashlib.sha256(t.encode()).hexdigest() for p,t in published_files.items()}
    local=inventory(stage)
    # The installed cache suffix is local state, never a reason to publish.
    manifest='plugins/collart-data-assistant/.codex-plugin/plugin.json'
    local_manifest=json.loads((stage/manifest).read_text(encoding='utf-8'))
    remote_manifest=json.loads(remote[manifest])
    normalize=lambda v: {**v,'version':v['version'].split('+codex.',1)[0]}
    if normalize(local_manifest)==normalize(remote_manifest):local[manifest]=hashlib.sha256(remote[manifest].encode()).hexdigest()
    remote_hashes={p:hashlib.sha256(t.encode()).hexdigest() for p,t in remote.items()}
    updates,conflicts=prepare_changes(baseline,local,remote_hashes)
    # Publish only conflict-free changes; candidate conflicts remain separately reviewable.
    proposal={'base_commit':remote_commit,'source_fingerprint':fingerprint,'updates':sorted(updates),'conflicts':conflicts,'status':'review_required' if conflicts else ('ready' if updates else 'unchanged')}
    write_json(state_root/'release-proposal.json',proposal)
    return proposal

def published(state_root,snapshot,fingerprint):
    commit,_=load_snapshot(snapshot)
    value={'published_commit':commit,'published_source_fingerprint':fingerprint,'snapshot':str(snapshot.resolve()),'installation':'pending'}
    write_json(state_root/'release-status.json',value)
    return value

def installed(state_root):
    p=state_root/'release-status.json';release=json.loads(p.read_text(encoding='utf-8'));state=json.loads((state_root/'state.json').read_text(encoding='utf-8'))
    if release['published_commit']!=state['commit']:raise ValueError('Published commit is not installed')
    release.update(installation='installed',installed_commit=state['commit'],installed_version=state['version'])
    write_json(p,release);return release

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('command',choices=['prepare','published','installed']);p.add_argument('--state-root',type=Path,required=True);p.add_argument('--snapshot',type=Path);p.add_argument('--stage',type=Path);p.add_argument('--fingerprint');a=p.parse_args()
    if a.command=='prepare':result=prepare(a.state_root,a.stage,a.snapshot,a.fingerprint)
    elif a.command=='published':result=published(a.state_root,a.snapshot,a.fingerprint)
    else:result=installed(a.state_root)
    print(json.dumps(result,ensure_ascii=False,indent=2))
