---
id: "android.ads"
title: "Android 激励广告点击、展示与奖励"
project: "collart_android"
kind: "event"
status: "documented"
sources: ["previous:android-reward-ad-click"]
tags: ["免费看广告", "激励广告", "点击率", "generate_watch_ad", "广告"]
tables: ["storytemplate-10a27.analytics_232977577.events_*"]
---

# Android 激励广告点击、展示与奖励

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

先按公司规则契约确认现有物化字段。历史规则将 `generate_watch_ad` 与 `generate_pro_create` 合并为生成准备，不能把该合并字段当纯广告点击。字段不适合时才查 DM 或原始事件；原始事件及直接暴露原始明细的 DM/DWD 仍仅允许最近 7 天。

原始 GA4 来源为 `storytemplate-10a27.analytics_232977577.events_*`，Android 过滤 `app_info.id='free.ai.photo.generator.collart.ai'`，必须同时有日期上下界及明确业务时区。不能用全产品扫描替代入口确认；仅取所需事件和参数。

## 来源与验证边界

原始字典 4.15 节、事件规则摘录。可用 read 来源 ID 加 --section '4.15 触发生成事件' 按节读取。2026-09-14 仅整理来源；没有进行 UI、生产事件或分母核验。
