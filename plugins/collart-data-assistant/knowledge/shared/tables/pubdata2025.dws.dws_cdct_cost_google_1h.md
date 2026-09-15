---
id: "table:pubdata2025.dws.dws_cdct_cost_google_1h"
title: "pubdata2025.dws.dws_cdct_cost_google_1h · ga投放平台花费"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.dws.dws_cdct_cost_google_1h.md", "dataform:pubdata/definitions/dws/cost/h_dws_cdct_cost_google_1h.sqlx", "feishu:pubdata2025.dws.dws_cdct_cost_google_1h", "schema:pubdata2025.dws.dws_cdct_cost_google_1h"]
tags: ["dws_cdct_cost_google_1h", "字段", "schema", "SQLX"]
tables: ["pubdata2025.dws.dws_cdct_cost_google_1h"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.dws.dws_cdct_cost_google_1h · ga投放平台花费

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.dws.dws_cdct_cost_google_1h` |
| 粒度 | 每天每个campaign每个国家一行 |
| 主键/去重键 | event_date+campaign_name+country；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `hour` | INTEGER | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `campaign_name` | STRING | NULLABLE | 投放campaign名称 | 飞书 |
| `cost` | FLOAT | NULLABLE | 投放花费 | 飞书 |
| `impressions` | INTEGER | NULLABLE | 投放广告展示次数 | 飞书 |
| `clicks` | INTEGER | NULLABLE | 点击次数 | 飞书 |
| `ctr` | FLOAT | NULLABLE | 点击率 | 飞书 |
| `conversions` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `average_cpc` | FLOAT | NULLABLE | 浮点型指标字段，用于统计金额、比率或均值。 | 飞书 |
| `cost_per_conversion` | FLOAT | NULLABLE | 每次转化成本 | 飞书 |
| `installs` | INTEGER | NULLABLE | 安装量 | 飞书 |
| `cost_per_install` | FLOAT | NULLABLE | 每次安装成本 | 飞书 |
| `hk_us_exchange_rate` | FLOAT | NULLABLE | 比率指标字段，用于表示转化率、留存率或占比。 | 飞书 |
| `intotime` | TIMESTAMP | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `gst_cost` | FLOAT | NULLABLE | 成本字段，用于记录投放、服务或业务成本。 | 飞书 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.ods.ods_google_ads_campaign_1h |
| 是否需要展示血缘 | 否 |
| 数据来源 | 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sdws!3sdws_cdct_cost_google_1h) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/pubdata/workspaces/script/files/definitions%2Fdws%2Fcost%2Fh_dws_cdct_cost_google_1h.sqlx?project=pubdata2025) |
| 看板 | - |

### 使用限制

- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:pubdata/definitions/dws/cost/h_dws_cdct_cost_google_1h.sqlx`；仓库 `pubdata`，路径 `definitions/dws/cost/h_dws_cdct_cost_google_1h.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.877805+00:00`。同一 SQLX 的产出：`pubdata2025.dws.dws_cdct_cost_google_1h`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
declare begin_date date default ${dataform.projectConfig.vars.biz_date} - 4;
declare end_date date default ${dataform.projectConfig.vars.biz_date} + 1;
WHERE event_date between begin_date and end_date;
inner join (
on c.currency = 'HKD' and (a.event_date - 1) = cast(c.stats_date as date)
where a.event_date between begin_date and end_date;
```

飞书登记上游（不保证当前依赖）：pubdata2025.ods.ods_google_ads_campaign_1h
- 物理上游：`gzdw2024.gz_dim.exchange_rate_days`
