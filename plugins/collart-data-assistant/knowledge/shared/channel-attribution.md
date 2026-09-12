---
id: "collart_web-channel-attribution"
title: "四端渠道归因：Web、Android、iOS 与 Fashion"
project: "shared"
kind: "metric"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: "2026-09-05"
sources: ["web-channel-review-7003847ee3", "ads-redlines-review-954bdf4e17", "team-collart_web-channel-attribution", "cursor-channels-attribution-md"]
tags: ["ASA", "Android", "DeepClick", "Facebook", "Instagram", "X", "fb_delivery", "iOS", "traffic_src_platform", "x_delivery", "归因", "渠道"]
supersedes: []
verification_evidence: []
historical_sources: ["web-channel", "ads-redlines"]
---

# Web 渠道层级与 X、Meta 归因

## 已记录的范围

Web `traffic_src_type` 是性质，主要为 `delivery / nature / inhouse / kol`；`traffic_src_platform` 是具体平台。不要混用性质与平台枚举。

- Web 平台 `x_delivery` 是现有资料的归一值，历史 `x` / `X` 为旧同义值。该规则不能外推到 iOS。
- Instagram 归入 Meta 的 `fb_delivery`；不要把自然 facebook.com referral 自动升为付费投放。
- `sptt-` / `tt_official` 等 KOL 规则与付费 TikTok 区分；平台字符串相似不能替代来源证据。
- attr 有平台维；country/daily 的 delivery 汇总不是具体平台分桶。

资料记载 Web X 规则始于 2026-09-05，并于 2026-09-10 处理画像残留旧值；这不证明当前各表已完全一致。分析时核对查询期间的枚举、归属层和 cohort 定义。

画像首次来源、当日来源、正式投放人群是不同对象。回答某渠道的付费转化前，明确“首次通过该渠道获得的用户”还是“当日在该渠道活跃的用户”，再确定付款窗口和成本映射。

## 来源与状态

来源摘录：[web-channel](../../library/text/7003847ee3571b56821e6c6a1df55b36d64edbfbe087fbf66ee737f90aaae32a.txt)、[ads-redlines](../../library/text/954bdf4e178b2f0cb89369eeeed99c2f3c2ac468f427db24fe151ee596c242a0.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

## 渠道与归因

### 两层拆分（新 ADS）

旧表把 `ga_delivery`/`fb_delivery` 写在 `traffic_src_type`；新表拆两层：

| 字段 | 含义 | 取值示例 |
|------|------|----------|
| `traffic_src_type` | 渠道**性质** | `delivery` / `nature` / `inhouse` / `kol` |
| `traffic_src_platform` | 具体**平台** | `ga_delivery` / `fb_delivery` / `asa` … |
| `traffic_src_name` | campaign/来源名 | — |

- `traffic_src_platform` 对齐旧 `traffic_src_type` 约 99.8%，对账时按 platform 重映射。
- Web / Fashion 画像 `page_referrer`：最早 `first_visit` 的完整上一跳 URL（空串保留；无 first_visit 则最早事件）。常规上一跳分析用画像，不必扫 `events_*`。

### organic → nature（Web 红线）

- 新 ADS 自然量桶叫 **`nature`**，不再是旧表的 `organic`。
- 但 `dnu_by_source.organic` 字段名保留，取值内部映射自 `nature`。
- 渠道看板**勿再期望 `organic`**；筛自然量用 `traffic_src_type='nature'`。

### Web 渠道优先级

日级多来源汇总的来源记录为（与下文单条事件分类的 KOL 前缀优先不是同一层）：`delivery → inhouse → kol → nature`。

### Android 投放

- `traffic_src_type='delivery'` + `traffic_src_platform` 区分 `ga_delivery` / `fb_delivery` / `x_delivery` / `tt_delivery`。Instagram 属于 Meta，一律 `fb_delivery`，不再单列 `ig_delivery`。
- `sptt-` / `tt_official` / `tt_*` / `youtube_*` 保持 **kol**；只有付费 TikTok（source/adjust 含 tiktok、bytedance，或 campaign `TT-` / `TIKTOK`）才叫 `tt_delivery`。
- 注册渠道（profile）= **首个 delivery 优先**；type/platform/name 三字段同源同行，勿跨行拼。

### iOS ASA

- ASA 成本先按统一 cdct 花费规则核对覆盖；若来源不覆盖则记录缺口，使用明确有血缘的补充源；归因三级兜底（campaignID/keywordID 生命周期扫描）。
- DM platform：`source=apple` **或** 数字 `campaignID`（含 traffic_src_name 为纯数字）→ `asa`，避免 (direct) 残留进 `other_delivery`。
- active **当日 delivery/ASA 快照优先**，避免被「末次 nature」冲掉（这是 ASA v3 修复点）。
- ASA params 在 2026-07-26 前缺失；campaign/keyword 读 active/profile，少扫 GA4。
- **intraday 坑**：2026-08-07 曾记录 intraday 未 finalize 导致归因缺失；后续归零必须重新查分区、归因与实际业务。
- campaign/keyword cohort 用 GA4 **finalized** 分区，`_TABLE_SUFFIX BETWEEN`。

### DeepClick（Web 投放识别）

DeepClick 分三层，A 与 B 大量不重叠，**不可混算**：

1. 回流后缀（`REGEXP_CONTAINS` 匹配后缀）
2. `from_app = dc_*`
3. 干净 FB campaign（清洗 campaign 名）

### Web delivery 判定（2026-09-05 对齐 Android）

`dm_collart_web_user_event_di` 同时写 type + platform：

1. **kol 前缀优先**：name/property 匹配 `^(kol|sptt-|spytb-|tt_|youtube_)` → kol（`sptt-`/`tt_official` 不是 tt_delivery）
2. **主**：`medium ∈ {paid_social,cpc,ppc,paid,display,paid_search,cpv,cpm}` → delivery  
3. **兜底**：campaign name 命中 `%fb%collart%` / `%ga%collart%` / `%meta%collart%` / `^fb-cw` / `^ga-cw` / `%sea%`，或 `page_location %offical%` / `utm_source=X`，或 `from_app=dc_*`  
4. 勿用 `source=facebook` 或 `source=tiktok.com` referral 单独判投放。2026-09-06 确认：**保持现网**，不要改成 traffic_source.name + page utm_source + user_properties.utm_source 三源拼 FB（付费量几乎一样，多出来的是自然 referral）。  
5. delivery platform：`x_delivery` / `tt_delivery` / `ga_delivery` / `fb_delivery` / `applovin_delivery` / `dc_delivery` / `other_delivery`。落地页 `utm_source=tiktok` 也进 `tt_delivery`。IG campaign / source=ig|instagram 并进 `fb_delivery`。  
6. Active：优先用 DM `traffic_src_platform`；当日出现过 X 落地页仍优先 `x_delivery`

### 日级 delivery 判定

当日**出现过** delivery → 该用户当日 `type=delivery`（否则取末次快照）。Web active 与 DM 的依赖存在来源表述冲突，须核对当前 SQLX，不能假定不受上游归因变化影响。

### 对账红线

- **禁止**为对账把 iOS 渠道回退到旧 basic 口径；保持 DM 归因，下游知悉即可（DM 归因更准，30% 差异非 bug）。
- 渠道看板对账时显式列「预期语义差」（organic→nature、type→platform），不要无说明地对冲数字。
- 内部用户不计入投放效果评估（见 [internal-users.md](../shared/internal-users.md)）。


来源快照：[cursor-channels-attribution-md](../../provenance/excerpts/cursor-channels-attribution-md.txt)。
