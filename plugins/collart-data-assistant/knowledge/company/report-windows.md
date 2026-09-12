---
id: "company-report-windows"
title: "经营日报日期与比较窗口"
project: "company"
kind: "metric"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["full-eeebc9e82bd76fe2"]
tags: ["company", "经营日报日期与比较窗口"]
supersedes: []
verification_evidence: []
---

# 经营日报日期与比较窗口

适用资料日期：2026-08-06，范围为 Android/Web/iOS 经营日报。

| 指标 | 比较值 | 前 7 日均值 |
|---|---|---|
| 收入、ARPU、留存 | T-2 | T-9 至 T-3 |
| DAU、新增、转化、AI 服务 | T-1 | T-8 至 T-2 |

实现中把收入和留存日期平移一天时，扫描必须覆盖 T-9。只扫到 T-8 会使前一类均值少一天。报告写清实际数据窗口及数据是否齐全，不用零补尚未入仓的日期。

## 来源与状态

- [1company/indicators/collart_daily_report_date_windows.md](../../library/text/b3cc071adc1c86669cb3155d6a78f4216706c260bcca47015eb12a786779edd1.txt)

以上是原文整理，documented 不表示已验证当前业务事实。
