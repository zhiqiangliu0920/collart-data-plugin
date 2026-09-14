# Collart Data Plugin

GitHub 分发地址：[zhiqiangliu0920/collart-data-plugin](https://github.com/zhiqiangliu0920/collart-data-plugin)。同事从该仓库下载或更新完整插件；安装入口见 [INSTALL.md](INSTALL.md)。

使用约定：只读数据，禁止写入/修改/删除表；原始埋点仅查询最近 30 天。安装前阅读 [数据访问约定](plugins/collart-data-assistant/docs/data-access-policy.md)，连接账号的数据库只读权限需另行配置。

面向 Collart 团队的知识与 Codex 插件。维护者于 2026-09-14 确认直接同步到当前 Public 仓库；仓库公开不授予任何数据库访问权限。原始资料继续在各自目录维护：

`ai-knowledge + cursor_summary + codex_summary → collart-data-plugin`

- [统一主题](plugins/collart-data-assistant/knowledge/INDEX.md)：公司与四端指标、业务规则、历史案例及待复核口径。
- [完整来源资料](plugins/collart-data-assistant/library/INDEX.md)：表字典、报告、SQL、血缘源码与两个旧包；保留日期、范围和来源。
- [SQL 入口](plugins/collart-data-assistant/library/SQL.md)：全文 SQL 与维护的 presets。
- [来源台账](plugins/collart-data-assistant/library/catalog.json) / [待处理](plugins/collart-data-assistant/library/pending.json)：每份来源的收录、重复、历史、排除或待处理状态。
- [安装](INSTALL.md) / [持续整合发布](SYNC.md)。

## 使用与维护

两个插件入口仍为 collart-analysis 与 collart-knowledge-maintain。业务资料先改原来源；统一主题在暂存版本中结合来源维护。历史包保留原内部名称，作为来源资料，不额外加载其旧执行流程。

插件副本可以独立检索，不依赖维护者磁盘；数据查询使用每个人自己的授权连接。仓库不携带凭证、个人运行状态或原始用户明细。

验证命令：`python -B plugins/collart-data-assistant/scripts/kb.py check`。documented 表示有资料依据；历史验证只在原日期与范围内成立。本次整理没有重新查询生产数据。
