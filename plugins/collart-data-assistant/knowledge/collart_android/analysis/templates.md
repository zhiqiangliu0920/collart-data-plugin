---
id: "android.templates"
title: "Android 模板覆盖与任务成功率"
project: "collart_android"
kind: "playbook"
status: "documented"
sources: ["ai-knowledge:collart_android/analysis_playbooks/template_coverage_diagnosis.md", "previous:collart-android-template-coverage-diagnosis"]
tags: ["Android", "模板", "成功率", "曝光"]
tables: []
---

# Android 模板覆盖与任务成功率

## 模板曝光覆盖

先从[事件字典](../events/events.md)和[规则契约](../../shared/events/event-rules.md)确认真实曝光事件及参数。`temp`、`temp_show_click`、`Home_Template_Show` 是历史候选，不能未经证实视为等价事件；缺少一个猜测事件不能证明模板未展示。

固定产品和完整日期，建立有效活跃用户集合 A 与实际曝光用户集合 B。未覆盖量为 `|A − B|`，覆盖率为 `|A ∩ B| / |A|`，按日期、版本、国家拆解。不直接计算“DAU − 曝光 UV”，因为 B 未必是 A 的子集；多版本用户先规定归属，避免跨组重复。

## AI 提交质量

`submit_start`、`submit_success` 是提交质量分析的候选事件，使用前核对当前上报。按日期 × service_type 观察开始量、成功量和错误码，再定位国家、版本、功能。选定 Top 国家样本的成功率不能代表全量。

事件次数比率受重试、重复和跨日完成影响。任务成功率需以已核验的 task_id 对齐开始与终态，同一任务的失败重试和最终成功分别定义。零分母返回 NULL，并报告样本量；不能用 1 替代零分母或把未知显示为 0。

活跃分母见[活动指标](../metrics/activity.md)，功能触达与任务创建的区别见[转化指标](../metrics/conversion.md)。先使用合适汇总；原始事件及行为明细遵守[只读和最近 7 天](../../shared/business/access.md)。
