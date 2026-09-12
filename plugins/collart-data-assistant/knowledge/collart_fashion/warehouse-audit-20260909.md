---
id: "collart-fashion-warehouse-audit-20260909"
title: "Fashion 2026-09-09 仓库审计的历史证据"
project: "collart_fashion"
kind: "quality"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["full-a7cc6cb8e2b227f3", "full-96da852291e4720b-review-7afb4b3f3b"]
tags: ["collart_fashion", "Fashion 2026-09-09 仓库审计的历史证据"]
supersedes: []
verification_evidence: []
historical_sources: ["full-96da852291e4720b"]
---

# Fashion 2026-09-09 仓库审计的历史证据

审计记录覆盖 2026-09-06～09-09 的部分运行窗口，业务数据截至 09-08。报告中的收入重叠、滚动画像不刷新、渠道枚举、固定零值及依赖顺序是当时快照的发现。

同日后续收入表文档已经出现订单粒度的新入口，旧审计中的用户日表名称不能当作现网默认。复核时按问题追到当前任务与分区，区分“历史已发现”“当前仍存在”“尚未复验”。

可复用原则：父级与子集收入不直接相加，固定零与真实零分开，任务成功不等于读到了最新上游，事件 PV 与服务任务数分开。

## 来源与状态

- [_generated/fashion_warehouse_audit_20260909/fashion_warehouse_review.md](../../library/text/30963c0d69f6b26d466c87f3e2ec4d574379ffa128300f3ea1b8baacded7b6c8.txt)
- [collart_fashion/tables/aidata2025.ads_collartfashion.ads_oper_user_revenue_di.md](../../library/text/7afb4b3f3b384566d72fcd095e7ae0ed518420afe66f3c8027447141d8ffe1bb.txt)

以上是原文整理，documented 不表示已验证当前业务事实。
