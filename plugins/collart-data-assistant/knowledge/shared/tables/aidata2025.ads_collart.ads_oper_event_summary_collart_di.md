---
id: "table:aidata2025.ads_collart.ads_oper_event_summary_collart_di"
title: "aidata2025.ads_collart.ads_oper_event_summary_collart_di"
project: "shared"
kind: "table"
status: "historical"
sources: ["ai-knowledge:1company/tables/aidata2025.ads_collart.ads_oper_event_summary_collart_di.md", "feishu:aidata2025.ads_collart.ads_oper_event_summary_collart_di", "schema:aidata2025.ads_collart.ads_oper_event_summary_collart_di"]
tags: ["ads_oper_event_summary_collart_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collart.ads_oper_event_summary_collart_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads_collart.ads_oper_event_summary_collart_di

## 使用边界

BigQuery 元数据返回 NOT_FOUND（2026-09-14）；可能为历史表/名称变化/不可见，不能作为默认当前入口。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collart.ads_oper_event_summary_collart_di` |
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

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `app_version` | string | app客户端版本号 |
| `country` | string | 国家 |
| `event_date` | date | 日期 |
| `event_name` | string | 事件名/事件英文名 |
| `event_num` | int | pv，统计某事件的触发次数 |
| `is_new` | boolean | 是否新老用户，true代表新用户、false代表老用户 |
| `is_vip` | boolean | 是否付费用户，true代表付费用户、false代表免费用户 |
| `package_name` | string | 包名 |
| `traffic_src_name` | string | 投放渠道名称 |
| `traffic_src_type` | string | 投放渠道类型 |
| `user_num` | int | uv，统计某事件的触发人数 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | storytemplate-10a27.analytics_232977577.events_*,aidata2025.dwd.dwd_oper_user_collart_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads_collart!3sads_oper_event_summary_collart_di) |
| 任务地址 | ads_oper_e…t_di.sqlx – Code – Dataform – BigQuery – AIDATA – Google Cloud 控制台 |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
