---
id: "table:pubdata2025.dwd.dwd_cdct_cost_azure_billing_di"
title: "pubdata2025.dwd.dwd_cdct_cost_azure_billing_di"
project: "shared"
kind: "table"
status: "documented"
sources: ["dataform:pubdata/definitions/dwd/cost/h_dwd_cdct_cost_azure_billing_di.sqlx", "schema:pubdata2025.dwd.dwd_cdct_cost_azure_billing_di"]
tags: ["dwd_cdct_cost_azure_billing_di", "字段", "schema", "SQLX"]
tables: ["pubdata2025.dwd.dwd_cdct_cost_azure_billing_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.dwd.dwd_cdct_cost_azure_billing_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.dwd.dwd_cdct_cost_azure_billing_di` |
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
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `atlasv_app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `atlasv_team` | STRING | NULLABLE | 未说明 | 缺口 |
| `billing_account_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `billing_account_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `billing_account_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `billing_currency` | STRING | NULLABLE | 未说明 | 缺口 |
| `billing_month` | DATE | NULLABLE | 未说明 | 缺口 |
| `charge_category` | STRING | NULLABLE | 未说明 | 缺口 |
| `charge_sub_category` | STRING | NULLABLE | 未说明 | 缺口 |
| `invoice_issuer_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `region` | STRING | NULLABLE | 未说明 | 缺口 |
| `resource_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `resource_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `resource_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `service_category` | STRING | NULLABLE | 未说明 | 缺口 |
| `service_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `sku_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `sub_account_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `usage_quantity` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `billing_cost` | FLOAT | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:pubdata/definitions/dwd/cost/h_dwd_cdct_cost_azure_billing_di.sqlx`；仓库 `pubdata`，路径 `definitions/dwd/cost/h_dwd_cdct_cost_azure_billing_di.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.174670+00:00`。同一 SQLX 的产出：`pubdata2025.dwd.dwd_cdct_cost_azure_billing_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。
