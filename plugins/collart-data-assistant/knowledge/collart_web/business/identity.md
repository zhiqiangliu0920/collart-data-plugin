---
id: "web.identity"
title: "Web 画像与账号映射"
project: "collart_web"
kind: "business"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_web/ads_oper_user_profile_df.sqlx", "previous:collart_web-identity", "schema:aidata2025.ads_collartweb.ads_oper_user_profile_df", "sql:web-profile"]
tags: ["画像", "user_id", "user_ids", "Web", "登录号"]
tables: ["aidata2025.ads_collartweb.ads_oper_user_profile_df"]
---

# Web 画像与账号映射

## 表与粒度

`aidata2025.ads_collartweb.ads_oper_user_profile_df` 一台设备/浏览器 user_pseudo_id 一行。2026-09-14 捕获的 schema 有 user_id、user_ids、current_active_days；releaseConfig 源码以近三日 active/UEM 变化设备为更新集合。它不是一账号一行，未验证最近生产运行覆盖。

| 字段 | 含义 |
|---|---|
| user_pseudo_id | 设备/浏览器键 |
| user_id | 该设备最后登录账号，源码比较 active 与 id_map 的最近绑定时间 |
| user_ids | 设备历史绑定账号的并集（id_map ∪ active） |
| current_active_days | 相对构建 biz_date 的滚动活跃天数，不是终身天数 |

## 按登录号检索

```sql
SELECT user_pseudo_id, user_id AS last_user_id, user_ids
FROM `aidata2025.ads_collartweb.ads_oper_user_profile_df`
WHERE user_id = @login_user_id
   OR @login_user_id IN UNNEST(IFNULL(user_ids, ARRAY<STRING>[]));
```

同时检查标量和历史数组，避免旧行数组未填全时漏设备。原样精确比较适用于大小写敏感账号；`sql:web-profile` 沿用原 UUID 大小写归一方式，仅在确认 UUID 语义时使用。输出可能多设备，一台设备又可能多账号。设备全部收入不能复制给每个账号；账号历史应使用交易 user_id。

## 活跃与收入

活跃日期/滚动活跃/留存只取 is_active=TRUE；收入与订阅计数保留 pay-only。画像收入为 SUM(active.revenue)，不二次叠加 orphan。仅变化设备被 MERGE，未变化设备滚动字段可能不随今天自动更新，需按 profile_updated_at / biz_date 解释。

完整字段和加工语句见[画像表字典](../tables/aidata2025.ads_collartweb.ads_oper_user_profile_df.md)。内部账号默认事件时点排除；按历史绑定排除整设备属于另行声明的人群范围。
