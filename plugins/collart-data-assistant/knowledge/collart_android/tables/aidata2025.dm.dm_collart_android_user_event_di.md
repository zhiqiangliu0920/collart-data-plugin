---
id: "table:aidata2025.dm.dm_collart_android_user_event_di"
title: "aidata2025.dm.dm_collart_android_user_event_di"
project: "collart_android"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/dm/daily/h_dm_collart_android_user_event_di.sqlx", "feishu:aidata2025.dm.dm_collart_android_user_event_di", "schema:aidata2025.dm.dm_collart_android_user_event_di"]
tags: ["dm_collart_android_user_event_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dm.dm_collart_android_user_event_di"]
review_required: true
applies_to: []
---

# aidata2025.dm.dm_collart_android_user_event_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dm.dm_collart_android_user_event_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | event_name, user_pseudo_id, country |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `event_time` | DATETIME | NULLABLE | 未说明 | 缺口 |
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `ga_session_id` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `ga_session_number` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `first_open_time` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `is_login` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_vip` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription` | RECORD | NULLABLE | 未说明 | 缺口 |
| `subscription.product_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.price` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.quantity` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.currency` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity` | RECORD | NULLABLE | 未说明 | 缺口 |
| `identity.atlasv_uid` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.android_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.adjust_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.advertising_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo` | RECORD | NULLABLE | 未说明 | 缺口 |
| `geo.city` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.continent` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.sub_continent` | STRING | NULLABLE | 未说明 | 缺口 |
| `device` | RECORD | NULLABLE | 未说明 | 缺口 |
| `device.category` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_brand_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_model_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.operating_system` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.operating_system_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.os_sdk_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.vendor_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.language` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.installer_package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src` | RECORD | NULLABLE | 未说明 | 缺口 |
| `traffic_src.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.fb_campaign` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.adjust_network` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.adjust_tracker_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.adjust_campaign_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.adjust_adgroup` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.campaign_info_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.install_referer_url` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.gclid` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.gad_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.gad_campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.utm_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.utm_medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad` | RECORD | NULLABLE | 未说明 | 缺口 |
| `ad.ad_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.ad_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.ad_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.unit_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.placement` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.segment_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.ad_unit_code` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.reward_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.reward_value` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `ad.ad_value` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.currency` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.is_retry` | STRING | NULLABLE | 未说明 | 缺口 |
| `ad.ab_test_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template` | RECORD | NULLABLE | 未说明 | 缺口 |
| `template.temp_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.module_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.module_title` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.module_index` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.category_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.template_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info` | RECORD | NULLABLE | 未说明 | 缺口 |
| `params_info.service_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.function_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.task_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.gen_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.biz_session_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.model` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.resolution` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.aspect_ratio` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.ratio` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.feature` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.event_from` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.event_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.content_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.page` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.tab_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.credit_cost` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.generate_count` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.duration` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.elapsed` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.engagement_time_msec` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `params_info.is_valid` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.is_free` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.is_frame` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.is_regenerate` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.chance_from` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.image_num` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.style_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.reference_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.change_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.error_code` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.service_code` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.error_msg` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.error_value` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.fail_reason` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.page_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.transaction_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.credit_count` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.purchase_content_mode` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.network_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.first_launch` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.search_keyword` | STRING | NULLABLE | Canonical template-search term extracted from end-specific event params | schema |
| `event_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dm/daily/h_dm_collart_android_user_event_di.sqlx`；仓库 `aidata`，路径 `definitions/dm/daily/h_dm_collart_android_user_event_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.830350+00:00`。同一 SQLX 的产出：`aidata2025.dm.dm_collart_android_user_event_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Android 第一张事件语义明细表
  Dataform: definitions/dm/daily/h_dm_collart_android_user_event_di.sqlx
  目标表: aidata2025.dm.dm_collart_android_user_event_di

  口径:
  - 与 iOS DM 表保持同一加工骨架：DWD event + params + properties
  - Android 包名: free.ai.photo.generator.collart.ai
  - Android 端不存在 device_id 埋点；advertising_id 来自 GA4 原生 device.advertising_id
    （DWD 列名带前导空格 ` advertising_id`，填充率约 99.9%），随 android_id 一并入 identity
  - atlasv_uid 优先取 DWD 事件表同名列，user properties 兜底，并在「当日 × 用户」内广播；
    旧 DWD 用户日表也是从事件表 MAX(atlasv_uid) 得到，二者口径保持一致
  - 渠道字段在「当日 × 用户」维度回填：归因参数只挂在极少数事件上，直接取会几乎全空
  - 渠道两层：traffic_src_type 只表达渠道性质（delivery / inhouse / kol / nature），
    traffic_src_platform 表达具体投放平台（ga_delivery / fb_delivery /
    x_delivery / tt_delivery / other_delivery；非投放沿用 type）。
    Instagram 属于 Meta，IG campaign / source 含 instagram 一律 fb_delivery。
    sptt- / tt_official 等达人命名保持 kol，只有付费 TikTok 才叫 tt_delivery。
  - subscription 存订阅/购点商品快照；Android 广告参数单开 ad STRUCT
  - 金额权威口径不在本表，仍以收入/订单链路为准
  - 后台技术事件（gp_billing_setup / ad_sdk_init / sync_model_info_*）保留在明细层，
    是否算活跃由下游 active 表按「有前台事件」判定
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 2;
DECLARE to_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
DECLARE vip_tech_events ARRAY<STRING> DEFAULT [
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN from_date AND to_date
AND lower(app_name) = 'collart_android'
AND package_name = 'free.ai.photo.generator.collart.ai'
AND user_pseudo_id IS NOT NULL
AND event_name NOT LIKE 'tech%'
AND event_name NOT LIKE 'dev%'
AND event_name NOT IN UNNEST(vip_tech_events)
GROUP BY event_date, package_name, user_pseudo_id, event_name, event_time
GROUP BY package_name, user_pseudo_id
LEFT JOIN event_params AS p
ON e.event_date = p.event_date
AND e.package_name = p.package_name
AND e.user_pseudo_id = p.user_pseudo_id
AND e.event_name = p.event_name
AND e.event_time = DATETIME(TIMESTAMP_MICROS(p.event_time))
LEFT JOIN user_properties AS up
ON e.package_name = up.package_name
AND e.user_pseudo_id = up.user_pseudo_id
```
- 物理上游：`aidata2025.dwd.dwd_oper_user_event_di`
- 物理上游：`aidata2025.dwd.dwd_oper_user_event_params_di`
- 物理上游：`aidata2025.dwd.dwd_oper_user_properties_di`
