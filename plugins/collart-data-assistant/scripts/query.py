#!/usr/bin/env python3
"""Generate bounded read-only SQL. No credentials, network or database execution."""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

PRODUCTS = {
    'collart_android': ('storytemplate-10a27.analytics_232977577.events_*', 'free.ai.photo.generator.collart.ai'),
    'collart_ios': ('vidart-8b8ca.analytics_528583115.events_*', 'ai.photo.video.generator.fotos.ai.image.picture.editor.app.free'),
    'collart_web': ('storytemplate-10a27.analytics_232977577.events_*', None),
    'collart_fashion': ('storytemplate-10a27.analytics_232977577.events_*', None),
}

def today():
    return dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).date()

def window(start=None, end=None, include_today=False, now=None):
    now = now or today()
    upper = now if include_today else now - dt.timedelta(days=1)
    lower = upper - dt.timedelta(days=6)
    start = dt.date.fromisoformat(start) if isinstance(start,str) else start or lower
    end = dt.date.fromisoformat(end) if isinstance(end,str) else end or upper
    if not lower <= start <= end <= upper:
        raise ValueError('Raw events must stay inside the latest seven days; historical seven-day windows are forbidden')
    return start, end

def raw_events(project, start=None, end=None, include_today=False, now=None, limit=30):
    if project not in PRODUCTS or not 1 <= limit <= 100:
        raise ValueError('Invalid project or output limit')
    start,end = window(start,end,include_today,now)
    table,bundle = PRODUCTS[project]
    predicate = f"e.app_info.id = '{bundle}'" if bundle else 'e.app_info.id IS NULL'
    extra = ''
    if project == 'collart_ios':
        extra += "\n    AND IFNULL(e.app_info.install_source, '') != 'manual_install'"
    if bundle is None:
        page = "(SELECT p.value.string_value FROM UNNEST(e.event_params) p WHERE p.key = 'page_location' LIMIT 1)"
        # Null/missing pages stay unclassified. Main site is not a synonym for every non-app event.
        extra += f"\n    AND {page} IS NOT NULL"
        extra += f"\n    AND {'NOT ' if project == 'collart_web' else ''}REGEXP_CONTAINS(LOWER({page}), r'studio|fashion')"
        extra += "\n    AND (e.user_id IS NULL OR e.user_id NOT IN UNNEST(@internal_user_ids))"
        # Missing or invalid exclusions fail at query evaluation rather than silently leaking into statistics.
        extra += "\n    AND IF(ARRAY_LENGTH(@internal_user_ids) > 0 AND NOT EXISTS (SELECT 1 FROM UNNEST(@internal_user_ids) id WHERE id IS NULL), TRUE, ERROR('Supply a nonempty authorized internal_user_ids list without NULL'))"
    sql = f"""-- Read only. Asia/Shanghai; {'today included, incomplete and finalized export only' if include_today else 'complete business days'}.
-- Metadata/schema and actual product event definitions must be checked before execution.
SELECT e.event_name, COUNT(*) AS pv, COUNT(DISTINCT e.user_pseudo_id) AS uv
FROM `{table}` e
WHERE _TABLE_SUFFIX BETWEEN '{start:%Y%m%d}' AND '{end:%Y%m%d}'
    AND {predicate}{extra}
GROUP BY e.event_name
ORDER BY pv DESC, e.event_name
LIMIT {limit};
"""
    return dict(project=project,start=str(start),end=str(end),sql=sql,parameters={'internal_user_ids':'ARRAY<STRING>; authorized, nonempty, no NULL, no duplicates'} if bundle is None else {},policy='Read only; raw data within latest 7 days; no batching older dates')

def tokens(sql):
    """Lex outside strings/comments. Reject unterminated constructs rather than ignoring them."""
    i=0;out=[]
    while i<len(sql):
        if sql.startswith('--',i):
            n=sql.find('\n',i);i=len(sql) if n<0 else n+1;continue
        if sql.startswith('/*',i):
            n=sql.find('*/',i+2)
            if n<0:raise ValueError('Unterminated comment')
            i=n+2;continue
        if sql[i] in "'\"`":
            q=sql[i];triple=sql.startswith(q*3,i) and q!='`';end=q*3 if triple else q;i+=len(end)
            while i<len(sql):
                if sql[i]=='\\':i+=2;continue
                if sql.startswith(end,i):
                    i+=len(end)
                    if not triple and i<len(sql) and sql[i]==q:i+=1;continue
                    break
                i+=1
            else:raise ValueError('Unterminated SQL literal')
            out.append('LITERAL');continue
        m=re.match(r'[A-Za-z_][A-Za-z_0-9]*',sql[i:])
        if m:out.append(m[0].upper());i+=len(m[0]);continue
        if not sql[i].isspace():out.append(sql[i])
        i+=1
    return out

def read_only(sql):
    ts=tokens(sql)
    if not ts or ts[0] not in {'SELECT','WITH'}:raise ValueError('Only a single SELECT/WITH SELECT is accepted')
    forbidden={'INSERT','UPDATE','DELETE','MERGE','TRUNCATE','CREATE','ALTER','DROP','CALL','EXPORT','GRANT','REVOKE','EXECUTE','BEGIN','COMMIT','ROLLBACK','DECLARE','SET','INTO','EXTERNAL_QUERY'}
    if set(ts)&forbidden:raise ValueError('Write/script/external operation rejected')
    if ';' in ts[:-1]:raise ValueError('Multiple statements rejected')
    return True

def main():
    p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='command',required=True)
    raw=s.add_parser('raw-events');raw.add_argument('--project',choices=PRODUCTS,required=True);raw.add_argument('--start');raw.add_argument('--end');raw.add_argument('--include-today',action='store_true');raw.add_argument('--limit',type=int,default=30)
    lint=s.add_parser('lint');lint.add_argument('file',type=Path)
    a=p.parse_args()
    if a.command=='raw-events':r=raw_events(a.project,a.start,a.end,a.include_today,limit=a.limit);read_only(r['sql'])
    else:
        sql=a.file.read_text(encoding='utf-8-sig');read_only(sql)
        if re.search(r'\bevents_\*|\.dm_collart_\w+_user_event_di|\.dwd_oper_user_event',sql,re.I):raise ValueError('Raw date/product predicates require explicit review; use raw-events generator for standard discovery')
        r={'read_only_syntax':True,'execution_authorized':False,'note':'Static syntax check only; schema, functions, dates, product, parameters and permissions still require review'}
    print(json.dumps(r,ensure_ascii=False,separators=(',',':')))
if __name__=='__main__':
    try:main()
    except (ValueError,OSError) as e:print(json.dumps({'error':str(e)},ensure_ascii=False));sys.exit(2)
