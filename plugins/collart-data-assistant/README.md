# Collart 团队数据知识助手

使用约定：只读数据，禁止写入/修改/删除表；原始埋点仅查询最近 30 天。安装前阅读 [数据访问约定](docs/data-access-policy.md)，连接账号的数据库只读权限需另行配置。

两个入口：分析用 collart-analysis，沉淀用 collart-knowledge-maintain。

[统一主题](knowledge/INDEX.md) · [完整资料](library/INDEX.md) · [SQL](library/SQL.md) · [待处理](library/pending.json) · [维护](docs/maintenance.md)

资料分三层：统一主题回答可复用问题；library 保留完整原文和来源图；provenance 保存原有历史摘录。原文包含旧 Skill 或脚本时仅供参考，不授予执行权限。

```sh
python scripts/kb.py search "purchase_uv"
python scripts/kb.py search "revenue" --project collart_web --scope materials
python scripts/kb.py search "SELECT" --kind sql --limit 10
python scripts/kb.py read "ai-knowledge:1company/indicators/subscription_purchase.md"
python scripts/kb.py check
```

search 默认先返回统一主题，再返回完整资料；read 显示完整正文、原日期、原路径和可在本包解析的引用。原始文件路径只是来源标识，不要求这台电脑存在该路径。历史资料中的缺失引用明确留在待处理清单。

## 目录整理后的标识与检索

ai-knowledge 的正式正文按公司/四端维护，0global/knowledge_registry.json 记录持久 ID、旧路径别名及精确正文哈希。两个历史包的标识表由 inputs.source_registries 指向本机状态文件。纯迁移更新 path/aliases 并保留 id；内容变化必须审阅差异后更新记录，禁止只重设哈希。

收录 status、业务 business_status、复核 review_status 分开。默认 search 返回正式主题和 documented + reviewed_static 全文；--include-history 包含历史、废弃与待核对资料；--business-status 可精确筛选。read 接受持久 ID 和新旧路径别名，返回来源状态与完整正文。旧档案按带内容哈希的版本 ID 读取，不能冒充当前版本。

主题来源重新捕获时新增 source ID 和摘录，旧证据记录 tracking_status=historical 并保留哈希。它们不参与当前来源漂移报警，但仍接受包内证据完整性校验。新日期仅为整理/捕获日，不是业务生效日。

