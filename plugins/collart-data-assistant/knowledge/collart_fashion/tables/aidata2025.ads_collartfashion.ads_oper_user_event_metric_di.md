---
id: "table:aidata2025.ads_collartfashion.ads_oper_user_event_metric_di"
title: "aidata2025.ads_collartfashion.ads_oper_user_event_metric_di"
project: "collart_fashion"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_fashion/tables/aidata2025.ads_collartfashion.ads_oper_user_event_metric_di.md", "dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_user_event_metric_di.sqlx", "feishu:aidata2025.ads_collartfashion.ads_oper_user_event_metric_di", "schema:aidata2025.ads_collartfashion.ads_oper_user_event_metric_di"]
tags: ["ads_oper_user_event_metric_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartfashion.ads_oper_user_event_metric_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartfashion.ads_oper_user_event_metric_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartfashion.ads_oper_user_event_metric_di` |
| 粒度 | event_date × user_pseudo_id（源码说明；需验唯一性） |
| 主键/去重键 | event_date, user_pseudo_id；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | user_pseudo_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe_succeed_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `seo_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `seo_click_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `valid_action_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `inspiration_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `inspiration_template_click_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_generate_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_generate_step2_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_generate_step3_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_generate_step4_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_generate_click_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_download_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `fashion_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aimodel_generate_click_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aimodel_generate_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aimodel_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aimodel_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aimodel_download_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `credit_pack_purchase_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

## 2. 核心作用

- 保存 Fashion 热漏斗事件的用户日 PV。
- 向 `ads_oper_event_metric_attr_di`、`ads_oper_event_metric_country_di` 和 `ads_oper_basic_indicator_daily_di` 提供事件指标。

## 6. 数据质量

2026-08-13 至 2026-08-26 回补结果：

- 开始：263 PV，71 个用户日。
- 成功：141 PV，57 个用户日。
- DM、用户日、Attr、Country、Daily 五层对账一致。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_user_event_metric_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_fashion/ads_oper_user_event_metric_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:50.775418+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartfashion.ads_oper_user_event_metric_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 30;
DECLARE to_date   DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN from_date AND to_date
AND user_pseudo_id IS NOT NULL
INNER JOIN act USING (event_date, user_pseudo_id)
WHERE e.event_date BETWEEN from_date AND to_date
AND e.package_name = 'collart_fashion'
AND e.event_name IN (
GROUP BY event_date, user_pseudo_id;
```
- 物理上游：`aidata2025.ads_collartfashion.ads_oper_user_active_di`
- 物理上游：`aidata2025.dm.dm_collart_web_user_event_di`

稀疏表：无热事件命中不出行。*_pv 汇总 PV、COUNTIF(*_pv>0) 汇总 UV；DAU/功能使用率分母来自完整 active/cohort。规则修改不等于 SQLX/物化列更新。
