---
id: "table:aidata2025.ads_collart.ads_vip_user_info_all"
title: "aidata2025.ads_collart.ads_vip_user_info_all"
project: "shared"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/ads_vip_user_info_all.sqlx", "feishu:aidata2025.ads_collart.ads_vip_user_info_all", "schema:aidata2025.ads_collart.ads_vip_user_info_all"]
tags: ["ads_vip_user_info_all", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collart.ads_vip_user_info_all"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads_collart.ads_vip_user_info_all

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collart.ads_vip_user_info_all` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | app_name, user_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `is_r` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `first_open_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `last_active_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `device_category` | STRING | NULLABLE | 未说明 | 缺口 |
| `device_operating_system` | STRING | NULLABLE | 未说明 | 缺口 |
| `mobile_brand_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `browser` | STRING | NULLABLE | 未说明 | 缺口 |
| `last_order_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `total_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `weekly_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `monthly_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `yearly_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `pack_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `sexual_score` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `task_num` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `succeed_task_num` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `cost_point` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `total_revenue_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `total_revenue_type2` | STRING | NULLABLE | 未说明 | 缺口 |
| `hv_user_tag` | STRING | NULLABLE | 未说明 | 缺口 |
| `event` | RECORD | NULLABLE | 未说明 | 缺口 |
| `event.video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event.video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event.img_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event.img_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/ads_vip_user_info_all.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/ads_vip_user_info_all.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:49.242223+00:00`。同一 SQLX 的产出：`aidata2025.ads_collart.ads_vip_user_info_all`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart 三端 VIP / 高价值用户合并表（日全量刷新）
  Dataform: definitions/ads/collart/ads_vip_user_info_all.sqlx
  目标表  : aidata2025.ads_collart.ads_vip_user_info_all

  口径:
  - 粒度: app_name × user_id
  - 收入 spine: Android 订单 / Web orders / iOS Apple 订阅（按产品周期拆 weekly/monthly/yearly/pack）
  - is_r: ads_high_value_user_production 中出现的 (app_name, user_id) 记为 1，否则 0
  - 基础维度: 三端 ads_oper_user_profile_df（按 first_open_date 取首次归因）
  - Web: UNNEST(user_ids) 挂每一个登录号；同设备多账号共享该设备首次归因，不再只挂最后一个 user_id
  - event: ods_ai_request_info_new_1d 终身生成次数（atlas_uid=user_id；smart_gen 算生图，不算视频）
  - 生成任务: ods_ai_request_info_new_1d sexual 审核分（近 270 天）
    sexual_score 取 moderation_text[].severity（该数据源无 probability 字段）
  - hv_user_tag: 近 270 天 sexual 任务按 created_at DESC 排序，
    COUNT(task_id)<50 → unknown；
    最近 50 次中 sexual_score>=0.6 占比>=0.3 → nsfw；否则 clean
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
WHERE package_name = 'free.ai.photo.generator.collart.ai'
AND user_id IS NOT NULL
GROUP BY ALL
where event_Date>='2025-01-01'
and charge_type != 'expired'
group by all
WHERE package_name = 'ai.photo.video.generator.fotos.ai.image.picture.editor.app.free'
AND event_date >= '2026-03-01'
WHERE user_id IS NOT NULL AND user_id != ''
GROUP BY app_name, user_id
AND user_id IS NOT NULL AND user_id != ''
CROSS JOIN UNNEST(
WHERE uid IS NOT NULL AND uid != ''
AND (
WHERE app_name IN ('collart-android', 'collart-web', 'vidart-ios', 'collart-ios')
AND atlas_uid IS NOT NULL AND atlas_uid != ''
GROUP BY 1, 2
PARTITION BY a.app_name, a.atlas_uid
ORDER BY a.created_at DESC
CROSS JOIN UNNEST(JSON_EXTRACT_ARRAY(request, '$.moderation_text')) AS item
WHERE a.event_date >= CURRENT_DATE() - 270
AND a.app_name IN ('collart-android', 'collart-web', 'collart-ios')
AND JSON_VALUE(item, '$.category') = 'sexual'
AND a.atlas_uid IS NOT NULL
full JOIN is_r_info AS b
ON a.user_id = b.user_id AND a.app_name = b.app_name
LEFT JOIN user_basic_info AS c
ON COALESCE(a.user_id, b.user_id) = c.user_id
AND COALESCE(a.app_name, b.app_name) = c.app_name
LEFT JOIN task_info AS d
ON COALESCE(a.user_id, b.user_id) = d.user_id
AND COALESCE(a.app_name, b.app_name) = d.app_name
LEFT JOIN ods_event AS e
ON COALESCE(a.user_id, b.user_id) = e.user_id
AND COALESCE(a.app_name, b.app_name) = e.app_name
```
- 物理上游：`aidata2025.ads.ads_high_value_user_production`
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_user_profile_df`
- 物理上游：`aidata2025.ads_collartios.ads_oper_user_profile_df`
- 物理上游：`aidata2025.ads_collartweb.ads_oper_user_profile_df`
- 物理上游：`aidata2025.dwd.dwd_apple_user_subscribtion_di`
- 物理上游：`aidata2025.dwd.dwd_oper_sub_order_revenue_df`
- 物理上游：`aidata2025.ods.ods_ai_request_info_new_1d`
