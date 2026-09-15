---
id: "table:aidata2025.dws.dws_oper_asa_collart_1d"
title: "aidata2025.dws.dws_oper_asa_collart_1d"
project: "collart_ios"
kind: "table"
status: "historical"
sources: ["ai-knowledge:1company/tables/aidata2025.dws.dws_oper_asa_collart_1d.md", "feishu:aidata2025.dws.dws_oper_asa_collart_1d", "schema:aidata2025.dws.dws_oper_asa_collart_1d"]
tags: ["dws_oper_asa_collart_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_oper_asa_collart_1d"]
review_required: true
applies_to: []
---

# aidata2025.dws.dws_oper_asa_collart_1d

## 使用边界

BigQuery 元数据返回 NOT_FOUND（2026-09-14）；可能为历史表/名称变化/不可见，不能作为默认当前入口。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_oper_asa_collart_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未取得元数据 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: historical；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| — | — | — | 当前 schema 缺失，下面保留来源字段，不保证当前可用 | 缺口 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `avg_cpm` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `avg_cpt` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `campaign_id` | string | 投放campaign id |
| `campaign_name` | string | 投放campaign名称 |
| `country_region` | string | 国家所在洲 |
| `event_date` | date | 日期 |
| `impressions` | int | 投放广告展示次数 |
| `local_spend` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `tap_install_cpi` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `tap_install_rate` | float | 比率指标字段，用于表示转化率、留存率或占比。 |
| `tap_installs` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `tap_new_downloads` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `tap_redownloads` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `taps` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `total_avg_cpi` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `total_install_rate` | float | 比率指标字段，用于表示转化率、留存率或占比。 |
| `total_installs` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `total_new_downloads` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `total_redownloads` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `ttr` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `view_installs` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `view_new_downloads` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `view_redownloads` | int | 整型指标字段，用于统计数量、金额或次数。 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.ods.ods_apple_campaigns_reports_1d |
| 是否需要展示血缘 | 否 |
| 数据来源 | 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m20!1m4!4m3!1saidata2025!2sdwd!3sdwd_id_convert_di!1m4!4m3!1saidata2025!2sdim!3sdim_country_info!1m4!1m3!1saidata2025!2sbquxjob_678dbd5d_19e1bb53b6c!3sUS!1m4!4m3!1saidata2025!2sdws!3sdws_oper_asa_collart_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdws%2Fdaily%2Fh_dws_oper_asa_collart_1d.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
