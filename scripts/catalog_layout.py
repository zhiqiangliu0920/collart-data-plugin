"""Route derived catalog documents to their owners; never copy business bodies.

Review ownership is navigation metadata. It does not change a source's original
scope, business status, review approval, or evidence date.
"""
from __future__ import annotations
import csv, hashlib, io, json, os, re
from pathlib import Path
from urllib.parse import quote, unquote

GLOBAL = '0global/catalog'
PRODUCTS = ('collart_android', 'collart_ios', 'collart_web', 'collart_fashion')
OWNERS = ('0global', '1company', *PRODUCTS)
LABELS = {'0global': '全局维护', '1company': '公司与跨产品', 'collart_android': 'Collart Android',
          'collart_ios': 'VidArt iOS', 'collart_web': 'Collart Web', 'collart_fashion': 'Fashion'}
LINK = re.compile(r'(?<!!)\[([^\]\n]+)\]\((<[^>]+>|[^)\n]+)\)')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def source_fields(text):
    def field(label):
        match = re.search(r'^- '+re.escape(label)+r'：(.*)$', text, re.M)
        return match.group(1).strip().strip('`') if match else ''
    ident = field('持久标识')
    if not ident:
        match = re.search(r'旧标识 `(ai-knowledge:[^`]+)`', text)
        ident = match.group(1) if match else ''
    path = field('当前位置') or ident.removeprefix('ai-knowledge:')
    return {'id': ident, 'path': path, 'project': field('产品范围')}

def owner(record):
    path = record.get('path', '').replace('collart_ fashion', 'collart_fashion')
    scope = record.get('project') or record.get('scope', '')
    # A specific recorded product can own an exported company table or a source
    # captured inside another product's audit. Keep that evidence relationship.
    if scope in PRODUCTS:
        return scope, '原文已记录明确产品；保留跨目录来源关系'
    if scope == 'other_projects':
        return '1company', '其他产品资料由公司层单列；不推定为存放目录所属产品'
    if path.startswith('1company/') or scope == 'company':
        return '1company', '公司共用、跨端或归属未确定的导出资料；未确定范围继续保留'
    for product in PRODUCTS:
        if path.startswith(product+'/'):
            return product, '按报告或工具的实际维护项目归类；原 shared 标记仍保留为来源元数据'
    return '0global', '知识维护、共用规范或全局导航'

def route(relative, text=''):
    relative = relative.replace('\\', '/')
    if relative.startswith('reviews/'):
        record = source_fields(text)
        if not record['id']:
            raise ValueError('Review card missing source identity: '+relative)
        target, reason = owner(record)
        return target+'/catalog/'+relative, reason
    if relative.startswith('projects/'):
        scope = Path(relative).stem
        if scope in PRODUCTS:
            return scope+'/catalog/README.md', '项目资料索引归本项目'
        if scope == 'company':
            return '1company/catalog/README.md', '公司资料索引归公司层'
        if scope == 'other_projects':
            return '1company/catalog/OTHER_PROJECTS.md', '其他产品单独列出，避免混入四端当前口径'
        if scope == 'shared':
            return GLOBAL+'/SOURCES.md', '全局资料索引；业务资料随审阅卡片归属重分组'
        raise ValueError('Unknown project index: '+relative)
    return GLOBAL+'/'+relative, '跨项目索引、分类入口、完整台账或整理验收证据归全局维护'

def mapped_relative(root, source, target):
    return quote(os.path.relpath((root/target).resolve(), (root/source).parent.resolve()).replace('\\','/'), safe='/._-')

def rebase(text, root, old_relative, new_relative, mapping):
    """Rewrite live Markdown links only, preserving code fences and old path facts."""
    root = root.resolve()
    old_path = root/old_relative
    new_path = root/new_relative
    def replace(match):
        label, raw = match.groups()
        ref = raw.strip('<>')
        value, mark, fragment = ref.partition('#')
        if not value or re.match(r'^(?:https?|mailto|app|plugin|codex|data):|^//', value):
            return match.group(0)
        decoded = unquote(value)
        absolute = bool(re.match(r'^[A-Za-z]:[\\/]|^/', decoded))
        resolved = Path(decoded).resolve() if absolute else (old_path.parent/decoded).resolve()
        try:
            old_key = resolved.relative_to(root).as_posix()
        except ValueError:
            if absolute:
                return match.group(0)
            # Agent archives live next to, rather than inside, the knowledge root.
            new_ref = quote(os.path.relpath(resolved, new_path.parent).replace('\\','/'), safe='/._-')
        else:
            new_key = mapping.get(old_key, old_key)
            if old_relative == new_relative and new_key == old_key:
                return match.group(0)
            new_ref = mapped_relative(root, new_relative, new_key)
        return '['+label+']('+new_ref+('#'+fragment if mark else '')+')'
    chunks = re.split(r'(^```[^\n]*\n[\s\S]*?^```[^\n]*(?:\n|$))', text, flags=re.M)
    return ''.join(chunk if i % 2 else LINK.sub(replace, chunk) for i, chunk in enumerate(chunks))

def write_changed(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    body = text.rstrip()+'\n'
    if not path.exists() or path.read_text(encoding='utf-8-sig') != body:
        path.write_text(body, encoding='utf-8', newline='\n')

def evidence_text(text, root, record, output, aliases, problems):
    """Resolve links copied from source prose in the source's own context.

    Unrecoverable or example paths remain visible as literal historical text;
    they must not become misleading clickable links in a derived review card.
    """
    def replace(match):
        label, raw = match.groups(); raw = raw.strip('<>')
        value, mark, fragment = raw.partition('#')
        if not value or re.match(r'^[A-Za-z]+:|^/|^//',value):
            return match.group(0)
        candidates = []
        for source in dict.fromkeys([record['path'],record.get('original_path',record['path'])]):
            resolved=(root/source).parent/unquote(value)
            try:key=resolved.resolve().relative_to(root.resolve()).as_posix()
            except ValueError:
                if resolved.exists():candidates.append(str(resolved.resolve()))
                continue
            target=aliases.get(key,key)
            if (root/target).exists():candidates.append(target)
        if candidates:
            return '['+label+']('+mapped_relative(root,output,candidates[0])+('#'+fragment if mark else '')+')'
        reason='模板或示例占位路径' if re.search(r'[{}]|\{project\}|your_',value) else '原始相对引用在当前路径与旧路径映射中均未找到'
        problems.append({'source':record.get('id'),'path':record['path'],'target':raw,'reason':reason})
        return label+'（'+reason+'：`'+raw.replace('`','')+'`）'
    chunks=re.split(r'(^```[^\n]*\n[\s\S]*?^```[^\n]*(?:\n|$))',text,flags=re.M)
    return ''.join(chunk if i%2 else LINK.sub(replace,chunk) for i,chunk in enumerate(chunks))

def publish(root, generated):
    """Publish legacy-rendered output from an isolated temp directory.

    Existing manual receipts and merged-source cards are preserved. A manifest
    records generated targets; no broad directory deletion occurs.
    """
    root, generated = root.resolve(), generated.resolve()
    layout_path = root/GLOBAL/'layout.json'
    saved = json.loads(layout_path.read_text(encoding='utf-8')) if layout_path.exists() else {}
    mapping = dict(saved.get('aliases', {}))
    texts, records, routes = {}, {}, {}
    for p in sorted(generated.rglob('*')):
        if not p.is_file():
            continue
        rel = p.relative_to(generated).as_posix()
        text = p.read_text(encoding='utf-8-sig')
        target, _ = route(rel, text)
        texts[rel] = text
        routes[rel] = target
        mapping['catalog/'+rel] = target
        if rel.startswith('reviews/'):
            records[rel] = source_fields(text)
    # A legacy-generated detail link appears in many scopes. Resolve by ID,
    # never by the index document's scope.
    for rel, record in records.items():
        target = routes[rel]
        prior = saved.get('review_targets', {}).get(record['id'])
        if prior and prior != target and (root/prior).exists():
            raise ValueError('Review owner changed; preserve and explicitly migrate '+prior)
    def cell(value):
        return str(value or '').replace('|',' / ').replace('\n',' ')
    def detail_link(record, dest):
        return '['+cell(record['path'])+']('+mapped_relative(root,dest,record['path'])+')'
    # Capture complete table rows from the original aggregate before regrouping.
    legacy_rows = {}
    for line in texts['FILE_REGISTER.md'].splitlines():
        if not line.startswith('| '):
            continue
        hit = re.search(r'reviews/([a-f0-9]{20}\.md)', line)
        if hit:
            legacy_rows['reviews/'+hit.group(1)] = line
    written = []
    for rel, text in texts.items():
        target = routes[rel]
        if rel.startswith('projects/'):
            continue
        if rel == 'before_after.csv' and (root/target).exists():
            old = {r['original_path']:r for r in csv.DictReader(io.StringIO((root/target).read_text(encoding='utf-8-sig')))}
            reader = csv.DictReader(io.StringIO(text)); fields = reader.fieldnames; data = list(reader)
            for row in data:
                prev = old.get(row['original_path'], {})
                if row['current_path'].startswith('../') and not row.get('current_sha256') and row['current_path'] == prev.get('current_path'):
                    row['current_sha256'] = prev.get('current_sha256','')
            buffer = io.StringIO(newline=''); writer = csv.DictWriter(buffer,fieldnames=fields); writer.writeheader(); writer.writerows(data); text = buffer.getvalue()
        if rel.endswith('.md'):
            text = rebase(text,root,'catalog/'+rel,target,mapping)
            if rel in records:
                record = records[rel]; assigned, reason = owner(record)
                text += '\n## 目录归类\n\n- 导航归属：'+LABELS[assigned]+'。'+reason+'。\n- 原文范围、业务日期和复核状态见上文；本归类不改变生产口径。\n'
                if record['project'] == 'other_projects':
                    text += '- 其他产品：仍以原文指明的 Vibedance、fx-editor 或实际产品范围为准；不自动认定为 Collart Android。\n'
        write_changed(root/target,text); written.append(target)
    for assigned in OWNERS:
        dest = GLOBAL+'/SOURCES.md' if assigned == '0global' else assigned+'/catalog/README.md'
        members = [rel for rel,r in records.items() if owner(r)[0] == assigned]
        current, historical, pending = [], [], []
        for rel in sorted(members, key=lambda k:records[k]['path']):
            line = legacy_rows.get(rel)
            if not line:
                raise ValueError('Full aggregate row missing for '+rel)
            line = rebase(line,root,'catalog/FILE_REGISTER.md',dest,mapping)
            if ' / documented / reviewed_static ' in line:
                current.append(line)
            elif re.search(r' / (historical|deprecated) / ',line):
                historical.append(line)
            else:
                pending.append(line)
        lines = ['# '+LABELS[assigned]+'资料索引','',
                 '本目录保存索引和审阅记录，正式业务正文仍由文件链接指向原维护位置。历史状态、原日期和未解决问题继续保留。','',
                 '[全局总目录]('+mapped_relative(root,dest,GLOBAL+'/README.md')+') · [表与版本](TABLES.md) · [SQL 与工具](SQL.md) · [待处理](REVIEW.md)','',
                 '本归属共 '+str(len(members))+' 份当前审阅卡片；不含仅供旧标识追溯的合并卡片。']
        for title, items in [('正式维护入口',current),('历史与废弃资料',historical),('待核对与边界',pending)]:
            if items:
                lines += ['', '## '+title,'','| 文件 | 收录 / 业务 / 复核 | 内容与结论 | 审阅 |','|---|---|---|---|',*items]
        if assigned == '1company':
            lines += ['','[其他产品资料](OTHER_PROJECTS.md)：Vibedance 等另列，不能按旧存放位置视为 Android 口径。']
        related = [rel for rel,r in records.items() if r['path'].startswith(assigned+'/') and owner(r)[0] != assigned]
        if related:
            lines += ['', '## 跨项目证据引用','', '以下原文保存在本项目的报告或历史批次中，审阅卡片按实际产品归属维护。','']
            lines += ['- '+detail_link(records[rel],dest)+' · [审阅]('+mapped_relative(root,dest,routes[rel])+')' for rel in sorted(related)]
        write_changed(root/dest,'\n'.join(lines)); written.append(dest)
        # Small owner-specific views use complete original rows, not copied bodies.
        if assigned != '0global':
            for view, predicate, title in [
                ('TABLES.md',lambda r:'/tables/' in r['path'],'表与版本'),
                ('SQL.md',lambda r:Path(r['path']).suffix in {'.sql','.sqlx','.py','.ps1'} or '/lineage/' in r['path'],'SQL 与工具'),
                ('REVIEW.md',lambda r:'## 待处理' in texts['reviews/'+hashlib.sha256(r['id'].encode()).hexdigest()[:20]+'.md'] or ' / needs_review' in texts['reviews/'+hashlib.sha256(r['id'].encode()).hexdigest()[:20]+'.md'],'待处理')]:
                page = assigned+'/catalog/'+view
                selected = [rel for rel in members if predicate(records[rel])]
                body = '# '+LABELS[assigned]+title+'\n\n[本项目资料](README.md) · [全局待处理]('+mapped_relative(root,page,GLOBAL+'/REVIEW.md')+')\n\n'
                body += '| 文件 | 收录 / 业务 / 复核 | 内容与结论 | 审阅 |\n|---|---|---|---|\n'
                body += '\n'.join(rebase(legacy_rows[rel],root,'catalog/FILE_REGISTER.md',page,mapping) for rel in sorted(selected,key=lambda k:records[k]['path']))
                write_changed(root/page,body); written.append(page)
    other = '1company/catalog/OTHER_PROJECTS.md'
    other_members = [rel for rel,r in records.items() if r['project']=='other_projects']
    body = '# 其他产品与范围待确认资料\n\n这些资料不能仅因保存在 Android 目录就被视为 Android 业务口径。沿用原文明确的产品、日期和限制。\n\n'
    body += '| 文件 | 收录 / 业务 / 复核 | 内容与结论 | 审阅 |\n|---|---|---|---|\n'
    body += '\n'.join(rebase(legacy_rows[rel],root,'catalog/FILE_REGISTER.md',other,mapping) for rel in sorted(other_members))
    write_changed(root/other,body); written.append(other)
    readme = '# 知识库目录与维护记录\n\n全局目录位于 `0global/catalog`，公司及各端的索引、审阅卡片在各自的 `catalog` 中。正式正文继续在原 tables、indicators、product、reports 等目录维护。所有 catalog 都是派生输出，不作为插件业务输入。\n\n'
    readme += '[全部审阅](FILE_REGISTER.md) · [文件清单](files.csv) · [表与版本](TABLES.md) · [SQL](SQL.md) · [主题](TOPICS.md) · [待处理](REVIEW.md) · [迁移映射](MIGRATIONS.md)\n\n'
    readme += '\n'.join('- ['+LABELS[o]+']('+mapped_relative(root,GLOBAL+'/README.md',GLOBAL+'/SOURCES.md' if o=='0global' else o+'/catalog/README.md')+')' for o in OWNERS)
    readme += '\n\n[目录说明](DIRECTORY_GUIDE.md) · [本次逐文件归类](CLASSIFICATION.csv) · [归类说明及验收](REORGANIZATION.md) · [_generated 归档](GENERATED_ARCHIVE.md) · [SQL 整理记录](SQL_STANDARDS_MERGE.md) · [2026-09-12 历史验收](DELIVERY.md)\n\n原业务日期、状态与问题按来源文档保留。静态审阅和目录归类均不代表生产事实已复验。\n'
    write_changed(root/GLOBAL/'README.md',readme)
    layout = {**saved, 'version':1, 'aliases':dict(sorted(mapping.items())),
              'review_targets':{r['id']:routes[rel] for rel,r in sorted(records.items())},
              'generated_targets':sorted(set(written))}
    write_changed(layout_path,json.dumps(layout,ensure_ascii=False,indent=2))
    return {'owners':{o:sum(owner(r)[0]==o for r in records.values()) for o in OWNERS},
            'generated_files':len(set(written)), 'root_catalog_created':False}
