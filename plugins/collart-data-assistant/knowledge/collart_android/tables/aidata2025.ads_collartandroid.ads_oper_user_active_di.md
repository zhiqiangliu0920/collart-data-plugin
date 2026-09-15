---
id: "table:aidata2025.ads_collartandroid.ads_oper_user_active_di"
title: "aidata2025.ads_collartandroid.ads_oper_user_active_di"
project: "collart_android"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_android/ads_oper_user_active_di.sqlx", "feishu:aidata2025.ads_collartandroid.ads_oper_user_active_di", "schema:aidata2025.ads_collartandroid.ads_oper_user_active_di"]
tags: ["ads_oper_user_active_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartandroid.ads_oper_user_active_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartandroid.ads_oper_user_active_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartandroid.ads_oper_user_active_di` |
| 粒度 | event_date × user_pseudo_id（源码说明；需验唯一性） |
| 主键/去重键 | event_date, user_pseudo_id；BigQuery 未声明即不代表强制唯一约束 |
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
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `is_new` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_churn` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_return` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_remove` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_login` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_vip` | STRING | NULLABLE | 未说明 | 缺口 |
| `first_open_time` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_platform` | STRING | NULLABLE | 未说明 | 缺口 |
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
| `subscription` | RECORD | NULLABLE | 未说明 | 缺口 |
| `subscription.product_ids` | STRING | REPEATED | 未说明 | 缺口 |
| `subscription.purchase_cnt` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.is_subscribe` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `subscription.is_credit_pack` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_cnt` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_amount` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.sub_in_7d` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_in_7d` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `subscription.is_purchase` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `revenue` | RECORD | NULLABLE | 未说明 | 缺口 |
| `revenue.purchase_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.resub_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.new_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.trial_conver_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.credit_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.ad_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
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
| `is_active` | BOOLEAN | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_android/ads_oper_user_active_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_android/ads_oper_user_active_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:49.978648+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartandroid.ads_oper_user_active_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Android 第二张表：用户日事实表（活跃 ∪ 当日有收入）
  Dataform: definitions/ads/collart/collart_android/ads_oper_user_active_di.sqlx
  目标表  : aidata2025.ads_collartandroid.ads_oper_user_active_di

  口径要点（依据用户确认）:
  - 粒度: event_date × user_pseudo_id；行 = 当日活跃 OR 当日有订阅/广告收入。
  - is_active = 当日存在 user_engagement/screen_view/app_exception/first_open 任一事件（落表）。
  - 付费-only 行 is_active=FALSE；维度取最近一次活跃快照；retain/churn/return 仅基于活跃日。
  - 下游: DAU/新增/留存/流失/回流滤 is_active；SUM(revenue) 不过滤。
  - is_new   = 当日存在 first_open（付费-only 为 FALSE）。
  - is_churn = 该活跃日后 14 日均未再次活跃；未来观察窗未完整时置 NULL。
  - is_return = 当日活跃、非新增，且此前 14 日均未活跃；历史观察窗不足时置 NULL。
  - identity / geo / device / traffic_src 结构与上游 dm_collart_android_user_event_di 保持一致，
    维度默认取「当日最后一个事件」快照；atlasv_uid 直接取 DM identity。
  - first_open_time 即老表 register_time（已改名）：取 DM 当日 first_open 事件时间，
    不能从当日最后事件快照取值；不再依赖旧 DWD。
  - subscription:
      product_ids       当日 vip_subscribe_succeed 命中的商品（去重合并，ARRAY）
      purchase_cnt      当日付费成功次数（vip_subscribe_succeed）
      is_subscribe      当日是否订阅（product_id LIKE 'collart_premium%'）
      is_credit_pack    当日是否购买点数包（product_id LIKE 'credits_pack%'）
      credit_pack_cnt   当日点数包购买次数
      credit_amount     当日购买点数数量（从 credits_pack_*_N 商品名尾号解析求和）
      sub_in_7d         次日起 7 天内是否发生订阅（date_diff 1..7，前视窗口）
      credit_pack_in_7d 次日起 7 天内是否购买点数包
  - revenue（当日购买贡献，来自 dws 权威收入表，按当日归属）:
      purchase_revenue      = dws.total_revenue_today（= SUM(全部订单 revenue)，**已含点数包**）
      resub_revenue         = dws.resub_revenue_today（subscribe_type=renew）
      new_revenue           = dws.new_revenue_today - credit_revenue_today（首购订阅，**不含点数包**）
      trial_conver_revenue  = dws.trial_conver_revenue_today
      credit_revenue        = dws.credit_revenue_today（order_type=点数包，是 total 的子集）
      ad_revenue            = dws_oper_user_ad_di.ad_value
      俄罗斯收银（RUB）叠加 Stripe `dwd_cdct_revenue_stripe_di`（app_name=collart_android）：
      金额加进 purchase_revenue 与 credit_revenue（与历史 ads_ad_sub 俄收入全算点数包一致）
      注: 勿再 purchase=total+credit，会把点数双计；total ≈ new+resub+trial+credit（四桶互斥）
  - retain / rolling_retain: 以每个活跃日为锚点（rolling cohort）；字段编号对齐旧表 retain_N。
      retain.dN         = 锚点后第 (N-1) 天当天活跃（date_diff = N-1）；**retain.d2 = 次日**
      rolling_retain.dN = 锚点后 [1, N-1] 天内任一天活跃（累计留存）
      字段范围 d2–d30（无 d1）；前视未到期置 NULL，随每日回刷逐步定稿。

  刷新窗口: 为覆盖 29 日前视留存，DELETE/INSERT 回刷 [biz_date-30, biz_date]。
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 30;
DECLARE to_date   DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
DECLARE source_from_date DATE DEFAULT from_date - 14;
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN source_from_date AND to_date
AND user_pseudo_id IS NOT NULL
GROUP BY event_date, user_pseudo_id
WHERE rn = 1
JOIN last_ev AS l USING (event_date, user_pseudo_id)
WHERE a.is_active
WHERE event_date BETWEEN from_date AND to_date
WHERE order_date BETWEEN from_date AND to_date
AND LOWER(app_name) = 'collart_android'
GROUP BY order_date, user_pseudo_id
AND IFNULL(revneue, 0) > 0
AND user_id IS NOT NULL AND TRIM(CAST(user_id AS STRING)) != ''
AND UPPER(currency) = 'RUB'
AND LOWER(REPLACE(IFNULL(app_name, ''), '_', '-')) = 'collart-android'
AND transaction_id IS NOT NULL
QUALIFY ROW_NUMBER() OVER (
PARTITION BY CAST(transaction_id AS STRING)
ORDER BY event_timestamp DESC, revneue DESC
WHERE user_id IS NOT NULL AND TRIM(CAST(user_id AS STRING)) != ''
GROUP BY event_date, user_id
WHERE event_date < from_date
AND event_date >= DATE_SUB(from_date, INTERVAL 400 DAY)
GROUP BY user_id
LEFT JOIN uid_map_day AS d
ON d.event_date = r.event_date AND d.user_id = r.user_id
LEFT JOIN uid_map_hist AS h
ON h.user_id = r.user_id
WHERE COALESCE(d.user_pseudo_id, h.user_pseudo_id) IS NOT NULL
GROUP BY 1, 2
WHERE IFNULL(total_revenue, 0) > 0
WHERE IFNULL(ad_revenue, 0) > 0
WHERE IFNULL(rub_revenue, 0) > 0
LEFT JOIN active AS a USING (event_date, user_pseudo_id)
WHERE a.user_pseudo_id IS NULL
AND IFNULL(is_active, TRUE)
LEFT JOIN (
PARTITION BY p2.event_date, p2.user_pseudo_id
ORDER BY d2.event_date DESC
JOIN dim_src AS d2
ON d2.user_pseudo_id = p2.user_pseudo_id
AND d2.event_date <= p2.event_date
ON d.pay_date = p.event_date
AND d.user_pseudo_id = p.user_pseudo_id
LEFT JOIN purch_day AS b
ON a.user_pseudo_id = b.user_pseudo_id
AND DATE_DIFF(b.event_date, a.event_date, DAY) BETWEEN 1 AND 7
AND (b.is_sub OR b.is_credit)
GROUP BY a.event_date, a.user_pseudo_id
JOIN active_all AS b
AND DATE_DIFF(b.event_date, a.event_date, DAY) BETWEEN 1 AND 29
WHERE n.user_pseudo_id = a.user_pseudo_id
AND DATE_DIFF(n.event_date, a.event_date, DAY) BETWEEN 1 AND 14
WHERE p.user_pseudo_id = a.user_pseudo_id
AND DATE_DIFF(a.event_date, p.event_date, DAY) BETWEEN 1 AND 14
CROSS JOIN coverage AS c
LEFT JOIN lifecycle_flags AS lf USING (event_date, user_pseudo_id)
LEFT JOIN fwd AS fw USING (event_date, user_pseudo_id)
LEFT JOIN retain_flags AS rf USING (event_date, user_pseudo_id)
LEFT JOIN sub_rev AS sr USING (event_date, user_pseudo_id)
LEFT JOIN ad_rev AS ar USING (event_date, user_pseudo_id)
LEFT JOIN rub_rev AS rr USING (event_date, user_pseudo_id);
```
- 物理上游：`aidata2025.dm.dm_collart_android_user_event_di`
- 物理上游：`aidata2025.dws.dws_oper_user_ad_di`
- 物理上游：`aidata2025.dws.dws_oper_user_sub_revenue_df`
- 物理上游：`pubdata2025.dwd.dwd_cdct_revenue_stripe_di`

活跃、留存与维度选择筛 is_active；金额保留付费-only 行。profile 和指标层关联要用产品 × event_date × user_pseudo_id，避免只按用户跨日放大。
