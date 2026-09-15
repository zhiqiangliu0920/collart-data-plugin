---
id: "table:aidata2025.dim.dim_collart_core_event_copy"
title: "aidata2025.dim.dim_collart_core_event_copy"
project: "shared"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/dim_table.sqlx", "schema:aidata2025.dim.dim_collart_core_event_copy"]
tags: ["dim_collart_core_event_copy", "字段", "schema", "SQLX"]
tables: ["aidata2025.dim.dim_collart_core_event_copy"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dim.dim_collart_core_event_copy

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dim.dim_collart_core_event_copy` |
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
| `event_module` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_name_chinese` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `key` | STRING | NULLABLE | 未说明 | 缺口 |
| `value1` | STRING | NULLABLE | 未说明 | 缺口 |
| `value2` | STRING | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/dim_table.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/dim_table.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.000874+00:00`。同一 SQLX 的产出：`aidata2025.dim.dim_ai_service_cost_unit_copy`, `aidata2025.dim.dim_collart_android_core_event_copy`, `aidata2025.dim.dim_collart_core_event_copy`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
where 1=1;
```
- 物理上游：`aidata2025.dim.dim_ai_service_cost_unit_copy`
- 物理上游：`aidata2025.dim.dim_collart_android_core_event_copy`
