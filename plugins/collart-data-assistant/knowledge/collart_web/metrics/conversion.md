---
id: "web.conversion"
title: "Web 页面与付费转化"
project: "collart_web"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_web/indicators/conversion.md", "ai-knowledge:collart_web/indicators/page_conversion.md"]
tags: ["Web", "转化", "付费", "漏斗"]
tables: []
---

# Web 页面与付费转化

## 付费指标

| 指标 | 分子 | 分母与限制 |
|---|---|---|
| 订阅成功事件转化 | cohort 内触发 vip_subscribe_succeed 的用户 | 同产品、同窗口 cohort；仅事件口径 |
| 成功支付转化 | cohort 内当窗有成功交易的用户 | 明确新老用户和观察窗，交易先去重 |
| 购买事件 UV | 订阅与点数包购买用户的去重并集 | 不把两个 UV 相加；见[公共购买定义](../../shared/metrics/revenue.md) |

窗口内支付者必须与分母 cohort 相交。活跃分母按[活动指标](activity.md)；历史已付费、当窗付款、首次付款和当前 VIP 身份分别计算。成功事件 UV/session_start UV 不能自动称为成功支付转化。

Web 交易按[收入口径](revenue.md)使用 Stripe `revneue`、`transaction_id` 去重；pending/available 打款状态与 orders 的 pending/expired 支付状态语义不同。Fashion 可能共享埋点和 Stripe 包名，须在建立 cohort 前固定[业务归属](../business/product.md)。

## 页面转化

页面 A → B 需要定义页面/功能进入事件、同一用户或会话以及允许耗时，并保证 A 在 B 之前。候选路径为首页 → AI Video → 创建任务 → 生成成功，实际进入及成功事件须从[事件字典](../events/events.md)核验。

仅 page_view 不能识别首页，必须过滤首页 URL；page_view 与 aivideo_edit_show 的同窗交集也不等于有顺序的首页到视频转化。曝光、进入、生成意图和成功分别定义。

无顺序触达与严格漏斗分别报告，国家和渠道拆解见[会话漏斗诊断](../analysis/funnel.md)。缺失分母返回 NULL，不预置通用告警阈值。
