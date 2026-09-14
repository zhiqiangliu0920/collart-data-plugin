"""Offline CLI benchmark. Output belongs in an analysis project, not the plugin cache."""
import argparse
import json
from pathlib import Path
import statistics
import subprocess
import sys
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plugin-root', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--samples', type=int, default=5)
    args = parser.parse_args()
    if not 1 <= args.samples <= 30:
        parser.error('samples must be 1..30')
    root, output = args.plugin_root.resolve(), args.output.resolve()
    if output.is_relative_to(root):
        parser.error('write measurements outside the plugin')
    cases = {'default': ['search', '收入', '--project', 'collart_android'],
             'all': ['search', '收入', '--project', 'collart_android', '--scope', 'all'],
             'ad_button': ['search', '免费看广告', '--project', 'collart_android'],
             'ad_read': ['read', 'android-reward-ad-click']}
    samples = {k: [] for k in cases}
    results = {}
    for i in range(args.samples + 1):
        items = list(cases.items())
        for name, command in (items if i % 2 == 0 else items[::-1]):
            start = time.perf_counter()
            proc = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(root/'scripts/kb.py'), *command], capture_output=True, encoding='utf-8', check=True)
            elapsed = time.perf_counter() - start
            payload = json.loads(proc.stdout)
            if i:
                samples[name].append(elapsed)
            results[name] = {'output_chars': len(proc.stdout), 'ids': [r['id'] for r in payload.get('results', [])],
                             'body_chars': len(payload.get('body', '')), 'truncated': payload.get('truncated')}
    report = {'plugin_version': json.loads((root/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))['version'],
              'method': 'one warmup, alternating subsequent trials; local retrieval only',
              'billed_tokens': None, 'query_jobs': 0,
              'results': {k: {**results[k], 'samples_seconds': v, 'median_seconds': statistics.median(v)} for k, v in samples.items()}}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
