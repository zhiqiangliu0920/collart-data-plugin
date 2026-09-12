---
id: "collart-android-dau-source-selection"
title: "Android 活跃用户与历史 SQL 选择"
project: "collart_android"
kind: "metric"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["full-b5bb84b662377244-review-ec7e5e69e4", "full-7190043e9eae148f-review-954bdf4e17"]
tags: ["collart_android", "Android 活跃用户与历史 SQL 选择"]
supersedes: []
verification_evidence: []
historical_sources: ["full-b5bb84b662377244", "full-7190043e9eae148f"]
---

# Android 活跃用户与历史 SQL 选择

Android DAU 文档在 2026-03-23 明确改用加工表，旧首页 session_start 公式不能继续作为默认 DAU。2026-09-07 的跨端规范又给出新版 ADS 入口，使用前应先核对所需粒度和分区。

保留历史 SQL 便于复现，固定日期、旧表和同名字段不自动升级。PV 行计数与去重用户数、总 DAU 与新用户 cohort 必须分开。缺失阈值或待补字段不能解释为已确认的告警标准。

## 来源与状态

- [collart_android/indicators/dau.md](../../library/text/ec7e5e69e41a23c131dfd5b6e803e3643646548c2c1f1c4ad52243632f9f60f3.txt)
- [1company/analysis_playbooks/collart_ads_redlines.md](../../library/text/954bdf4e178b2f0cb89369eeeed99c2f3c2ac468f427db24fe151ee596c242a0.txt)

以上是原文整理，documented 不表示已验证当前业务事实。
