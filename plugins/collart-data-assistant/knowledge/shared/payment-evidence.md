---
id: "shared-payment-evidence"
title: "付费转化与收入口径"
project: "shared"
kind: "metric"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["metrics", "revenue", "ads-redlines-review-954bdf4e17", "fashion-orders-review-7afb4b3f3b", "team-shared-payment-evidence", "cursor-revenue-subscription-md"]
tags: ["付费", "订阅", "收入", "conversion", "Stripe", "purchase_revenue", "ROAS"]
supersedes: []
verification_evidence: []
historical_sources: ["ads-redlines", "fashion-orders"]
---

# 付费转化与收入口径

## 先选业务问题

| 要回答的问题 | 需要的证据 |
|---|---|
| 有多少人进入支付流程 | 对应访问/点击/checkout 事件及真实触发语义 |
| 有多少人触发订阅成功埋点 | 已核对的事件或 `subscription` 字段 |
| 窗口内实际付费多少人、多少收入 | 成功交易、金额与交易时间；核对服务端来源 |
| 这批用户历史是否付过费 | 历史交易或画像定义；与本窗口成功付款分别统计 |

不能仅用开始支付、VIP 状态或历史付费状态表示本窗口付款。埋点和订单口径需分别命名，不要把客户端 `subscription.*` 与服务端 `revenue.*` 合成同一转化人数。

## 金额与用户范围

现有指标资料将 `purchase_revenue` 定义为已含点数包的内购收入；不能再加 `credit_revenue`。广告收入是否加入取决于报告定义。四个金额桶的等式要在目标端和目标层验证，尤其 iOS 不一定提供完整拆桶。

Web/Fashion 和移动端俄罗斯支付资料推荐 Stripe 或 active.revenue；完整移动端收入还涉及 Apple/DWS，不能套用仅 RUB 的条件覆盖全部支付。`revneue` 是来源中的原字段拼写；币种、毛额/净额、手续费和退款必须按报告契约确认。

付费转化明确 cohort、新老用户、去重键和付款窗口。不能只因两个付款类别分别有 UV，就相加得到购买总 UV，交集用户需去重。ROAS 另需核对投放成本和该 cohort 的映射是否可得。

## 仍需复核

旧资料中的 `ods.orders` 成功状态、HI 空表与延迟窗口是有时间背景的规则或观察，不能跨表通用。服务端总收入和有设备映射的用户收入可能不一致；说明未归属交易，而不是强行分摊。Fashion 与主站是否可加总见 [收入边界](../collart_fashion/revenue-boundary.md)。

## 来源与状态

来源摘录：[metrics](../../provenance/excerpts/metrics.txt)、[revenue](../../provenance/excerpts/revenue.txt)、[ads-redlines](../../library/text/954bdf4e178b2f0cb89369eeeed99c2f3c2ac468f427db24fe151ee596c242a0.txt)、[fashion-orders](../../library/text/7afb4b3f3b384566d72fcd095e7ae0ed518420afe66f3c8027447141d8ffe1bb.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

## 收入与订阅

先读 [metric-glossary.md](core-metrics.md) 的「订阅 vs 收入」；本文补充订单真值、Stripe、收入源对齐等细节。

### 三个收入真值源

| 端 | 服务端收入源 | 备注 |
|----|--------------|------|
| Android | DWS IAP + 广告 + Stripe RUB 叠加 | new_revenue 已扣点数包；RUB 进 purchase/credit；profile = SUM(active) |
| iOS | Apple IAP + Stripe RUB 叠加 | country 层无 new/resub/trial 拆分；`ad_revenue=0` |
| Web / Fashion | Stripe T+1（含 Web RUB） | Fashion 用户日写在 active，上卷 country/daily；不要用已停写的旧日收入表 |
| 移动端俄罗斯支付 | Stripe `dwd_cdct_revenue_stripe_di`，`currency='RUB'` | 不要用 `ods.orders`；Android=`collart_android`，iOS=`vidart`/`vidart_ios`/`vidart-ios` |

### 用户粒度收入（2026-08-28）

Web 用户收入可从 `pubdata2025.dwd.dwd_cdct_revenue_stripe_di` 核对；不能把 Web 全部支付限制成 RUB。Android/iOS 的俄罗斯 Stripe 补充支付才限定 `UPPER(currency)='RUB'`。按 `transaction_id` 和适用产品去重，币种及毛净额采用下述规则。不要使用旧 `ods.orders` 替代成功收入证据。

既有资料曾记录 `dwd_cdct_orders_revenue_hi` 为 0 行；这不是本次实时检查，不能假定它可补当天数据。

落表：Android/iOS `ads_oper_user_active_di.revenue.purchase_revenue` 与 `credit_revenue` 叠加 RUB；**四端 profile 终身收入都是 `SUM(active.revenue)`**，不再回扫 DWS、不再 orphan 二次叠加。country/daily 仍读 `ads_ad_sub`（用户粒度与国家层允许对不齐）。

金额：Stripe 用户侧美元（USD=`amount`，非 USD=`revneue+fee`）。`revneue` 是实收；`pending` 的含义依赖具体支付源和状态机，不能仅凭该字符串判断付款成功或失败。

### 订单表 status 口径（历史）

`ods.orders` 旧口径：`status IN ('active','paid','active_ending')`。新分析不要再用它算用户收入。

### 收入四桶与 UV

见 [metric-glossary.md](core-metrics.md)。要点复述：

- `purchase_revenue = new + resub + trial_conver + credit`；**勿 purchase+credit 双计**。
- 服务端分类人数可读 `revenue.*_uv`；类别可能重叠，实际总付费人数须按窗口内成功支付用户去重；埋点转化人数用 `subscription.*`。

### country 收入 vs ads_ad_sub_revenue_1h

- country 层订阅三类（new/resub/credit）来自 **DWS**，不是 `ads_ad_sub_revenue_1h`。
- 原历史样本中，国家×日仅约 15% 键与 `ads_ad_sub_revenue_1h` 完全对齐；日级 `new_revenue` 可对齐，国家拆分不完全等价。
- 2026-08-10 起 ADS 层 `new_revenue` 已扣点数包，可与旧表直比。

### Stripe 归属（Web）

- active：同日 DM 末次 pseudo，否则 id_map **最近一次绑定（不卡首见日）**；两级都没有才丢掉。
- profile：`SUM(active.revenue)`，不再 orphan 叠加。2026-09-06 起 too_new 进日活；真 miss（无设备）仍不硬挂。
- 原历史样本中的 profile 无 active 骨架人约 2442，付费为 0，不是漏单。

### Stripe 归属（Fashion）

- 订单表 `ads_collartfashion.ads_oper_user_revenue_di`：±10 分钟最近 `vip_subscribe_succeed` 且 `package_name='collart_fashion'`。
- 用户日写入 `ads_oper_user_active_di`（含 `purchase_cnt` / credit 字段），上卷 attr → country → daily。
- 旧日表 `ads_oper_revenue_collart_fashion_di` 已删除。
- 无活跃支付日补 `is_active=FALSE`；country 空值用 Stripe 或 `unknown`。

### 订阅档位（Web）

- 订单数偏月包 Standard，收入偏年包 Premium（历史约 82.9% 收入来自年包）。
- 分析付费结构时区分「订单口径」与「收入口径」，结论可能相反。

### ARPU / ARPPU

- 历史样本的 Web/OS 维度中：iOS 端 ARPPU 最高，Android 量大付费率低、收入以点数包为主。
- ARPDAU 敏感性用于收入作战台（见 [playbooks.md](analysis-playbook.md)）。

### 埋点 vs 订单差异

`vip_subscribe_succeed` 埋点与服务端成功单不一致（埋点在支付成功前触发/漏报）。评估「实际收入」以 Stripe / `active.revenue` 为准；评估「转化漏斗」用埋点。不要拿 `ods.orders` 对埋点。


来源快照：[cursor-revenue-subscription-md](../../provenance/excerpts/cursor-revenue-subscription-md.txt)。
