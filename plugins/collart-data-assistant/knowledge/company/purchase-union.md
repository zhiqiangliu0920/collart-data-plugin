---
id: "company-purchase-union"
title: "订阅与点数包购买人数并集"
project: "company"
kind: "metric"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["full-1fd6dc1741d54dde"]
tags: ["company", "订阅与点数包购买人数并集"]
supersedes: []
verification_evidence: []
---

# 订阅与点数包购买人数并集

适用资料日期：2026-08-24。`is_purchase = is_subscribe OR is_credit_pack`；`purchase_uv` 是两类用户的去重并集，不能将两个 UV 相加。`purchase_uv_1d` 对应新用户当日并集。

Android、iOS、Web、Fashion 的来源不同。资料说明俄罗斯 RUB Stripe 支付不进入客户端 purchase_uv，而用户收入可叠加 RUB。因此购买用户指标接近零不能单独证明没有付费。Fashion 的 is_purchase 与尚未填充的 is_subscribe/is_credit_pack 也不能混为同一完整能力。按字段、端、日期分别核对。

## 来源与状态

- [1company/indicators/subscription_purchase.md](../../library/text/06f8ed14451fd932afccaab126e4ae18fed2f0d64d51dd6843753925ee2a3302.txt)

以上是原文整理，documented 不表示已验证当前业务事实。
