---
id: "table:aidata2025.dm.dm_collart_web_user_event_di"
title: "aidata2025.dm.dm_collart_web_user_event_di"
project: "shared"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/dm/daily/h_dm_collart_web_user_event_di.sqlx", "feishu:aidata2025.dm.dm_collart_web_user_event_di", "schema:aidata2025.dm.dm_collart_web_user_event_di"]
tags: ["dm_collart_web_user_event_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dm.dm_collart_web_user_event_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dm.dm_collart_web_user_event_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dm.dm_collart_web_user_event_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | package_name, event_name, user_pseudo_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `event_time` | DATETIME | NULLABLE | 未说明 | 缺口 |
| `event_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `is_login` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_vip` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `ga_session_id` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `ga_session_number` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `session_engaged` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `engagement_time_msec` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `first_open_time` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `page` | RECORD | NULLABLE | 未说明 | 缺口 |
| `page.location` | STRING | NULLABLE | 未说明 | 缺口 |
| `page.title` | STRING | NULLABLE | 未说明 | 缺口 |
| `page.referrer` | STRING | NULLABLE | 未说明 | 缺口 |
| `page.name` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo` | RECORD | NULLABLE | 未说明 | 缺口 |
| `geo.city` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.continent` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo.sub_continent` | STRING | NULLABLE | 未说明 | 缺口 |
| `device` | RECORD | NULLABLE | 未说明 | 缺口 |
| `device.device_category` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_brand_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.mobile_model_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.operating_system` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.device_operating_system_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.device_vendor_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.device_language` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.browser` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.browser_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic` | RECORD | NULLABLE | 未说明 | 缺口 |
| `traffic.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic.campaign` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic.term` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic.content` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity` | RECORD | NULLABLE | 未说明 | 缺口 |
| `identity.clarity_user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.clarity_session_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.atlasv_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription` | RECORD | NULLABLE | 未说明 | 缺口 |
| `subscription.product_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.price` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.currency` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.points` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.product_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info` | RECORD | NULLABLE | 未说明 | 缺口 |
| `web_params_info.service_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.task_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.feature` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.event_from` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.category` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.module_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.entry` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.template_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.list_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.result_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.result_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.target_path` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.total_ms` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `web_params_info.success` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.model` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.model_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.model_value` | STRING | NULLABLE | 未说明 | 缺口 |
| `web_params_info.search_keyword` | STRING | NULLABLE | Canonical template-search term extracted from end-specific event params | schema |
| `fashion_params_info` | RECORD | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.step` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.module_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.template_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.model_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.model_preset_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.outfit_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.outfit_preset_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.outfit_count` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.video_model` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.resolution` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.bgm_enabled` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.has_prompt` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.has_scene` | STRING | NULLABLE | 未说明 | 缺口 |
| `fashion_params_info.generate_count` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `traffic_src_platform` | STRING | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dm/daily/h_dm_collart_web_user_event_di.sqlx`；仓库 `aidata`，路径 `definitions/dm/daily/h_dm_collart_web_user_event_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.788801+00:00`。同一 SQLX 的产出：`aidata2025.dm.dm_collart_web_user_event_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
WHERE event_date BETWEEN from_date AND to_date;
WHERE up.key = 'clarity_user_id'
WHERE up.key IN ('is_vip', 'vip_type')
WHERE up.key = 'from_app'
WHERE up.key = 'traffic_srouce_name'
WHERE ( _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', from_date)
AND FORMAT_DATE('%Y%m%d', to_date)
AND CONCAT('intraday_', FORMAT_DATE('%Y%m%d', to_date))
AND app_info.id IS NULL
AND user_pseudo_id IS NOT NULL
AND event_name NOT LIKE 'tech%'
AND event_name NOT LIKE 'dev%'
AND event_name NOT IN (
```
- 物理上游：`storytemplate-10a27.analytics_232977577.events_*`
