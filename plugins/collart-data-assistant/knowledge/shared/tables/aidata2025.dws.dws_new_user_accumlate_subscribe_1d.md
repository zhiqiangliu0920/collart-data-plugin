---
id: "table:aidata2025.dws.dws_new_user_accumlate_subscribe_1d"
title: "aidata2025.dws.dws_new_user_accumlate_subscribe_1d · N日用户订阅表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dws.dws_new_user_accumlate_subscribe_1d.md", "feishu:aidata2025.dws.dws_new_user_accumlate_subscribe_1d", "schema:aidata2025.dws.dws_new_user_accumlate_subscribe_1d"]
tags: ["dws_new_user_accumlate_subscribe_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_new_user_accumlate_subscribe_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dws.dws_new_user_accumlate_subscribe_1d · N日用户订阅表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_new_user_accumlate_subscribe_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `traffic_source_type` | STRING | NULLABLE | 投放渠道类型 | 飞书 |
| `product_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `day1` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day2` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day3` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day4` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day5` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day6` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day7` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day8` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day9` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day10` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day11` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day12` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day13` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day14` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day15` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day16` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day17` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day18` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day19` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day20` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day21` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day22` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day23` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day24` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day25` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day26` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day27` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day28` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day29` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day30` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day31` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day32` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day33` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day34` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day35` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day36` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day37` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day38` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day39` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day40` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day41` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day42` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day43` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day44` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day45` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day46` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day47` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day48` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day49` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day50` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day51` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day52` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day53` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day54` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day55` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day56` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day57` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day58` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day59` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day60` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day61` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day62` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day63` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day64` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day65` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day66` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day67` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day68` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day69` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day70` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day71` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day72` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day73` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day74` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day75` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day76` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day77` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day78` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day79` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day80` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day81` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day82` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day83` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day84` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day85` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day86` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day87` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day88` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day89` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `day90` | INTEGER | NULLABLE | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdws!3sdws_new_user_accumlate_subscribe_1d) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
