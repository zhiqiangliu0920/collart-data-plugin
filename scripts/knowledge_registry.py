"""Stable source identity and hash-bound editorial decisions; no network or writes."""
import hashlib,json,re
from pathlib import Path,PurePosixPath

BUSINESS_STATES={'documented','historical','deprecated','uncertain'}
REVIEW_STATES={'reviewed_static','needs_review','boundary_only'}

def digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load(root,registry_path=None):
    path=Path(registry_path) if registry_path else Path(root)/'0global/knowledge_registry.json'
    if not path.exists():return {},{}
    data=json.loads(path.read_text(encoding='utf-8'))
    bypath={};identities=set();aliases={}
    for item in data['documents']:
        ident=item['id'];rel=item['path'];p=PurePosixPath(rel)
        if p.is_absolute() or '..' in p.parts or '\\' in rel or ':' in rel:raise ValueError('Unsafe registry path')
        if ident in identities or rel in bypath:raise ValueError('Duplicate registry identity/path')
        if item['business_status'] not in BUSINESS_STATES or item['review_status'] not in REVIEW_STATES:raise ValueError('Invalid editorial state')
        if not re.fullmatch('[0-9a-f]{64}',item['reviewed_sha256']):raise ValueError('Invalid reviewed source hash')
        identities.add(ident);bypath[rel]=item
        for alias in {ident,*item.get('aliases',[])}:
            if alias in aliases and aliases[alias]!=ident:raise ValueError('Ambiguous source alias')
            aliases[alias]=ident
    return bypath,aliases

def annotate(row,record):
    row.update(record_id=row['id'],aliases=[row['source']+':'+row['path']],business_status='historical' if row['status']=='historical' else 'uncertain',review_status='needs_review',reviewed_on=None)
    if not record:return row
    row['id']=record['id'];row['record_id']=record['id']
    row['aliases']=sorted(set([row['source']+':'+row['path'],*record.get('aliases',[])]))
    row['original_path']=record.get('original_path',record['id'].split(':',1)[-1])
    row['disposition']=record.get('disposition','retain')
    row['project']=record.get('scope',row['project'])
    matches=row['sha256']==record['reviewed_sha256']
    row['review_digest']=digest(record)
    if matches:
        for key in ['business_status','review_status','reviewed_on','summary','review_notes','effective_date','scope','replacement_ids','review_evidence','analysis_summary']:
            if key in record:row[key]=record[key]
        row['issues']=list(dict.fromkeys(row['issues']+record.get('open_issues',[])))
    else:
        row['business_status']='historical' if row['status']=='historical' else 'uncertain'
        row['review_status']='needs_review';row['issues'].append('正文变化后原审阅失效，需重新核对')
    return row

def source_fingerprint(rows):
    return digest([(r['id'],r['sha256'],r['status'],r.get('review_digest')) for r in sorted(rows,key=lambda r:r['id']) if r['sha256']])
