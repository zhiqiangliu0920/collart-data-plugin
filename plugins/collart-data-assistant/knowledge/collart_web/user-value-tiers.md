---
id: "collart-web-user-value-tiers"
title: "Web 累计实收用户价值分层"
project: "collart_web"
kind: "metric"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: "2026-09-13"
sources: ["review-20260914-41b25158a11f"]
tags: ["用户分层", "大R", "lifetime", "净收入", "500", "100", "50"]
supersedes: []
verification_evidence: []
---

# Web 累计实收用户价值分层

采用用户于 2026-09-13 确认的 500 / 100 / 50 美元阈值。R 是 Web 业务范围内同一 `user_id` 截至指定日期的累计实收美元。

| 层级 | R |
|---|---|
| 超大 R | R ≥ 500 |
| 大 R | 100 ≤ R < 500 |
| 中 R | 50 ≤ R < 100 |
| 小 R | 0 < R < 50 |
| 未付费 | R = 0，不能并入小 R |

Stripe 按 `transaction_id` 去重，金额取实收美元 `revneue`；不能混用历史 `revneue + fee` 毛额公式。重复交易金额冲突须确认保留规则，不能任意 ANY_VALUE。退款/负净额另列并明确政策，不能默认归为未付费。

累计收入需要完整历史覆盖；最近 30 天收入不等于 lifetime value。优先使用符合该净额、身份和产品定义的已有累计表或成功交易数据，不能为补历史扫描超过 30 天的原始埋点。`user_id` 与 `user_pseudo_id` 不可混用。Stripe app_name 不能单独区分 Web 主站与 Fashion，先确认互斥归属。

旧 500 / 200 / 100 阈值和只保留 R ≥ 50 的样本已被当前规则替代。旧报告人数、分组计数和百分比矛盾仍是历史统计问题，不能用新阈值推断其当时结果正确。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [collart_web/indicators/user_value_tier.md](../../library/text/0c2685cfa8e32c90ab56b90f8cf22cb5c2f4d4369567f927f2e705130879dbf2.txt)
