---
id: "collart-android-template-coverage-diagnosis"
title: "Android 模板覆盖与任务成功率"
project: "collart_android"
kind: "playbook"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-1dc20cad9661"]
tags: ["模板", "覆盖率", "任务", "成功率"]
supersedes: []
verification_evidence: []
---

# Android 模板覆盖与任务成功率

先证实曝光事件及参数，不能用猜测的 temp、temp_show_click 或 Home_Template_Show 等同真实曝光。固定日期与产品后建立有效活跃用户集合 A 和实际曝光集合 B，曝光缺失按 `|A − B|`，不直接计算 DAU − 曝光 UV。版本/国家归属先定义，防止用户跨组重复。

提交开始/成功事件数比率受重试、跨日和多事件影响。分析任务成功率时按 task_id 对齐开始与终态；零分母为 NULL，同时报告样本量。不得以 1 替代零分母或把未知显示为 0。

Top10 国家、旧 1000 UV 门槛和固定日期切片不代表全量或告警基线；Top10 比率简单平均不等于全量点击 UV / 曝光 UV。旧执行脚本及发送流程只作历史证据。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [collart_android/analysis_playbooks/template_coverage_diagnosis.md](../../library/text/568819d319d2ae89be1993ad668acb40bd7d1314d1db428c3e2e9a94807f6072.txt)
