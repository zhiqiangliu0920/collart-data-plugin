---
id: "table:aidata2025.dws.dws_oper_asa_delivery_di"
title: "aidata2025.dws.dws_oper_asa_delivery_di · asa投放平台数据"
project: "collart_ios"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/dws/daily/h_dws_oper_asa_delivery_di.sqlx", "feishu:aidata2025.dws.dws_oper_asa_delivery_di", "schema:aidata2025.dws.dws_oper_asa_delivery_di"]
tags: ["dws_oper_asa_delivery_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_oper_asa_delivery_di"]
review_required: true
applies_to: []
---

# aidata2025.dws.dws_oper_asa_delivery_di · asa投放平台数据

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_oper_asa_delivery_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | package_name, campaign_id, adgroup_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `adgroup_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `adgroup_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `keyword` | STRING | NULLABLE | 未说明 | 缺口 |
| `is_keyword_attributed` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `cost_cny` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `cost_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `impressions` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `clicks` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `installs` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `keyword_id` | STRING | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dws/daily/h_dws_oper_asa_delivery_di.sqlx`；仓库 `aidata`，路径 `definitions/dws/daily/h_dws_oper_asa_delivery_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:55.264990+00:00`。同一 SQLX 的产出：`aidata2025.dws.dws_oper_asa_delivery_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 3;
DECLARE to_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
WHERE event_date BETWEEN from_date AND to_date;
WHERE stats_date BETWEEN from_date AND to_date
GROUP BY event_date, campaign_id
LEFT JOIN campaign_names AS c
ON a.stats_date = c.event_date
AND CAST(a.campaign_id AS STRING) = c.campaign_id
WHERE a.stats_date BETWEEN from_date AND to_date
LEFT JOIN adgroup_total AS a
ON k.stats_date = a.event_date
AND CAST(k.adgroup_id AS STRING) = a.adgroup_id
AND k.country_region = a.country
WHERE k.stats_date BETWEEN from_date AND to_date
GROUP BY event_date, adgroup_id, country
LEFT JOIN keyword_sum AS k USING (event_date, adgroup_id, country)
WHERE a.cost_cny - COALESCE(k.cost_cny, 0) > 0.005
WHERE currency = 'CNY'
LEFT JOIN rate_cny AS r USING (event_date)
```
- 物理上游：`aidata2025.dim.exchange_rate_days`
- 物理上游：`pubdata2025.ods.ods_apple_adgroups_reports_1d`
- 物理上游：`pubdata2025.ods.ods_apple_campaigns_reports_1d`
- 物理上游：`pubdata2025.ods.ods_apple_keyword_reports_1d`
