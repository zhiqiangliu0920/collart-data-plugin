---
id: "shared-known-conflicts"
title: "旧资料冲突与待核验清单"
project: "shared"
kind: "quality"
status: "draft"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-09-26"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-278206cde726", "ads-routing", "review-20260914-c52206ae2ac1", "metrics", "revenue", "review-20260914-ca27ec86b3b2", "review-20260914-af2e0602c86f", "team-shared-known-conflicts", "review-20260914-ec2c2ccaf2c5", "review-20260914-86810c962658", "review-20260914-41b25158a11f", "review-20260914-3dd331efb6c6", "review-20260914-7552f1c9b18c"]
tags: ["冲突", "旧口径", "空表", "DAU", "iOS", "收入", "current_active_days"]
supersedes: []
verification_evidence: []
historical_sources: ["legacy-ios", "legacy-conversion", "ads-redlines", "web-profile", "ads-redlines-review-954bdf4e17", "web-profile-review-be4e210655", "legacy-ios-review-7873df86c6", "legacy-conversion-review-95f777f166", "review-e4b31288e0a4a0ad", "review-979740ccfe320f48"]
---

# 旧资料冲突与待核验清单

## 已发现的资料差异

这是一份待处理清单，不能作为当前生产状态结论。

| 主题 | 相冲突或易混淆的资料 | 本次处理及下一步 |
|---|---|---|
| iOS ADS 可用性 | 最新 README 已移除 dataset 为空的旧说法 | 文档冲突已消除；当前分区和可用性仍需实际元数据核查 |
| Web DAU / 转化 | 最新 conversion 已区分同一 cohort、真实支付与行为事件，不再默认 session_start | 文档已对齐；经营 DAU 选 ADS，具体分析继续确认身份与分母 |
| 收入来源 | 旧订单状态说明与 Stripe/active 收入约定并存；用户层与 country 来源有差别 | 按项目、层、币种、毛净额与生效时间确认，不能把表名替换当作口径等价 |
| 画像/设备活跃字段 | Web profile 表文档用 `current_active_days`，另有通用资料提到 active_days 结构 | 当前字段及更新条件以现网 schema/实现为准，不直接复制字段名 |
| HI、固定 0、历史断档 | 来源把 HI 称为空表，并描述 Fashion delivery 固定 0 | 这些是历史状态，不作为永续规则；查询时复核 |

## 可复现的核验建议

查看相关 dataset 的 INFORMATION_SCHEMA.TABLES / COLUMNS / PARTITIONS；对于全量画像检查构建逻辑与更新时间字段；使用一致窗口对账两套指标并说明差异归因。未执行前不填写 verified 日期。

解决一项后更新受影响的正式条目、保留旧适用范围，并在本表记录解决证据。结构校验通过不会自动解决这里的业务冲突。

## 来源与状态

来源摘录：[legacy-ios](../../library/text/fab62e50840f3bbd656cf03fde66dc8307e59b64ce87804bb9c94f5c8af8a7a5.txt)、[ads-routing](../../provenance/excerpts/ads-routing.txt)、[legacy-conversion](../../library/text/c2a1f847b440b722f91bff925c69d0896d1798d2bd86bcd16565fa0e8fda59d4.txt)、[metrics](../../provenance/excerpts/metrics.txt)、[revenue](../../provenance/excerpts/revenue.txt)、[ads-redlines](../../library/text/0b81b22d1f69db06c82072ba3fd281d4a0c50d057038b6543cf9c82aa1ba6104.txt)、[web-profile](../../library/text/f6eec2435b8e252431253e1ec9a866ddff8d33f1cb3514e0f3d0c279afe9fbd3.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 本次整合增加的待核验项

- Web 事件分类 KOL 前缀优先与日级 delivery 优先处于不同层；active 与 DM 依赖的旧说法有冲突，需查 SQLX 及同一用户日样本。
- 移动端 ASA 花费旧说明使用未指明的 DWS 新表，统一 cdct 是否完整覆盖需实际对账；不能静默换源。
- 18 个内部账号名单源于 2026-06-23；当前默认按事件时点 user_id 排除并保留适用的匿名用户。整设备排除是另行声明的保守口径；名单是否增减仍需业务依据。

## 目录与正文复核新增记录（2026-09-12）

- Fashion 收入旧“首次成功后全部交易”规则已依据现有订单表和 2026-08-28 说明修正为每单前后 600 秒最近事件；旧版本保留，不将本次日期作为生效日期。
- BigR 播报概述的旧 ADS＋today_income 求和与状态表账本定义冲突，已统一为 lifetime_value；未执行播报。
- Web 分层阈值损坏已依据 2026-09-13 用户确认解决：500 / 100 / 50，累计实收美元；旧 500 / 200 / 100 失效。历史报告人数矛盾仍未验证。
- 旧表名/标题和订单分区信息仍需以对应当前表正文及实际 schema 复核，不将历史字典当现网定义。
- 2026-05-21 的生成字典和已废弃分端规则表作为历史资料；移路径不改变其业务有效状态。

本次校正依据：[collart_android/tables/aidata2025.ads_collart.big_r_user_value_state.md](../../library/text/e3c9f0985b81dd2e82b81dc8137524506c9b4722d44cdcdd5800528dbf2e4978.txt)。

本次校正依据：[collart_fashion/indicators/fashion_revenue.md](../../library/text/44105210e9257fd2cd1fe584833b5d7ce8d6b799f8e81250bcebf0f2ef089d46.txt)。

2026-09-14 已对齐：Android 全部固定 DAU 阈值删除；经营成本与历史 ASA 关键词粒度分开；Web 分层净额与历史收入毛額分开；原始埋点只能最近 30 天，旧任意历史 30 天规则不再适用。文档层解决不等于生产数据验证。

## 2026-09-14 对齐依据

- [collart_web/indicators/user_value_tier.md](../../library/text/0c2685cfa8e32c90ab56b90f8cf22cb5c2f4d4369567f927f2e705130879dbf2.txt)
- [collart_android/indicators/dau.md](../../library/text/5126e2275883955da33ab341e7f2e3a86de550334d2dc4644a6394211a7d7ccb.txt)
- [1company/analysis_playbooks/internal_user_filter.md](../../library/text/caa37c80bb7cb697b26799d050b2d4c91826197db6905e4e136745e360987807.txt)
- [1company/analysis_playbooks/collart_ads_redlines.md](../../library/text/0b81b22d1f69db06c82072ba3fd281d4a0c50d057038b6543cf9c82aa1ba6104.txt)
