---
id: "table:pubdata2025.dwd.dwd_cdct_revenue_adplatform_di"
title: "pubdata2025.dwd.dwd_cdct_revenue_adplatform_di · 广告平台明细汇总表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.dwd.dwd_cdct_revenue_adplatform_di.md", "feishu:pubdata2025.dwd.dwd_cdct_revenue_adplatform_di", "schema:pubdata2025.dwd.dwd_cdct_revenue_adplatform_di"]
tags: ["dwd_cdct_revenue_adplatform_di", "字段", "schema", "SQLX"]
tables: ["pubdata2025.dwd.dwd_cdct_revenue_adplatform_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.dwd.dwd_cdct_revenue_adplatform_di · 广告平台明细汇总表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.dwd.dwd_cdct_revenue_adplatform_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | ad_platform |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `ad_platform` | STRING | NULLABLE | 广告平台 | 飞书 |
| `region` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `ad_source_name` | STRING | NULLABLE | 广告源名称 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `ad_unit_id` | STRING | NULLABLE | 广告位id | 飞书 |
| `ad_unit_display_label` | STRING | NULLABLE | 广告位 | 飞书 |
| `platform` | STRING | NULLABLE | 应用所属平台，如 iOS、Android、Web。 | 飞书 |
| `ad_format` | STRING | NULLABLE | 广告样式 | 飞书 |
| `request_cnt` | INTEGER | NULLABLE | 计数指标字段，用于统计人数、次数或记录量。 | 飞书 |
| `impression_cnt` | INTEGER | NULLABLE | 广告展示次数 | 飞书 |
| `click_cnt` | INTEGER | NULLABLE | 点击次数 | 飞书 |
| `revenue` | FLOAT | NULLABLE | 收入 | 飞书 |
| `is_bidding` | BOOLEAN | NULLABLE | 是否bidding | 飞书 |
| `matched_requests` | INTEGER | NULLABLE | 请求成功 | schema |

## 定义差异与补充

- matched_requests: 飞书补充解释：整型指标字段，用于统计数量、金额或次数。
- matched_requests: 旧文档补充解释：整型指标字段，用于统计数量、金额或次数。

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.ods.ods_ad_revenue_admob_1d pubdata2025.ods.ods_ad_revenue_applovin_1d pubdata2025.ods.ods_ad_revenue_appodeal_1d pubdata2025.ods.ods_ad_revenue_topon_1d pubdata2025.ods.ods_ad_tradplus_data_1d |
| 是否需要展示血缘 | 是 |
| 数据来源 | 广告平台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sdwd!3sdwd_cdct_revenue_adplatform_di) |
| 任务地址 | dwd/revenue/h_dwd_cdct_revenue_adplatform_di.sqlx |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：pubdata2025.ods.ods_ad_revenue_admob_1d<br>pubdata2025.ods.ods_ad_revenue_applovin_1d<br>pubdata2025.ods.ods_ad_revenue_appodeal_1d<br>pubdata2025.ods.ods_ad_revenue_topon_1d<br>pubdata2025.ods.ods_ad_tradplus_data_1d
