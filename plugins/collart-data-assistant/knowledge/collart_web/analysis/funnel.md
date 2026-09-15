---
id: "web.funnel"
title: "Web 会话无交互率与严格漏斗"
project: "collart_web"
kind: "playbook"
status: "documented"
sources: ["ai-knowledge:collart_web/analysis_playbooks/session_funnel_diagnosis.md", "previous:collart-web-session-funnel-diagnosis"]
tags: ["Web", "会话", "跳出率", "漏斗"]
tables: []
---

# Web 会话无交互率与严格漏斗

## 会话无交互率

会话键为 `user_pseudo_id × ga_session_id`。缺失 session_id 的事件单列，不合并成一个会话。两个自定义指标分别命名：①只有 1 次 page_view 且没有核心交互；②没有核心交互、允许多次浏览。分母均为同一范围的有效会话，二者都不能标为 GA4 跳出率。

核心交互候选包括 `explore_content_click`、`feature_content_click`、`login_success`、`vip_show`、`vip_subscribe`、`vip_subscribe_succeed`、`credit_pack_purchase` 及 `*generate_click`。使用前对照[事件字典](../events/events.md)，随功能版本确认完整性，不能把没有上报当作没有交互。

## 严格漏斗

先在用户/会话粒度计算登录、模板点击、生成点击、VIP 展示和购买触达，再按[页面与付费转化](../metrics/conversion.md)建立顺序。严格漏斗要求同一用户/会话、时间先后、人群交集和统一观察窗；同窗各事件 UV 的比值仅表示触达关系。

支付行为事件用于诊断，实付以[交易口径](../metrics/revenue.md)核对。未登录不能直接等同低质量流量；国家间转化差异不能单独证明原因。

## 国家、渠道与产品范围

国家别名如 Turkey / Türkiye 先统一映射；渠道按[渠道归因](../metrics/channel.md)，`traffic_source.name` 中 `%fb-%` 只是历史候选匹配。比较总变化贡献、样本量和结构占比，同时检查事件缺失。

`app_info.id IS NULL` 不足以区分 Web 主站与 Fashion，须加[站点归属](../business/product.md)和内部账号过滤。原始事件只读[最近 7 天](../../shared/business/access.md)，长期趋势用合适汇总。
