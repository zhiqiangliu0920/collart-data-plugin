---
id: "table:aidata2025.ads_collart.ads_oper_tempalte_data_android"
title: "aidata2025.ads_collart.ads_oper_tempalte_data_android · collart android模板数据表"
project: "collart_android"
kind: "table"
status: "historical"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads_collart.ads_oper_tempalte_data_android.md", "feishu:aidata2025.ads_collart.ads_oper_tempalte_data_android", "schema:aidata2025.ads_collart.ads_oper_tempalte_data_android"]
tags: ["ads_oper_tempalte_data_android", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collart.ads_oper_tempalte_data_android"]
review_required: true
applies_to: []
---

# aidata2025.ads_collart.ads_oper_tempalte_data_android · collart android模板数据表

## 使用边界

BigQuery 元数据返回 NOT_FOUND（2026-09-14）；可能为历史表/名称变化/不可见，不能作为默认当前入口。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collart.ads_oper_tempalte_data_android` |
| 粒度 | 每天、每个模板、每个事件一行 |
| 主键/去重键 | event_date、module_title、event_name；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未取得元数据 |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: historical；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| — | — | — | 当前 schema 缺失，下面保留来源字段，不保证当前可用 | 缺口 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `event_date` | date | 日期 |
| `event_name` | string | 事件名称 |
| `module_title` | string | 模块名称 |
| `pv` | int | 事件pv |
| `service_type` | string | ai服务类型 |
| `uv` | int | 事件uv |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | storytemplate-10a27.analytics_232977577.events_* |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m10!1m4!4m3!1saidata2025!2sads_collart!3sads_high_value_user_Info!1m4!4m3!1saidata2025!2sads_collart!3sads_oper_tempalte_data_android) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery?tc=us:__REDACTED_ID__&project=aidata2025&ws=!1m0) |
| 看板 | collart android模板看板 |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | storytemplate-10a27.analytics_232977577.events_*,aidata2025.ai_service.collart_template_data |
| 是否需要展示血缘 | 否 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | - |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Fcollart%2Fads_high_value_user_info.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 导出没有字段明细，不能据此编写字段查询。
- 该记录把浏览器标题拼进表名；只作为模板表的矛盾元数据保存。原粒度“每个用户一行”不覆盖另一记录的模板粒度。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：storytemplate-10a27.analytics_232977577.events_*
