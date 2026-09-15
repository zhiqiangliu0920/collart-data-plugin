---
id: "shared.event-rules"
title: "事件规则、物化指标与测量边界"
project: "shared"
kind: "event"
status: "documented"
sources: ["ai-knowledge:1company/analysis_playbooks/event_metric_from_rule.md", "ai-knowledge:1company/indicators/event_metric_from_rule.md", "ai-knowledge:1company/tables/ads_dim_metric_rule.md", "previous:company-event-rule-contract", "dataform:aidata/definitions/ads/collart/collart_android/sp_query_event_metric_by_tag.sqlx"]
tags: ["事件", "埋点", "规则", "热指标", "冷指标", "is_materialized"]
tables: ["aidata2025.ads_collart.ads_dim_metric_rule"]
---

# 事件规则、物化指标与测量边界

## 事件与测量

曝光、点击、任务创建、任务成功、下载、支付发起、成功交易是不同阶段。严格漏斗需要同一身份/会话/任务、事件时间顺序、窗口和去重；同日 flags 或独立 UV 只说明触达。开始/成功事件数比率受重试与跨日影响，任务成功率按 task_id 对齐终态。参数需同时检查 string/int/double/float，拼写/大小写不能擅改。

原始 GA4 的 event_date 为 YYYYMMDD 字符串，event_timestamp 为微秒；_TABLE_SUFFIX 才控制分片。UNNEST(event_params) 不受控会放大其他指标。先验证键唯一性，再用标量子查询。原始日期和产品边界见 [shared.access](../business/access.md)。

适用资料日期：2026-09-02。统一规则在 `aidata2025.ads_collart.ads_dim_metric_rule`，用 app_name 区分四端。旧分端规则表与 tag_code 命名是历史记录。

热指标由 is_enabled/is_materialized 确定；用户日为 *_pv，汇总为对应 STRUCT。修改 Sheet 不会自动改变已生成的 SQLX 或宽表字段。冷指标按规则查询 DM；必要时再下钻 GA4。本文是知识说明，不授权运行生成器、回补或生产写入。

## 统一规则的当前读取方式

源知识于 2026-09-14 记录：`aidata2025.ads_collart.ads_dim_metric_rule` 已从 Sheet 外表迁移为普通 TABLE，Sheet 仍为维护源，每 5 分钟校验同步，失败保留上一版。查询者使用 BigQuery 只读权限，无需为读此普通表另取 Drive 权限。规则同步和热列物化是两个独立流程，表变更不保证 SQLX/热列同步。

app_name 映射：Android=collart_android，iOS/VidArt=**vidart_ios**，Web=collart_web，Fashion=collart_fashion。只查询 is_enabled=TRUE 的适用规则；逻辑键 app_name × metric_name 只对启用规则要求唯一，草稿/空行/未启用重复允许保留，不能把全表当唯一维表。

## 表达式与聚合

event_name 支持等值、IN、LIKE；event_params 由参数 key 的等值/IN/LIKE 通过 AND 组合，先确认 Android/iOS 的 params_info 或 Web/Fashion 的 web_params_info 存在该键及大小写约定。禁止把规则内容当任意 SQL 执行；Web valid_user_pv 的 COMPOSITE 是生成器特判，不能据其特例放宽通用表达式。

count_events → COUNTIF；count_distinct_task_id → COUNT(DISTINCT IF(条件, task_id, NULL))。metric_name 为用户日 *_pv 列；上卷通常去掉 _pv，使用 STRUCT<uv,pv>，额外 new_uv 等不一定由 Sheet 驱动。is_enabled / is_materialized 与实际列同时核对，description 为正式第十个字段。

Android 的 sp_query_event_metric_by_tag 仅作为已捕获的加工/解析依据，不提供 CALL 执行入口；冷指标查询仍受只读与最近 7 天约定。旧规则行清单是历史配置快照，当前值需从统一规则表读取。
