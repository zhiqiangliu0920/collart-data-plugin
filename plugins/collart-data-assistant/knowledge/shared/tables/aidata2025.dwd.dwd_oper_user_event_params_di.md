---
id: "table:aidata2025.dwd.dwd_oper_user_event_params_di"
title: "aidata2025.dwd.dwd_oper_user_event_params_di"
project: "shared"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_event_params_di.sqlx", "feishu:aidata2025.dwd.dwd_oper_user_event_params_di", "schema:aidata2025.dwd.dwd_oper_user_event_params_di"]
tags: ["dwd_oper_user_event_params_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_oper_user_event_params_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_oper_user_event_params_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_oper_user_event_params_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | app_name, event_name |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_time` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_param` | RECORD | REPEATED | 未说明 | 缺口 |
| `event_param.key` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_param.value` | RECORD | NULLABLE | 未说明 | 缺口 |
| `event_param.value.string_value` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_param.value.int_value` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `event_param.value.float_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `event_param.value.double_value` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `install_source` | STRING | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_event_params_di.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_oper_user_event_params_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:54.689081+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_oper_user_event_params_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
WHERE ( _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', from_date)
AND FORMAT_DATE('%Y%m%d', to_date)
AND CONCAT('intraday_', FORMAT_DATE('%Y%m%d', to_date))
AND event_name NOT LIKE 'tech%'
AND event_name NOT LIKE 'dev%'
AND event_name NOT IN ('fire_base_start_request',
and (app_info.install_source <>'manual_install' or app_info.id is null)
AND app_info.id NOT IN ('com.my.drama.box.reel.short.stream.tv.app')
and ((app_info.id = 'ai.photo.generator.fotos.ai.image.editor.app.free' and app_info.install_source <>'manual_install')
```
- 物理上游：`fx-editor.analytics_263446298.events_*`
- 物理上游：`muselab-9b0d3.analytics_530699929.events_*`
- 物理上游：`muselab-9b0d3.analytics_530699929.events_intraday_*`
- 物理上游：`removeobjects-17cd7.analytics_348205064.events_intraday_*`
- 物理上游：`storytemplate-10a27.analytics_232977577.events_*`
- 物理上游：`vibedance-540a0.analytics_533044528.events_*`
- 物理上游：`vidart-8b8ca.analytics_528583115.events_*`
