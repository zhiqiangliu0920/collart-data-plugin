---
id: "android.acquisition"
title: "Android 活跃与首订变化诊断"
project: "collart_android"
kind: "playbook"
status: "documented"
sources: ["ai-knowledge:collart_android/analysis_playbooks/dau_diagnosis.md", "ai-knowledge:collart_android/analysis_playbooks/first_subscription_diagnosis.md", "previous:collart-android-first-subscription-diagnosis"]
tags: ["Android", "首订", "DAU下降", "新增"]
tables: []
---

# Android 活跃与首订变化诊断

## 活跃变化

从[DAU、新增与留存](../metrics/activity.md)固定用户键、活跃规则和成熟窗口，按[选表入口](../../shared/business/routing.md)读取 daily/country/active。先检查日期完整、每日唯一和数据新鲜度；active 只计 `is_active`，排除仅收入骨架行。

补齐日期轴后，用 `LAG(dau, 1)`、`LAG(dau, 7)` 与 `SAFE_DIVIDE` 比较日环比和同星期几。先拆新增/回访，再拆国家、版本和渠道，比较变化量及对总变化的贡献。跨维度的用户可能重复，不直接加总 UV；不预置固定 DAU 或百分比告警阈值。

## 首次付款

独立构建正式新增 cohort，再关联该 cohort 在观察窗内的首笔成功支付，定义见[付费转化](../metrics/conversion.md)。分母为 cohort 人数，分子为其中首付人数；窗口内付款、首次付款、历史已付费和当前 VIP 状态分别计算。

对比必须使用相同观察时长和成熟度，不能直接比较 14 日与 15 日累计人群。`first_open` 与 `subscription_first` 的用户并集不是新增人数；`subscription_first` 是否存在、是否表示支付成功均需事件与交易证据，零行不能证明追踪失效。

## 查询边界

仅 `platform='ANDROID'` 会混入共享数据集的其他产品，必须使用业务包名。原始查询遵守[最近 7 天](../../shared/business/access.md)。GA4 `event_date` 是字符串，`events_*` 与 `events_2026*` 的后缀长度不同；DWD 扁平字段与 GA4 的 `geo.country`、`traffic_source.source` 不可混用。

新增 cohort 按安装/首次识别日和用户键形成，回访按明确日偏移关联。D30 只比较完整观察的 cohort，补出零回访，并按总回访人数/总 cohort 人数汇总。具体 `retain_N` 日序必须核对加工定义。
