#!/usr/bin/env python3
"""Detect source changes and queue affected canonical knowledge. Never copy old folders."""
import argparse, hashlib, importlib.util, json, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[1]

def dependency_map(plugin,catalog):
    """Follow explicit knowledge links and physical lineage until impact is closed."""
    by_path={(plugin/r['path']).resolve():r['id'] for r in catalog}
    dependencies={r['id']:set() for r in catalog}
    by_table={t:r['id'] for r in catalog if r['kind']=='table' for t in r.get('tables',[])}
    coverage_path=plugin.parents[1]/'maintainer/table-coverage.json'
    coverage=json.loads(coverage_path.read_text(encoding='utf-8')) if coverage_path.exists() else {}
    for r in catalog:
        deps=dependencies[r['id']]
        deps.update(by_table[t] for t in r.get('tables',[]) if t in by_table)
        if r['kind']=='table':
            for t in r.get('tables',[]):deps.update(by_table[u] for u in coverage.get(t,{}).get('upstream',[]) if u in by_table)
        path=plugin/r['path'];body=path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',body):
            target=target.strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):continue
            dest=(path.parent/unquote(target.split('#',1)[0])).resolve()
            if dest in by_path:deps.add(by_path[dest])
    return dependencies

def dependent_documents(plugin,catalog,direct,dependencies=None):
    dependencies=dependency_map(plugin,catalog) if dependencies is None else dependencies
    affected=set(direct)
    while True:
        expanded=affected|{id for id,deps in dependencies.items() if deps & affected}
        if expanded==affected:return sorted(affected)
        affected=expanded

def detect(root,knowledge=None,capture=None):
    plugin=root/'plugins/collart-data-assistant';sources=json.loads((plugin/'_meta/sources.json').read_text(encoding='utf-8'))['sources'];catalog=json.loads((plugin/'_meta/catalog.json').read_text(encoding='utf-8'))['entries'];changes=[];checked=0
    incoming={s['id']:s for s in json.loads(capture.read_text(encoding='utf-8'))['sources']} if capture else {}
    dependencies=dependency_map(plugin,catalog)
    for s in sources:
        state=None;new_hash=None
        if s['origin']=='ai-knowledge' and knowledge:
            p=(knowledge/s['locator']).resolve()
            if not p.is_relative_to(knowledge.resolve()):raise ValueError('Source locator escaped knowledge root')
            checked+=1
            if not p.is_file():state='source_missing'
            else:
                new_hash=hashlib.sha256(p.read_bytes()).hexdigest()
                if new_hash!=s['sha256']:state='source_changed'
        elif capture and s['origin'] in {'dataform','bigquery_metadata','feishu'}:
            checked+=1;n=incoming.get(s['id'])
            if not n:state='not_in_new_capture'
            else:
                new_hash=n['sha256']
                if new_hash!=s['sha256'] or n.get('revision')!=s.get('revision'):state='source_changed'
        if state:
            direct={r['id'] for r in catalog if s['id'] in r['sources']}
            if s['origin']=='dataform' and not s.get('outputs'):
                direct.update(r['id'] for r in catalog if set(s.get('referenced_by',[])) & set(r['sources']))
            # Include metrics and methods referencing an affected physical table.
            tables={t for r in catalog if r['id'] in direct for t in r.get('tables',[])}
            direct.update(r['id'] for r in catalog if set(r.get('tables',[])) & tables)
            changes.append(dict(source=s['id'],status=state,old_sha256=s['sha256'],new_sha256=new_hash,documents=dependent_documents(plugin,catalog,direct,dependencies)))
    return {'schema_version':2,'checked':checked,'changes':changes}

def queue(root,result):
    plugin=root/'plugins/collart-data-assistant';path=root/'maintainer/review-queue.json';old=json.loads(path.read_text(encoding='utf-8')) if path.exists() else {'changes':[]}
    pending={c['source']:c for c in old['changes']}
    for c in result['changes']:pending[c['source']]=c
    # Rechecking an unchanged snapshot never erases an unresolved review.
    payload={'schema_version':2,'changes':sorted(pending.values(),key=lambda c:c['source'])};path.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    spec=importlib.util.spec_from_file_location('kb',plugin/'scripts/kb.py');kb=importlib.util.module_from_spec(spec);spec.loader.exec_module(kb)
    ids={id for c in payload['changes'] for id in c['documents']}
    for p in kb.paths(plugin):
        m,b=kb.parse(p)
        if m['id'] in ids:m['review_required']=True;m['review_reason']='upstream_source_changed';p.write_text(kb.encode(m,b),encoding='utf-8',newline='\n')
    kb.index(plugin)
    return len(ids)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--knowledge',type=Path);p.add_argument('--capture',type=Path,help='New source registry JSON, not credential config');p.add_argument('--queue',action='store_true');a=p.parse_args()
    if not (a.knowledge or a.capture):p.error('Provide --knowledge or --capture')
    root=a.root.resolve()
    if a.queue and 'plugins/cache' in root.as_posix().lower():raise ValueError('Installed cache is not an authoring workspace')
    r=detect(root,a.knowledge,a.capture)
    if a.queue:r['marked_documents']=queue(root,r)
    print(json.dumps(r,ensure_ascii=False,separators=(',',':')))
    return int(bool(r['changes']))
if __name__=='__main__':sys.exit(main())
