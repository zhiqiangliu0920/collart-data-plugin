---
id: "ios.paid-users"
title: "VidArt 付费人群与行为诊断"
project: "collart_ios"
kind: "playbook"
status: "documented"
sources: ["ai-knowledge:collart_ios/analysis_playbooks/paid_user_behavior.md"]
tags: ["VidArt", "iOS", "付费用户", "行为"]
tables: []
---

# VidArt 付费人群与行为诊断

## 人群、身份和窗口

旧方法以窗口内有 `vip_subscribe_succeed` 的 `user_pseudo_id` 建 cohort。这是“出现成功事件的人群”，不能等同当前 VIP、历史付费全部人群、实收订单数。`app_info.install_source <> 'manual_install'` 会一并排除 NULL，测试过滤与未知来源要分开评估。明确已完成日期上下界；原脚本仅给下界，可能包含今天。

基础输出包括日付费事件 UV/PV、vip_level/price 分布、复购事件频次、国家、设备、渠道，以及活跃天数和会话数。事件 `price` 参数不是已去重实收收入；分布中的各国 UV 可能重叠，不能相加当总人数。

## 付费前后与功能使用

- 首次安装到首付：旧 MIN 只发生在 90 天窗口内；未见 first_open、负时间差应单列，不能落入“30d+”或“0–1h”。历史覆盖不足时称“窗口首次观察”。
- 付费前最后 10 个事件：同一用户按时间排序，旧 `mins_before_purchase` 为负值，含义需改为“距首付分钟数”。时间相同需明确次序。
- 旧 AFTER 查询使用 MAX(purchase_ts)，而 BEFORE 使用 MIN，两者分别围绕末次与首次付款，不能当成同一干预前后对比。分析时显式选择一次付款和前后窗口。
- AI 分布按 `service_type`、`model_type`、credits；积分不是货币成本。旧 CAST 遇非数字会失败，应先检测多类型与异常值；均值缺失不能强行格式化为数值。
- 成功/失败事件候选 `ai_service_execute_success/failed` 与 `ai_generation_success/failed` 不保证全都实际存在；按 task_id 与终态映射验证，不能把候选事件并集直接当成功率。

## 参数与隐私

模板标识与事件参数见 参数排查方法。用户级路径、Top20 列表属于分析时受控明细，本知识页只保留方法。原 Python 中凭证路径、客户端初始化和打印执行壳已移除。
