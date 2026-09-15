---
id: "table:aidata2025.ads.ads_aidata_retain_di"
title: "aidata2025.ads.ads_aidata_retain_di · ai组基础数据表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ads.ads_aidata_retain_di.md", "dataform:aidata/definitions/ads/daily/ads_aidata_retain_di.sqlx", "feishu:aidata2025.ads.ads_aidata_retain_di", "schema:aidata2025.ads.ads_aidata_retain_di"]
tags: ["ads_aidata_retain_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_aidata_retain_di"]
review_required: false
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_aidata_retain_di · ai组基础数据表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_aidata_retain_di` |
| 粒度 | 每天每个产品每个国家分版本 一行数据 |
| 主键/去重键 | 日期+产品+国家+版本；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `is_new` | BOOLEAN | NULLABLE | 是否新老用户，true代表新用户、false代表老用户 | 飞书 |
| `is_vip` | STRING | NULLABLE | 是否付费用户，true代表付费用户、false代表免费用户 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `app_version` | STRING | NULLABLE | app客户端版本号 | 飞书 |
| `dau` | INTEGER | NULLABLE | dau | 飞书 |
| `retain_2` | INTEGER | NULLABLE | 次日留存用户数，计算新用户次留需要过滤is_new=true时用retain_2/dau计算； | 飞书 |
| `retain_3` | INTEGER | NULLABLE | 该字段表示用户的3日留存情况，即某一特定时间节点新增的用户在3天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_4` | INTEGER | NULLABLE | 该字段表示用户的4日留存情况，即某一特定时间节点新增的用户在4天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_5` | INTEGER | NULLABLE | 该字段表示用户的5日留存情况，即某一特定时间节点新增的用户在5天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_6` | INTEGER | NULLABLE | 该字段表示用户的6日留存情况，即某一特定时间节点新增的用户在6天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_7` | INTEGER | NULLABLE | 该字段表示用户的7日留存情况，即某一特定时间节点新增的用户在7天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_8` | INTEGER | NULLABLE | 该字段表示用户的8日留存情况，即某一特定时间节点新增的用户在8天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_9` | INTEGER | NULLABLE | 该字段表示用户的9日留存情况，即某一特定时间节点新增的用户在9天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_10` | INTEGER | NULLABLE | 该字段表示用户的10日留存情况，即某一特定时间节点新增的用户在10天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_11` | INTEGER | NULLABLE | 该字段表示用户的11日留存情况，即某一特定时间节点新增的用户在11天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_12` | INTEGER | NULLABLE | 该字段表示用户的12日留存情况，即某一特定时间节点新增的用户在12天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_13` | INTEGER | NULLABLE | 该字段表示用户的13日留存情况，即某一特定时间节点新增的用户在13天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_14` | INTEGER | NULLABLE | 该字段表示用户的14日留存情况，即某一特定时间节点新增的用户在14天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_15` | INTEGER | NULLABLE | 该字段表示用户的15日留存情况，即某一特定时间节点新增的用户在15天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_16` | INTEGER | NULLABLE | 该字段表示用户的16日留存情况，即某一特定时间节点新增的用户在16天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_17` | INTEGER | NULLABLE | 该字段表示用户的17日留存情况，即某一特定时间节点新增的用户在17天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_18` | INTEGER | NULLABLE | 该字段表示用户的18日留存情况，即某一特定时间节点新增的用户在18天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_19` | INTEGER | NULLABLE | 该字段表示用户的19日留存情况，即某一特定时间节点新增的用户在19天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_20` | INTEGER | NULLABLE | 该字段表示用户的20日留存情况，即某一特定时间节点新增的用户在20天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_21` | INTEGER | NULLABLE | 该字段表示用户的21日留存情况，即某一特定时间节点新增的用户在21天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_22` | INTEGER | NULLABLE | 该字段表示用户22日留存情况，即某一特定时间节点新增的用户22天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_23` | INTEGER | NULLABLE | 该字段表示用户的23日留存情况，即某一特定时间节点新增的用户在23天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_24` | INTEGER | NULLABLE | 该字段表示用户的24日留存情况，即某一特定时间节点新增的用户在24天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_25` | INTEGER | NULLABLE | 该字段表示用户的25日留存情况，即某一特定时间节点新增的用户在25天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_26` | INTEGER | NULLABLE | 该字段表示用户的26日留存情况，即某一特定时间节点新增的用户在26天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_27` | INTEGER | NULLABLE | 该字段表示用户的27日留存情况，即某一特定时间节点新增的用户在27天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_28` | INTEGER | NULLABLE | 该字段表示用户的28日留存情况，即某一特定时间节点新增的用户在28天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_29` | INTEGER | NULLABLE | 该字段表示用户的29日留存情况，即某一特定时间节点新增的用户在29天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_30` | INTEGER | NULLABLE | 该字段表示用户的30日留存情况，即某一特定时间节点新增的用户在30天后仍然活跃的数量，数据类型为整数。 | 飞书 |
| `retain_31` | INTEGER | NULLABLE | 该字段表示用户的31日留存情况，即某一特定时间节点新增的用户在31天后仍然活跃的数量，数据类型为整数。 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_user_basic_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_aidata_retain_di) |
| 任务地址 | ads/daily/ads_aidata_retain_di.sqlx |
| 看板 | - |

### 使用限制

- retain_2 的历史说明为次日；其他 retain_N 的自动解释可能偏移一天，不能按字段后缀直接认定 Dn。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/daily/ads_aidata_retain_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/daily/ads_aidata_retain_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.055615+00:00`。同一 SQLX 的产出：`aidata2025.ads.ads_aidata_retain_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
declare from_date date default  date_sub(${dataform.projectConfig.vars.biz_date} ,interval 31 day);
declare to_date date default ${dataform.projectConfig.vars.biz_date};
where event_date between from_date and to_date
and is_active=True
left join (
where event_date between from_date and to_date + 31
on a.package_name=b.package_name
and a.user_pseudo_id=b.user_pseudo_id
group by 1,2,3,4,5,6,7,8
group by 1,2,3,4,5,6,7
```

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_oper_user_basic_di
