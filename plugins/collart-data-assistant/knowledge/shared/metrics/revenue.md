---
id: "shared.revenue"
title: "成功支付、收入与购买人数"
project: "shared"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:1company/analysis_playbooks/collart_ads_redlines.md", "ai-knowledge:1company/indicators/subscription_purchase.md", "ai-knowledge:collart_android/indicators/russia_orders_payment_broadcast.md", "ai-knowledge:collart_ios/indicators/russia_orders_payment.md", "previous:company-purchase-union", "previous:shared-payment-evidence"]
tags: ["收入", "支付", "purchase_uv", "Stripe", "RUB", "订阅", "credit"]
tables: []
---

# 成功支付、收入与购买人数

## 先定义统计对象

客户端 subscription / VIP 点击与成功事件衡量行为转化；服务端 revenue / 成功交易衡量实际付费。VIP 状态、曾经付费、支付发起、窗口内成功支付分别命名。新增访客首付率以同一新增 cohort 为分母，不以首订人数除全量 DNU 混称新增转化。

is_purchase = is_subscribe OR is_credit_pack；purchase_uv 是去重并集，不等于 subscribe_uv + credit_pack_uv。*_1d 是新用户首日，*_old 为老用户当日；_7d 方向按端核验。RUB 补充支付可能不进入客户端 purchase_uv；Fashion 部分订阅拆分字段曾固定零，须核对源码和当前字段。

## 金额

在具备拆分的端：purchase_revenue = new_revenue + resub_revenue + trial_conver_revenue + credit_revenue。purchase 已含点数包，不能再加 credit。广告收入单列；总收入是否加广告由问题决定。iOS country 的 Apple Sales 不一定有新/续/试拆桶，Web/Fashion 无试转桶。新旧 total_revenue、purchase_revenue 不等价。

| 端/范围 | 来源与边界 |
|---|---|
| Android | IAP/DWS + 广告 + Stripe RUB；country/daily 与用户层可能不同，核对同层口径 |
| iOS | Apple + Stripe RUB；Apple Sales 国家收入和用户订阅净收入不能混用 |
| Web | Stripe T+1 与 ADS revenue；用户实收美元用原拼写 revneue，勿默认加 fee |
| Fashion | Stripe 订单按每单附近事件归属 → active → attr → country → daily；和 Web 有交集 |
| 移动端 RUB | Stripe 且 UPPER(currency)='RUB'，Android app_name=collart_android；iOS=vidart/vidart_ios/vidart-ios；不用于筛 Web 全部收入 |

## 去重、关联与边界

按 transaction_id 去重；缺 ID 或相同 ID 金额冲突显式检查，不任意 ANY_VALUE。收入保留 pay-only 行和未归属金额。user_id 与 pseudo 不能当作同一身份；设备映射覆盖与服务端总量可能不同。profile 收入按 SUM(active) 不再二次叠加 orphan。退款、负额、币种、毛净额、手续费及业务时区须在报告中明确。

ods.orders 的旧 active/paid/active_ending 状态不能替代 Stripe 成功收入；HI 曾为空不代表可补今天。收入增长不等于付费率上升，续订金额下降不等于续订率下降（需应续订 cohort 分母）。

## 移动端俄罗斯支付补充

2026-08-28 的俄罗斯支付方法使用 Stripe revneue>0、有效 user_id、按 transaction_id 去重；Android app_name 包括 collart_android / collart-android，iOS 包括 vidart / vidart_ios / vidart-ios，UPPER(currency)='RUB'。Stripe pending/available 是打款状态，不能当未支付。

该专项的历史播报美元金额是 revneue + IFNULL(fee,0)，属于毛额说明；Web 实收分层仍使用 revneue，不能混用。不可再除汇率或 100，不为 RUB 专项额外关联 Apple 订阅表；若读 ADS 已含 RUB，不能二次相加。次日零点汇总属于前一个北京时间自然日，T+1 延迟必须标注。发送卡片、维护播报状态和列出用户 ID 的工作流已退出分析插件。
