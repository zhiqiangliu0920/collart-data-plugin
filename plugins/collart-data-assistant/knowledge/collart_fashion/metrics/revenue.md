---
id: "fashion.revenue"
title: "Fashion 收入归属与 Web 交集"
project: "collart_fashion"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_fashion/indicators/fashion_revenue.md", "ai-knowledge:collart_fashion/lineage/revenue_pipeline.md", "dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_user_revenue_di.sqlx", "previous:collart_fashion-revenue-boundary", "schema:aidata2025.ads_collartfashion.ads_oper_user_revenue_di"]
tags: ["Fashion", "收入", "交集", "Web", "600秒"]
tables: ["aidata2025.ads_collartfashion.ads_oper_user_revenue_di", "pubdata2025.dwd.dwd_cdct_revenue_stripe_di"]
---

# Fashion 收入归属与 Web 交集

## 金额、粒度与默认来源

金额真值为 Stripe 的 `revneue`；按 `transaction_id` 去重。Fashion 默认订单表为 `aidata2025.ads_collartfashion.ads_oper_user_revenue_di`，一笔 Stripe 交易一行。用户日与上卷金额分别查看 active、attr/country/daily，不能把层间粒度直接混加。

## 交易归属

按当前订单表文档及2026-08-28 支付直连规则：

1. Stripe 限定 `app_name='collart_web'`、`revneue>0`，以非空 `user_id` 关联支付成功事件。
2. 每笔交易查同一 `user_id` 前后 600 秒内的 `vip_subscribe_succeed`，选择最近事件。
3. 最近事件的 `package_name` 必须为 `collart_fashion`；最近事件属于主站或没有时间近邻时，不归入 Fashion。
4. 使用交易时间与事件时间比较，避免用两侧业务日期相等代替时间匹配；收入日期保留 Stripe `event_date`。
5. 排除内部用户；`vip_subscribe_succeed` 提供场景归属，不替代 Stripe 金额。

## 用户日与 DAU

订单按用户日进入 active；仅收入补齐行可为 `is_active=FALSE`。统计 DAU 必须按活跃标志，不把所有收入行计入活跃。购买事件人数、交易笔数和收入分别定义，不能因存在 Stripe 金额就推定客户端购买事件发生。

## 历史版本与待核验边界

- 整理前完整原文中的“首次 Fashion succeed 后全部 Stripe 收入归 Fashion”已被支付时间近邻方法替代，可能误把后续主站购买归入 Fashion。
- 旧 GA4 URL/价格估算金额、旧用户日收入表和旧每日收入表仅留作历史。
- 2026-08-28 为已有文档记载的归属规则生效日；本次仅完成跨文档一致性整理，不宣称重新验证当前线上实现。
- 重复事件时间完全相同时的稳定取舍、迟到事件回刷覆盖仍应在具体查询中核对。

业务演进依据：2026-08-27、08-28、09-09 的原文；整理不改变这些日期。

当前文档链路为 Stripe 订单 → 按同一 user_id、付款时间前后 600 秒最近的 `vip_subscribe_succeed` 判业务归属 → Fashion 订单表 → 用户日 active / 汇总。保留 Stripe event_date；收入字段为 `revneue`，按 transaction_id 去重。

| 旧入口 | 原状态日期 | 变化与当前替代 |
|---|---|---|
| `ads_collart.ads_oper_revenue_collart_fashion_di` | 2026-09-09 删除 | 原为 event_date 日汇总，字段 event_date、package_name、revenue_usd、pay_cnt、etl_time；从当前订单表按日汇总 |
| `ads_collart.ads_oper_user_revenue_collart_fashion_di` | 2026-09-09 停写 | 原为 event_date × user_id，event_date 分区、user_id 聚簇；订单与 active 承接 |

原用户日字段另有 user_pseudo_id、first_fashion_succeed_date、revenue_usd、pay_cnt、etl_time。2026-08-27 的“首次 Fashion 成功后全部 Web 收入归 Fashion”已被 08-28 的最近支付事件归属替代；仅日期相等也不是最终规则。不能把这些旧字段或用户日粒度套到当前订单表。

旧版回验记录：2026-08-14～08-27 为 10 个付费用户、16 个用户日、17 笔交易、392.44 美元，未在本次重算。09-09 订单定义的生效日与数据回填覆盖（06-01 起）分别记录。

最近事件相同距离的优先级、迟到事件重算规则未在旧文档中充分定义。已停用 DWD 用户表不能继续作为当前归属补全源；其他替代源需按现有 active/profile 与仓库任务确认。完整金额和业务红线见 收入指标。

## 已有资料定义

表：`aidata2025.ads_collartfashion.ads_oper_user_revenue_di`。一笔 Stripe 订单一行，按 `transaction_id` 去重，分区字段 `event_date`；资料注明必须分区过滤。

上游是 `pubdata2025.dwd.dwd_cdct_revenue_stripe_di` 的 Web 订单。资料记录：相同 user_id，订单时间与 `vip_subscribe_succeed` 前后 600 秒内匹配，选最近事件且 package_name 为 Fashion，从而形成 Fashion 归属。实际 tie-break、时区、退款、重复事件和排除规则仍需看实现。

用户日金额再进入 active 并上卷指标层。金额字段保留上游 `revneue` 拼写；毛额/净额不得从“收入”标题自行推断。

## 合并主站时的约束

本条只能说明 Fashion 如何取子集，不能证明 Web 总收入已经扣掉该子集。合并前应以交易键比较两侧交集和未分配交易，定义互斥归属或合并后去重。两张表结构同构不等于业务范围互斥。

旧日收入表停更/删除、Fashion 投放花费固定为 0 是来源中的时间性描述；分析当天需重查，固定 0 未必代表实际无投放。
