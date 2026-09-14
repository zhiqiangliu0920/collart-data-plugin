---
id: "collart_fashion-revenue-boundary"
title: "Fashion 订单收入与主站边界"
project: "collart_fashion"
kind: "table"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-626470cd87d2", "revenue", "review-20260914-ca27ec86b3b2", "team-collart_fashion-revenue-boundary", "review-20260914-86810c962658"]
tags: ["Fashion", "收入", "Web", "去重", "transaction_id", "ads_oper_user_revenue_di"]
supersedes: []
verification_evidence: []
historical_sources: ["fashion-orders", "ads-redlines", "ads-redlines-review-954bdf4e17", "fashion-orders-review-7afb4b3f3b", "review-979740ccfe320f48"]
---

# Fashion 订单收入与主站边界

## 已有资料定义

表：`aidata2025.ads_collartfashion.ads_oper_user_revenue_di`。一笔 Stripe 订单一行，按 `transaction_id` 去重，分区字段 `event_date`；资料注明必须分区过滤。

上游是 `pubdata2025.dwd.dwd_cdct_revenue_stripe_di` 的 Web 订单。资料记录：相同 user_id，订单时间与 `vip_subscribe_succeed` 前后 600 秒内匹配，选最近事件且 package_name 为 Fashion，从而形成 Fashion 归属。实际 tie-break、时区、退款、重复事件和排除规则仍需看实现。

用户日金额再进入 active 并上卷指标层。金额字段保留上游 `revneue` 拼写；毛额/净额不得从“收入”标题自行推断。

## 合并主站时的约束

本条只能说明 Fashion 如何取子集，不能证明 Web 总收入已经扣掉该子集。合并前应以交易键比较两侧交集和未分配交易，定义互斥归属或合并后去重。两张表结构同构不等于业务范围互斥。

旧日收入表停更/删除、Fashion 投放花费固定为 0 是来源中的时间性描述；分析当天需重查，固定 0 未必代表实际无投放。

## 来源与状态

来源摘录：[fashion-orders](../../library/text/1a7862e647a0bfca563564f79432fb2282f01e4bdf214f763575a9cd8816637f.txt)、[revenue](../../provenance/excerpts/revenue.txt)、[ads-redlines](../../library/text/0b81b22d1f69db06c82072ba3fd281d4a0c50d057038b6543cf9c82aa1ba6104.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

本次校正依据：[collart_fashion/indicators/fashion_revenue.md](../../library/text/44105210e9257fd2cd1fe584833b5d7ce8d6b799f8e81250bcebf0f2ef089d46.txt)。

文档适用日期与数据覆盖分开：订单表口径记录于 2026-09-09，历史数据回填起点为 2026-06-01；不能把回填起点解释为该文档的业务确认日期。保持每单前后 600 秒最近事件的项目归属规则。

## 2026-09-14 对齐依据

- [collart_fashion/tables/aidata2025.ads_collartfashion.ads_oper_user_revenue_di.md](../../library/text/1a7862e647a0bfca563564f79432fb2282f01e4bdf214f763575a9cd8816637f.txt)
