---
id: "table:aidata2025.ai_service.ai_service_record_info_1d"
title: "aidata2025.ai_service.ai_service_record_info_1d"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ai_service.ai_service_record_info_1d.md", "feishu:aidata2025.ai_service.ai_service_record_info_1d", "schema:aidata2025.ai_service.ai_service_record_info_1d"]
tags: ["ai_service_record_info_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ai_service.ai_service_record_info_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ai_service.ai_service_record_info_1d

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ai_service.ai_service_record_info_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "create_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `data_source` | STRING | NULLABLE | 数据源，数据来自哪张表 | 飞书 |
| `create_time` | DATETIME | NULLABLE | ai服务任务创建时间，北京时间 | 飞书 |
| `create_date` | DATE | NULLABLE | ai服务任务创建日期，北京时间 | 飞书 |
| `app_name` | STRING | NULLABLE | 产品名称 | 飞书 |
| `model_type` | STRING | NULLABLE | ai服务的模型 | 飞书 |
| `client_task_id` | STRING | NULLABLE | client_task_id | 飞书 |
| `task_id` | STRING | NULLABLE | task_id | 飞书 |
| `user_id` | STRING | NULLABLE | 用户uid | 飞书 |
| `time_cost` | FLOAT | NULLABLE | 任务消耗时长，单位：s | 飞书 |
| `cost_point` | INTEGER | NULLABLE | 任务消耗积分 | 飞书 |
| `status` | STRING | NULLABLE | 任务状态：completed为成功，其他为失败 | 飞书 |

## 定义差异与补充

- time_cost: 飞书 类型 string；schema 类型 FLOAT
- time_cost: 旧文档 类型 string；schema 类型 FLOAT

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | hzdw2024.ods.ai_base_record_store,hzdw2024.ods.ods_ai_record_info |
| 是否需要展示血缘 | 是 |
| 数据来源 | 服务端 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m10!1m4!4m3!1saidata2025!2sads_collart!3sads_high_value_user_Info!1m4!4m3!1saidata2025!2sai_service!3sai_service_record_info_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery?tc=us:__REDACTED_ID__&project=aidata2025) |
| 看板 | ai服务看板服务端 |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
