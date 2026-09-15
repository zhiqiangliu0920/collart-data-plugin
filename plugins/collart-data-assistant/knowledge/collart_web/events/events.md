---
id: "web.events"
title: "Web 浏览、生成与付费埋点"
project: "collart_web"
kind: "event"
status: "documented"
sources: ["ai-knowledge:collart_web/product/page_structure.md", "previous:shared-event-evidence"]
tags: ["Web", "事件", "埋点", "ga_session_id"]
tables: []
---

# Web 浏览、生成与付费埋点

| 流程 | 事件 | 参数/边界 |
|---|---|---|
| 访问 | page_view、first_visit、session_start | page_location/referrer、ga_session_id；会话键 pseudo × session |
| 功能选择/生成 | img2video_generate_click、text2video_generate_click、img2img_generate_click、text2img_generate_click | 点击意图，不等于执行或成功 |
| AI 服务 | ai_service_start → upload_* → execute_* → ai_service_success / failed | service_type、task_id；重试与跨日终态需匹配 |
| 结果 | ai_result_download | 下载不能代替生成成功 |
| 订阅 | vip_show → vip_subscribe → vip_subscribe_succeed | from 等来源；客户端成功不保证真实交易 |

原始表与 Fashion 共用。app_info.id IS NULL 只区分 Web 与 App，不区分两个站点；还需 page_location 的 studio/fashion 归属。空页面值须作为未知归属单列，不能自动并入主站。加工层 package_name=collart_web / collart_fashion 区分。原始事件仅最近 7 天，内部账号按事件时点过滤。
