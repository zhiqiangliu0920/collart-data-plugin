# 可复用 SQL

7 个 BigQuery GoogleSQL 模板，使用命名参数，不内嵌原作者日期或凭证。含 ASSERT 的文件须作为 GoogleSQL script 执行。整合时仅做离线检查，首次运行需核对现网 schema、来源覆盖与业务日；生产查询不是安装步骤。

| 模板 | 参数 | 用途 / 限制 |
|---|---|---|
| [country_metrics.sql](country_metrics.sql) | DATE start_date/end_date/as_of_date | Web 国家指标；全部新增次留；首购订阅人数不等于新访客付费人数 |
| [four_platform_daily.sql](four_platform_daily.sql) | DATE start_date/end_date | 四端分行比较，不输出重叠收入之和 |
| [probe_event_names.sql](probe_event_names.sql) | DATE start_date/end_date | Android 原始事件探查，含首尾最多 30 天 |
| [extract_event_param.sql](extract_event_param.sql) | 上述日期；STRING event_name/param_key | 保留参数值类型，不把参数缺失当成某个业务枚举 |
| [web_profile_by_userid.sql](web_profile_by_userid.sql) | STRING uid | 同时查最后登录及历史账号数组 |
| [internal_user_filter.sql](internal_user_filter.sql) | ARRAY&lt;STRING&gt; internal_user_ids | 保守排除曾关联内部账号的设备，避免展开重复 |
| [web_new_user_cohort.sql](web_new_user_cohort.sql) | 日期含 as_of_date；内部账号数组 | profile 可观察的设备 cohort，未成熟 NULL，非完整历史新增 |

`as_of_date` 是确认分区完整且回刷完成的最后业务日。d2 是 cohort 后一天，因此 cohort+1 不晚于 as_of_date 才成熟。取跨日汇总率必须累计同一批成熟分子与分母。

内部账号参数取自 [配置](../config/internal-user-ids.json) 的 user_ids，使用连接库的数组参数绑定，勿拼接进 SQL；清单来源为 2026-06-23，当前状态仍需团队复核。聚合表无法下游精确排除账号，应验证上游规则或报告缺口。

没有统一预设币种、去重范围或多平台 schema 保证。扩展模板时按 [收入证据](../knowledge/shared/payment-evidence.md) 和 [冲突清单](../knowledge/shared/known-conflicts.md) 确认字段、毛净额、退款和时间范围。
