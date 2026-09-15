---
id: "table:aidata2025.ads.ads_ad_sub_revenue_1h"
title: "aidata2025.ads.ads_ad_sub_revenue_1h · ai组产品分国家收入数据报告"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ads.ads_ad_sub_revenue_1h.md", "dataform:aidata/definitions/ads/revenue/h_ads_ad_sub_revenue_1h.sqlx", "feishu:aidata2025.ads.ads_ad_sub_revenue_1h", "schema:aidata2025.ads.ads_ad_sub_revenue_1h"]
tags: ["ads_ad_sub_revenue_1h", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_ad_sub_revenue_1h"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_ad_sub_revenue_1h · ai组产品分国家收入数据报告

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_ad_sub_revenue_1h` |
| 粒度 | 每天、每个产品每个国家一行 |
| 主键/去重键 | 日期+产品+国家；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 每小时刷新；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `ad_revenue` | FLOAT | NULLABLE | 广告收入 | 飞书 |
| `sub_revenue` | FLOAT | NULLABLE | 订阅收入 | 飞书 |
| `new_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `renew_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `credit_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `purchase_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `new_subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `renew_subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `credit_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `order_num` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `new_order_num` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `renew_order_num` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `credit_order_num` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue` | FLOAT | NULLABLE | 收入 | 飞书 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `sub_new_num` | int | 首次订单数量 |
| `sub_new_revenue` | float | 首次订阅收入 |
| `sub_renew_num` | int | 续订订单数量 |
| `sub_renew_revenue` | float | 续订收入 |

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.dws.dws_cdct_revenue_country_1d,aidata2025.dwd.dwd_oper_sub_order_revenue_df,pubdata2025.ods.ods_apple_sales_1d,pubdata2025.dwd.dwd_cdct_revenue_stripe_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 苹果商店 / 谷歌商店 / 广告平台 / 第三方支付平台（stripe等） |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_ad_sub_revenue_1h) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Frevenue%2Fh_ads_ad_sub_revenue_1h.sqlx?project=aidata2025&supportedpurview=project) |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/revenue/h_ads_ad_sub_revenue_1h.sqlx`；仓库 `aidata`，路径 `definitions/ads/revenue/h_ads_ad_sub_revenue_1h.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.662599+00:00`。同一 SQLX 的产出：`aidata2025.ads.ads_ad_sub_revenue_1h`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT  "2025-01-01";
WHERE  event_date >= from_date;
left join aidata2025.dim.dim_product_info_copy b on a.package_name=b.package_name
where event_date >= from_date
and b.team='ai_photo'
group by 1, 2, 3
left join `aidata2025.dim.exchange_rate_days` b
on cast(a.stats_date as date) = cast(b.stats_date as date) and a.currency_of_proceeds=b.currency
WHERE CAST(a.stats_date AS DATE) >= from_date
and revenue_usd >0
GROUP BY 1, 2, 3
WHERE d.event_date >= from_date
LEFT JOIN ios_sales_dwd d
ON a.event_date = d.event_date
AND a.package_name = d.package_name
AND a.country_code = d.country_code
where a.event_date>=from_date
and revneue>0
and charge_type != 'expired'
group by all
full join ad_revenue ad
left join `aidata2025.dim.dim_country_info` c2c on if(d.country='Russia','RU',d.country)  = c2c.country_name_3
left join aidata2025.dim.dim_product_info_copy f on d.package_name = f.package_name
where f.team='ai_photo'
```

飞书登记上游（不保证当前依赖）：pubdata2025.dws.dws_cdct_revenue_country_1d,aidata2025.dwd.dwd_oper_sub_order_revenue_df,pubdata2025.ods.ods_apple_sales_1d,pubdata2025.dwd.dwd_cdct_revenue_stripe_di
- 物理上游：`aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di`
- 物理上游：`aidata2025.dim.dim_country_info`
- 物理上游：`aidata2025.dim.exchange_rate_days`
- 物理上游：`aidata2025.dwd.dwd_apple_user_subscribtion_di`
- 物理上游：`aidata2025.ods.ods_apple_sales_1d`
