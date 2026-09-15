---
id: "table:aidata2025.dim.dim_ai_service_model_info_copy"
title: "aidata2025.dim.dim_ai_service_model_info_copy · ai服务模型信息表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dim.dim_ai_service_model_info_copy.md", "feishu:aidata2025.dim.dim_ai_service_model_info_copy", "schema:aidata2025.dim.dim_ai_service_model_info_copy"]
tags: ["dim_ai_service_model_info_copy", "字段", "schema", "SQLX"]
tables: ["aidata2025.dim.dim_ai_service_model_info_copy"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dim.dim_ai_service_model_info_copy · ai服务模型信息表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dim.dim_ai_service_model_info_copy` |
| 粒度 | 每个model_type一行 |
| 主键/去重键 | model_type；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 手动维护；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `ai_service_type` | STRING | NULLABLE | ai服务类型 | 飞书 |
| `provider` | STRING | NULLABLE | ai服务供应商 | 飞书 |
| `model_type` | STRING | NULLABLE | ai服务模型 | 飞书 |
| `description` | STRING | NULLABLE | ai服务模型的描述 | 飞书 |
| `datasource` | STRING | NULLABLE | 数据源 | 飞书 |
| `ai_service_num` | INTEGER | NULLABLE | ai服务的调用量级 | 飞书 |
| `remark` | STRING | NULLABLE | 补充信息 | 飞书 |

## 定义差异与补充

- ai_service_num: 飞书 类型 string；schema 类型 INTEGER
- ai_service_num: 旧文档 类型 string；schema 类型 INTEGER
- remark: 飞书 类型 int；schema 类型 STRING
- remark: 旧文档 类型 int；schema 类型 STRING

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 否 |
| 数据来源 | 业务信息 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m10!1m4!4m3!1saidata2025!2sads_collart!3sads_high_value_user_Info!1m4!4m3!1saidata2025!2sdim!3sdim_ai_service_model_info_copy) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/scheduled-queries/locations/us/configs/__REDACTED_ID__/runs?project=aidata2025) |
| 看板 | ai服务看板（服务端数据） |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
