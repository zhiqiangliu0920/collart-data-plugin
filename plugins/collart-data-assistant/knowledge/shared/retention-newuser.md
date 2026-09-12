---
id: "shared-retention-newuser"
title: "新用户与留存"
project: "shared"
kind: "metric"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["cursor-retention-newuser-md"]
tags: ["retention-newuser", "新用户与留存"]
supersedes: []
verification_evidence: []
---

# 新用户与留存

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

## 新用户与留存

### is_new 四端口径

| 端 | 口径 | 红线 |
|----|------|------|
| Android / iOS | 当日有 `first_open` | 付费-only 行 FALSE；DAU/留存滤 `is_active=TRUE` |
| Web / Fashion | 当日有 `first_visit` | 同上 |
| 统一语义 | pseudo **首次发现日**，不绑死 first_visit/first_open 分裂口径 | — |

- 旧 Web DWD 的 is_new 填充更窄；新表 2026-08 起 DNU 可能比旧表高 ~8–17%，属语义升级，**不可逐日硬比新增总量**。
- Web 新用户主口径推荐按 `user_pseudo_id` 首次发现（`new_user_by_pseudo_id`），而非 first_visit 事件手拼。

### is_active

- 表只落「活跃 ∪ 当日有收入」行。
- DAU / 留存 / 流失 / 回流 **必须** `is_active=TRUE`。
- 汇总 `revenue.*` 金额时**不过滤** is_active（含付费-only 行）。
- 旧 DWD 表 2025-08 前 `is_active` 全 NULL；与旧表对账时**勿筛 is_active**。

### 留存编号与成熟度

| 字段 | 含义 | 分层 |
|------|------|------|
| `retain.d2` | 次日留存（对齐旧 `retain_2`） | attr=全活跃可按 is_new 切片；**country/daily=仅新用户** |
| `retain.dN` | 锚点后第 (N-1) 天当天活跃 | 同上 |
| `rolling_retain.dN` | 锚点后 [1,N-1] 内任一天活跃 | 同上 |
| `retain2_vip`/`retain2_free`/`retain2_by_source` | 新增×VIP/渠道次日留存 | country/daily 切片；与 `retain.d2` 同属新用户 |

- 前视未到期 = **NULL**，随每日回刷定稿；勿当 0。
- 取成熟留存的典型写法：`SUM(IF(DATE_ADD(event_date, INTERVAL (N-1) DAY) <= @as_of_date, retain.dN, NULL))`；@as_of_date 是已确认完整且回刷完成的最后数据日，分母使用同一批成熟 cohort。
- country/daily 次留率：`retain.d2 / dnu`（不要用 `retain.d2 / dau`）。

### 回补起点（覆盖窗）

| 端 | 有效起点 | 备注 |
|----|----------|------|
| Android | 2025-01-01 | 无断档 |
| iOS | 2026-05-24 | 更早无包数据 |
| Web | 2026-02-12 | 行为层无更早；GA4 导出此前稀疏 |
| Fashion | 2026-06-01 | 缺 2026-06-06 |

- 查早于起点的日期 → 说明限制或回落旧表。
- 回填坑：按月回填 active/指标层必须带 `to_date+29` overhang，否则 `retain.d30` 会被永久冻住（见 [data-caveats.md](data-caveats.md)）。

### 新用户 cohort

- Web/Fashion 用 new 表 + `package_name`，禁用 events 手工拼新增。
- profile 对单用户画像好用，但 Web 历史新增名单历史样本曾缺约 8.5%（当前缺口需复核）（从未进 active 的用户）→ 需要完整历史新增时回落 `ads_oper_user_new_collartweb_di`。
- 有覆盖限制的 profile 设备 cohort 模板见 [presets/web_new_user_cohort.sql](../../presets/web_new_user_cohort.sql)。


来源快照：[cursor-retention-newuser-md](../../provenance/excerpts/cursor-retention-newuser-md.txt)。
