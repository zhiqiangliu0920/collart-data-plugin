---
id: "table:aidata2025.ads.ads_hangzhou_revenue_country_1d"
title: "aidata2025.ads.ads_hangzhou_revenue_country_1d · 公司分产品、国家、分来源收入"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ads.ads_hangzhou_revenue_country_1d.md", "dataform:aidata/definitions/ads/revenue/ads_hangzhou_revenue_country_1d.sqlx", "feishu:aidata2025.ads.ads_hangzhou_revenue_country_1d", "schema:aidata2025.ads.ads_hangzhou_revenue_country_1d"]
tags: ["ads_hangzhou_revenue_country_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_hangzhou_revenue_country_1d"]
review_required: false
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_hangzhou_revenue_country_1d · 公司分产品、国家、分来源收入

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_hangzhou_revenue_country_1d` |
| 粒度 | 每天每个产品每个国家一行 |
| 主键/去重键 | 日期、产品、国家；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `google_ad_revenue` | FLOAT | NULLABLE | 来自谷歌平台的广告收入 | 飞书 |
| `else_ad_revenue` | FLOAT | NULLABLE | 来自其他平台的广告收入 | 飞书 |
| `ad_revenue` | FLOAT | NULLABLE | 广告收入 | 飞书 |
| `google_vip_revenue` | FLOAT | NULLABLE | 来自谷歌平台的订阅收入 | 飞书 |
| `apple_vip_revenue` | FLOAT | NULLABLE | 来自苹果平台的订阅收入 | 飞书 |
| `vip_revenue` | FLOAT | NULLABLE | 订阅收入 | 飞书 |
| `revenue` | FLOAT | NULLABLE | 收入 | 飞书 |

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | downloaddata2025.ads.ads_ad_sub_revenue_1h,aidata2025.dwd.dwd_oper_sub_order_revenue_df,pubdata2025.ods.ods_apple_sales_1d,pubdata2025.dws.dws_cdct_revenue_country_1d |
| 是否需要展示血缘 | 否 |
| 数据来源 | 苹果商店 / 谷歌商店 / 广告平台 / 第三方支付平台（stripe等） |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_hangzhou_revenue_country_1d) |
| 任务地址 | BigQuery – AIDATA – Google Cloud 控制台 |
| 看板 | 公司层收入看板 |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/revenue/ads_hangzhou_revenue_country_1d.sqlx`；仓库 `aidata`，路径 `definitions/ads/revenue/ads_hangzhou_revenue_country_1d.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:52.873302+00:00`。同一 SQLX 的产出：`aidata2025.ads.ads_hangzhou_revenue_country_1d`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT  "2025-01-01";
WHERE  event_date >= from_date;
left join aidata2025.dim.dim_product_info_copy b on a.package_name=b.package_name
left join `hzdw2024.hz_dim.dim_country` c2c on a.country = c2c.country_name_3
where event_date >='2025-01-01'
and b.team='ai_photo'
group by 1, 2, 3
where event_date >= "2025-01-01"
and package_name in (
where event_Date>='2025-01-01'
left join aidata2025.dim.dim_product_info_copy f on a.package_name = f.package_name
where order_date>='2025-01-01'
and f.team='ai_photo'
left join `gzdw2024.gz_dim.exchange_rate_days` b
on cast(a.stats_date as date) = cast(b.stats_date as date) and a.currency_of_proceeds=b.currency
left join `hzdw2024.hz_dim.dim_country` c2c on a.country_code = c2c.country_name_3
WHERE a.stats_date>='2025-01-01'
group by a.stats_date
full join vip_platform_info b
on a.event_date=b.event_date
and a.package_name=b.package_name
and a.country=B.country
where event_date>='2025-01-01'
group by all
```

飞书登记上游（不保证当前依赖）：<br>downloaddata2025.ads.ads_ad_sub_revenue_1h,aidata2025.dwd.dwd_oper_sub_order_revenue_df,pubdata2025.ods.ods_apple_sales_1d,pubdata2025.dws.dws_cdct_revenue_country_1d
- 物理上游：`downloaddata2025.ads.ads_ad_sub_revenue_1h`
- 物理上游：`gzdw2024.gz_dim.exchange_rate_days`
- 物理上游：`hzdw2024.hz_dim.dim_country`
