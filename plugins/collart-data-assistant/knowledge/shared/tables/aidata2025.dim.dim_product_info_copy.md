---
id: "table:aidata2025.dim.dim_product_info_copy"
title: "aidata2025.dim.dim_product_info_copy · 产品名称表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dim.dim_product_info_copy.md", "feishu:aidata2025.dim.dim_product_info_copy", "schema:aidata2025.dim.dim_product_info_copy"]
tags: ["dim_product_info_copy", "字段", "schema", "SQLX"]
tables: ["aidata2025.dim.dim_product_info_copy"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dim.dim_product_info_copy · 产品名称表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dim.dim_product_info_copy` |
| 粒度 | 每个产品名一行 |
| 主键/去重键 | package_name；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 手动维护；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `platform` | STRING | NULLABLE | 产品的操作系统平台 | 飞书 |
| `app_type` | STRING | NULLABLE | 产品类型 | 飞书 |
| `city` | STRING | NULLABLE | 产品所在城市 | 飞书 |
| `revenue` | INTEGER | NULLABLE | 收入 | 飞书 |
| `team` | STRING | NULLABLE | 项目组 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dim.dim_product_info |
| 是否需要展示血缘 | 否 |
| 数据来源 | 业务信息 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdim!3sdim_product_info_copy) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/scheduled-queries/locations/us/configs/__REDACTED_ID__/runs?project=aidata2025) |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：aidata2025.dim.dim_product_info
