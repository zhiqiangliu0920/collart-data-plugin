---
id: "table:aidata2025.dm.dm_user_profile_collart_df"
title: "aidata2025.dm.dm_user_profile_collart_df"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dm.dm_user_profile_collart_df.md", "feishu:aidata2025.dm.dm_user_profile_collart_df", "schema:aidata2025.dm.dm_user_profile_collart_df"]
tags: ["dm_user_profile_collart_df", "字段", "schema", "SQLX"]
tables: ["aidata2025.dm.dm_user_profile_collart_df"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dm.dm_user_profile_collart_df

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dm.dm_user_profile_collart_df` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `user_pseudo_id` | STRING | NULLABLE | 用户id，firebase分配的唯一id | 飞书 |
| `user_id` | STRING | NULLABLE | 用户id，内部平台分配的唯一id | 飞书 |
| `atlasv_uid` | STRING | NULLABLE | 技术团队给用户定义的唯一id | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_user_collart_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdm!3sdm_user_profile_collart_df) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdm%2Fdaily%2Fh_dm_user_collart_df.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
