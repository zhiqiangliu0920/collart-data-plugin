---
id: "table:pubdata2025.ods.user_ai_base_video_record"
title: "pubdata2025.ods.user_ai_base_video_record"
project: "shared"
kind: "table"
status: "documented"
sources: ["dataform:pubdata/definitions/dwd/log/h_dwd_cdct_ai_service_record_info_hi.sqlx", "schema:pubdata2025.ods.user_ai_base_video_record"]
tags: ["user_ai_base_video_record", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ods.user_ai_base_video_record"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ods.user_ai_base_video_record

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ods.user_ai_base_video_record` |
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
| `data_source` | STRING | NULLABLE | 未说明 | 缺口 |
| `create_time` | DATETIME | NULLABLE | 未说明 | 缺口 |
| `create_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `model_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `client_task_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `task_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `time_cost` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `cost_point` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `status` | STRING | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:pubdata/definitions/dwd/log/h_dwd_cdct_ai_service_record_info_hi.sqlx`；仓库 `pubdata`，路径 `definitions/dwd/log/h_dwd_cdct_ai_service_record_info_hi.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.662235+00:00`。同一 SQLX 的产出：`pubdata2025.dwd.dwd_cdct_ai_service_record_info_hi`, `pubdata2025.ods.user_ai_base_video_record`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
WHERE DATE(TIMESTAMP_SECONDS(CAST(created_at AS INT64)), "Asia/Shanghai") BETWEEN from_date AND to_date
AND to_date;
WHERE DATE(TIMESTAMP_SECONDS(created_at), "Asia/Shanghai") BETWEEN from_date AND to_date
where DATE(TIMESTAMP_SECONDS(update_time), "Asia/Shanghai") between from_date AND to_date
group by all
left join new_base b
on a.create_date = b.create_date
and a.task_id = b.task_id
where b.task_id is null
```
- 物理上游：`aidata2025.ods.ai_user_base_record`
- 物理上游：`aidata2025.ods_aibaseprod.user_a_i_base_video_record`
