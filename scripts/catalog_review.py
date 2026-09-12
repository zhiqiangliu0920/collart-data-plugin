"""Local navigation and complete before/after ledger; excluded bodies are not read."""
import argparse,collections,csv,hashlib,json,re,zipfile
from pathlib import Path
from urllib.parse import quote
import knowledge_registry

def read(path,default):return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default
def clean(s):return str(s or '').replace('|',' / ').replace('\n',' ').replace('\r',' ')
def token(ident):return hashlib.sha256(ident.encode()).hexdigest()[:20]
def build(root,audit,evidence=None):
    root=root.resolve();rows=read(audit,{})['files'];out=root/'catalog';out.mkdir(exist_ok=True)
    if evidence is None:
        saved=read(out/'evidence-location.json',{})
        if saved.get('path'):evidence=Path(saved['path'])
    if evidence:(out/'evidence-location.json').write_text(json.dumps({'path':str(evidence.resolve())}),encoding='utf-8',newline='\n')
    registry,_=knowledge_registry.load(root);byid={r['id']:r for r in registry.values()}
    before=read(evidence/'baseline/files.json',[]) if evidence else []
    mapping=read(evidence/'migration-map.json',{}) if evidence else {}
    moves=mapping.get('moves',{});merges=mapping.get('merges',{})
    deep={r['path']:r for r in read(evidence/'deep-review-before.json',[])} if evidence else {}
    diffs={r['path']:r['diff'] for r in read(evidence/'body-diff-index.json',[])} if evidence else {}
    local={r['path']:r for r in rows if r['source']=='ai-knowledge'}
    def save(name,body):
        p=out/name;p.parent.mkdir(parents=True,exist_ok=True);body=body.rstrip()+'\n'
        if not p.exists() or p.read_text(encoding='utf-8')!=body:p.write_text(body,encoding='utf-8',newline='\n')
    def link(r,depth=1):return '['+clean(r['path']).replace('[','').replace(']','')+']('+quote('../'*depth+r['path'],safe='/._-')+')'
    def states(r):return ' / '.join([r.get('status','excluded'),r.get('business_status','未评定'),r.get('review_status','boundary_only')])
    business=[r for r in rows if r['source']=='ai-knowledge' and r.get('sha256')]
    existing={r['id'] for r in business}
    for path,rec in registry.items():
        if rec['id'] not in existing:
            row={**local.get(path,{}),**rec};row.update(source='ai-knowledge',project=rec['scope'],sha256=rec['reviewed_sha256']);business.append(row)
    business.sort(key=lambda r:r['id'])
    def table(items,depth=1):
        lines=['| 文件 | 收录 / 业务 / 复核 | 内容与结论 | 审阅 |','|---|---|---|---|']
        for r in items:lines.append('| '+' | '.join([link(r,depth),states(r),clean(r.get('summary') or r.get('reason')),'[详情]('+('../'*(depth-1))+'reviews/'+token(r['id'])+'.md)'])+' |')
        return '\n'.join(lines)
    def group(items,depth=1):
        current=lambda r:r.get('business_status')=='documented' and r.get('review_status')=='reviewed_static'
        groups=[('正式维护入口',[r for r in items if current(r)]),('历史与废弃资料',[r for r in items if r.get('business_status') in {'historical','deprecated'}]),('待核对与边界',[r for r in items if not current(r) and r.get('business_status') not in {'historical','deprecated'}])]
        return '\n\n'.join('## '+name+'\n\n'+table(part,depth) for name,part in groups if part)
    for row in business:
        rec=byid.get(row['id'],{});old=rec.get('original_path',row['path']);profile=deep.get(old,{})
        issues=list(dict.fromkeys(row.get('issues',[])+rec.get('open_issues',[])))
        lines=['# '+row['path'],'',link(row,2),'',
          '- 持久标识：`'+row['id']+'`','- 原路径：`'+old+'`','- 当前位置：`'+row['path']+'`',
          '- 状态（收录 / 业务 / 复核）：'+states(row),
          '- 内容审阅：'+rec.get('content_review_status','完成静态内容审阅' if profile.get('review_method','').startswith('full_') else '边界登记'),
          '- 处置：'+rec.get('disposition','retain')+'；'+row.get('reason',''),
          '- 原业务日期：'+(rec.get('effective_date') or '以原文标记与统计窗口为准；未确定生效日'),
          '- 产品范围：'+row.get('project',rec.get('scope','shared')),
          '- 方法：'+rec.get('review_method',profile.get('review_method','boundary_inventory'))+'；未执行源码、未查询生产。',
          '- 当前 SHA-256：`'+str(row.get('sha256'))+'`',
          '- 审阅绑定 SHA-256：`'+str(rec.get('reviewed_sha256'))+'`','',
          '## 核心知识、用途与结论','',row.get('summary') or rec.get('summary') or row.get('reason',''),'',
          '## 处置依据与限制','']
        lines+=['- '+n for n in dict.fromkeys(rec.get('review_notes',[]))] or ['- 保留原日期和适用范围，文档依据不能替代现网验证。']
        if issues:lines+=['','## 待处理','']+['- '+clean(n) for n in issues]
        lines+=['','## 来源与引用关系','', '- 路径别名：'+', '.join('`'+s+'`' for s in rec.get('aliases',[]))]
        if evidence and (evidence/'backup'/old).is_file():lines.append('- [整理前原件](<'+(evidence/'backup'/old).as_posix()+'>)')
        if evidence and row['path'] in diffs:lines.append('- [正文修改差异](<'+(evidence/diffs[row['path']]).as_posix()+'>)')
        for ref in row.get('links',[]):lines.append('- `'+ref['target']+'`：'+('存在' if ref['exists'] else '本地未找到；保留待处理'))
        if rec.get('disposition')!='exclude' and profile.get('analysis'):
            a=profile['analysis'];lines+=['','## 全文静态审阅证据','',f"原文件共 {profile.get('whole_file_lines','未记录')} 行。以下按全部章节、SQL、AST 或完整数据结构记录证据；不是生产运行结果。",'']
            if 'sections' in a:
                facts=collections.defaultdict(list)
                for f in a.get('facts',[]):facts[f['section']].append(f['evidence'])
                for section in a['sections']:
                    lines+=['### '+section['heading'],'']+(facts.get(section['heading']) or ['本节为导航、背景或一般说明，原文从文件链接读取。'])+['']
                if a.get('sql_blocks'):lines+=['### 全部 SQL 的输入、输出、过滤和副作用','', '```json',json.dumps(a['sql_blocks'],ensure_ascii=False,indent=2),'```']
            else:lines+=['```json',json.dumps(a,ensure_ascii=False,indent=2),'```']
        if row.get('transforms'):lines+=['','## 发布转换','']+['- '+x for x in row['transforms']]
        save('reviews/'+token(row['id'])+'.md','\n'.join(lines))
    projects=sorted({r.get('project','shared') for r in business});kinds=sorted({r.get('kind','local') for r in business})
    for project in projects:save('projects/'+project+'.md','# '+project+' 资料\n\n'+group([r for r in business if r.get('project')==project],2))
    for kind in kinds:save('types/'+kind+'.md','# '+kind+' 入口\n\n'+group([r for r in business if r.get('kind')==kind],2))
    save('FILE_REGISTER.md','# 逐文件审阅台账\n\n业务候选逐项链接到全文结构证据与内容结论。审阅完成与处理结果分别记录；问题已被审阅，不代表事实冲突已解决。[所有文件 CSV](files.csv) 包含隐藏文件和边界；[迁移追溯](MIGRATIONS.md) 连接原路径与现位置。\n\n'+group(business))
    tables=collections.defaultdict(list)
    for r in business:
        if r.get('kind')=='table':
            name=re.search(r'(?:aidata2025|pubdata2025|storytemplate-10a27|vidart-8b8ca)\.[\w]+\.[\w*]+',r.get('title','')) or re.search(r'(?:aidata2025|pubdata2025)\.[\w]+\.[\w*]+',Path(r['path']).stem)
            if name:tables[name.group()].append(r)
    save('TABLES.md','# 表名与版本目录\n\n同名表按日期、粒度和业务状态分别展示，不按文件修改时间覆盖。\n\n'+'\n\n'.join('## '+name+'\n\n'+table(sorted(items,key=lambda r:r.get('business_status')!='documented')) for name,items in sorted(tables.items())))
    save('SQL.md','# SQL、SQLX 与工具\n\n日期写死、未限定产品、生成 DML、BigQuery/CLI 调用等限制见逐份审阅。历史源码不会因收录而执行。\n\n'+group([r for r in business if r.get('kind') in {'sql','lineage','script'}]))
    save('TOPICS.md','# 主题入口\n\n'+'\n'.join('- ['+k+'](types/'+k+'.md)' for k in kinds)+'\n\n[表与版本](TABLES.md) · [SQL](SQL.md) · [待处理](REVIEW.md)')
    problems=[r for r in business if r.get('review_status')=='needs_review' or r.get('issues') or byid.get(r['id'],{}).get('open_issues')]
    broken=[{'source':r['id'],'path':r['path'],'target':ref['target']} for r in business for ref in r.get('links',[]) if not ref['exists']]
    save('REVIEW.md','# 待处理清单\n\n本清单是文件审阅结果，未重新查询生产。编码损坏、表身份和业务冲突均保留原件；不补造字段、金额或生效日期。\n\n'+table(problems)+'\n\n## 未找到的引用\n\n'+'\n'.join('- `'+r['path']+'` → `'+r['target']+'`；原证据未找到。' for r in broken))
    save('pending.json',json.dumps({'items':[{'id':r['id'],'path':r['path'],'summary':r.get('summary'),'reason':r.get('reason'),'issues':list(dict.fromkeys(r.get('issues',[])+byid.get(r['id'],{}).get('open_issues',[])))} for r in problems],'broken_references':broken},ensure_ascii=False,indent=2))
    complete=[]
    for b in before:
        old=b['path'];target=moves.get(old,merges.get(old,old));r=local.get(target,{});rec=registry.get(target,{})
        complete.append({'original_path':old,'current_path':target,'original_sha256':b.get('sha256'),'current_sha256':r.get('sha256'),'type':b.get('type','file'),'link_target':b.get('target',''),'id':rec.get('id',r.get('id','ai-knowledge:'+old)),
          'disposition':'merge' if old in merges else ('move' if old in moves else rec.get('disposition','exclude' if r.get('status')=='excluded' else 'retain')),
          'reason':rec.get('exclusion_reason') or r.get('reason') or deep.get(old,{}).get('reason','原位保留；个人配置不变'),
          'content_review_status':rec.get('content_review_status','边界登记' if not deep.get(old,{}).get('sha256') else '完成静态内容审阅'),
          'review_status':rec.get('review_status','boundary_only'),'business_status':rec.get('business_status','not_applicable')})
    def writecsv(name,items,fields):
        with (out/name).open('w',encoding='utf-8-sig',newline='') as f:
            wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader()
            for item in items:wr.writerow({k:json.dumps(item.get(k),ensure_ascii=False) if isinstance(item.get(k),(dict,list)) else item.get(k) for k in fields})
    writecsv('before_after.csv',complete,list(complete[0]) if complete else ['original_path','current_path'])
    writecsv('files.csv',rows,['id','source','path','sha256','bytes','project','kind','status','business_status','review_status','summary','reason','issues','aliases'])
    save('MIGRATIONS.md','# 迁移与恢复映射\n\n[全部迁移前后记录](before_after.csv) 覆盖初始基线，备份、正文差异与 Git 未提交修改存放在本机同步状态目录。\n\n| 原路径 | 当前路径 | 处理 |\n|---|---|---|\n'+'\n'.join('| `'+r['original_path']+'` | `'+r['current_path']+'` | '+r['disposition']+' |' for r in complete if r['disposition'] in {'move','merge'}))
    archives=[]
    for rel in sorted({r['path'] for r in rows if r['source']=='ai-knowledge' and r['path'].lower().endswith('.zip')}):
        try:
            with zipfile.ZipFile(root/rel) as z:archives.append({'path':rel,'policy':'仅登记目录，不解压或循环收录','entries':[{'path':i.filename,'bytes':i.file_size,'crc':i.CRC} for i in z.infolist()]})
        except (OSError,zipfile.BadZipFile) as e:archives.append({'path':rel,'error':type(e).__name__})
    save('archives.json',json.dumps(archives,ensure_ascii=False,indent=2))
    stats={'inventory_files':len(rows),'baseline_items':len(before),'baseline_dispositions':len(complete),'review_cards':len(business),'moves':len(moves),'merges':len(merges),'tables':len(tables),'pending_cards':len(problems),'broken_references':len(broken),'source_counts':dict(collections.Counter(r['source'] for r in rows))}
    save('coverage.json',json.dumps(stats,ensure_ascii=False,indent=2))
    save('README.md','# 知识库结构化总目录\n\n公司与四端顶层目录保留。正式定义、历史报告、旧字典、SQL 和运行边界分别维护；全文静态审阅不表示本次验证了生产状态。\n\n[逐文件审阅](FILE_REGISTER.md) · [全文件清单](files.csv) · [迁移映射](MIGRATIONS.md) · [主题](TOPICS.md) · [表与版本](TABLES.md) · [SQL](SQL.md) · [待处理](REVIEW.md)\n\n## 项目\n\n'+'\n'.join('- ['+p+'](projects/'+p+'.md)' for p in projects)+'\n\n## 维护\n\n正式正文在原项目维护；表 tables、指标 indicators、产品 product、加工 lineage、方法 analysis_playbooks、模板 sql_presets。报告 reports/原日期/主题 与 SQL/证据一起保留；旧资料 history/原日期，日期未知为 undated。\n\n持久标识及别名见 0global/knowledge_registry.json。内容变化后旧复核失效；收录、业务有效性、复核分开。凭证、个人偏好、原始用户明细及输出目录不进入插件。')
    return stats
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--audit',type=Path,required=True);p.add_argument('--evidence',type=Path);a=p.parse_args();print(json.dumps(build(a.root,a.audit,a.evidence),ensure_ascii=False,indent=2))
