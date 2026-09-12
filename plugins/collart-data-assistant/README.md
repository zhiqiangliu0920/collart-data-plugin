# Collart 团队数据助手

将 Cursor 的 collart-biz-analysis 与 team-data-knowledge 整合为一个 Codex 插件，面向公司内部同事。提供数据分析与知识维护两个 skill，共享一套规范知识、来源和 SQL。

| 入口 | 使用示例 |
|---|---|
| collart-analysis | 使用 Collart 数据助手分析 Web 最近 7 个完整日的收入变化，区分新老用户并解释口径。 |
| collart-knowledge-maintain | 把这份表字段说明沉淀到团队知识，注明来源和待核验项。 |

从 [知识索引](knowledge/INDEX.md) 进入 17 个条目；参阅 [SQL 模板](presets/README.md)、[维护说明](docs/maintenance.md) 与 [整合说明](docs/integration.md)。插件本身不提供 BigQuery 连接，同事使用各自已有的连接和权限。

本次 2026-09-12 整理包含 16 个 documented 和 1 个 draft，未进行生产查数。历史文档中的规模、固定 0、断档或部署记录不代表当前状态。安装后开启新任务试用；测试 SQL 前检查现网 schema 和请求窗口。

插件随团队发行目录内的 install.ps1 安装。仅拷贝本插件子目录会缺少发行目录的 marketplace；请分发完整发行 ZIP。维护者只改源码，安装缓存不会自动同步回团队。
