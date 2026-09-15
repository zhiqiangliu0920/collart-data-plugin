---
id: "fashion.activity"
title: "Fashion 新增、活跃与留存"
project: "collart_fashion"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_fashion/indicators/fashion_new_user.md"]
tags: ["Fashion", "新增", "留存", "cohort"]
tables: ["aidata2025.ads_collartfashion.ads_oper_user_active_di", "aidata2025.ads_collartfashion.ads_oper_user_profile_df", "aidata2025.ads_collartfashion.ads_oper_user_revenue_di"]
---

# Fashion 新增、活跃与留存

## 当前经营口径

采用 aidata2025.ads_collartfashion 的 active / daily / country，package_name=collart_fashion，设备键 user_pseudo_id。活跃过滤 is_active=TRUE；正式新增使用当前 active.is_new 及其加工定义。留存仅比较成熟 cohort，公式见[公共指标](../../shared/metrics/activity.md)。

“第一次进入 Fashion”和“整个 Web 首次发现且首访归属 Fashion”是两种 cohort。旧 2026-07-23 文档采用后者并推荐旧 ads_oper_user_new_collartweb_di；新分析不可把该旧表直接当当前真值。需要 Fashion 专属首次访问但现有历史未记录时，标明缺口，不能靠最近七天原始首见推断终身首次。

## 站点、身份与支付

Web 原始 page_location 包含 studio 或 fashion 属 Fashion；仅匹配 ai-fashion-video 过窄。原始 app_info.id IS NULL 还需页面归属；缺页事件单列未知。设备与账号多对多，cohort 先以 pseudo 构造，再用截止观察时点有效的 user_id 映射成功交易。

新人付费率 = 该 cohort 在统一观察窗内成功支付的去重人数 / cohort 人数。付款发生在 cohort 后且在窗口内；不能用所有历史订单或 pending/expired 宽状态。成功收入采用 Fashion 每单附近事件归属后的 Stripe 表，见[收入与 Web 交集](revenue.md)。不使用 ods.orders 的旧状态组合代替当前真实付费。

## 关联表

[active](../tables/aidata2025.ads_collartfashion.ads_oper_user_active_di.md)、[画像](../tables/aidata2025.ads_collartfashion.ads_oper_user_profile_df.md)、[订单收入](../tables/aidata2025.ads_collartfashion.ads_oper_user_revenue_di.md)。cohort 日期 × pseudo 先去重再聚合，不把同日功能 flags 当作按顺序转化。
