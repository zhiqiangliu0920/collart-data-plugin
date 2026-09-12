# Collart 团队数据知识助手

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
