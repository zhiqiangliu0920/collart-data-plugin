---
id: "table:aidata2025.dim.dim_country_info"
title: "aidata2025.dim.dim_country_info · 国家名称表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dim.dim_country_info.md", "feishu:aidata2025.dim.dim_country_info", "schema:aidata2025.dim.dim_country_info"]
tags: ["dim_country_info", "字段", "schema", "SQLX"]
tables: ["aidata2025.dim.dim_country_info"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dim.dim_country_info · 国家名称表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dim.dim_country_info` |
| 粒度 | country_name |
| 主键/去重键 | country_name；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 手动维护；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `class` | STRING | NULLABLE | 国家梯级，比如T1/T2/T3 | 飞书 |
| `country_name` | STRING | NULLABLE | 国家英文名，首字母大写；最常用 | 飞书 |
| `country_name_2` | STRING | NULLABLE | 国家英文名，字母全部大写 | 飞书 |
| `country_name_3` | STRING | NULLABLE | 国家英文简称，两个字母，字母全部大写 | 飞书 |
| `country_name_4` | STRING | NULLABLE | 国家英文简称，三个字母，全部大写 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 否 |
| 数据来源 | 业务信息 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdim!3sdim_country_info) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
