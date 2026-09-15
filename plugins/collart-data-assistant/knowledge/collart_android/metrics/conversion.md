---
id: "android.conversion"
title: "Android 付费与功能转化"
project: "collart_android"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_android/indicators/conversion.md", "ai-knowledge:collart_android/indicators/event_usage.md", "ai-knowledge:collart_android/indicators/feature_usage.md"]
tags: ["Android", "转化", "功能", "付费"]
tables: []
---

# Android 付费与功能转化

成功收入与客户端人数分开，参见 [shared.revenue](../../shared/metrics/revenue.md)。曝光缺失时不输出伪 CTR。

## 指标分别定义

| 指标 | 分子 | 分母与限制 |
|---|---|---|
| 订阅成功事件转化 | cohort 内触发 vip_subscribe_succeed 的用户 | 同一窗口、同一产品 cohort；仅事件口径 |
| 成功支付转化 | cohort 内当窗有成功订单的用户 | 区分新/老用户，明确观察窗，订单需去重 |
| 购买事件 UV | 订阅与点数包购买用户去重并集 | 见公司 purchase 定义；不是两个 UV 简单相加 |

活跃分母按 DAU 定义；窗口内支付者需与分母 cohort 相交。历史已付费状态、当窗付款、首次付款与当前 VIP 身份分开。

## 功能指标

功能使用率 = 指定活跃 cohort 内使用某功能的人数 / cohort 活跃人数。`ai_service_task_create` 按 service_type 的 PV/UV 只表示任务创建量/创建用户数，缺少活跃分母时不能称使用率；创建也不等于执行成功。

候选 service_type 有 img2video、text2video、img2img、text2img、video_edit，分别为图生视频、文生视频、图生图、文生图、视频编辑。该枚举来自历史定义，不保证当前完整；重试、事件重复与 task_id 需核验。

## 事件与可测量内容

| 主题 | 原事件 / 参数 | 实际可计算内容与限制 |
|---|---|---|
| 搜索 | action_search_template_start | 去重用户数，不等于搜索成功 |
| Banner | material_banner_did_click | 只有点击 UV，没有 Banner 曝光分母，不能单独称 CTR |
| 分类 | home_category_show / category_name | 曝光 PV，未查询分类点击 |
| 模块 | home_module_show / home_module_click / module_id | 点击 PV / 曝光 PV；NULL 模块和 0 曝光单列 |
| 功能 | home_feature_click / feature | 旧 SUM(日 UV)/SUM(日 session_start UV) 是用户日权重比率；缺失点击日仍应保留分母，不是整窗去重 UV 比率 |
| 图片、视频编辑 | aiimage_edit_show、aivideo_edit_show / type | 按 type 的展示 UV，不等于生成或保存 |
| AI 服务 | ai_service_task_create / service_type | 任务创建事件 PV/用户 UV；feature_usage 与 service_type 两份 SQL 内容重复 |
| 编辑操作 | aiedit_show、aiedit_retake、aiedit_faceretouch、aiedit_improve、aiedit_remove、aiedit_save_success | 同窗出现次数/人数，不保证按顺序完成，不能称严格转化漏斗 |

对搜索、Banner、图片、视频 UV 使用 session_start UV 作分母只能表示相对启动用户的触达，不是对应页面点击率。日 UV 相加形成用户日权重口径，不等于整窗去重用户比率。

参数展开后先确认事件/用户/任务粒度，避免一条事件多个参数被计成多次事件。事件候选需对照[事件字典](../events/events.md)及[公共规则](../../shared/events/event-rules.md)；分母按[活跃指标](activity.md)，实付按[收入指标](revenue.md)。
