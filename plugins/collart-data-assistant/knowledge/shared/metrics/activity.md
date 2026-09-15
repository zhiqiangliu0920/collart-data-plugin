---
id: "shared.activity"
title: "活跃、新增与成熟留存"
project: "shared"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_android/indicators/retention.md", "previous:shared-core-metrics", "previous:shared-retention-newuser"]
tags: ["DAU", "DNU", "留存", "成熟", "retain.d2", "is_active"]
tables: []
---

# 活跃、新增与成熟留存

## 活跃与新增

DAU = 当日符合产品活跃定义的去重 user_pseudo_id；明细用 active.is_active=TRUE。DNU = 相同范围内正式新增设备，不等于注册账号数。Android/iOS 通常 first_open，Web/Fashion 通常 first_visit；具体首次发现与回填逻辑查项目表。付费-only 行不计 DAU/DNU，但收入保留。不能默认用 session_start UV 替代经营 DAU；不设固定 DAU 告警阈值。

dnu_by_source.organic 是字段名，其源 traffic_src_type 可能为 nature；未覆盖的渠道单列，分项之和未必等于总量。多日 DAU 相加是用户日数，不是期间独立用户数。

## 成熟留存

新增留存 cohort 为指定日新增设备；活跃回访 cohort 为指定日活跃设备。`Dn = cohort 在 cohort_date+n 活跃的去重用户数 / cohort 用户数`。资料中的 `retain.d2` 对应次日，`retain.dN` 对应偏移 N-1；旧 retain_N 后缀不可直接推定。`rolling_retain.dN` 是锚点后 [1,N-1] 任一天活跃。

attr 保留全活跃并用 is_new 切片；country/daily 的 retain 通常已仅上卷新增 cohort，次留分母用 dnu 而非 dau。未到期为 NULL，不能补零；成熟后无回访才计零。跨 cohort 按分子/分母人数加权，窗口包含相同成熟 cohort，不能平均百分比。

## 字段与窗口风险

Android subscribe_uv_7d 资料定义前向 [0,6]；其他端必须核对 DATE_DIFF 方向。滚动 active_days/current_active_days 相对 biz_date，非终身活跃；具体名称以表字典为准。历史覆盖起点、缺分区和更新日期需现场元数据核查，不能沿用旧规模/空表快照。
