---
id: "company-event-rule-contract"
title: "四端事件指标规则与宽表关系"
project: "company"
kind: "event"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-2cd993415a48", "review-20260914-77dd0384efff"]
tags: ["company", "四端事件指标规则与宽表关系"]
supersedes: []
verification_evidence: []
historical_sources: ["full-2ce0fdb15495c7bc", "full-199b51ce0dcab10c", "full-2ce0fdb15495c7bc-review-00d8e8ef02", "full-199b51ce0dcab10c-review-d5bb4ac56d"]
---

# 四端事件指标规则与宽表关系

适用资料日期：2026-09-02。统一规则在 `aidata2025.ads_collart.ads_dim_metric_rule`，用 app_name 区分四端。旧分端规则表与 tag_code 命名是历史记录。

热指标由 is_enabled/is_materialized 确定；用户日为 *_pv，汇总为对应 STRUCT。修改 Sheet 不会自动改变已生成的 SQLX 或宽表字段。冷指标按规则查询 DM；必要时再下钻 GA4。本文是知识说明，不授权运行生成器、回补或生产写入。

## 来源与状态

- [1company/tables/ads_dim_metric_rule.md](../../library/text/0e25237cb6cc34df9058cdc123c8a520eb6247f4ce4f0d0250f18c5bcc401e3f.txt)
- [1company/analysis_playbooks/event_metric_from_rule.md](../../library/text/b28a72492625b0be076c71fabed4e9f212e7677ed6630f9adb9485ea28e55195.txt)

以上是原文整理，documented 不表示已验证当前业务事实。
