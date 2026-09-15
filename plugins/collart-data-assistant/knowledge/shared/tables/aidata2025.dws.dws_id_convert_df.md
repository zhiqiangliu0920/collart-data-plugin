---
id: "table:aidata2025.dws.dws_id_convert_df"
title: "aidata2025.dws.dws_id_convert_df"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dws.dws_id_convert_df.md", "dataform:aidata/definitions/dws/daily/h_dws_id_convert_df.sqlx", "feishu:aidata2025.dws.dws_id_convert_df", "schema:aidata2025.dws.dws_id_convert_df"]
tags: ["dws_id_convert_df", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_id_convert_df"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dws.dws_id_convert_df

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_id_convert_df` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | package_name |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 用户事件最后出现日期 | schema |
| `package_name` | STRING | NULLABLE | 包名 | schema |
| `app_name` | STRING | NULLABLE | app名 | schema |
| `user_pseudo_id` | STRING | NULLABLE | firebase id | schema |
| `atlasv_uid` | STRING | NULLABLE | atlasv 统一id | schema |
| `advertising_id` | STRING | NULLABLE | gaid | schema |
| `user_id` | STRING | NULLABLE | 支付信息id | schema |
| `adjust_id` | STRING | NULLABLE | adjust id | 飞书 |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- user_pseudo_id: 飞书补充解释：用户id，firebase分配的唯一id
- user_pseudo_id: 旧文档补充解释：用户id，firebase分配的唯一id
- atlasv_uid: 飞书补充解释：技术团队给用户定义的唯一id
- atlasv_uid: 旧文档补充解释：技术团队给用户定义的唯一id
- advertising_id: 飞书补充解释：用户的广告id身份，也是一种唯一id
- advertising_id: 旧文档补充解释：用户的广告id身份，也是一种唯一id
- user_id: 飞书补充解释：用户id，内部平台分配的唯一id
- user_id: 旧文档补充解释：用户id，内部平台分配的唯一id

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_id_convert_di |
| 是否需要展示血缘 | 否 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m10!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_delivery_adjust_user_di!1m4!4m3!1saidata2025!2sdws!3sdws_id_convert_df) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdws%2Fdaily%2Fh_dws_id_convert_df.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dws/daily/h_dws_id_convert_df.sqlx`；仓库 `aidata`，路径 `definitions/dws/daily/h_dws_id_convert_df.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:55.214061+00:00`。同一 SQLX 的产出：`aidata2025.dws.dws_id_convert_df`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
declare from_date date default ${dataform.projectConfig.vars.biz_date};
where event_date >= from_date;
where event_date >= from_date or exists (
where b.package_name = a.package_name
and b.user_pseudo_id = a.user_pseudo_id
where event_date >= from_date
group by package_name, user_pseudo_id
left join unnest(atlasv_uid) atlasv_uid
left join unnest(user_id) user_id
left join unnest(advertising_id) advertising_id
left join unnest(adjust_id) adjust_id;
```
- 物理上游：`aidata2025.dwd.dwd_id_convert_di`
