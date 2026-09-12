---
id: "shared-known-conflicts"
title: "旧资料冲突与待核验清单"
project: "shared"
kind: "quality"
status: "draft"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-09-26"
owner: null
verified_by: null
effective_from: null
sources: ["legacy-ios-review-7873df86c6", "ads-routing", "legacy-conversion-review-95f777f166", "metrics", "revenue", "ads-redlines-review-954bdf4e17", "web-profile-review-be4e210655", "team-shared-known-conflicts", "review-e4b31288e0a4a0ad", "review-979740ccfe320f48"]
tags: ["冲突", "旧口径", "空表", "DAU", "iOS", "收入", "current_active_days"]
supersedes: []
verification_evidence: []
historical_sources: ["legacy-ios", "legacy-conversion", "ads-redlines", "web-profile"]
---

# 旧资料冲突与待核验清单

## 已发现的资料差异

这是一份待处理清单，不能作为当前生产状态结论。

| 主题 | 相冲突或易混淆的资料 | 本次处理及下一步 |
|---|---|---|
| iOS ADS 可用性 | 旧 iOS README 称 dataset 为空；ADS 选表资料列出了四端新表 | 不认定哪份代表今天；核对 INFORMATION_SCHEMA 与请求日期的分区 |
| Web DAU | conversion 文档用 session_start 去重作分母；ADS 指标资料要求加工表 | 区分旧事件口径与经营口径，明确本次分析采用哪一种并对账 |
| 收入来源 | 旧订单状态说明与 Stripe/active 收入约定并存；用户层与 country 来源有差别 | 按项目、层、币种、毛净额与生效时间确认，不能把表名替换当作口径等价 |
| 画像/设备活跃字段 | Web profile 表文档用 `current_active_days`，另有通用资料提到 active_days 结构 | 当前字段及更新条件以现网 schema/实现为准，不直接复制字段名 |
| HI、固定 0、历史断档 | 来源把 HI 称为空表，并描述 Fashion delivery 固定 0 | 这些是历史状态，不作为永续规则；查询时复核 |

## 可复现的核验建议

查看相关 dataset 的 INFORMATION_SCHEMA.TABLES / COLUMNS / PARTITIONS；对于全量画像检查构建逻辑与更新时间字段；使用一致窗口对账两套指标并说明差异归因。未执行前不填写 verified 日期。

解决一项后更新受影响的正式条目、保留旧适用范围，并在本表记录解决证据。结构校验通过不会自动解决这里的业务冲突。

## 来源与状态

来源摘录：[legacy-ios](../../library/text/7873df86c69295f85ed8e9755eeb3d430d763d7da3b80770e34a94a7a5201c95.txt)、[ads-routing](../../provenance/excerpts/ads-routing.txt)、[legacy-conversion](../../library/text/95f777f166eb1b047679b87e249be2d23256592aec35ea025fecc122ab8a2d33.txt)、[metrics](../../provenance/excerpts/metrics.txt)、[revenue](../../provenance/excerpts/revenue.txt)、[ads-redlines](../../library/text/954bdf4e178b2f0cb89369eeeed99c2f3c2ac468f427db24fe151ee596c242a0.txt)、[web-profile](../../library/text/89103e23f6e453c60ca981f572a9f9dfe9c4454db375035a9efe1a5490493d78.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 本次整合增加的待核验项

- Web 事件分类 KOL 前缀优先与日级 delivery 优先处于不同层；active 与 DM 依赖的旧说法有冲突，需查 SQLX 及同一用户日样本。
- 移动端 ASA 花费旧说明使用未指明的 DWS 新表，统一 cdct 是否完整覆盖需实际对账；不能静默换源。
- 18 个内部账号名单源于 2026-06-23；需要团队负责人确认是否有增减，以及采用设备历史绑定排除还是事件时点排除。

## 目录与正文复核新增记录（2026-09-12）

- Fashion 收入旧“首次成功后全部交易”规则已依据现有订单表和 2026-08-28 说明修正为每单前后 600 秒最近事件；旧版本保留，不将本次日期作为生效日期。
- BigR 播报概述的旧 ADS＋today_income 求和与状态表账本定义冲突，已统一为 lifetime_value；未执行播报。
- Web 两份用户分层文档阈值损坏、两份 ADS 文件正文标题为 DWD、Web/Fashion orders 分区说明矛盾；保留原件待核对。
- 2026-05-21 的生成字典和已废弃分端规则表作为历史资料；移路径不改变其业务有效状态。

本次校正依据：[collart_android/tables/aidata2025.ads_collart.big_r_user_value_state.md](../../library/text/947f56e7da0a743ed6c7940ea59ea07f0952cb7437d98621fa4e9bb160156e96.txt)。

本次校正依据：[collart_fashion/indicators/fashion_revenue.md](../../library/text/46dea22014119ee3fe10b47a69e0e06102e3d8b4b59a7f5efcf631e206de5e19.txt)。
