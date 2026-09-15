---
id: "table:aidata2025.ods.orders"
title: "aidata2025.ods.orders"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_fashion/tables/aidata2025.ods.orders.md", "ai-knowledge:collart_web/tables/aidata2025.ods.orders.md", "schema:aidata2025.ods.orders"]
tags: ["orders", "字段", "schema", "SQLX"]
tables: ["aidata2025.ods.orders"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ods.orders

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ods.orders` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `id` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `product_id` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `product_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `quantity` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `total_price` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `currency` | STRING | NULLABLE | 未说明 | 缺口 |
| `payment_channel` | STRING | NULLABLE | 未说明 | 缺口 |
| `stripe_session_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `stripe_payment_intent_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `stripe_subscription_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `stripe_customer_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `enjoypay_order_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `enjoypay_subscription_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `payermax_order_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `payermax_subscription_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `renewal_notified_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `payinsider_order_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `payinsider_subscription_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `payinsider_customer_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `meta_event_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `meta_event_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `meta_capi_reported_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `meta_capi_report_error` | STRING | NULLABLE | 未说明 | 缺口 |
| `tiktok_events` | STRING | NULLABLE | 未说明 | 缺口 |
| `status` | STRING | NULLABLE | 说明 | 旧文档 |
| `price_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `paid_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `subscription_start_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `subscription_end_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `current_period_start_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `current_period_end_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |
| `cancel_reason` | STRING | NULLABLE | 未说明 | 缺口 |
| `created_at` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `updated_at` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `deleted_at` | BIGNUMERIC | NULLABLE | 未说明 | 缺口 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `active` | ✅ 是 | 订阅类订单生效中 |
| `active_ending` | ✅ 是 | 订阅即将到期但仍属有效付费 |
| `canceled` | ❌ 否 | 订单已取消（2026-08-18 补充） |
| `expired` | ❌ 否 | 订单已过期/失败 |
| `failed` | ❌ 否 | 支付失败（2026-08-18 补充） |
| `paid` | ✅ 是 | 一次性购买（如点数包）已支付 |
| `pending` | ❌ 否 | 支付未完成或待确认；**仅有 orders 记录、无 `vip_subscribe_succeed` 时常见** |

## 定义差异与补充

- status: 旧文档 类型 是否计入付费/收入；schema 类型 STRING

## 表专属业务说明

## 2. 核心作用
本表主要用于以下场景：
1. 关联user_id字段，计算每个用户的价值贡献，对用户进行价值分层
2. 计算不同场景、设备、国家的用户价值贡献分布

> **2026-08-28 起不再作为用户粒度收入真值**（推荐 vs 历史）：
> Web 用户粒度收入、以及移动端俄罗斯支付用户粒度收入，一律改用
> `pubdata2025.dwd.dwd_cdct_revenue_stripe_di`（T+1），或各端 `ads_oper_user_active_di.revenue`。
> `dwd_cdct_orders_revenue_hi` 是空表，不要当补洞。
> 本表仅作历史对照或排查，新分析不要再 `JOIN` / 扫 `ods.orders` 算收入。

## 6. 数据质量与风险提示

- 未过滤 `status` 时，pending 订单数量可能很多（用户多次发起订阅未成功）
- `total_price` 单位为分，需 `/100` 并关联 `dim.exchange_rate_days` 换算美元
- 时间字段用 `created_at`（非仅 `event_date`）查精确付费时刻；展示北京时间：`DATETIME(TIMESTAMP(created_at), 'Asia/Shanghai')`

## 2. 核心作用
本表主要用于以下场景：
1. 关联user_id字段，计算每个用户的价值贡献，对用户进行价值分层
2. 计算不同场景、设备、国家的用户价值贡献分布

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
