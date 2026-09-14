---
id: "collart-android-first-subscription-diagnosis"
title: "Android 新增 cohort 与首付诊断"
project: "collart_android"
kind: "playbook"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-4497c62de285"]
tags: ["首订", "首付", "新增", "cohort"]
supersedes: []
verification_evidence: []
---

# Android 新增 cohort 与首付诊断

分别定义正式新增 cohort、窗口内首笔成功付款和历史已付费状态。不能把 first_open 与 subscription_first 的并集当作新增人数；仅 platform=ANDROID 还会混入共享数据集的其他产品，必须核对业务包名。

先独立构建 first_open/正式新增 cohort，再关联该 cohort 在观察窗内的首笔成功支付。分母为 cohort 用户数，分子为其中首付用户数。对比时统一观察时长和成熟度，不直接比较 14 日与 15 日累计人群。

subscription_first 的存在和付款成功语义都要证据；零行不能证明追踪失效。GA4 event_date 是字符串，events_2026* 与 events_* 的后缀长度不同。原三四月 SQL 已停止作为执行模板；受最近 30 天约定约束。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [collart_android/analysis_playbooks/first_subscription_diagnosis.md](../../library/text/3723c246375a7f31ed36a537fd16fb60cebccac38412894914eac272889bbc6c.txt)
