---
id: "table:aidata2025.ads_collart.ads_dim_metric_rule"
title: "aidata2025.ads_collart.ads_dim_metric_rule"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/ads_dim_metric_rule.md", "schema:aidata2025.ads_collart.ads_dim_metric_rule"]
tags: ["ads_dim_metric_rule", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collart.ads_dim_metric_rule"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads_collart.ads_dim_metric_rule

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collart.ads_dim_metric_rule` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `app_name` | STRING | NULLABLE | 产品：collart_android / vidart_ios / collart_web / collart_fashion | schema |
| `metric_name` | STRING | NULLABLE | 指标编码 / ads_oper_user_event_metric_di 列名 | schema |
| `metric_chinese_name` | STRING | NULLABLE | 指标中文名 | schema |
| `event_name` | STRING | NULLABLE | 事件匹配表达式 | schema |
| `event_params` | STRING | NULLABLE | 事件参数过滤，AND 拼接；可空 | schema |
| `agg_type` | STRING | NULLABLE | count_events \| count_distinct_task_id | schema |
| `is_enabled` | BOOLEAN | NULLABLE | 是否启用 | schema |
| `is_materialized` | BOOLEAN | NULLABLE | TRUE 才物化到用户日宽表 | schema |
| `sort_order` | INTEGER | NULLABLE | 列顺序 | schema |
| `description` | STRING | NULLABLE | 备注 | schema |

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

## 2026-09-14 文档补充

已迁移为普通 TABLE；人工改 Sheet 后每 5 分钟校验同步，失败保留旧版本。只对 is_enabled=TRUE 的 app_name × metric_name 检查唯一性；草稿/空行/未启用重复并非数据损坏。iOS 规则的 app_name 为 vidart_ios。10 字段含 description；冷热规则的表达式与物化关系见[公共事件规则](../events/event-rules.md)。此同步由现有服务维护，插件不执行修改或同步。
