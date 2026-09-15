---
id: "ios.activity"
title: "VidArt 活跃、收入与成熟留存"
project: "collart_ios"
kind: "metric"
status: "documented"
sources: ["previous:shared-core-metrics", "previous:shared-payment-evidence"]
tags: ["iOS", "VidArt", "留存", "收入", "DAU"]
tables: []
---

# VidArt 活跃、收入与成熟留存

使用 ads_collartios 的 daily/country/active 作为当前入口；活跃与成熟留存公式见 [shared.activity](../../shared/metrics/activity.md)，支付/收入见 [shared.revenue](../../shared/metrics/revenue.md)。DAU 与留存只计 is_active，收入保留 pay-only。

Apple Sales 国家层与用户订阅净收入粒度不同，country 不能默认拆出 new/resub/trial。ASA 文档中 IAP 订阅×0.85、点数包×0.70 是历史净额估算，不代替结算真值。俄罗斯 Stripe 补充支付按 RUB 与 VidArt app_name 核验，不重复叠加已进入 ADS 的金额。

若问长期留存，使用足够成熟的汇总/cohort 表；原始七天不能推断更长历史。缺乏有效 cohort 或分区时标记缺口。
