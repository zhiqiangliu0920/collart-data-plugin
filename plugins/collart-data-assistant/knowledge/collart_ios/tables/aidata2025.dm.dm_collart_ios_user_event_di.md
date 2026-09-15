---
id: "table:aidata2025.dm.dm_collart_ios_user_event_di"
title: "aidata2025.dm.dm_collart_ios_user_event_di"
project: "collart_ios"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_ios/tables/aidata2025.dm.dm_collart_ios_user_event_di.md", "dataform:aidata/definitions/dm/daily/h_dm_collart_ios_user_event_di.sqlx", "feishu:aidata2025.dm.dm_collart_ios_user_event_di", "schema:aidata2025.dm.dm_collart_ios_user_event_di"]
tags: ["dm_collart_ios_user_event_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dm.dm_collart_ios_user_event_di"]
review_required: true
applies_to: []
---

# aidata2025.dm.dm_collart_ios_user_event_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dm.dm_collart_ios_user_event_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | user_pseudo_id, country |
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
| `identity.adjust_id` | STRING | NULLABLE | DWD 原生列；不要从 event params 提取，近三日 event param 无该 key | 旧文档 |
| `identity.clarity_user_id` | STRING | NULLABLE | 用户维度属性 | 旧文档 |
| `identity.advertising_id` | STRING | NULLABLE | 源列名带前导空格；DM 必须 alias 为无空格标准字段名 | 旧文档 |
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
| `device.vendor_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.language` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src` | RECORD | NULLABLE | 未说明 | 缺口 |
| `traffic_src.src_medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.src_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.ad_group_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.keyword_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template` | RECORD | NULLABLE | 未说明 | 缺口 |
| `template.temp_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.module_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.module_index` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.category_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.banner_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.presret_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `template.template_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info` | RECORD | NULLABLE | 未说明 | 缺口 |
| `params_info.service_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.feature_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.model` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.model_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.submodel_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.task_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.result_task_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.result_generation_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.workspace_task_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.result_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.resolution` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.ratio` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.variations` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `params_info.native_audio` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.credits` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.event_from` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.duration` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.engagement_time_msec` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `params_info.is_retry` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.error_code` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.service_code` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.error_msg` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.api` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.path` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.file_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.url` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.time_ms` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `params_info.success` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.page_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.project_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `params_info.previous_first_open_count` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_name` | STRING | NULLABLE | 未说明 | 缺口 |

## 定义差异与补充

- identity.adjust_id: 旧文档 类型 dwd_oper_user_event_di.adjust_id；schema 类型 STRING
- identity.clarity_user_id: 旧文档 类型 用户属性；schema 类型 STRING
- identity.advertising_id: 旧文档 类型 DWD 历史列 `` ` advertising_id；schema 类型 STRING

## 表专属业务说明

## 2. 核心作用

Collart iOS 新 ADS 体系的统一事件入口。`ads_collartios.ads_oper_user_active_di` 等下游应优先从本表读取身份、渠道、设备和事件字段，不应为补字段反向依赖旧 `dwd_oper_user_basic_di`。

## 5. 数据质量验证（2026-08-07~2026-08-09）

- `adjust_id` 用户填充：843 / 813 / 819。
- `advertising_id` 用户填充：855 / 828 / 827（100%）。
- 对旧 basic 活跃用户逐值对账：两个 ID 三日均 100% 一致。
- Dataform workspace 编译：0 errors。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dm/daily/h_dm_collart_ios_user_event_di.sqlx`；仓库 `aidata`，路径 `definitions/dm/daily/h_dm_collart_ios_user_event_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.787917+00:00`。同一 SQLX 的产出：`aidata2025.dm.dm_collart_ios_user_event_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 2;
DECLARE to_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN from_date AND to_date
and lower(app_name) = 'vidart'
AND package_name = 'ai.photo.video.generator.fotos.ai.image.picture.editor.app.free'
AND user_pseudo_id IS NOT NULL
AND event_name NOT LIKE 'tech%'
AND event_name NOT LIKE 'dev%'
GROUP BY package_name, user_pseudo_id
AND REGEXP_CONTAINS(IFNULL(e.traffic_src_name, ''), r'^[0-9]{6,}$'),
LEFT JOIN event_params AS p
ON e.event_date = p.event_date
AND e.package_name = p.package_name
AND e.user_pseudo_id = p.user_pseudo_id
AND e.event_name = p.event_name
AND e.event_time = DATETIME(TIMESTAMP_MICROS(p.event_time))
LEFT JOIN user_properties AS up
ON e.package_name = up.package_name
AND e.user_pseudo_id = up.user_pseudo_id;
```
- 物理上游：`aidata2025.dwd.dwd_oper_user_event_di`
- 物理上游：`aidata2025.dwd.dwd_oper_user_event_params_di`
- 物理上游：`aidata2025.dwd.dwd_oper_user_properties_di`
