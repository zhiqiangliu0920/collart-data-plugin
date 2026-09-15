# 维护与发布流程

## 编辑

ai-knowledge 原目录只读保留。其新增/修正资料先比对，再编辑插件规范正文，不重新复制历史目录。来源中的本机配置、凭证、账号清单、分析输出和维护执行脚本不收录。

知识 Markdown 的 frontmatter 是每行 JSON 值，必需 id/title/project/kind/status/sources。项目固定四端及 shared/company；类型 business/table/event/metric/playbook/policy。未核验业务值用 documented；schema_observed 是来源状态，不能据此改成 verified。表字典含完整字段、粒度、分区、增量/去重/关联及风险，未知明确记录。

## 来源变化与增量复核

```text
python -X utf8 scripts/source_review.py --knowledge <ai-knowledge目录>
python -X utf8 scripts/source_review.py --knowledge <ai-knowledge目录> --queue
python -X utf8 scripts/source_review.py --capture <新来源清单.json> --queue
```

新来源清单采用插件 _meta/sources.json 的 sources 结构。维护者通过本人授权的只读服务读取 Feishu、BigQuery tables 元数据和 Dataform releaseConfig 对应 revision 的 readFile，生成无凭证 capture。工作区编辑和发布编译分别记录，不能拿工作区内容冒充已发布版本。原始完整 API 响应不直接加入仓库。

索引仅含 ID、项目、类型、路径及哈希等机器元数据，不分发全文副本。

工具按 hash/revision 判断变化，生成 maintainer/review-queue.json 并标记受影响条目，**不会自动把变化内容覆盖正文**。标记后按缺口复核：补齐正文与字段、来源文件和来源哈希；核验后手工关闭对应 queue 条目，记录 evidence、日期和覆盖范围。保留尚未解决的项，重新扫描不能清空旧队列。

## 构建与验证

```text
python -X utf8 scripts/build.py
python -B -m unittest discover -s tests
python -X utf8 scripts/build.py --check
```

构建不抓取外部数据、不创建目录镜像，只生成新结构索引与明确的文件/hash 收录清单；重复构建须一致。字段遗漏、失效引用、来源哈希不符、遗留导入器、包外文件、执行 SQL 写入及原始模板越界必须失败。不要为通过检查删除有用字段；缺来源时保留 gap 状态。

## 发布

先比较远程 main 并处理新的用户改动。在独立 codex/ 分支完成变更和校验，将具体版本提交同步 GitHub，再确认远程 commit/CI。按用户既有授权发布，版本写 plugin.json；本机按 SYNC.md 更新。维护记录不进入 plugins/collart-data-assistant。未经授权不得发布数据库写任务或凭证。
