---
id: "table:aidata2025.ai_service.ai_cost_data"
title: "aidata2025.ai_service.ai_cost_data · 分产品服务器、ai服务成本"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ai_service.ai_cost_data.md", "dataform:aidata/definitions/ads/ai_service/ai_cost_data_1h.sqlx", "feishu:aidata2025.ai_service.ai_cost_data", "schema:aidata2025.ai_service.ai_cost_data"]
tags: ["ai_cost_data", "字段", "schema", "SQLX"]
tables: ["aidata2025.ai_service.ai_cost_data"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ai_service.ai_cost_data · 分产品服务器、ai服务成本

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ai_service.ai_cost_data` |
| 粒度 | 每天每个产品一行 |
| 主键/去重键 | event_date+ package_name；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 每小时刷新；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_Date` | DATE | NULLABLE | 日期 | 飞书 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `cost_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `cost` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `ai_cost` | float | ai服务成本 |
| `else_cost` | float | 服务器成本 |
| `server_cost` | float | 成本字段，用于记录投放、服务或业务成本。 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.dws.dws_cdct_log_ai_record_1d,hzdw2024.ods.ai_base_record_store,pubdata2025.ads.ads_cdct_service_cost_1d,aidata2025.dim.dim_ai_service_cost_unit |
| 是否需要展示血缘 | 是 |
| 数据来源 | 服务端 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sai_service!3sai_cost_data) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Fai_service%2Fai_cost_data_1h.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/ai_service/ai_cost_data_1h.sqlx`；仓库 `aidata`，路径 `definitions/ads/ai_service/ai_cost_data_1h.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:49.173858+00:00`。同一 SQLX 的产出：`aidata2025.ai_service.ai_cost_data`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
declare from_date date default ${dataform.projectConfig.vars.biz_date}-29;
declare to_date date default ${dataform.projectConfig.vars.biz_date} + 1;
LEFT JOIN app_mapping b
ON LOWER(a.atlasv_app_name) = LOWER(b.atlasv_app_name)
WHERE event_date between from_date and to_date
GROUP BY all
left join aidata2025.dim.dim_product_info b
on a.app_name = b.app_name
group by all
```

飞书登记上游（不保证当前依赖）：pubdata2025.dws.dws_cdct_log_ai_record_1d,hzdw2024.ods.ai_base_record_store,pubdata2025.ads.ads_cdct_service_cost_1d,aidata2025.dim.dim_ai_service_cost_unit
- 物理上游：`pubdata2025.ads.ads_atlasv_service_cost_all_1d`
