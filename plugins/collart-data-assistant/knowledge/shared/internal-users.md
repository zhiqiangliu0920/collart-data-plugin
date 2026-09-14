---
id: "shared-internal-users"
title: "内部用户过滤"
project: "shared"
kind: "metric"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["cursor-internal-users-md", "review-20260914-7552f1c9b18c"]
tags: ["internal-users", "内部用户过滤"]
supersedes: []
verification_evidence: []
---

# 内部用户过滤

适用于 Web 与 Fashion，不自动扩展到 Android/iOS。统一名单见[内部账号配置](../../config/internal-user-ids.json)，当前沿用 18 个 ID，原提供日期为 2026-06-23。名单必须非空、无 NULL、无重复；本次来源核对不表示重新确认人员增减。

默认按事件时点 `user_id` 排除。允许匿名的指标使用 `(user_id IS NULL OR user_id NOT IN (...))`，登录或映射到用户的付费分析使用 `user_id NOT IN (...)`。只有 pseudo 时先依据适用身份映射，无法映射的部分说明覆盖限制，不排除所有匿名用户。

在已有确定用户键的只读查询中，可参考[时点过滤片段](../../presets/internal_user_filter_event_time.sql)。设备画像按历史绑定整设备排除是一种额外的保守口径，可能连带真实客户；仅在明确采用该口径时使用[整设备模板](../../presets/internal_user_filter.sql)，不能将其称为默认时点排除。

过滤名单之外还须保留产品归属、成功订单、去重和观察窗。不能仅因用户访问 Fashion 就将其所有支付归入 Fashion，也不能从另一套聚合收入直接扣测试账号收入。

## 2026-09-14 对齐依据

- [1company/analysis_playbooks/internal_user_filter.md](../../library/text/caa37c80bb7cb697b26799d050b2d4c91826197db6905e4e136745e360987807.txt)
