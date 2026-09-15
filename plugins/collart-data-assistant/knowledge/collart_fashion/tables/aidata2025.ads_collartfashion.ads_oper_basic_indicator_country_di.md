---
id: "table:aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di"
title: "aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di"
project: "collart_fashion"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_basic_indicator_country_di.sqlx", "feishu:aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di", "schema:aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di"]
tags: ["ads_oper_basic_indicator_country_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | country |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `dau` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_dau` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `churn_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `return_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_vip` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_free` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source` | RECORD | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.organic` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.delivery` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.kol` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.inhouse` | INTEGER | NULLABLE | 未说明 | 缺口 |
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
| `retain2_vip` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_free` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source` | RECORD | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.organic` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.delivery` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.kol` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.inhouse` | INTEGER | NULLABLE | 未说明 | 缺口 |
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
| `subscription.subscribe_uv_1d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv_old` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv_7d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv_1d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv_old` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv_7d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_cnt` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_amount` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.purchase_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.purchase_uv_1d` | INTEGER | NULLABLE | 未说明 | 缺口 |
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
| `revenue.revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `delivery` | RECORD | NULLABLE | 未说明 | 缺口 |
| `delivery.cost` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `delivery.impressions` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `delivery.clicks` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `delivery.installs` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_basic_indicator_country_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_fashion/ads_oper_basic_indicator_country_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:50.175070+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Fashion 第六张表：日 × 国家基础指标
  目标表: aidata2025.ads_collartfashion.ads_oper_basic_indicator_country_di
  - 行为: attr 按 country SUM；country 空值落到 unknown，避免支付行收入丢失
  - 上游 attr：is_studio_active 或 purchase_revenue>0；retain / rolling_retain：仅 is_new（= is_studio_new）
  - 收入 revenue STRUCT: 从 attr 上卷 Fashion Stripe 用户收入
  - 花费: 首版置 0（投放包名映射待确认）
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 30;
DECLARE to_date   DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN from_date AND to_date
GROUP BY event_date, COALESCE(country, 'unknown')
```
- 物理上游：`aidata2025.ads_collartfashion.ads_oper_basic_indicator_attr_di`
