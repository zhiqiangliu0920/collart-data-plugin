---
id: "table:aidata2025.dws.dws_oper_fb_delivery_1d"
title: "aidata2025.dws.dws_oper_fb_delivery_1d"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dws.dws_oper_fb_delivery_1d.md", "feishu:aidata2025.dws.dws_oper_fb_delivery_1d", "schema:aidata2025.dws.dws_oper_fb_delivery_1d"]
tags: ["dws_oper_fb_delivery_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_oper_fb_delivery_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dws.dws_oper_fb_delivery_1d

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_oper_fb_delivery_1d` |
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
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `campaign` | STRING | NULLABLE | 投放campaign id | 飞书 |
| `campaign_name` | STRING | NULLABLE | 投放campaign名称 | 飞书 |
| `spend` | FLOAT | NULLABLE | 浮点型指标字段，用于统计金额、比率或均值。 | 飞书 |
| `impressions` | INTEGER | NULLABLE | 投放广告展示次数 | 飞书 |
| `clicks` | INTEGER | NULLABLE | 点击次数 | 飞书 |
| `reach` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `actions` | RECORD | REPEATED | 复杂结构字段，通常包含嵌套对象或数组信息。 | 飞书 |
| `actions.action_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `actions.action_count` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.dws.dws_cdct_cost_delivery_fb_1d |
| 是否需要展示血缘 | 否 |
| 数据来源 | 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdws!3sdws_oper_fb_delivery_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdws%2Fdaily%2Fh_dws_oper_fb_delivery_1d.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
