---
id: "collart_web-identity"
title: "Web 设备画像与登录账号映射"
project: "collart_web"
kind: "table"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: "2026-09-07"
sources: ["review-20260914-af2e0602c86f", "review-20260914-ca27ec86b3b2", "team-collart_web-identity"]
tags: ["user_ids", "user_id", "user_pseudo_id", "身份", "UUID", "ads_oper_user_profile_df"]
supersedes: []
verification_evidence: []
historical_sources: ["web-profile", "ads-redlines", "ads-redlines-review-954bdf4e17", "web-profile-review-be4e210655"]
---

# Web 设备画像与登录账号映射

## 表与粒度

`aidata2025.ads_collartweb.ads_oper_user_profile_df` 的资料定义是一台设备/浏览器（`user_pseudo_id`）一行的生命周期画像，不是登录账号一行。资料称此表无分区、按近期变化 MERGE；是否仍如此需查当前 schema 和实现。

| 字段 | 含义 |
|---|---|
| `user_pseudo_id` | 设备/浏览器键 |
| `user_id` | 设备最后一次登录号 |
| `user_ids` | 该设备历史绑定的登录号数组 |
| `current_active_days` | 资料中的滚动活跃天数 STRUCT，不能解释成终身活跃天数 |

## 按登录号检索

```sql
SELECT user_pseudo_id, user_id AS last_user_id, user_ids
FROM `aidata2025.ads_collartweb.ads_oper_user_profile_df`
WHERE @login_user_id IN UNNEST(user_ids)
```

这是资料支持的画像查找方式，未在本次执行；不能只用当前标量 `user_id` 等值来找历史绑定。对其他原始事件或业务表，需按其自身 schema 同时考虑标量/数组身份，不把画像规则盲目套用。

一个账号可能对应多个设备，一个设备可能绑定多个账号。设备收入不能完整复制给所有绑定账号；账号行为日期也不能直接用设备滚动活跃天数代替。Fashion 是否有同名数组字段需单独核验。

## 依赖与已知限制

上游包括 active、user_event_metric 与身份映射。画像滚动字段是否随时间推进更新，要检查当前 MERGE 条件；“字段存在”不代表字段及时刷新。

## 来源与状态

来源摘录：[web-profile](../../library/text/f6eec2435b8e252431253e1ec9a866ddff8d33f1cb3514e0f3d0c279afe9fbd3.txt)、[ads-redlines](../../library/text/0b81b22d1f69db06c82072ba3fd281d4a0c50d057038b6543cf9c82aa1ba6104.txt)。原始路径、定位和哈希见 [来源清单](../../provenance/sources.json)。本条是 2026-09-12 的资料整理，未进行本次生产查询或业务负责人确认；当前可用性与未明确的细节需继续核验。
