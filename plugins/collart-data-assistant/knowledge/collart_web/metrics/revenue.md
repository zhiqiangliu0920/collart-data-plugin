---
id: "web.revenue"
title: "Web 收入趋势与交易核对"
project: "collart_web"
kind: "metric"
status: "documented"
sources: ["previous:collart-web-revenue-report-20260912", "previous:shared-payment-evidence"]
tags: ["Web", "收入", "Stripe", "趋势"]
tables: ["pubdata2025.dwd.dwd_cdct_revenue_stripe_di"]
---

# Web 收入趋势与交易核对

先用 ads_collartweb.ads_oper_basic_indicator_daily_di 看收入趋势，再核对 Stripe `pubdata2025.dwd.dwd_cdct_revenue_stripe_di` 的同窗同产品成功交易。采用北京时间最近七个完整日与前七日比较时，展示实际覆盖，不把未入仓日补零。

按 transaction_id 去重，实收美元 revneue 与历史 revneue+fee 毛额分开；未知账号金额保留。订单数与收入结构不同，分首订、续订、点数包，同时做高额交易敏感性检查。收入归因必须解释活跃设备映射覆盖。首次订阅不等于新访客，续订金额不等于续订率。Fashion 是可能重叠的交易子集，不直接相加。

默认时点排除内部账号，使用授权名单；无法做相同范围的过滤时说明对账不等价。画像收入 SUM(active) 不替代完整服务端交易总额。
