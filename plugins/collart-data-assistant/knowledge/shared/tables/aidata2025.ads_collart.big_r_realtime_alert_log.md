---
id: "table:aidata2025.ads_collart.big_r_realtime_alert_log"
title: "aidata2025.ads_collart.big_r_realtime_alert_log"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads_collart.big_r_realtime_alert_log.md", "feishu:aidata2025.ads_collart.big_r_realtime_alert_log", "schema:aidata2025.ads_collart.big_r_realtime_alert_log"]
tags: ["big_r_realtime_alert_log", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collart.big_r_realtime_alert_log"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads_collart.big_r_realtime_alert_log

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collart.big_r_realtime_alert_log` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | app_name, user_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `first_sent_at` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |
| `last_total_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `source` | STRING | NULLABLE | 未说明 | 缺口 |
| `updated_at` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

## 2. 核心作用

记录已经成功发送过准实时大R卡片的用户，防止每 5 分钟重复播报。
Web 用户从 50 档升到 100 档仍视为同一用户，不产生第二次播报。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
