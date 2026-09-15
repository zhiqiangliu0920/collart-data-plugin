---
id: "table:aidata2025.ads_collartandroid.ads_oper_user_profile_df"
title: "aidata2025.ads_collartandroid.ads_oper_user_profile_df"
project: "collart_android"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_android/ads_oper_user_profile_df.sqlx", "feishu:aidata2025.ads_collartandroid.ads_oper_user_profile_df", "schema:aidata2025.ads_collartandroid.ads_oper_user_profile_df"]
tags: ["ads_oper_user_profile_df", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartandroid.ads_oper_user_profile_df"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartandroid.ads_oper_user_profile_df

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartandroid.ads_oper_user_profile_df` |
| 粒度 | 每个 user_pseudo_id 一行（源码说明；账号不是主键） |
| 主键/去重键 | user_pseudo_id；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | user_pseudo_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `first_open_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `first_open_time` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `register_app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `last_active_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `last_app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `current_active_days` | RECORD | NULLABLE | 未说明 | 缺口 |
| `current_active_days.d7` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `current_active_days.d14` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `current_active_days.d30` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `current_active_days.d90` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `current_active_days.d360` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `current_is_churn_14d` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_vip` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_remove_on_first_open` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_ever_remove` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `identity` | RECORD | NULLABLE | 未说明 | 缺口 |
| `identity.atlasv_uid` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.android_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.adjust_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.advertising_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `geo` | RECORD | NULLABLE | 未说明 | 缺口 |
| `geo.country` | STRING | NULLABLE | 未说明 | 缺口 |
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
| `traffic_src.name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.type` | STRING | NULLABLE | 未说明 | 缺口 |
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
| `subscription` | RECORD | NULLABLE | 未说明 | 缺口 |
| `subscription.first_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `subscription.first_product_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.first_app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.last_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `subscription.last_product_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.last_app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription.purchase_cnt_all` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_cnt_all` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_amount_all` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue` | RECORD | NULLABLE | 未说明 | 缺口 |
| `revenue.purchase_revenue_all` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.subscription_revenue_all` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.credit_revenue_all` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.ad_revenue_all` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.total_revenue_all` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ltv` | RECORD | NULLABLE | 未说明 | 缺口 |
| `ltv.d1` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ltv.d7` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ltv.d30` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ltv.d90` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ltv.d360` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `retain` | RECORD | NULLABLE | 未说明 | 缺口 |
| `retain.d2` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d3` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d4` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d5` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d6` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d7` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d8` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d9` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d10` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d11` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d12` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d13` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d14` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d15` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d16` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d17` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d18` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d19` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d20` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d21` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d22` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d23` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d24` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d25` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d26` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d27` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d28` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d29` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `retain.d30` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain` | RECORD | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d2` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d3` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d4` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d5` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d6` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d7` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d8` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d9` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d10` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d11` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d12` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d13` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d14` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d15` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d16` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d17` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d18` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d19` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d20` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d21` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d22` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d23` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d24` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d25` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d26` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d27` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d28` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d29` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d30` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `profile_updated_at` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `event` | RECORD | NULLABLE | 未说明 | 缺口 |
| `event.video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event.video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event.img_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event.img_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_android/ads_oper_user_profile_df.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_android/ads_oper_user_profile_df.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:50.016579+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartandroid.ads_oper_user_profile_df`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Android 第三张表：用户生命周期画像（1 用户 1 行）
  Dataform: definitions/ads/collart/collart_android/ads_oper_user_profile_df.sqlx
  目标表  : aidata2025.ads_collartandroid.ads_oper_user_profile_df

  更新方式：只 MERGE 近 3 日在新 active / UEM 中有变化的用户。
  event：终身事件 PV，来自 ads_oper_user_event_metric_di 对用户 SUM(*_pv)。

  历史骨架已于 2026-08 由旧表一次性补齐，脚本不再随日常调度保留，

  收入 / LTV：全部来自 SUM(active.revenue)，不再回扫 DWS 订阅/广告表。
  Stripe RUB 已写入 active.revenue（purchase + credit），profile 不再二次叠加。
  LTV 桶只用 purchase_revenue，不含广告。

  is_active 分流（active 表含「付费-only」行 is_active=FALSE）:
  - 活跃类（last_active_date / current_active_days / 14 日流失 / retain / 首次归因与维度快照）
    仅取 is_active=TRUE 行；
  - 订阅次数与收入 / LTV 不过滤 is_active，付费-only 行照常累计。
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE biz_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
DECLARE change_from_date DATE DEFAULT biz_date - 2;
WHERE event_date BETWEEN change_from_date AND biz_date
AND user_pseudo_id IS NOT NULL
JOIN changed_users AS c USING (user_pseudo_id)
ORDER BY IF(traffic_src_type = 'delivery', 0, 1), event_date
WHERE is_active
GROUP BY user_pseudo_id
LEFT JOIN `aidata2025.ads_collartandroid.ads_oper_user_profile_df` AS p USING (user_pseudo_id)
LEFT JOIN active_profile AS a USING (user_pseudo_id)
GROUP BY r.user_pseudo_id
GROUP BY e.user_pseudo_id
LEFT JOIN purchase_profile AS p USING (user_pseudo_id)
LEFT JOIN rev_profile AS rv USING (user_pseudo_id)
LEFT JOIN ltv_profile AS ltv USING (user_pseudo_id)
LEFT JOIN event_profile AS ev USING (user_pseudo_id)
ON t.user_pseudo_id = s.user_pseudo_id
WHEN MATCHED THEN UPDATE SET
WHEN NOT MATCHED THEN INSERT (
```
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_user_active_di`
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_user_event_metric_di`

画像是设备粒度。按登录号检索用 user_id = @user_id OR @user_id IN UNNEST(user_ids)（字段存在时）；多账号/多设备需单独归并。滚动活跃只随触达的 MERGE 行更新，历史未变设备可能不是今天状态。
