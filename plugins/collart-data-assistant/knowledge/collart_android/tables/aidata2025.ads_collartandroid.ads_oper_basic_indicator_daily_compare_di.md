---
id: "table:aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_compare_di"
title: "aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_compare_di"
project: "collart_android"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_android/ads_oper_basic_indicator_daily_compare_di.sqlx", "schema:aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_compare_di"]
tags: ["ads_oper_basic_indicator_daily_compare_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_compare_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_compare_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_compare_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | metric_name, country |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `metric_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `yestoday` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `avg_7days` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `diff` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `ratio` | FLOAT | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_android/ads_oper_basic_indicator_daily_compare_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_android/ads_oper_basic_indicator_daily_compare_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:49.245214+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_compare_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Android 日报环比表：新 ADS 替代旧
  ads_collart.ads_oper_basic_metric_agent_collart_android_di。

  粒度：metric_name × country；country 保留 all + 旧 top_country 分桶。
  窗口：昨日 vs 前 7 日均值；收入与成熟次留按旧任务保持 +1 日错位。
  次日留存：用 country/daily 的 retain.d2（已仅新用户）；VIP/免费切片仍用 retain2_*。
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
WHERE TRUE;
WHERE event_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY) AND DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
GROUP BY event_date, country
LEFT JOIN country_event AS e USING (event_date, country)
GROUP BY ALL
WHERE event_date = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
WHERE event_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 8 DAY) AND DATE_SUB(CURRENT_DATE(), INTERVAL 2 DAY)
GROUP BY country, metric_name
GROUP BY metric_name, country;
```
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_basic_indicator_country_di`
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_di`
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_event_metric_country_di`
