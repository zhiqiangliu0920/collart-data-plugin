---
id: "collart-fashion-cohort-dashboard-analysis"
title: "Fashion 新人订单与看板粒度"
project: "collart_fashion"
kind: "playbook"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-363a700114de"]
tags: ["Fashion", "cohort", "看板", "支付"]
supersedes: []
verification_evidence: []
---

# Fashion 新人订单与看板粒度

新人 cohort 以 cohort_date × user_pseudo_id 构建，订单按可靠 user_id 映射关联。新人支付转化要求订单发生在 cohort 之后、观察窗之内，成功状态和交易去重均成立；旧包含 pending/expired 的订单诊断不等于实际付费。

身份映射明确截至时间，防止未来登录映射改变历史 cohort。日期 × pseudo 先形成新老、渠道、国家与行为 flags，再按维度汇总；ANY_VALUE 不能替代确定性的归因规则。同日登录/生成/下载/VIP flags 不证明步骤顺序。

内部名单使用统一当前入口，不能固化旧 SQL 中的名单。留存仅比较成熟 cohort，缺失不作零；日期要有上下界。旧 DWD 回补源、旧订单筛选与固定 2026-07 窗口不作为可直接运行模板。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [collart_fashion/analysis_playbooks/cohort_dashboard_analysis.md](../../library/text/a00ffd851751c3c75e7494c85450664582bc6025f7f352ff1709478a4ec850f9.txt)
