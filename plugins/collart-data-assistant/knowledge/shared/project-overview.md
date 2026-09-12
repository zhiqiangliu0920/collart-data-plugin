---
id: "shared-project-overview"
title: "项目范围与四端标识"
project: "shared"
kind: "business"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["ads-routing", "events", "fashion-orders", "team-shared-project-overview", "cursor-platforms-md"]
tags: ["业务", "项目", "Android", "iOS", "VidArt", "Web", "Fashion"]
supersedes: []
verification_evidence: []
---

# 项目范围与四端标识

## 适用范围

首版面向 Collart 的 Android、iOS/VidArt、Web 主站和 Fashion 服装子站。Fashion 与主站共用部分数据底座，分析时应显式选择项目边界。完整用户画像、商业策略与市场目标尚未收录。

| 项目 | ADS dataset | 加工层 package_name | 业务区分 |
|---|---|---|---|
| collart_android | `aidata2025.ads_collartandroid` | `free.ai.photo.generator.collart.ai` | Android App |
| collart_ios | `aidata2025.ads_collartios` | `ai.photo.video.generator.fotos.ai.image.picture.editor.app.free` | iOS；历史项目名 VidArt |
| collart_web | `aidata2025.ads_collartweb` | `collart_web` | Web 主站 |
| collart_fashion | `aidata2025.ads_collartfashion` | `collart_fashion` | 服装子站 |

ODS、旧 DWD、DM 和 ADS 可能使用不同 app_name / package_name，不能全局替换名称。例如 ODS `collart-web` 与 ADS `collart_web` 需按表确认。

## 业务与数据边界

- 用户、设备、访问和付费订单是不同实体，人数计算必须先选身份粒度。
- Fashion 与 Web 收入涉及同一 Stripe 来源，合并前先证明交易归属互斥，不能直接相加。
- `app_info.id IS NULL` 能区分 Web 事件与 App，但不足以独立区分 Web 主站与 Fashion，需相应产品归属条件。

继续查 [选表](table-routing.md)、[身份映射](../collart_web/identity.md) 或 [Fashion 收入](../collart_fashion/revenue-boundary.md)。

## 来源与状态

来源摘录：[ads-routing](../../provenance/excerpts/ads-routing.txt)、[events](../../provenance/excerpts/events.txt)、[fashion-orders](../../provenance/excerpts/fashion-orders.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

> 历史资料：下列规模、百分比、收入金额、覆盖起点、缺口和固定 0 均来自原文中的历史观察；缺少采样日期的数字只作背景，不能作为当前基线、目标或现网状态。仓库改造说明是维护经验，不是部署授权。

## 四端平台笔记

各端基线、核心功能、专属口径与坑。分析该端前先扫对应小节。

---

### Android（`collart_android`）

- **DAU 基线**：约 5–8 万为正常区间；异常时看国家/新老结构健康度。
- **结构特征**：高 churn，新用户常占 DAU >45%；ARPU 波动来自投放缩量 + 点数包大单。
- **核心功能梯队**：img2video 等生成功能为主；功能渗透率/漏斗用 event_metric 三层。
- **投放**：ga_delivery / fb_delivery 留存弱于自然量；巴西常见无效流量拖累。
- **巴西订阅瓶颈**：卡在支付成功率（点击→成功约 1.06%），非曝光；关注 GP 可用性与场景化定价。
- **大 R 准实时**：`ads_oper_...big_r_realtime_today_income`（当日累计价值播报）；手动加大 R 走平台+UUID 直写，不查高价值表。
- **俄罗斯支付**：用户粒度收入用 Stripe `currency='RUB'`（不要 `ods.orders`）；整点播报见知识库。

### iOS（`collart_ios` / 项目名 VidArt）

- **标识**：bundle `ai.photo.video.generator.fotos.ai.image.picture.editor.app.free`；app_name `vidart_ios`；DM 另滤 `LOWER(app_name)='vidart'`。
- **覆盖**：ADS 自 2026-05-24；更早无包数据。
- **结构**：放量期新增/DAU 大涨但 D1 偏低（如约 3.3%）；收入靠点数包大单；美国依赖高、巴西无效流量高（约 44%）。
- **ASA**：成本首选 DWS 新表；归因三级兜底；active delivery/ASA 快照优先（见 [channels-attribution.md](channel-attribution.md)）。
- **收入**：用户粒度 = Apple IAP + Stripe RUB；country 层无 new/resub/trial 拆分；`ad_revenue=0`。
- **周环比**：与 Android 对齐 sort_id/metric_name 矩阵。

### Web 主站（`collart_web`）

- **过滤**：events 必带 `app_info.id IS NULL`；统计默认排除内部用户（[internal-users.md](internal-users.md)）。
- **覆盖**：行为层自 2026-02-12。
- **结构**：2 月起量、5 月变现峰值、6 月量额双降；D2 留存走弱（约 6.7%→4.5%）；商业化转向点数包 + 高 ARPU 老用户。
- **付费结构**：iOS 端 ARPPU 最高；订单偏月包 Standard，收入偏年包 Premium（约 82.9% 收入来自年包）。
- **ROAS**：delivery 3 月首日 ROAS 约 9.4%，实操回本下限约 20%；缺完整 D180 delivery cohort 时标注模型假设。
- **DeepClick**：投放识别分三层，不可混算（见 channels-attribution.md）。
- **Fashion 划分**：加工表用 `package_name`；events 用 `page_location` 含 studio/fashion。

### Fashion 服装子站（`collart_fashion`）

- **共用底座**：与 Web 同 DM/旧表，靠 `package_name='collart_fashion'` 分端。
- **覆盖**：自 2026-06-01，缺 2026-06-06。
- **收入**：Stripe 订单表 → active → attr/country/daily；`purchase_revenue` 含点数包。旧日收入表已停写。country `delivery` 仍为 0。
- **访客口径**：有效访客率 = 有效访客/访客；关注视频漏斗 step2→step3 流失。
- **新用户**：用 new 表 + package_name，禁 events 手拼。
- **专属埋点**：`fashion_*` 事件与扩展 service_type。
- **内部用户**：沿用 Web 排除名单。

---

### 四端对比要点

- 四端 ADS 有共同框架，实际字段可能不同；选取经核实的共同列用 daily/country `UNION ALL`（见 [table-routing.md](table-routing.md)）。
- Fashion 收入已接 Stripe；country 花费仍为 0，四端花费对比时单独说明。
- 周环比矩阵四端共用 sort_id/metric_name，视觉与口径可对齐。


来源快照：[cursor-platforms-md](../../provenance/excerpts/cursor-platforms-md.txt)。
