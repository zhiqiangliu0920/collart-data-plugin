---
id: "table:aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di"
title: "aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di"
project: "collart_web"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_web/ads_oper_basic_indicator_attr_di.sqlx", "feishu:aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di", "schema:aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di"]
tags: ["ads_oper_basic_indicator_attr_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | country, app_version, is_new |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `is_new` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_vip` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `dau` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `churn_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `return_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain` | RECORD | NULLABLE | 未说明 | 缺口 |
| `retain.d2` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d3` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d4` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d5` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d6` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d7` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d8` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d9` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d10` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d11` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d12` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d13` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d14` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d15` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d16` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d17` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d18` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d19` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d20` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d21` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d22` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d23` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d24` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d25` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d26` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d27` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d28` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d29` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d30` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain` | RECORD | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d2` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d3` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d4` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d5` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d6` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d7` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d8` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d9` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d10` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d11` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d12` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d13` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d14` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d15` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d16` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d17` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d18` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d19` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d20` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d21` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d22` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d23` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d24` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d25` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d26` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d27` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d28` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d29` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d30` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription` | RECORD | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv_7d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv_7d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_cnt` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_amount` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.purchase_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue` | RECORD | NULLABLE | 未说明 | 缺口 |
| `revenue.purchase_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.resub_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.new_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.credit_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.ad_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.new_subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue.renew_subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue.credit_pack_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue.ad_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_web/ads_oper_basic_indicator_attr_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_web/ads_oper_basic_indicator_attr_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:52.271866+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Web 第五张表：日 × 默认维度基础指标
  Dataform: definitions/ads/collart/collart_web/ads_oper_basic_indicator_attr_di.sqlx
  目标表  : aidata2025.ads_collartweb.ads_oper_basic_indicator_attr_di
  上游    : ads_collartweb.ads_oper_user_active_di

  口径（对齐 Android 表 5 + iOS active）:
  - 维度：is_new / is_vip / country / traffic_src_type / traffic_src_platform / traffic_src_name / app_version
  - app_version：当日 Top5，其余折叠为 'other'；不加 city / package_name；不做 MAU
  - retain / rolling_retain：STRUCT d2-d30（与 active 1:1，d2=次日）；COUNTIF 分子，NULL 不计
  - 当日订阅/购点：active.subscription.is_subscribe / is_credit_pack（源=Apple IAP）
  - 7 日内订阅/购点：含当日，date_diff ∈ [0,6]
  - 金额：SUM(active.revenue.*)（用户粒度 Apple IAP；country/daily 汇总层另取官方 Sales）
  - 流失/回流：COUNTIF(is_churn/is_return)；观察窗未满 NULL 不计
  - 刷新窗口 [biz_date-30, biz_date]；源表额外前读 6 日供 7 日商业窗口
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 30;
DECLARE to_date   DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
DECLARE source_from_date DATE DEFAULT from_date - 6;
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN source_from_date AND to_date
AND user_pseudo_id IS NOT NULL
GROUP BY event_date, user_pseudo_id
LEFT JOIN purch_day AS p
ON a.user_pseudo_id = p.user_pseudo_id
AND DATE_DIFF(a.event_date, p.event_date, DAY) BETWEEN 0 AND 6
WHERE a.event_date BETWEEN from_date AND to_date
GROUP BY a.event_date, a.user_pseudo_id
LEFT JOIN win7 AS w
ORDER BY COUNT(DISTINCT user_pseudo_id) DESC, app_version
GROUP BY event_date, app_version
WHERE rn <= 5
LEFT JOIN top_version AS t
ON a.event_date = t.event_date
AND a.app_version = t.app_version
```
- 物理上游：`aidata2025.ads_collartweb.ads_oper_user_active_di`
