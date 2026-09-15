---
id: "table:pubdata2025.ads.ads_atlasv_deliver_cost_daily"
title: "pubdata2025.ads.ads_atlasv_deliver_cost_daily · 全公司分产品投放花费数据"
project: "company"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.ads.ads_atlasv_deliver_cost_daily.md", "dataform:aidata/definitions/ads/reports/h_pubdata_ads_atlasv_deliver_cost_daily.sqlx", "dataform:pubdata/definitions/ads/h_pubdata_ads_atlasv_deliver_cost_daily.sqlx", "feishu:pubdata2025.ads.ads_atlasv_deliver_cost_daily", "schema:pubdata2025.ads.ads_atlasv_deliver_cost_daily"]
tags: ["ads_atlasv_deliver_cost_daily", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ads.ads_atlasv_deliver_cost_daily"]
review_required: false
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ads.ads_atlasv_deliver_cost_daily · 全公司分产品投放花费数据

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ads.ads_atlasv_deliver_cost_daily` |
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
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `cost` | FLOAT | NULLABLE | 投放花费 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_cdct_delivery_cost_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sads!3sads_atlasv_deliver_cost_daily) |
| 任务地址 | h_pubdata_…aily.sqlx – Code – Dataform – BigQuery – AIDATA – Google Cloud 控制台 |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/reports/h_pubdata_ads_atlasv_deliver_cost_daily.sqlx`；仓库 `aidata`，路径 `definitions/ads/reports/h_pubdata_ads_atlasv_deliver_cost_daily.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.056625+00:00`。同一 SQLX 的产出：`pubdata2025.ads.ads_atlasv_deliver_cost_daily`。
- 加工源码：`dataform:pubdata/definitions/ads/h_pubdata_ads_atlasv_deliver_cost_daily.sqlx`；仓库 `pubdata`，路径 `definitions/ads/h_pubdata_ads_atlasv_deliver_cost_daily.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.052866+00:00`。同一 SQLX 的产出：`pubdata2025.ads.ads_atlasv_deliver_cost_daily`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
where event_date >= form_date
GROUP BY ALL

where event_date >= from_date
GROUP BY ALL
```

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_cdct_delivery_cost_di
