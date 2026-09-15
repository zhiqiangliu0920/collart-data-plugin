---
id: "ios.events"
title: "VidArt 生成、购买与归因参数"
project: "collart_ios"
kind: "event"
status: "documented"
sources: ["ai-knowledge:collart_ios/product/event_parameter_discovery.md"]
tags: ["iOS", "VidArt", "事件", "参数", "in_app_purchase"]
tables: []
---

# VidArt 生成、购买与归因参数

## 业务流程与事件

first_open → ai_service_start → ai_service_success / ai_generation_success → in_app_purchase。这只是分析映射，严格顺序需事件证据。ai_service_start 参数 credits、model_type、service_type；success 参数 result_type、service_type；ai_generation_success 另有 template_type、uniqueId。关联同一任务前核验 uniqueId 与 task_id 的关系。

in_app_purchase.event_value_in_usd 为毛额线索；vip_subscribe_succeed 无金额只能计数。Apple 交易及净额与客户端事件分开。ASA campaignID/keywordID 在 user_properties、firebase_campaign 等出现，不保证首开事件携带。

原始窗口和 bundle 过滤见 [shared.access](../../shared/business/access.md) / [shared.routing](../../shared/business/routing.md)，完整跨版本事件触发语义待补齐。

## 参数发现与缺口

先在指定完整日期窗口内枚举实际 event_name 与 `UNNEST(event_params)` 的 key，再按事件核对参数类型和覆盖率。`template_id`、`template_name`、`material_id`、`service_type`、`model_type`、`credits`、`firebase_screen`、`firebase_screen_class`、`is_vip` 均是旧脚本的排查候选，不是本次证实已上报的字段。

参数可能存于 string/int/double/float value；只读 string_value 会误报缺失。参数 key 不存在、某一事件不带值、SQL 类型选错与权限不足需分别记录。用 template/temp/material 或 select/choose/apply/use 做名称搜索，只能发现候选；材料 ID 是否就是模板 ID 要有产品或事件证据。

`ga_session_id` 一般需从参数中读取；旧 SQL 使用顶层 `e.ga_session_id`，须按实际 schema 核查。通用 GA4 参数不能当作本产品自定义业务埋点。

参数结构检查只统计事件 × key × 类型的覆盖，不导出个人参数值。以上事件关系来自静态材料，完整触发条件和跨版本覆盖仍待核验。
