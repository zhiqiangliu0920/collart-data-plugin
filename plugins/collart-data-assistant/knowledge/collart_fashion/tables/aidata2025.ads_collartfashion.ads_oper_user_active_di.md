---
id: "table:aidata2025.ads_collartfashion.ads_oper_user_active_di"
title: "aidata2025.ads_collartfashion.ads_oper_user_active_di"
project: "collart_fashion"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_fashion/tables/aidata2025.ads_collartfashion.ads_oper_user_active_di.md", "dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_user_active_di.sqlx", "feishu:aidata2025.ads_collartfashion.ads_oper_user_active_di", "schema:aidata2025.ads_collartfashion.ads_oper_user_active_di"]
tags: ["ads_oper_user_active_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartfashion.ads_oper_user_active_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartfashion.ads_oper_user_active_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartfashion.ads_oper_user_active_di` |
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
| `identity.clarity_user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.clarity_session_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `identity.atlasv_id` | STRING | NULLABLE | 未说明 | 缺口 |
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
| `device.browser` | STRING | NULLABLE | 未说明 | 缺口 |
| `device.browser_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src` | RECORD | NULLABLE | 未说明 | 缺口 |
| `traffic_src.source` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.medium` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.campaign` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.campaign_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.term` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src.content` | STRING | NULLABLE | 未说明 | 缺口 |
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
| `is_studio_active` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_studio_new` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_from_main_web` | BOOLEAN | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

## 2. 核心作用

- 提供 Fashion 用户日活、渠道、国家、设备、留存等用户级维度。
- 自 2026-08-27 起承接 Fashion Stripe 用户日收入，写入 `revenue.purchase_revenue`。
- 作为 `ads_oper_user_profile_df`、`ads_oper_basic_indicator_attr_di` 和事件指标表的上游。

## 3. 收入字段

- `revenue.purchase_revenue`：该 `user_id` 当日 Fashion Stripe 实收（含点数包）。
- `revenue.new_revenue` / `resub_revenue` / `credit_revenue`：按订单 `description_type` 拆桶。
- `subscription.purchase_cnt` / `is_credit_pack` / `credit_pack_cnt` / `credit_amount`：与订单表同口径；`is_purchase` 在埋点或 `purchase_cnt>0` 时为真。
- 同一 `event_date × user_id` 只落到一个 `user_pseudo_id`。
- 国家空值用 Stripe `country`，仍空则 `unknown`。

## 6. 数据质量

- 2026-07-11～2026-09-08：订单 / active / attr / country / daily 均为 $632.59；用户日 33 行字段 0 差异。
- 纯支付补行不计 DAU。Stripe 二字码（如 `ID`）可能与 GA4 国名并存。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_user_active_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_fashion/ads_oper_user_active_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:50.478784+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartfashion.ads_oper_user_active_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Fashion 第二张表：用户日明细（活跃 + 收入补充）
  Dataform: definitions/ads/collart/collart_fashion/ads_oper_user_active_di.sqlx
  目标表  : aidata2025.ads_collartfashion.ads_oper_user_active_di

  【已确认口径 2026-08-11】见 OPEN_QUESTIONS_WEB_FASHION.md
  - DM 过滤: package_name = 'collart_fashion'（ads 层 package_name 统一为 'collart_fashion'）
  - 粒度: event_date × user_pseudo_id；包含活跃用户及收入用户补充行
  - is_active = page_view / user_engagement / session_start / first_visit（含 SEO）
  - is_active 落表：真实活跃行为为 TRUE；无同日 Fashion 行为的收入补充行为 FALSE
  - is_new   = first_visit（含 SEO，不改）
  - is_login = 当日任意 Fashion 事件 user_id 非空
  - is_studio_active = 当日 page.location 含 /studio
  - is_studio_new = 当天 is_studio_active 且当天 is_new（first_visit）
  - is_from_main_web = 当日或更早主站 active 有过该 pseudo / user_id
  - is_vip: 保留原始值('0'/'1')；下游 VIP 判定用 is_vip IN ('1','2')
  - 经营 DAU/DNU（basic attr）只留 is_studio_active；UEM / 事件表不再按 studio 过滤
  - 收入补行仍 is_active=FALSE
  - 收入: ads_oper_user_revenue_di 按用户日写入 revenue / subscription（purchase=全额，credit 另拆）；同一用户日仅落一个 pseudo
  - 刷新: DELETE/INSERT [biz_date-30, biz_date]
  - 禁止改动其他 dataset 表
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
AND package_name = 'collart_fashion'
AND user_pseudo_id IS NOT NULL
GROUP BY event_date, user_pseudo_id
WHERE is_active
AND event_date <= to_date
GROUP BY 1
AND NULLIF(user_id, '') IS NOT NULL
PARTITION BY event_date, user_pseudo_id
ORDER BY event_time DESC
WHERE rn = 1
WHERE traffic_src_type = 'delivery'
JOIN last_ev AS l USING (event_date, user_pseudo_id)
LEFT JOIN delivery_ev AS d USING (event_date, user_pseudo_id)
LEFT JOIN web_first_pseudo AS wp ON a.user_pseudo_id = wp.user_pseudo_id
LEFT JOIN web_first_uid AS wu ON NULLIF(l.user_id, '') = wu.user_id
WHERE a.is_active
WHERE event_date BETWEEN from_date AND to_date
GROUP BY event_date, user_id
JOIN active AS a USING (event_date, user_id)
QUALIFY ROW_NUMBER() OVER (
PARTITION BY r.event_date, r.user_id
ORDER BY a.user_pseudo_id = r.user_pseudo_id DESC, a.user_pseudo_id
WHERE NULLIF(user_id, '') IS NOT NULL
WHERE event_date BETWEEN DATE '2026-06-01' AND from_date - 1
JOIN user_dim_candidates AS h
ON (r.user_pseudo_id = h.user_pseudo_id OR r.user_id = h.user_id)
AND h.event_date <= DATE_ADD(r.event_date, INTERVAL 1 DAY)
QUALIFY ROW_NUMBER() OVER (PARTITION BY r.event_date, r.user_id ORDER BY h.event_date DESC, h.user_pseudo_id) = 1
LEFT JOIN direct_revenue_target AS d USING (event_date, user_id)
LEFT JOIN historical_revenue_target AS h USING (event_date, user_id)
WHERE r.target_user_pseudo_id IS NOT NULL
AND NOT EXISTS (
WHERE a.event_date = r.event_date
AND a.user_pseudo_id = r.target_user_pseudo_id
JOIN active_all AS b
ON a.user_pseudo_id = b.user_pseudo_id
AND DATE_DIFF(b.event_date, a.event_date, DAY) BETWEEN 1 AND 29
WHERE n.user_pseudo_id = a.user_pseudo_id
AND DATE_DIFF(n.event_date, a.event_date, DAY) BETWEEN 1 AND 14
WHERE p.user_pseudo_id = a.user_pseudo_id
AND DATE_DIFF(a.event_date, p.event_date, DAY) BETWEEN 1 AND 14
CROSS JOIN coverage AS c
LEFT JOIN lifecycle_flags AS lf USING (event_date, user_pseudo_id)
LEFT JOIN retain_flags AS rf USING (event_date, user_pseudo_id)
LEFT JOIN revenue_target AS rv
ON f.event_date = rv.event_date
AND f.user_pseudo_id = rv.target_user_pseudo_id
```
- 物理上游：`aidata2025.ads_collartfashion.ads_oper_user_revenue_di`
- 物理上游：`aidata2025.ads_collartweb.ads_oper_user_active_di`
- 物理上游：`aidata2025.dm.dm_collart_web_user_event_di`

活跃、留存与维度选择筛 is_active；金额保留付费-only 行。profile 和指标层关联要用产品 × event_date × user_pseudo_id，避免只按用户跨日放大。
