---
id: "table:pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h"
title: "pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h · 公司分产品、分来源的收入与成本"
project: "company"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h.md", "feishu:pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h", "schema:pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h"]
tags: ["ads_atlasv_basic_data_platform_daily_1h", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h · 公司分产品、分来源的收入与成本

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ads.ads_atlasv_basic_data_platform_daily_1h` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_Date` | DATE | NULLABLE | 日期 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `apple_revenue` | FLOAT | NULLABLE | 来自苹果平台的收入 | 飞书 |
| `google_revenue` | FLOAT | NULLABLE | 来自谷歌平台的收入 | 飞书 |
| `meta_revenue` | FLOAT | NULLABLE | 来自meta平台的收入 | 飞书 |
| `tt_revenue` | FLOAT | NULLABLE | 来自TT平台的收入 | 飞书 |
| `else_revenue` | FLOAT | NULLABLE | 来自其他平台的收入 | 飞书 |
| `apple_cost` | FLOAT | NULLABLE | 苹果平台的成本 | 飞书 |
| `google_cost` | FLOAT | NULLABLE | 来自谷歌平台的成本 | 飞书 |
| `meta_cost` | FLOAT | NULLABLE | 来自meta平台的成本 | 飞书 |
| `tt_cost` | FLOAT | NULLABLE | 成本字段，用于记录投放、服务或业务成本。 | 飞书 |
| `else_cost` | FLOAT | NULLABLE | 服务器成本 | 飞书 |

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.dws.dws_cdct_cost_google_1h aidata2025.ads.ads_hangzhou_revenue_country_1d gzdw2024.gz_bi.dws_app_platform_daily_reports |
| 是否需要展示血缘 | 是 |
| 数据来源 | - |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sads!3sads_atlasv_basic_data_platform_daily_1h) |
| 任务地址 | 定时计划：ads_atlasv_basic_data_platform_daily_1h |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：pubdata2025.dws.dws_cdct_cost_google_1h<br>aidata2025.ads.ads_hangzhou_revenue_country_1d<br>gzdw2024.gz_bi.dws_app_platform_daily_reports
