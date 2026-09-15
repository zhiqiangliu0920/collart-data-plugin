---
id: "android.events"
title: "Android 首页、生成与付费埋点"
project: "collart_android"
kind: "event"
status: "documented"
sources: ["ai-knowledge:collart_android/product/home_screenshots.md", "previous:shared-event-evidence"]
tags: ["Android", "埋点", "Home_Template_Show", "task_id"]
tables: ["storytemplate-10a27.analytics_232977577.events_*"]
---

# Android 首页、生成与付费埋点

## 从入口到结果

| 流程 | 事件候选 | 测量边界 |
|---|---|---|
| 首页 | Home_show、Home_Template_Show、Home_Template_Click、home_feature_click | 曝光与点击的真实触发、模块位置按版本核验 |
| 生成准备 | generate_watch_ad、generate_pro_create | 广告按钮不是广告展示；详见 [android.ads](ads.md) |
| 创建与执行 | ai_service_task_create、ai_service_start、ai_service_success、ai_service_failed | 服务事件按 task_id；upload/submit/query 子链路不能重复算失败 |
| 结果消费 | ai_service_result_show、ai_service_download_start 等 | 展示/下载/保存分别计数 |
| 付费漏斗 | Subscription_Page_Show、vip_subscribe、vip_subscribe_succeed | 最后一个仍为埋点证据，成功收入见服务端 |
| 首次体验 | first_open、First_Page_Animation_*、Second_Page_Animation_* | first_open 为设备新增线索，原始窗口内首次出现不等于终身首次 |

## 参数与热列

使用 service_type、function_type 区分视频/生图与功能；模板 id/name 与 task_id 分开。热列 home_show 对 Home_show；home_template_click 对 Home_Template_Click；generate_ready 对 generate_watch_ad / generate_pro_create；generate_start / generate_success 对任务开始/成功，具体过滤以统一规则与 SQLX 为准。

原始来源为 storytemplate-10a27.analytics_232977577.events_*，必选 Android app_info.id；逐条行为限最近 7 天。完整事件及参数字典尚未覆盖所有版本，候选事件未获现场核验时不能称已确认。

## 首页入口参数

| 元素 | 事件 | 参数/取值 |
|---|---|---|
| AI Video / AI Image / AI Edit | home_feature_click | feature = aiVideo / aiImage / aiEdit |
| AI Remove / AI Upscale / Motion Sync | home_feature_click | feature = aiRemove / aiEnhance / motion |
| Image to Video 快捷入口 | home_feature_click | feature = video_edit（不能仅按中文名改值） |
| 搜索 | action_search_template_start | 源资料未说明必需参数 |
| Banner | material_banner_did_click | 源资料未说明必需参数 |
| POPULAR / FREE 分类 | home_category_show | category_name |
| 模板 | Home_Template_Show / Home_Template_Click | 模板标识、曝光触发按当前版本核验 |
