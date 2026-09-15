---
id: "table:storytemplate-10a27.analytics_232977577.events_*"
title: "storytemplate-10a27.analytics_232977577.events_* · ai组原始埋点表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/storytemplate-10a27.analytics_232977577.events_.md", "ai-knowledge:collart_fashion/tables/storytemplate-10a27.analytics_232977577.events_.md", "ai-knowledge:collart_web/tables/storytemplate-10a27.analytics_232977577.events_.md", "feishu:storytemplate-10a27.analytics_232977577.events_*", "schema:storytemplate-10a27.analytics_232977577.events_*"]
tags: ["events_*", "字段", "schema", "SQLX"]
tables: ["storytemplate-10a27.analytics_232977577.events_*"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# storytemplate-10a27.analytics_232977577.events_* · ai组原始埋点表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `storytemplate-10a27.analytics_232977577.events_*` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | T+1  4:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_timestamp` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_params` | RECORD | REPEATED | 未说明 | 缺口 |
| `event_params.key` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_params.value` | RECORD | NULLABLE | 未说明 | 缺口 |
| `event_params.value.string_value` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_params.value.int_value` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event_params.value.float_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `event_params.value.double_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `event_previous_timestamp` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event_value_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `event_bundle_sequence_id` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event_server_timestamp_offset` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `privacy_info` | RECORD | NULLABLE | 未说明 | 缺口 |
| `privacy_info.analytics_storage` | STRING | NULLABLE | 未说明 | 缺口 |
| `privacy_info.ads_storage` | STRING | NULLABLE | 未说明 | 缺口 |
| `privacy_info.uses_transient_token` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_properties` | RECORD | REPEATED | 未说明 | 缺口 |
| `user_properties.key` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_properties.value` | RECORD | NULLABLE | 未说明 | 缺口 |
| `user_properties.value.string_value` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_properties.value.int_value` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `user_properties.value.float_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `user_properties.value.double_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `user_properties.value.set_timestamp_micros` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `user_first_touch_timestamp` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `user_ltv` | RECORD | NULLABLE | 未说明 | 缺口 |
| `user_ltv.revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `user_ltv.currency` | STRING | NULLABLE | 未说明 | 缺口 |
| `device` | RECORD | NULLABLE | 未说明 | 缺口 |
| `device.category` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_brand_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_model_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_marketing_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_os_hardware_model` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.operating_system` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.operating_system_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.vendor_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.advertising_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.language` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.is_limited_ad_tracking` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.time_zone_offset_seconds` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `device.browser` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.browser_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.web_info` | RECORD | NULLABLE | 未说明 | 缺口 |
| `device.web_info.browser` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.web_info.browser_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.web_info.hostname` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo` | RECORD | NULLABLE | 未说明 | 缺口 |
| `geo.city` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.country` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.continent` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.region` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.sub_continent` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.metro` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_info` | RECORD | NULLABLE | 未说明 | 缺口 |
| `app_info.id` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_info.version` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_info.install_store` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_info.firebase_app_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_info.install_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_source` | RECORD | NULLABLE | 未说明 | 缺口 |
| `traffic_source.name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_source.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_source.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `stream_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_dimensions` | RECORD | NULLABLE | 未说明 | 缺口 |
| `event_dimensions.hostname` | STRING | NULLABLE | 未说明 | 缺口 |
| `ecommerce` | RECORD | NULLABLE | 未说明 | 缺口 |
| `ecommerce.total_item_quantity` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `ecommerce.purchase_revenue_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.purchase_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.refund_value_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.refund_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.shipping_value_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.shipping_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.tax_value_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.tax_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ecommerce.unique_items` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `ecommerce.transaction_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `items` | RECORD | REPEATED | 未说明 | 缺口 |
| `items.item_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_brand` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_variant` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_category` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_category2` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_category3` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_category4` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_category5` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.price_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `items.price` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `items.quantity` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `items.item_revenue_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `items.item_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `items.item_refund_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `items.item_refund` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `items.coupon` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.affiliation` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.location_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_list_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_list_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_list_index` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.promotion_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.promotion_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.creative_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.creative_slot` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_params` | RECORD | REPEATED | 未说明 | 缺口 |
| `items.item_params.key` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_params.value` | RECORD | NULLABLE | 未说明 | 缺口 |
| `items.item_params.value.string_value` | STRING | NULLABLE | 未说明 | 缺口 |
| `items.item_params.value.int_value` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `items.item_params.value.float_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `items.item_params.value.double_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source` | RECORD | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_term` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_content` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_source_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_creative_format` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.manual_marketing_tactic` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.gclid` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.dclid` | STRING | NULLABLE | 未说明 | 缺口 |
| `collected_traffic_source.srsltid` | STRING | NULLABLE | 未说明 | 缺口 |
| `is_active_user` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `batch_event_index` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `batch_page_id` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `batch_ordering_id` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.term` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.content` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.source_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.creative_format` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.manual_campaign.marketing_tactic` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.google_ads_campaign` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.google_ads_campaign.customer_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.google_ads_campaign.account_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.google_ads_campaign.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.google_ads_campaign.campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.google_ads_campaign.ad_group_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.google_ads_campaign.ad_group_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign.campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign.source_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign.default_channel_group` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cross_channel_campaign.primary_channel_group` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.ad_group_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.ad_group_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.creative_format` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.engine_account_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.engine_account_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.sa360_campaign.manager_account_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.account_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.account_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.advertiser_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.advertiser_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.creative_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.creative_format` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.creative_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.creative_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.creative_type_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.creative_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.placement_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.placement_cost_structure` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.placement_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.rendering_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.site_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.cm360_campaign.site_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.advertiser_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.advertiser_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.creative_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.creative_format` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.creative_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.exchange_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.exchange_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.insertion_order_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.insertion_order_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.line_item_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.line_item_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.partner_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `session_traffic_source_last_click.dv360_campaign.partner_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `publisher` | RECORD | NULLABLE | 未说明 | 缺口 |
| `publisher.ad_revenue_in_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `publisher.ad_format` | STRING | NULLABLE | 未说明 | 缺口 |
| `publisher.ad_source_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `publisher.ad_unit_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_original_occurrence_timestamp` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

---

## 事件字段说明：
-  做时间范围过滤时，一定要使用 `_TABLE_SUFFIX`
- `event_date`：事件日期，在该表中不用做分区过滤
- `event_timestamp`：事件发生/接收时间戳，微秒级
- 做精确时间分析时优先使用 `event_timestamp`

## 质量说明:
- 半结构化事件表
- 含重复 RECORD 字段
- 依赖参数字典配合使用
- event_date 和 event_timestamp 含义不同

### 付费模式说明
（旧执行片段已退出发行包；加工依据见 SQLX，只读查询见关联指标。）

注意事项：
- 是核心商业转化事件

### 付费模式说明
用户先免费获得30点数，用完后需订阅；订阅后每周赠送点数，赠送的点数消费完毕后，需要额外购买点数包才能继续使用。

注意事项：
- 建议补充商品信息参数（点数数量、价格等）

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

### 原始事件查询入口

本次 schema 从一个已 finalized 日期分片读取，不保证全部分片字段一致。查询模板由 scripts/query.py raw-events 按项目生成。event_timestamp 为微秒；event_params/user_properties 为 repeated record，按 key 提取避免笛卡尔放大。Web/Fashion 必须同时筛 app_info.id 和页面产品归属，Android/iOS 必须筛 bundle/package。
