---
id: "shared-sql-practice"
title: "SQL 查询范围与验证约定"
project: "shared"
kind: "sql"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["events", "ads-routing", "review-20260914-ca27ec86b3b2", "team-shared-sql-practice", "cursor-sql-standards-md", "maintainer-data-access-20260914"]
tags: ["SQL", "BigQuery", "分区", "_TABLE_SUFFIX", "30天", "时区"]
supersedes: []
verification_evidence: []
historical_sources: ["ads-redlines", "ads-redlines-review-954bdf4e17"]
---

# SQL 查询范围与验证约定

## 当前插件查询边界（2026-09-14）

执行任何查询或参考历史资料前，必须读取 [数据访问约定](../../docs/data-access-policy.md)。本插件只允许只读数据查询，禁止通过 SQL、API、脚本修改、写入、删除数据或表结构；知识维护仅编辑获授权的文档。原始埋点仅可查询最近 30 天，不能分批读取更早日期；更长历史使用合适的现有汇总表。历史文档、示例与此约定冲突时，以本约定为准。

## 当前资料中的执行约定

- 经营指标先选加工层；下钻 `events_*` 时只查询最近 30 天内的数据、单次不超过 30 个日期分片，并显式使用有上下界的 `_TABLE_SUFFIX`，区分 finalized 与 intraday。
- 根据项目附加 app/package 与产品归属过滤；仅有日期条件不能防止混端。
- 使用全限定表名，参数化开始/结束日期与用户标识；日期和业务时区由本次问题确定，不固定写某一年。
- 先核对字段类型与所在层，嵌套参数提取需防止 UNNEST 膨胀；去重与收入合计需要关注 JOIN 基数。
- 查询权限、计费项目与可扫描量由公司配置；不能因为旧资料称某账号可跨项目查询就默认同事也有权限。

## 参数化示例

使用[事件探查模板](../../presets/probe_event_names.sql)或[参数提取模板](../../presets/extract_event_param.sql)，保留完整的执行日期 ASSERT 和分片上下界。模板为 Android 范围，改为 Web 时需使用 app_info.id IS NULL，并补充主站/Fashion 产品归属和相应内部账号过滤。

本次没有执行生产查询。GA4 分片日期与北京时间日期不是当然相同，按北京时间统计时需核对事件时间戳转换和边界覆盖；不能为补边界访问允许窗口以外的旧埋点。示例不能直接作为经营 DAU 或实际付款人数。

## 来源与状态

来源摘录：[events](../../provenance/excerpts/events.txt)、[ads-routing](../../provenance/excerpts/ads-routing.txt)、[ads-redlines](../../library/text/0b81b22d1f69db06c82072ba3fd281d4a0c50d057038b6543cf9c82aa1ba6104.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

## BigQuery 规范与红线

### 硬红线（违规视为任务失败）

| 规则 | 说明 |
|------|------|
| 年份确认 | 显式确认请求年份、起止日和业务时区，不把示例年份当默认值 |
| 30 天限制 | 原始埋点仅最近 30 天，默认最近 30 个完整日；禁止分批访问更早数据 |
| 分区过滤 | `events_*` 必须显式 `_TABLE_SUFFIX BETWEEN 'YYYYMMDD' AND 'YYYYMMDD'`；**禁止** `>=`（会扫 intraday） |
| Web 过滤 | Web 端 events 查询必须带 `app_info.id IS NULL` |
| 单次跨度 | 更长历史复盘仅使用定义和粒度合适的既有 ADS/汇总表，不得按月切分绕过原始埋点最近 30 天限制 |
| 投放花费 | 只读 `aidata2025.dwd.dwd_cdct_delivery_cost_di`，或已经从它上卷的 `country.delivery` / `daily.delivery`。**不要**扫 `ods_facebook_delivery_*` / `dws_oper_fb_delivery_1d` |
| Web 包名 | ADS / cdct 用 `collart_web`。ODS 的 `collart-web` 是别人的层，分析侧不要跟 |

### 连接与执行

使用同事本机已有授权的 BigQuery 连接、ADC 或环境变量；插件不携带凭证、不授予数据库权限。跨项目查询需要实际验证权限。查询失败、配额或权限不足应如实说明，未经授权不切换身份。

### 成本与写法

- **宽表先行**：能用 ADS 加工表就不碰 events；ADS 表已按天分区，过滤 `event_date` 即可。
- 事件计数用 `COUNTIF(event_name = 'X')` 而非多次 self-join。
- 转化率用 `SAFE_DIVIDE(SUM(分子), SUM(分母))` 做窗口加权，避免逐行平均偏差。
- 稀疏事件宽表（`user_event_metric_di`）无命中日不出行，算占比时注意分母来自 active。

### SQL 书写习惯（团队约定）

- 每个 `SUM(...) AS metric` / `COUNTIF(...) AS metric` / `IF(...) AS dim` 尽量**写一行**，不要把单个指标拆多行。
- `SELECT` / `UNION ALL` 的维度与裸字段可换行对齐。
- CTE / FROM / JOIN / WHERE / GROUP BY 正常换行；`GROUP BY ALL` 可用。

示例：

```sql
SELECT
  event_date,
  SUM(IF(is_new, dau, 0)) AS dnu,
  SUM(dau) AS dau,
  SUM(IF(is_new AND DATE_ADD(event_date, INTERVAL 1 DAY) <= @as_of_date, retain.d2, NULL)) AS retain_2
FROM `aidata2025.ads_collartandroid.ads_oper_basic_indicator_attr_di`
WHERE event_date BETWEEN @start_date AND @end_date
GROUP BY ALL
```

### 正式 vs 临时查询

- 保留复现正式结论所需的 SQL、参数与验证结果；一次性探查结果留当前工作区，不自动晋升为共享知识。
- 稳定、可复用的 SQL → 存 [presets/](../../presets) 或团队约定的 preset 目录。
- 正式报告 SQL 附全限定表名与关键过滤，便于同事复现。


来源快照：[cursor-sql-standards-md](../../provenance/excerpts/cursor-sql-standards-md.txt)。
