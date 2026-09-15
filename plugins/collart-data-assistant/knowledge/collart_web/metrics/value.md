---
id: "web.value"
title: "Web 累计实收用户价值分层"
project: "collart_web"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_web/indicators/user_value_tier.md"]
tags: ["Web", "大R", "价值分层", "500", "LTV"]
tables: []
---

# Web 累计实收用户价值分层

> 业务状态：documented；复核：reviewed_static。阈值由用户于 2026-09-13 确认；适用当前知识维护，不追溯改写历史报告。

按 Web 业务范围内、同一 `user_id` 的累计实收美元分层。先固定统计截止日期和可用历史覆盖，再计算累计金额；仅扫描最近 7 天的收入不能称为 lifetime value。未确认成功支付或无法映射用户的记录另列。

| 层级 | 累计实收美元 R |
|---|---|
| 超大 R | R ≥ 500 |
| 大 R | 100 ≤ R < 500 |
| 中 R | 50 ≤ R < 100 |
| 小 R | 0 < R < 50 |
| 未付费 | R = 0，不并入小 R 付费用户 |

## 金额、身份与业务范围

2026-08-28 起的本地口径以 [Stripe 订单](revenue.md) 为用户收入来源：`revneue` 是实收美元，按 `transaction_id` 去重，不再套用旧 `orders.total_price / rate / 100` 公式。Stripe 包名可能覆盖多端；Fashion 也可能使用 Web 的 Stripe 包名，不能仅凭 `app_name='collart_web'` 认定主站收入。产品归属要与当前 Web/Fashion 订单归属规则一致。

先检查同一交易的重复行与冲突金额；无法确定去重保留规则时列为待核对，不任意使用 `ANY_VALUE`。`user_pseudo_id` 与 `user_id` 不可混为一个键；缺失映射、历史覆盖不足、负收入/退款的净额政策分别说明。
