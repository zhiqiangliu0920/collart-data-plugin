---
id: "collart-android-dau-source-selection"
title: "Android 活跃用户与历史 SQL 选择"
project: "collart_android"
kind: "metric"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-3dd331efb6c6", "review-20260914-ca27ec86b3b2"]
tags: ["collart_android", "Android 活跃用户与历史 SQL 选择"]
supersedes: []
verification_evidence: []
historical_sources: ["full-b5bb84b662377244", "full-7190043e9eae148f", "full-b5bb84b662377244-review-ec7e5e69e4", "full-7190043e9eae148f-review-954bdf4e17"]
---

# Android 活跃用户与历史 SQL 选择

Android DAU 文档在 2026-03-23 明确改用加工表，旧首页 session_start 公式不能继续作为默认 DAU。2026-09-07 的跨端规范又给出新版 ADS 入口，使用前应先核对所需粒度和分区。

保留历史 SQL 便于复现，固定日期、旧表和同名字段不自动升级。PV 行计数与去重用户数、总 DAU 与新用户 cohort 必须分开。2026-09-13 用户明确删除全部固定 DAU 阈值，包括同比例占位阈值；不能继续采用旧“正常规模”、±5% 或相近经验值。active 计活跃须筛 is_active，收入骨架行不计 DAU。

## 来源与状态

- [collart_android/indicators/dau.md](../../library/text/5126e2275883955da33ab341e7f2e3a86de550334d2dc4644a6394211a7d7ccb.txt)
- [1company/analysis_playbooks/collart_ads_redlines.md](../../library/text/0b81b22d1f69db06c82072ba3fd281d4a0c50d057038b6543cf9c82aa1ba6104.txt)

以上是原文整理，documented 不表示已验证当前业务事实。

## 2026-09-14 对齐依据

- [collart_android/indicators/dau.md](../../library/text/5126e2275883955da33ab341e7f2e3a86de550334d2dc4644a6394211a7d7ccb.txt)
