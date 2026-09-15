---
id: "android.revenue"
title: "Android 收入定义与查询入口"
project: "collart_android"
kind: "metric"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_android/ads_oper_basic_indicator_daily_di.sqlx", "previous:android-revenue-trend", "schema:aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_di", "sql:android-revenue"]
tags: ["Android", "收入", "趋势"]
tables: ["aidata2025.ads_collartandroid.ads_oper_basic_indicator_country_di", "aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_di"]
---

# Android 收入定义与查询入口

## 当前取数契约

日趋势先用 `aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_di`；国家贡献用同 dataset 的 `ads_oper_basic_indicator_country_di`。日表的 `revenue.purchase_revenue` 与 `revenue.ad_revenue` 分列输出；币种、毛净额和覆盖确认后才汇总。不要把 Web Stripe 实收口径直接套给 Android，也不要在 ADS 总额外再加一次移动端 RUB 补充支付。

原收入资料记载 Android country 使用 `ads_ad_sub_revenue_1h`，用户层另有 DWS/RUB 链路；层间不保证完全相等。这是资料中的血缘，不是本次线上检查。用户收入保留仅支付行，DAU 才使用 is_active 条件。

## 最近七个完整日

默认北京时间，运行日 D 的本期为 D-7 至 D-1，前期 D-14 至 D-8。先检查请求的日期覆盖；缺日时说明缺口，不能静默改窗口。日期、当前连接和相关 schema 在同一任务两个分析分支共享。

Android 收入模板 输出 14 天的收入分项及窗口汇总、变化量和变化率。只检查本次用到的字段、分区与粒度；有国家/渠道驱动问题时再展开，普通趋势不默认查四端和用户明细。NULL 收入与缺日期都需要核验，不能自动当作零。

## 来源与验证边界

收入定义、选表。模板仅离线验证，首次使用核对当前 schema、计费项目和金额范围。2026-09-14 是整理日期，不代表收入口径生效日期。没有运行生产查询。

## 关联查询

参数化只读模板：`sql:android-revenue`（`knowledge/collart_android/sql/android-revenue.sql`）。执行前检查参数、字段、日期覆盖和金额/人群范围。
