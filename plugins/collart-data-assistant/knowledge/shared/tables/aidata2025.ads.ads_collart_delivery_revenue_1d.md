---
id: "table:aidata2025.ads.ads_collart_delivery_revenue_1d"
title: "aidata2025.ads.ads_collart_delivery_revenue_1d · collart ga、asa投放看板"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads.ads_collart_delivery_revenue_1d.md", "feishu:aidata2025.ads.ads_collart_delivery_revenue_1d", "schema:aidata2025.ads.ads_collart_delivery_revenue_1d"]
tags: ["ads_collart_delivery_revenue_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_collart_delivery_revenue_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_collart_delivery_revenue_1d · collart ga、asa投放看板

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_collart_delivery_revenue_1d` |
| 粒度 | 每天每个产品每个投放渠道每个国家一行 |
| 主键/去重键 | 日期+包名+投放渠道+国家；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | campaign_name, country |
| 更新 | T+1 8:30；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `campaign_name` | STRING | NULLABLE | 投放campaign名称 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `cost` | FLOAT | NULLABLE | 投放花费 | 飞书 |
| `installs` | INTEGER | NULLABLE | 安装量 | 飞书 |
| `revenue_total` | FLOAT | NULLABLE | 收入 | 飞书 |
| `vip_revenue_total` | FLOAT | NULLABLE | 订阅收入 | 飞书 |
| `sub_revenue_total` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `pack_revenue_total` | FLOAT | NULLABLE | 点数包收入 | 飞书 |
| `ad_revenue_total` | FLOAT | NULLABLE | 广告收入 | 飞书 |
| `firebase_install_user` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `vip_user` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `pack_user` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue_0` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_1` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_2` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_3` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_4` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_5` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_6` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_7` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_14` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_21` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_30` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_45` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `revenue_60` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `dnu` | INTEGER | NULLABLE | 新增用户 | 飞书 |
| `retain_2` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `sub_revenue_aivideo` | float | 直接订阅收入 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dws.dws_oper_newuser_lifecycle_1d,aidata2025.ads_collart.ads_oper_basic_indicator_collart_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 服务端 / 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_collart_delivery_revenue_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Fdaily%2Fh_ads_collart_delivery_revenue_1d.sqlx?project=aidata2025) |
| 看板 | collart ga、asa投放看板 |

### 使用限制

- retain_2 的历史说明为次日；其他 retain_N 的自动解释可能偏移一天，不能按字段后缀直接认定 Dn。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：aidata2025.dws.dws_oper_newuser_lifecycle_1d,aidata2025.ads_collart.ads_oper_basic_indicator_collart_di
