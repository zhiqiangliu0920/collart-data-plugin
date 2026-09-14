---
id: "collart-web-session-funnel-diagnosis"
title: "Web 会话无交互率与严格漏斗"
project: "collart_web"
kind: "playbook"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-f1777a02415b"]
tags: ["会话", "漏斗", "跳出率"]
supersedes: []
verification_evidence: []
---

# Web 会话无交互率与严格漏斗

会话键为 `user_pseudo_id × ga_session_id`。缺失 session_id 的事件单列，不合并成一个会话。v1“1 次 page_view 且无交互”和 v2“没有核心交互、允许多次浏览”是不同指标，均称自定义会话无交互率，不能标为 GA4 跳出率。

同窗登录/模板/生成/VIP/支付 UV 仅表示触达。严格漏斗需要同一身份或会话、事件时间顺序、人群交集和统一观察窗。付款行为事件与成功交易证据分开。旧交互事件列表和 FB 名称匹配只作候选，使用前核对真实事件及当前归因。

`app_info.id IS NULL` 不足以区分 Web 主站与 Fashion，须加产品归属及内部账号过滤。原 2026-03-31 查询只保留方法，不允许再按原日期扫描埋点。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [collart_web/analysis_playbooks/session_funnel_diagnosis.md](../../library/text/05fce5b2d65ad2b2ee09120cd9270dcc63dc01a9bc2cf9f03c7f99b836058313.txt)
