#!/usr/bin/env python3
"""Structured Collart knowledge. Standard library, no network or database execution."""
import argparse, hashlib, json, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT=Path(__file__).resolve().parents[1]
KINDS={'business','table','event','metric','playbook','policy'}
POLICY='只读；原始埋点仅最近 7 天，禁止拆批读取更早日期。SQLX 仅供理解加工逻辑，不能执行。'
def emit(v):print(json.dumps(v,ensure_ascii=False,separators=(',',':')))
def inside(root,relative):
    p=(root/relative).resolve()
    if not p.is_relative_to(root.resolve()):raise ValueError('Path leaves plugin root')
    return p
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(root,p,default=None):
    p=inside(root,p)
    return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default
def parse(p):
    parts=p.read_text(encoding='utf-8-sig').split('---\n',2)
    if len(parts)!=3 or parts[0]:raise ValueError('Missing metadata: '+p.name)
    m={}
    for line in parts[1].splitlines():
        if line.strip():
            k,sep,v=line.partition(':')
            if not sep or k in m or not re.fullmatch('[a-z_]+',k):raise ValueError('Invalid metadata')
            m[k]=json.loads(v)
    return m,parts[2].strip()
def encode(m,b):return '---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in m.items())+'\n---\n\n'+b.strip()+'\n'
def paths(root):return sorted((p for p in (root/'knowledge').rglob('*.md') if p.name not in {'README.md','INDEX.md'}),key=lambda p:p.relative_to(root).as_posix())
def documents(root):
    for p in paths(root):
        inside(root,p.relative_to(root));m,b=parse(p)
        yield dict(m,path=p.relative_to(root).as_posix(),sha256=sha(p),text=b)
def sections(body):
    rows=[];fenced=False;lines=body.splitlines(keepends=True)
    for i,line in enumerate(lines):
        if line.lstrip().startswith('```'):fenced=not fenced;continue
        m=re.match(r'^(#{1,6})\s+(.+)',line)
        if m and not fenced:rows.append({'heading':m[2].strip(),'level':len(m[1]),'start_line':i+1})
    for i,h in enumerate(rows):h['end_line']=next((x['start_line']-1 for x in rows[i+1:] if x['level']<=h['level']),len(lines))
    return rows
def artifacts(root):
    rows=list(documents(root))
    return {'_meta/catalog.json':{'schema_version':2,'entries':[{k:v for k,v in r.items() if k!='text'} for r in rows]}}
def index(root):
    data=artifacts(root)
    for name,value in data.items():
        p=inside(root,name);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value,ensure_ascii=False,separators=(',',':'))+'\n',encoding='utf-8',newline='\n')
    return {'written':list(data),'documents':len(data['_meta/catalog.json']['entries'])}
def search_rows(root,project=None,kind=None):
    # The distributed index contains metadata only. Read canonical prose locally,
    # after project/type routing, instead of distributing a second full-text copy.
    data=load(root,'_meta/catalog.json',{});entries=data.get('entries',[]);files={p.relative_to(root).as_posix():p for p in paths(root)}
    if data.get('schema_version')!=2 or set(files)!={r['path'] for r in entries} or any(sha(files[r['path']])!=r['sha256'] for r in entries):return list(documents(root)),'live_fallback'
    return [dict(r,text=parse(files[r['path']])[1]) for r in entries if allowed(r,project) and (not kind or r['kind']==kind)],'current'
def allowed(r,project):return not project or r['project'] in {project,'shared'} or project in r.get('applies_to',[])
def snippet(body,words):
    lines=body.splitlines();candidates=[(sum(w in line.casefold() for w in words),i,line.strip()) for i,line in enumerate(lines) if line.strip() and not line.startswith('#')]
    _,i,text=max(candidates,key=lambda x:(x[0],-x[1]),default=(0,0,''));offset=max(0,min([text.casefold().find(w) for w in words if w in text.casefold()],default=0)-40)
    return {'text':text[offset:offset+180],'section':next((h['heading'] for h in reversed(sections(body)) if h['start_line']<=i+1),None)}
def search(root,a):
    if not 1<=a.limit<=50 or not a.query.strip():raise ValueError('Invalid query/limit')
    raw=a.query.casefold().strip();rules=load(root,'config/search-routing.json',{});intents=[r for r in rules.get('intents',[]) if any(x.casefold() in raw for x in r['aliases'])]
    words=list(dict.fromkeys(w.casefold() for r in intents for w in r['terms'])) if intents else raw.split()
    rows,state=search_rows(root,a.project,a.kind);hits=[]
    for r in rows:
        if not allowed(r,a.project) or (a.kind and a.kind!=r['kind']):continue
        if r['status'] in {'historical','deprecated','draft'} and not a.include_history:continue
        title=r['title'].casefold();tags=' '.join(r.get('tags',[])+r.get('tables',[])+r.get('aliases',[])).casefold();body=r['text'];text=title+' '+tags+' '+body.casefold();matches=[w for w in words if w in text]
        if not matches or (not intents and len(matches)!=len(words)):continue
        score=sum(22*(w in title)+16*(w in tags)+2*(w in body.casefold()) for w in matches)
        if raw in [t.casefold() for t in r.get('tables',[])]:score+=500 if r['kind']=='table' else 70
        score+=sum(x.get('boosts',{}).get(r['id'],0) for x in intents)
        hit={k:r[k] for k in ['id','title','project','kind','status','path']};hit.update(score=score,snippet=snippet(body,words),review_required=r.get('review_required',False));hits.append(hit)
    hits.sort(key=lambda r:(-r['score'],r['id']))
    return {'results':hits[:a.limit],'matches':len(hits),'index_state':state}
def resolve(root,ident):
    alias=load(root,'_meta/aliases.json',{}).get(ident,{})
    if alias.get('archived'):return {'archived':True,'reason':alias['reason'],'migration':'仓库 maintainer/migration.json'},None
    ident=alias.get('id',ident);entries=load(root,'_meta/catalog.json',{}).get('entries',[])
    found=[e for e in entries if ident in {e['id'],e['path'],*e.get('aliases',[]),*e.get('tables',[])}]
    if len(found)>1:found=[e for e in found if e['kind']=='table']
    if len(found)==1:
        r=found[0];p=inside(root,r['path']);m,b=parse(p);return dict(m,path=r['path'],index_stale=sha(p)!=r['sha256']),b
    source=[s for s in load(root,'_meta/sources.json',{}).get('sources',[]) if ident in {s['id'],s.get('path')}]
    if len(source)==1:
        s=source[0]
        if not s.get('path'):return dict(s,title=s['id'],kind='source',status=s.get('state','source')),json.dumps(s,ensure_ascii=False,indent=2)
        p=inside(root,s['path'])
        if sha(p)!=s['sha256']:raise ValueError('Source integrity check failed')
        return dict(s,title=s.get('title',s['path']),kind='source',status=s.get('state','source')),p.read_text(encoding='utf-8-sig')
    live=[r for r in documents(root) if ident in {r['id'],r['path']}]
    if len(live)==1:return live[0],live[0]['text']
    raise ValueError('Unknown/ambiguous knowledge or source ID')
def read(root,a):
    if not 1<=a.max_chars<=20000 or a.offset<0:raise ValueError('Invalid output bound')
    if a.section and (a.start_line or a.end_line):raise ValueError('Choose section or lines')
    m,body=resolve(root,a.id)
    if body is None:return m
    headings=sections(body);lines=body.splitlines(keepends=True);start,end=a.start_line if a.start_line is not None else 1,a.end_line if a.end_line is not None else len(lines)
    if a.section:
        hs=[h for h in headings if h['heading'].casefold()==a.section.casefold()] or [h for h in headings if a.section.casefold() in h['heading'].casefold()]
        if len(hs)!=1:raise ValueError('Unknown/ambiguous section; use --toc')
        start,end=hs[0]['start_line'],hs[0]['end_line']
    if start<1 or end<start or end>len(lines):raise ValueError('Invalid line range')
    selected=''.join(lines[start-1:end])
    if a.field:
        if a.section or a.start_line or a.end_line:raise ValueError('Field and section/lines are mutually exclusive')
        selected=''.join(line for line in lines if re.search(r'^\|\s*`?'+re.escape(a.field)+r'`?\s*\|',line))
        if not selected:raise ValueError('Field absent from dictionary')
        guard=next((h for h in headings if '使用边界' in h['heading']),None)
        if guard:selected+='\n'+''.join(lines[guard['start_line']-1:guard['end_line']])
    if a.offset>len(selected):raise ValueError('Offset exceeds selection')
    remaining=selected[a.offset:];out=remaining if a.full else remaining[:a.max_chars]
    r={k:m[k] for k in ['id','title','project','kind','status','path','review_required','index_stale'] if k in m};r.update(body=out,policy=POLICY,truncated=len(out)<len(remaining),next_offset=a.offset+len(out) if len(out)<len(remaining) else None,sources=m.get('sources',[])[:6])
    if a.toc:r['headings']=headings
    return r
def check(root):
    errors=[];rows=list(documents(root));seen=set();sources=load(root,'_meta/sources.json',{}).get('sources',[]);source_ids={s['id'] for s in sources}
    if len(source_ids)!=len(sources):errors.append('Duplicate source IDs')
    for r in rows:
        if not r.get('id') or r['id'] in seen:errors.append('Invalid/duplicate knowledge ID')
        seen.add(r['id'])
        if r.get('kind') not in KINDS:errors.append('Invalid kind: '+r['id'])
        if r.get('project') not in {'shared','company','collart_android','collart_ios','collart_web','collart_fashion'}:errors.append('Invalid project')
        if not r.get('sources') or set(r['sources'])-source_ids:errors.append('Unknown/missing source: '+r['id'])
        if r.get('status')=='verified' and not r.get('verification_evidence'):errors.append('Unsubstantiated verification')
        if r.get('status') not in {'documented','verified','historical','deprecated','draft'}:errors.append('Invalid status: '+r['id'])
        if not r['text'].startswith('# '):errors.append('Missing title: '+r['id'])
    for s in sources:
        if s.get('path'):
            p=inside(root,s['path'])
            if not p.is_file() or sha(p)!=s['sha256']:errors.append('Changed/missing source: '+s['id'])
    for alias,r in load(root,'_meta/aliases.json',{}).items():
        if r.get('id') and r['id'] not in seen:errors.append('Missing alias target: '+alias)
    for name,expected in artifacts(root).items():
        if load(root,name)!=expected:errors.append('Stale index: '+name)
    if (root/'_meta/search-index.json').exists():errors.append('Full-text distribution copy is forbidden; use metadata catalog')
    forbidden={'private key':r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----','personal path':r'[A-Za-z]:[\\/]Users[\\/]','webhook':r'https://[^\s]+/open-apis/bot/v2/hook/','credential':r'(?i)(?:app_secret|api_key|access_token)\s*[:=]\s*[\"\x27][^\"\x27\s]{12,}[\"\x27]','token':r'\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AIza[0-9A-Za-z_-]{30,})'}
    for p in root.rglob('*'):
        if not p.is_file() or p.suffix not in {'.md','.sql','.sqlx','.js','.json','.yaml','.txt'}:continue
        rel=p.relative_to(root).as_posix();text=p.read_text(encoding='utf-8-sig')
        for label,pattern in forbidden.items():
            if re.search(pattern,text):errors.append(rel+': '+label)
        if p.suffix=='.md':
            prose=re.sub(r'```.*?```','',text,flags=re.S)
            for t in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',prose):
                t=t.strip('<>')
                if urlsplit(t).scheme or t.startswith('#'):continue
                if not inside(root,p.parent.relative_to(root)/unquote(t.split('#',1)[0])).exists():errors.append(rel+': broken link '+t)
    for old in ['library','presets','provenance','catalog.json','search-index.json']:
        if (root/old).exists():errors.append('Legacy structure remains: '+old)
    return {'errors':errors,'documents':len(rows),'sources':len(sources),'counts':{k:sum(r['kind']==k for r in rows) for k in sorted(KINDS)}}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--authoring',action='store_true');sub=p.add_subparsers(dest='command',required=True)
    s=sub.add_parser('search');s.add_argument('query');s.add_argument('--project');s.add_argument('--kind',choices=sorted(KINDS));s.add_argument('--limit',type=int,default=3);s.add_argument('--include-history',action='store_true');s.add_argument('--scope',choices=['auto','topics','materials','all'],default='auto',help='0.4 alias; searches structured knowledge')
    r=sub.add_parser('read');r.add_argument('id');r.add_argument('--section');r.add_argument('--field');r.add_argument('--start-line',type=int);r.add_argument('--end-line',type=int);r.add_argument('--offset',type=int,default=0);r.add_argument('--max-chars',type=int,default=2800);r.add_argument('--full',action='store_true');r.add_argument('--toc',action='store_true')
    sub.add_parser('check');sub.add_parser('index');a=p.parse_args();root=a.root.resolve()
    if a.command=='index':
        if not a.authoring or '--root' not in sys.argv:raise ValueError('Index writes require --authoring and explicit --root')
        if 'plugins/cache' in root.as_posix().casefold():raise ValueError('Installed cache is not an authoring workspace')
        if not (root/'.codex-plugin/plugin.json').is_file():raise ValueError('Not a plugin root')
        emit(index(root))
    elif a.command=='check':r=check(root);emit(r);return int(bool(r['errors']))
    elif a.command=='search':emit(search(root,a))
    elif a.command=='read':emit(read(root,a))
    return 0
if __name__=='__main__':
    try:sys.exit(main())
    except (ValueError,OSError,KeyError,TypeError) as e:emit({'error':str(e)});sys.exit(2)
