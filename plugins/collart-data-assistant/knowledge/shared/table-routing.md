---
id: "shared-table-routing"
title: "按分析问题选择 ADS 表"
project: "shared"
kind: "table"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["ads-routing", "ads-redlines", "team-shared-table-routing", "cursor-table-routing-md"]
tags: ["选表", "DAU", "日活", "收入", "渠道", "国家", "profile"]
supersedes: []
verification_evidence: []
---

# 按分析问题选择 ADS 表

## 选择原则

下面是现有资料提供的四端 ADS 表族，完整表名为 [项目 dataset](project-overview.md) 加表名。作为查数起点；实际字段、分区和有效覆盖需现场检查。

| 问题 | 表名 | 主要粒度与限制 |
|---|---|---|
| 日总览、趋势 | `ads_oper_basic_indicator_daily_di` | 日 × 项目/包；确认实际唯一键 |
| 国家、投放、服务端收入 | `ads_oper_basic_indicator_country_di` | 日 × 国家；核实总计行，避免重复汇总 |
| 渠道、版本、新老、VIP | `ads_oper_basic_indicator_attr_di` | 日 × 多维；无设备维，不能按设备直接下钻 |
| 用户日活、设备、当日行为/收入 | `ads_oper_user_active_di` | 设备/用户 × 日；可能含有收入但无活跃行 |
| 生命周期画像 | `ads_oper_user_profile_df` | Web 一设备一行；不等于一登录账号一行 |
| 已配置事件、漏斗 | `ads_oper_user_event_metric_di`、`ads_oper_event_metric_attr_di`、`ads_oper_event_metric_country_di` | 用户事件表可能稀疏，缺行不表示用户不存在 |
| 埋点规则 | `ads_dim_metric_rule` | 确认指标事件、参数条件及是否已进宽表 |

## 验证取数是否可靠

先查请求时间范围内的分区、唯一键和关键字段，再计算指标。下游执行显示成功不代表上游数据完整。缺分区、空表、占位 0、查询无权限需要分别记录。

旧表仅用于字段缺失、历史窗口或旧看板对照，并说明映射。不要根据旧文档中“新 dataset 为空”直接绕过 ADS；见 [资料冲突](known-conflicts.md)。

## 来源与状态

来源摘录：[ads-routing](../../provenance/excerpts/ads-routing.txt)、[ads-redlines](../../provenance/excerpts/ads-redlines.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

## Collart 表路由

### 决策树

```
问什么？
├─ 日总览 / 趋势 → daily
├─ 按国家 / MAU / 投放花费 / 服务端收入 UV → country
├─ 按渠道·版本·新老·VIP → attr
├─ 用户明细 / Web 设备维（OS/browser/language）→ active
├─ 单用户画像 / 生命周期 → profile_df
├─ 事件漏斗（生成开始→成功等）→ event_metric_* 或 daily 事件 STRUCT
├─ 新埋点 / 参数明细 / ADS 没有的事件 → 先查 ads_dim_metric_rule；热用宽表，冷按规则扫 DM，再下钻 [raw-events.md](event-evidence.md)
└─ 「订阅 UV」？
    ├─ 埋点转化人数 → subscription.*（attr/country）
    └─ 实际付费人数（订单）→ revenue.*_uv（country/daily 为准）
```

口诀：总量→daily；国家/收入/投放→country；渠道版本新老→attr；设备维→active；单用户→profile；已配置热漏斗→event_metric；探新埋点→raw events。

### Dataset 与表族（共同框架，具体字段按端核实）

| 端 | dataset |
|----|---------|
| Android | `aidata2025.ads_collartandroid` |
| iOS | `aidata2025.ads_collartios` |
| Web | `aidata2025.ads_collartweb` |
| Fashion | `aidata2025.ads_collartfashion` |

每端常用表（全限定 = `{dataset}.表名`）：

| 层 | 表名 | 粒度 | 主要用途 |
|----|------|------|----------|
| 用户日活 | `ads_oper_user_active_di` | 用户×日 | 明细、设备维、前视留存、订阅/收入行 |
| 画像 | `ads_oper_user_profile_df` | 1 用户 1 行（Web=1 设备 1 行） | 生命周期、注册渠道、LTV、active_days；Web/Fashion 另有完整 `page_referrer`；Web 另有 `user_ids`（该设备全部登录号），`user_id` 只是最后一次登录 |
| 指标 attr | `ads_oper_basic_indicator_attr_di` | 日×默认维 | 渠道/版本/新老/VIP 下钻 + 埋点订阅 |
| 指标 country | `ads_oper_basic_indicator_country_di` | 日×国家 | 国家排行、投放 delivery、MAU、**服务端 revenue** |
| 指标 daily | `ads_oper_basic_indicator_daily_di` | 日×包 | 日报总览、趋势、事件漏斗列、AI 成本 |
| 用户事件宽表 | `ads_oper_user_event_metric_di` | 用户×日 | 热指标 `*_pv`，稀疏（无命中不出行） |
| 事件 attr | `ads_oper_event_metric_attr_di` | 日×默认维 | 漏斗 `STRUCT<uv,pv>` 多维 |
| 事件 country | `ads_oper_event_metric_country_di` | 日×国家 | 漏斗上卷 → daily |
| 日报环比 | `ads_oper_basic_indicator_daily_compare_di` | 指标×国家 | 昨日 vs 前 7 日均；`首日订阅转化率` 用 `purchase_uv_1d` |
| 指标规则维表 | `ads_dim_metric_rule` | 1 指标 1 行 | 热/冷漏斗口径；Sheet 外表。宽表没有的指标按规则扫 DM / `events_*`，见 [raw-events.md](event-evidence.md) |

默认维度（attr）：`is_new × is_vip × country × traffic_src_type × traffic_src_platform × traffic_src_name × app_version`(Top5→other)。

依赖链：`GA4 events_* → DWD → DM → active → attr → country → daily`；事件：`DM+active → user_event_metric → event_metric_attr → event_metric_country → daily`。

#### DM（上游事件语义层）

| 端 | 表 | 备注 |
|----|----|------|
| Android | `aidata2025.dm.dm_collart_android_user_event_di` | 上游多为 DWD 事件三表 |
| iOS | `aidata2025.dm.dm_collart_ios_user_event_di` | 同上 |
| Web + Fashion | `aidata2025.dm.dm_collart_web_user_event_di` | **共用**，按 `package_name` 分流；上游直接扫 GA4 |

原始埋点表位置、过滤、关键 `event_name`、参数提取见 [raw-events.md](event-evidence.md)。

### package_name / app_name

| 端 | package_name | app_name | 旧表注意 |
|----|--------------|----------|----------|
| Android | `free.ai.photo.generator.collart.ai` | `collart_android` | events 过滤 `app_info.id = 'free.ai.photo.generator.collart.ai'` |
| iOS | `ai.photo.video.generator.fotos.ai.image.picture.editor.app.free` | `vidart_ios` | DM 另滤 `LOWER(app_name)='vidart'`；旧 `ads_oper_user_new_collart_di` 不含本包 |
| Web | `collart_web` | `collart_web` | 旧 DWD/ADS 写 `collartweb`（无下划线）；events `app_info.id IS NULL`；**ODS 是 `collart-web`，ADS/cdct 用 `collart_web`，不要混** |
| Fashion | `collart_fashion` | `collart_fashion` | 旧数据混在 Web DWD；events 用 `page_location` 含 studio/fashion |

跨端 ODS / 播报里的 app_name 另有写法：`vidart-ios`、`collart-android`、`collart-web`（带连字符）。**ADS / cdct 分析层用下划线：`collart_web`。** 两套命名并存，不是脏数据。

### attr / country / daily 选型细节

| 表 | 有 | 没有 / 限制 |
|----|-----|-------------|
| attr | 埋点 `subscription` STRUCT、渠道/版本/新老/VIP 多维 | **无 MAU**、**无设备维**；Web `app_version` 多为 NULL |
| country | MAU（Android）、投放 `delivery`（来自 `dwd_cdct_delivery_cost_di`）、**服务端 `revenue`（Android/iOS/Web 独立源；Fashion 从上卷 attr）** | Fashion `delivery` 仍硬编码 0，专项再接 |
| daily | 每端每日 1 行；事件漏斗 STRUCT、AI 成本 | = SUM(country) + SUM(event_metric_country) |

### 历史覆盖起点（查数前先看）

| 端 | 有效起点 | 备注 |
|----|----------|------|
| Android | 2025-01-01 | 587 日无断档 |
| iOS | 2026-05-24 | 更早 DWD 无包数据 |
| Web | 2026-02-12 | GA4 导出此前稀疏；行为层无更早 |
| Fashion | 2026-06-01 | 缺 2026-06-06；收入看 active/daily `purchase_revenue`，country `delivery` 仍为 0 |

### 旧表回落（默认不用）

仅当新表缺字段、日期在覆盖窗外、或必须对齐旧看板时回落，并显式映射包名/渠道枚举、在回复标「旧表」：

| 旧表 | 场景 |
|------|------|
| `aidata2025.dwd.dwd_oper_user_collart_di` | Android 旧字段：`subscribe_time`/`country_level`/`network_type`/`device_total_ram`/`mobile_marketing_name` |
| `aidata2025.dwd.dwd_oper_user_collartweb_di` | Web 旧 `collartweb` 对账、`is_main`、更早分区；Fashion 历史混存 |
| `aidata2025.ads_collart.ads_oper_basic_indicator_collart_di` | Android 2025 长历史维度指标对照 |
| `aidata2025.ads_collart.ads_oper_basic_indicator_collartweb_di` | 旧 Web/Fashion 指标看板对照（按 `package_name` 分端） |
| `aidata2025.ads_collart.ads_oper_basic_metric_collart_android_di` | 旧巨型 CASE 漏斗（71 字段）；新表改用 event_metric 三层 |
| `aidata2025.ads_collart.ads_oper_user_new_collartweb_di` | Web 完整历史新增名单（原历史样本中 profile 缺约 8.5% 从未进 active 的用户，当前覆盖需复核） |

旧→新 daily 字段映射（对账用）：`new_user→dnu`、`vip_user_0→purchase_uv_1d`（2026-08-25 起）等，详见 [metric-upgrades.md](metric-upgrades.md)。

### 四端合并查询骨架

采用 [统一参数化模板](../../presets/four_platform_daily.sql)，各端显式限定日期，保留端维度。扩展字段前分别核对 schema，不能假定 iOS 的分类收入 UV 与其他端一致。Web/Fashion 的人数及收入不能直接跨端相加。

来源快照：[cursor-table-routing-md](../../provenance/excerpts/cursor-table-routing-md.txt)。
