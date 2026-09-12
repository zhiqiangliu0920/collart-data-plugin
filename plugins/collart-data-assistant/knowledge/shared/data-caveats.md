---
id: "shared-data-caveats"
title: "数据坑与校验经验"
project: "shared"
kind: "quality"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["cursor-data-caveats-md"]
tags: ["data-caveats", "数据坑与校验经验"]
supersedes: []
verification_evidence: []
---

# 数据坑与校验经验

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

> 历史资料：下列规模、百分比、收入金额、覆盖起点、缺口和固定 0 均来自原文中的历史观察；缺少采样日期的数字只作背景，不能作为当前基线、目标或现网状态。仓库改造说明是维护经验，不是部署授权。

## 数据坑与校验经验

分析前快速扫一眼；对账/异常排查时详读对应条目。

### 覆盖与时间

| 坑 | 说明 |
|----|------|
| 覆盖起点 | Android 2025-01-01、iOS 2026-05-24、Web 2026-02-12、Fashion 2026-06-01（缺 06-06）；早于起点回落旧表 |
| 收入 T+1/T+2 | 当日订阅/充值 UV 可能尚未完整；需验证回刷任务，不预先排除故障。收入类指标日报常用 T-2，其他 T-1 |
| GA4 intraday | `events_intraday_*` 未 finalize；iOS 2026-08-07 曾有相关事故；不能据此诊断之后的所有归零 |

### 对账（新表 vs 旧表）

| 坑 | 说明 |
|----|------|
| DAU 高度一致 | Android/Web active vs 旧 DWD，约 86% 日完全相等 |
| is_active NULL | 旧 DWD 2025-08 前 `is_active` 全 NULL，对账勿筛 is_active |
| Web 渠道 | `organic→delivery/nature` 是口径升级；8 月起 DNU 偏高 ~8–17% |
| iOS 渠道 | `traffic_src_type` 约 30% 差异是 DM 归因更准，非 bug；禁止为对账回退旧口径 |
| subscribe_7d | 旧 `first_7_vip_user` 与新 `subscribe_uv_7d` 语义不等价，不可硬比 |
| country vs ad_sub | 订阅三类来自 DWS，非 `ads_ad_sub_revenue_1h`；国家×日仅 ~15% 键完全对齐 |
| Stripe 漏单 | Web：同日 DM 优先，否则 id_map 不卡首见日。2026-09-06 回补后 90 天 active purchase **$182,766**；真 miss（无设备）约 $8.7k 仍不进表。profile = SUM(active) |

### 收入口径

| 坑 | 说明 |
|----|------|
| 双计 | 勿 `purchase_revenue + credit_revenue`（purchase 已含 credit） |
| 新旧 total | 旧 `total_revenue`=内购+广告 ≠ 新 `purchase_revenue`（仅内购） |
| Fashion 收入 | 用户日走 active（订单表汇总）；country/daily 从上卷，不再读旧日收入表。country `delivery` 仍硬编码 0，专项再接 |
| 俄罗斯 purchase_uv | App 端接近 0：RUB 不打客户端 `is_purchase`；用户粒度金额看 active/profile 的 Stripe RUB，勿扫 `ods.orders`，勿当回补失败 |

### 留存 / 窗口

| 坑 | 说明 |
|----|------|
| 未到期 NULL | 前视留存未到期是 NULL，勿 COALESCE 成 0 |
| 回填 overhang | 按月回填 active/指标层要带 `to_date+29`，否则 retain.d30 永久冻住 |
| active 重写窗 | active 重写窗 biz-30 由 retain.d30 决定，不可缩；event_metric 可缩到 biz-2 |
| 窗口方向 | Android subscribe_uv_7d 前向 [0,6]；iOS/Web/Fashion 部分 DATE_DIFF 方向相反 |

### 事件 / 漏斗

| 坑 | 说明 |
|----|------|
| 稀疏宽表 | `user_event_metric_di` 无命中日不出行，算占比分母用 active |
| AI 失败事件 | 不同失败事件勿简单相加；区分区域性 timeout（如俄罗斯模板失败是 apiv2 区域 timeout，非内容问题） |
| 广告展示 | `ad_value` 与国家 ADS DAU 表混用时注意口径一致 |
| 投放花费 | 只认 cdct / country.delivery。ODS facebook 表、旧 `dws_oper_fb_delivery_1d` 会停更或包名不同，勿当现网 |
| Web 包名 | ODS `collart-web` vs ADS/cdct `collart_web` 是两层命名，不是脏数据 |
| Web 一设备多登录 | profile 一行一个 `user_pseudo_id`。`user_id` 只是最后一次登录；按登录号查用 `UNNEST(user_ids)`，不要 `WHERE user_id =` |

### 表结构（维护侧，供数据同学）

| 坑 | 说明 |
|----|------|
| 列序 | country/daily 是位置式 INSERT，物理列序必须与 SQLX 一致；漏改 INSERT 列清单会报 column count |
| 字段说明 | `DROP+CREATE` 会丢 schema description，重建后重跑 apply 脚本 |
| 生成器 | 只改 SQLX 生成器、勿手改 sqlx；热指标改 Google Sheet、勿跑 seed |


来源快照：[cursor-data-caveats-md](../../provenance/excerpts/cursor-data-caveats-md.txt)。
