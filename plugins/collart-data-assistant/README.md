# Collart 团队数据助手 0.5.0

用于 Android、iOS/VidArt、Web 主站、Fashion 的经营分析、事件漏斗、表字段查询和口径维护。

- [按项目查看知识](knowledge/INDEX.md)：每个项目固定业务、表字典、埋点、指标、分析方法五类。
- [访问约定](knowledge/shared/business/access.md)：只读；原始逐条行为仅最近 **7 天**。长历史用合适的汇总表。
- [选表及 ADS 回退](knowledge/shared/business/routing.md)：先查结构化字典，追溯时才读 SQLX。

在 Codex 中说“用 Collart 插件分析 Android 最近七个完整日收入变化”，或“查看 Web 画像表 user_ids 的含义”。使用本人已授权的数据连接；插件不含密钥、内部账号名单或数据查询结果。

`scripts/kb.py search/read` 提供有界检索；`scripts/query.py` 生成只读原始查询模板，不执行 SQL。完整用法见 [仓库使用说明](https://github.com/zhiqiangliu0920/collart-data-plugin/blob/main/INSTALL.md)。维护记录在仓库 maintainer，不随插件目录安装。
