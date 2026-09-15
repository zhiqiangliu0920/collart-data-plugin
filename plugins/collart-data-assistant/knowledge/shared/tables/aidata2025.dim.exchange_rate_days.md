---
id: "table:aidata2025.dim.exchange_rate_days"
title: "aidata2025.dim.exchange_rate_days · 国家汇率转换表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dim.exchange_rate_days.md", "dataform:aidata/definitions/dim/dim_exchange_rate_days.sqlx", "feishu:aidata2025.dim.exchange_rate_days", "schema:aidata2025.dim.exchange_rate_days"]
tags: ["exchange_rate_days", "字段", "schema", "SQLX"]
tables: ["aidata2025.dim.exchange_rate_days"]
review_required: false
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dim.exchange_rate_days · 国家汇率转换表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dim.exchange_rate_days` |
| 粒度 | 每天每个币种一行 |
| 主键/去重键 | stats_date+currency；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `stats_date` | STRING | NULLABLE | 日期 | 飞书 |
| `currency` | STRING | NULLABLE | 汇率 | 飞书 |
| `rate` | FLOAT | NULLABLE | 币种对美元的汇率 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 否 |
| 数据来源 | 业务信息 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdim!3sexchange_rate_days) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 旧说明把币种字段写作“汇率”；币种代码与换算比率应分别确认，不直接用该列作除数。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dim/dim_exchange_rate_days.sqlx`；仓库 `aidata`，路径 `definitions/dim/dim_exchange_rate_days.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.695815+00:00`。同一 SQLX 的产出：`aidata2025.dim.exchange_rate_days`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
declare from_date date default ${dataform.projectConfig.vars.biz_date}-1;
declare to_date date default ${dataform.projectConfig.vars.biz_date};
where date(stats_date) between from_date and to_date;
where date(stats_date) between from_date and to_date
```
