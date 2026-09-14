---
id: "android-reward-ad-click"
title: "Android 免费看广告按钮：事件候选与点击率边界"
project: "collart_android"
kind: "metric"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-android-ad-events", "cursor-raw-events-md", "maintainer-data-access-20260914"]
tags: ["免费看广告", "广告按钮", "广告 按钮", "点击率", "激励广告", "generate_watch_ad"]
supersedes: []
verification_evidence: []
---

# Android 免费看广告按钮与点击率

## 事件候选与未知项

“免费看广告”“激励广告按钮”是业务检索别名，尚未核对当前 UI 文案/入口和版本，不表示已确认映射。现有 Android 字典记录：

| 事件 | 字典语义 |
|---|---|
| `generate_watch_ad` | 点击激励视频解锁，按钮点击的候选事件 |
| `generate_watch_ad_show` | 点击后广告展示成功；不是已确认的按钮曝光 |
| `generate_watch_ad_show_failed` | 展示失败 |
| `generate_watch_ad_reward_earned` | 展示成功获得奖励 |

参数包括 service_type、id、name；点击事件另有 is_vip。此处 is_vip 被字典解释为模板类型，不直接用作用户 VIP 身份。

## 点击率的分子与分母

确认该 UI 入口映射后，PV 点击率是同入口按钮点击次数 / 按钮有效曝光次数；UV 点击率是曝光人群中点击用户数 / 曝光用户数，须用一致身份、窗口和产品版本。当前来源没有确认该按钮曝光事件，不能把广告展示成功作为按钮曝光，也不能把未知曝光填零。

如只能计算点击 UV / ADS DAU，名称应为“点击用户占活跃用户比例”，并说明分母与覆盖差异。分母未确认时，只报告已确认的点击数量或明确待核验；不要输出伪 CTR。收入与该指标同时请求时，收入分支可独立完成，只为真正缺失的入口/分母信息提出必要问题。

## 最短取数路径

先按[公司规则契约](../company/event-rule-contract.md)确认现有物化字段。历史规则将 `generate_watch_ad` 与 `generate_pro_create` 合并为生成准备，不能把该合并字段当纯广告点击。字段不适合时才查 DM 或原始事件；原始事件及直接暴露原始明细的 DM/DWD 仍仅允许最近 30 天。

原始 GA4 来源为 `storytemplate-10a27.analytics_232977577.events_*`，Android 过滤 `app_info.id='free.ai.photo.generator.collart.ai'`，必须同时有日期上下界及明确业务时区。不能用全产品扫描替代入口确认；仅取所需事件和参数。

## 来源与验证边界

[原始字典 4.15 节](../../library/text/ccc1f71feb3728e07810e2cf40b8f9fe3c1a5e78abc3910cfe91dea6e08ba177.txt#415-触发生成事件)、[事件规则摘录](../shared/event-evidence.md)。可用 read 来源 ID 加 --section '4.15 触发生成事件' 按节读取。2026-09-14 仅整理来源；没有进行 UI、生产事件或分母核验。
