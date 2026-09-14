---
id: "shared-core-metrics"
title: "活跃、新增、留存与指标粒度"
project: "shared"
kind: "metric"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["metrics", "retention", "review-20260914-c52206ae2ac1", "team-shared-core-metrics", "cursor-metric-glossary-md"]
tags: ["DAU", "DNU", "日活", "新增", "留存", "retain.d2", "is_active"]
supersedes: []
verification_evidence: []
historical_sources: ["legacy-conversion", "legacy-conversion-review-95f777f166"]
---

# 活跃、新增、留存与指标粒度

## 资料提供的 ADS 口径

| 指标 | 起点 | 易错点 |
|---|---|---|
| DAU | daily/country `dau`；明细需 `is_active=TRUE` | active 可能包含仅付费、无活跃的行 |
| DNU | daily/country `dnu`；明细确认 `is_new` | 新用户是设备首次发现、first_visit 还是业务注册，不能混称 |
| 新用户次留 | country/daily `retain.d2 / dnu` | `d2` 表示锚点后第 1 天；不能用 DAU 作新用户分母 |
| 当天留存 | `retain.dN` | 锚点后第 N−1 天当天活跃 |
| 区间留存 | `rolling_retain.dN` | 锚点后 [1,N−1] 任一天活跃，语义不同 |

未成熟留存是 NULL，不能补成 0。汇总跨日期留存时，分子和分母使用相同的成熟 cohort 范围。跨维度 UV、跨日 DAU不能直接相加后称为独立用户数。

## 分析前明确

写清项目、起止日期、日期所属时区、设备/账号去重、是否新用户、是否去除内部测试流量。既有资料中“session_start 去重算 DAU”和“使用加工表 DAU”并存，不能把二者视为相同指标，见 [冲突清单](known-conflicts.md)。

金额汇总不要沿用活跃人数的 `is_active=TRUE` 过滤，否则可能丢掉无活跃支付日。`is_vip` 或曾经 VIP 状态不是指定时间窗实际付款证据。

## 来源与状态

来源摘录：[metrics](../../provenance/excerpts/metrics.txt)、[retention](../../provenance/excerpts/retention.txt)、[legacy-conversion](../../library/text/c2a1f847b440b722f91bff925c69d0896d1798d2bd86bcd16565fa0e8fda59d4.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

## Collart 指标口径

### DAU / DNU / MAU

| 指标 | 口径 | 取数 |
|------|------|------|
| DAU | 日活跃用户 | daily/country `SUM(dau)`；查 active 明细时滤 `is_active=TRUE` |
| DNU | 日新增 | daily/country `SUM(dnu)`（旧名 `new_dau`）；attr 上按 `is_new` 切片 |
| MAU | 月活 | **仅 country 表**（Android）有；attr/daily 无 |

- **禁止**用 events `session_start` 去重算 DAU；用加工表。
- `dnu_by_source.{organic,delivery,kol,inhouse}`：字段名保留 `organic`，但取值来自 `traffic_src_type='nature'`；四渠道之外的 type 不进 by_source，SUM 可能 < dnu。

### is_active / is_new / is_vip

| 字段 | 要点 |
|------|------|
| `is_active` | 表只落「活跃 ∪ 当日有收入」行；**DAU/留存/流失/回流必须** `is_active=TRUE`；汇总 `revenue.*` 金额时**不过滤**（含付费-only 行） |
| `is_new` | Android/iOS≈当日有 `first_open`；Web/Fashion≈当日有 `first_visit`；统一语义=pseudo 首次发现日。付费-only 行为 FALSE |
| `is_vip` | Android attr 多为 BOOL；active/profile 为 STRING；**Web/Fashion 的 `is_vip IN ('1','2')` 仅表示对应 VIP 状态；实际窗口内付费必须核实成功交易**；profile 的 is_vip 是「曾经 VIP」sticky |

详见 [retention-newuser.md](retention-newuser.md)。

### 留存

| 字段 | 含义 | 分层注意 |
|------|------|----------|
| `retain.d2` | **次日**留存（对齐旧 `retain_2`） | **attr**：全活跃，按 `is_new` 切片；**country/daily**：已仅汇总 `is_new` |
| `retain.dN` | 锚点后第 (N-1) 天当天活跃 | 同上 |
| `rolling_retain.dN` | 锚点后 [1, N-1] 天内任一天活跃 | 同上 |
| `retain2_vip`/`retain2_free`/`retain2_by_source.*` | 新增×VIP/渠道的次日留存 | country/daily 专用切片；`retain.d2 ≈ retain2_vip+retain2_free` |

- 前视未到期窗口 = **NULL**，随每日回刷定稿；**不要** `COALESCE(...,0)` 当真实 0。
- 前后视窗口方向：Android `subscribe_uv_7d` 为前向 `[0,6]`；iOS/Web/Fashion 部分 DATE_DIFF 方向相反，跨端拼窗口先核对。
- **禁止**在 country/daily 再把 `retain.d2/dau` 当「新用户次留」（分母应是 `dnu`）。

### 订阅 vs 收入（两套「订阅」，必区分）

| 位置 | 含义 | 数据源 |
|------|------|--------|
| `subscription` STRUCT（attr/country） | **客户端/埋点**转化 | active `is_subscribe`/`is_credit_pack`（Android `vip_subscribe_succeed`；iOS Apple 交易类型） |
| `revenue` STRUCT（attr/country/daily） | **服务端/订单/广告**有收入 | DWS / Apple / Stripe |

#### subscription 字段（埋点）

| 字段 | 口径 |
|------|------|
| `subscribe_uv` / `credit_pack_uv` | 新+老当日合计 |
| `*_1d` | 新用户首日 |
| `purchase_uv` | 订阅或点数包去重并集（禁止 `subscribe_uv + credit_pack_uv`） |
| `purchase_uv_1d` | 新用户首日购买并集；country=`SUM(IF(is_new, purchase_uv, 0))` |
| `*_old` | 老用户当日 |
| `*_7d` | 含当日共 7 日窗（`date_diff∈[0,6]`） |
| 恒等式 | `uv = _1d + _old`（`purchase_uv` 无 `_old` 拆分字段） |

#### revenue 金额四桶（在具备该拆分的端与来源内互斥；iOS 等需查实际 schema）

```
purchase_revenue = new_revenue + resub_revenue + trial_conver_revenue + credit_revenue
```

| 字段 | 口径 |
|------|------|
| `purchase_revenue` | 内购合计（已含点数包；= DWS `total_revenue_today`） |
| `new_revenue` | 首购订阅，**不含点数包**（ADS 层已扣 credit） |
| `resub_revenue` | 续订 |
| `trial_conver_revenue` | 试用转正（Web/Fashion 无此桶） |
| `credit_revenue` | 点数包 |
| `ad_revenue` | 广告（country/daily 取自 `ads_ad_sub_revenue_1h`） |

**红线**：勿 `purchase + credit` 双计；旧 metric 的 `total_revenue`（内购+广告）≠ 新 `purchase_revenue`。

#### revenue UV 字段（服务端有收入用户数）

| 字段 | 含义 |
|------|------|
| `new_subscribe_uv` | 当日首购订阅有收入用户（不含点数包） |
| `renew_subscribe_uv` | 当日续订有收入用户 |
| `credit_pack_uv` | 当日点数包有收入用户 |
| `ad_uv` | 当日广告有收入用户；Web/Fashion 固定 0 |

权威层看 **country / daily** 的 `revenue`。iOS country 来自 Apple Sales，无 new/resub 拆分。Fashion 收入从 active 上卷（源=订单表）。T+1：当日订阅/充值 UV 可能尚未完整，需验证回刷任务和数据，不能仅凭偏低认定正常。

### profile active_days

`active_days.d7/d14/d30/d90/d360` = 近 N 日活跃天数（含当日，相对 biz_date）；旧顶层列 `active_days_7d` 已收进 STRUCT。

### SQL 书写习惯

- 每个 `SUM(...)`/派生指标尽量**一行**；维度字段列表可多行。
- `GROUP BY ALL` 可用。
- 业务表项目常为 `aidata2025`；执行使用同事已有授权的连接与计费项目。


首购订阅用户不一定是当天新增访客，不能直接用 new_subscribe_uv/dnu 称作新增用户付费率。分类收入 UV 不能相加代替总付费人数。


来源快照：[cursor-metric-glossary-md](../../provenance/excerpts/cursor-metric-glossary-md.txt)。
