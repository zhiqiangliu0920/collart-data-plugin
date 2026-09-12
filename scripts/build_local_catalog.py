"""Build local navigation from the audited file inventory; does not edit original facts."""
import argparse,collections,csv,json,os,re
from pathlib import Path
from urllib.parse import quote

def build(root,audit):
    data=json.loads(audit.read_text(encoding='utf-8'));rows=data['files'];out=root/'catalog';out.mkdir(exist_ok=True)
    def save(name,text):
        p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text+'\n',encoding='utf-8')
    def link(row,depth=1):
        if row['source']!='ai-knowledge':return '`'+row['id']+'`'
        return '['+row['path'].replace('[','').replace(']','')+']('+quote('../'*depth+row['path'],safe='/._-')+')'
    business=[r for r in rows if r['source']=='ai-knowledge' and r['status']!='excluded']
    projects=sorted({r['project'] for r in business}|{'company','collart_android','collart_ios','collart_web','collart_fashion','shared'})
    kinds=sorted({r['kind'] for r in business})
    intro=['# 知识库结构化总目录','','整理基于全文静态扫描、目录核对与重点口径交叉检查；不是本次生产数据验证。凭证和个人状态只列路径边界。每个普通文本文件的完整扫描结果可在台账 JSON 中复查。','', '[逐文件分析](FILE_REGISTER.md) · [完整台账 CSV](files.csv) · [表名与多版本](TABLES.md) · [问题与待处理](REVIEW.md)','', '## 按项目']
    for project in projects:intro.append(f'- [{project}](projects/{project}.md)')
    intro+=['','## 按内容类型']+[f'- [{k}](types/{k}.md)' for k in kinds]
    intro+=['','## 分层维护','', '| 层 | 维护方式 |','|---|---|','| 原始业务资料 | 原项目目录维护；保留历史原文和日期 |','| 统一目录 | 本目录自动生成，修正正文后重新构建 |','| 统一主题知识 | 插件 knowledge 中的带来源条目；冲突不自动晋升 |','| 全文资料 | 插件 library 中的独立副本与来源图 |','| 待处理和排除 | 原件保留，按路径与哈希记录原因 |','', '旧包正文在 ai-project 下，插件由三个输入持续构建。索引、发布副本与插件缓存不反向收录。']
    save('README.md','\n'.join(intro))
    def tabular(items,depth):
        lines=['| 文件 | 类型 | 状态 | 原日期 | 内容与处理 |','|---|---|---|---|---|']
        for r in items:
            text=(r['summary'] or r['reason']).replace('|','/').replace('\n',' ')[:240]
            lines.append('| '+' | '.join([link(r,depth),r['kind'],r['status'],', '.join(r['dates'][-3:]) or '未标明',text])+' |')
        return '\n'.join(lines)
    for project in projects:
        items=[r for r in business if r['project']==project]
        save(f'projects/{project}.md',f'# {project} 文件与知识入口\n\n共 {len(items)} 份。日期列来自正文，不代表本次验证日期。\n\n'+tabular(items,2))
    for kind in kinds:
        items=[r for r in business if r['kind']==kind]
        save(f'types/{kind}.md',f'# {kind} 入口\n\n共 {len(items)} 份。历史 SQL 必须重新核对日期、表、粒度和权限；不会自动执行。\n\n'+tabular(items,2))
    details=['# 逐文件内容分析','','全文扫描覆盖三个来源；下方展开 ai-knowledge 的业务文件。Git 对象、凭证、运行配置和派生产物逐文件列在 [完整台账](files.csv)，不展开秘密或个人内容。两个旧包也在同一 CSV / JSON 中逐项列出。','']
    for r in business:
        details+=['## '+r['path'],'',link(r),'',f"用途：{r['title']}。分类：{r['project']} / {r['kind']}。状态：{r['status']}。",'',r['summary'] or r['reason'],'',f"处理：{r['reason']}",f"正文日期：{', '.join(r['dates']) or '原文未注明；不能用文件时间推定生效日期'}",f"内容结构：{'；'.join(r['headings'][:14]) or '无章节标题'}",f"引用表：{', '.join(r['tables']) or '未提取到全限定表名'}"]
        profile=r.get('content_analysis',{})
        if profile:details+=['静态检查：'+json.dumps(profile,ensure_ascii=False)]
        if r['issues']:details+=['待处理：'+'；'.join(r['issues'])]
        if r['transforms']:details+=['发布转换：'+'；'.join(r['transforms'])]
        if r.get('duplicate_of'):details+=['重复来源：'+r['duplicate_of']]
        details+=['SHA-256：`'+str(r['sha256'])+'`','']
    save('FILE_REGISTER.md','\n'.join(details))
    with (out/'files.csv').open('w',encoding='utf-8-sig',newline='') as f:
        fields=['id','source','path','bytes','sha256','project','kind','status','reason','title','summary','dates','tables','issues','transforms']
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        for r in rows:writer.writerow({k:json.dumps(r[k],ensure_ascii=False) if isinstance(r[k],list) else r[k] for k in fields})
    # Table identity is grouped, never resolved by modification time alone.
    tables=collections.defaultdict(list)
    for row in business:
        if row['kind']=='table':
            name=re.search(r'\b(?:aidata2025|pubdata2025|storytemplate-10a27|vidart-8b8ca)\.[\w]+\.[\w*]+',row['title'])
            if name:tables[name.group()].append(row)
    lines=['# 表名、版本与字段入口','','按正文表名归组；同表多文档并不代表同日期、同粒度或同业务规则。2026-05-21 生成字典保留为历史字段快照。','']
    for table,items in sorted(tables.items()):
        lines+=['## '+table,'']
        for r in items:lines+=[f"- {link(r)} — {r['status']}；{', '.join(r['dates'][-3:]) or '无日期'}"]
        if len(items)>1:lines+=['- 多版本保留；优先查看业务维护文档及适用日期，存在差异时核对任务源码与现网字段。']
        lines+=['']
    save('TABLES.md','\n'.join(lines))
    review=['# 整理发现与待核对事项','','2026-09-12 文档整理。以下事实是对本地材料的观察，不代表已修复数仓。','',
    '1. **入口与实际目录不一致**：已修复根目录及 Android/Web 的 company、metrics、analysis、lineage 链接；补全 iOS、Fashion 与公司入口。原文改动均有本机备份。',
    '2. **Fashion 分成两个目录**：统一维护到 collart_fashion；带空格目录保留兼容 Junction。同名收入表两版均保留，旧版在 history/2026-09-09。',
    '3. **旧表字典被埋在生成目录**：完整字段字典纳入表名索引及插件。complete/available 是 2026-05-21 导出状态，不能据此断定今天仍可用。',
    '4. **收入与购买人数不是同一指标**：2026-08-24 purchase_uv 是订阅和点数包用户并集；俄罗斯 Stripe 收入不必体现在客户端 purchase_uv。Fashion 新用户文档中的 orders 关联与 2026-09-07 收入红线不同，保留旧方法但不可用于默认现网收入。',
    '5. **iOS 历史“数据集为空”与新版 ADS 文档冲突**：已修正 README 的无条件结论，保留历史原文；ASA 旧 DWS 成本与新 cdct 标准需按报表粒度选择和对账。',
    '6. **DAU、PV/UV、日期窗口易混用**：Android DAU 正文已明确优先加工表，与旧入口 session_start 公式冲突。SQL 条件聚合的 COUNTIF 是次数，去重用户必须使用 DISTINCT。日报收入/留存对比用 T-2 和 T-9～T-3，其余指标用 T-1 和 T-8～T-2，不能共用不完整的 6 天均值。',
    '7. **静态历史报告需要保留边界**：Fashion 仓库审计是 2026-09-09 的问题快照；同日后续表改动可能已解决部分问题。Web 收入报告是 2026-09-12 生成、实际统计 09-04～09-10，不能当成 09-05～09-11。',
    '8. **混入其他项目与临时查询**：Vibedance、fx-editor 归入 other_projects；临时探查代码不进入默认插件资料。历史脚本与 SQL 仅作为证据，不因被检索而执行。',
    '9. **敏感内容与损坏正文**：疑似凭证的旧脚本整份拦截；大批用户 ID SQL 留在本机；测试 ID 集中配置，已复核示例占位替换。含替换字符的 Web DWD 文档和 CHANGELOG 无法通过转码恢复，保留原件待找回来源。',
    '10. **SQL 双命名版本**：sql_best_practices 与 sql-best-practices 内容不同，保持原文并补充关系说明；没有按文件名相似度删除或覆盖。','', '## 每份异常记录','', '| 文件 | 状态 | 原因 / 问题 |','|---|---|---|']
    for row in business:
        if row['issues'] or row['status']=='pending':review.append('| '+link(row)+' | '+row['status']+' | '+(row['reason']+'；'+'；'.join(row['issues'])).replace('|','/')+' |')
    review+=['','## 尚未找到的相对引用','']
    for row in business:
        for l in row['links']:
            if not l['exists']:review.append('- '+row['path']+' → `'+l['target']+'`。不创建空白内容冒充原证据。')
    save('REVIEW.md','\n'.join(review))
    return {'catalog_files':len(list(out.rglob('*'))),'business_files':len(business),'tables':len(tables),'projects':projects,'source_counts':dict(collections.Counter(r['source'] for r in rows))}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,required=True);p.add_argument('--audit',type=Path,required=True);a=p.parse_args();print(json.dumps(build(a.root,a.audit),ensure_ascii=False,indent=2))
