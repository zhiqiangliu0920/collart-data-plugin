---
id: "table:aidata2025.ads_collart.big_r_realtime_today_income"
title: "aidata2025.ads_collart.big_r_realtime_today_income"
project: "shared"
kind: "table"
status: "historical"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads_collart.big_r_realtime_today_income.md", "schema:aidata2025.ads_collart.big_r_realtime_today_income"]
tags: ["big_r_realtime_today_income", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collart.big_r_realtime_today_income"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads_collart.big_r_realtime_today_income

## 使用边界

BigQuery 元数据返回 NOT_FOUND（2026-09-14）；可能为历史表/名称变化/不可见，不能作为默认当前入口。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collart.big_r_realtime_today_income` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未取得元数据 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: historical；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| — | — | — | 当前 schema 缺失，下面保留来源字段，不保证当前可用 | 缺口 |

## 表专属业务说明

## 2. 核心作用

为大R准实时播报提供当天收入。n8n 将本表 `total_value`
与 T+1 ADS 高价值用户表的历史 `value` 相加，得到当前累计价值。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
