#!/usr/bin/env python3
"""Build only the canonical 0.5 knowledge, never re-import 0.4 folders."""
import argparse, hashlib, importlib.util, json, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[1]
PLUGIN=ROOT/'plugins/collart-data-assistant'
SKIP={'.git','__pycache__','.pytest_cache'}

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def release_files(root):
    files=[]
    allowed={'.agents','.github','maintainer','plugins','scripts','tests','.gitattributes','.gitignore','README.md','INSTALL.md','SYNC.md','CHANGELOG.md','install.ps1'}
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root)
        if not p.is_file() or any(x in SKIP for x in rel.parts) or p.suffix=='.pyc':continue
        if rel.parts[0] not in allowed:raise ValueError('Unapproved release entry: '+rel.as_posix())
        if rel.as_posix()=='maintainer/release-files.json':continue
        if p.is_symlink() or not p.resolve().is_relative_to(root.resolve()):raise ValueError('Linked/outside file: '+rel.as_posix())
        files.append({'path':rel.as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    return files

def validate(root):
    plugin=root/'plugins/collart-data-assistant';kb=module('kb',plugin/'scripts/kb.py');query=module('query',plugin/'scripts/query.py')
    result=kb.check(plugin);errors=result['errors'];catalog=list(kb.documents(plugin));sources=kb.load(plugin,'_meta/sources.json')['sources']
    for project in ['collart_android','collart_ios','collart_web','collart_fashion']:
        for kind in ['business','table','event','metric','playbook']:
            if not any(r['project']==project and r['kind']==kind for r in catalog):errors.append('Missing project/category: '+project+'/'+kind)
    refs={s for r in catalog for s in r['sources']};source_ids={s['id'] for s in sources}
    for s in sources:
        if s['id'] not in refs and not set(s.get('referenced_by',[])) & refs:errors.append('Unreferenced source: '+s['id'])
        if not re.fullmatch('[a-f0-9]{64}',s.get('sha256','')):errors.append('Invalid hash: '+s['id'])
        if s.get('origin')=='query_template':
            try:query.read_only((plugin/s['path']).read_text(encoding='utf-8'))
            except ValueError as e:errors.append(s['id']+': '+str(e))
        if s.get('origin')=='dataform' and s.get('outputs'):
            missing=[t for t in s['outputs'] if not any(r['kind']=='table' and t in r['tables'] for r in catalog)]
            if missing:errors.append('SQLX has no output dictionary: '+s['id'])
    for r in catalog:
        if r['kind']!='table':continue
        table=r['tables'][0];schema_id='schema:'+table;s=next((s for s in sources if s['id']==schema_id),None)
        if not s:errors.append('Table has no schema capture/status: '+table);continue
        d=kb.load(plugin,s['path']);fields=d.get('schema',{}).get('fields',[])
        def walk(fs,prefix=''):
            for f in fs:yield prefix+f['name'];yield from walk(f.get('fields',[]),prefix+f['name']+'.')
        for name in walk(fields):
            if f'| `{name}` |' not in r['text']:errors.append('Lost field: '+table+'.'+name)
        if d.get('error') and r['status'] not in {'historical','deprecated'}:errors.append('Unavailable table marked current: '+table)
    package_allowed={'.codex-plugin','skills','scripts','knowledge','sources','_meta','config','README.md'}
    for p in plugin.iterdir():
        if p.name not in package_allowed:errors.append('Unapproved package entry: '+p.name)
    for p in plugin.rglob('*'):
        if p.is_file() and (p.name.startswith('.env') or p.suffix in {'.pem','.key','.p12','.pfx','.csv','.parquet','.db','.zip'}):errors.append('Sensitive/runtime file: '+p.name)
    registered={s['path'] for s in sources if s.get('path')}
    for folder in [plugin/'sources',plugin/'knowledge']:
        for p in folder.rglob('*'):
            if p.is_file() and (folder.name=='sources' or p.suffix=='.sql') and p.relative_to(plugin).as_posix() not in registered:errors.append('Unregistered source/template: '+p.name)
    # Current documentation links must resolve; archived historical notes are not navigation.
    for p in root.rglob('*.md'):
        rel=p.relative_to(root)
        if any(x in SKIP for x in rel.parts) or rel.as_posix().startswith('maintainer/history/'):continue
        prose=re.sub(r'```.*?```','',p.read_text(encoding='utf-8-sig'),flags=re.S)
        for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',prose):
            target=target.strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):continue
            dest=(p.parent/unquote(target.split('#',1)[0])).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():errors.append(rel.as_posix()+': broken/outside link '+target)
    # Executable SQL is either registered SELECT templates or an explicitly marked expression.
    for p in (plugin/'knowledge').rglob('*.md'):
        for sql in re.findall(r'```sql\s*\n([\s\S]*?)```',p.read_text(encoding='utf-8')):
            try:query.read_only(sql)
            except ValueError as e:errors.append(p.name+': invalid inline SQL: '+str(e))
            if re.search(r'\bevents_\*|\.dm_collart_\w+_user_event_di|\.dwd_oper_user_event',sql,re.I):errors.append(p.name+': inline raw SQL must use the bounded generator')
    for removed in ['build_local_catalog.py','catalog_layout.py','catalog_review.py','knowledge_registry.py','source_pipeline.py']:
        if (root/'scripts'/removed).exists():errors.append('Old source importer remains: '+removed)
    result['release_files']=len(release_files(root));return result

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--check',action='store_true');a=p.parse_args();root=a.root.resolve();plugin=root/'plugins/collart-data-assistant'
    if 'plugins/cache' in root.as_posix().lower():raise ValueError('Do not build inside installed cache')
    kb=module('kb',plugin/'scripts/kb.py')
    if not a.check:kb.index(plugin)
    result=validate(root);manifest=root/'maintainer/release-files.json';expected={'schema_version':2,'files':release_files(root)}
    if a.check:
        if not manifest.exists() or json.loads(manifest.read_text(encoding='utf-8'))!=expected:result['errors'].append('Release inventory stale')
    elif not result['errors']:manifest.write_text(json.dumps(expected,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,ensure_ascii=False,separators=(',',':')));return int(bool(result['errors']))
if __name__=='__main__':sys.exit(main())
