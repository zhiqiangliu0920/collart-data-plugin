---
id: "table:aidata2025.dws.dws_oper_basic_aidata_1d"
title: "aidata2025.dws.dws_oper_basic_aidata_1d · ai组 新增、活跃、留存基础数据汇总"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dws.dws_oper_basic_aidata_1d.md", "dataform:aidata/definitions/dws/daily/h_dws_oper_basic_aidata_1d.sqlx", "feishu:aidata2025.dws.dws_oper_basic_aidata_1d", "schema:aidata2025.dws.dws_oper_basic_aidata_1d"]
tags: ["dws_oper_basic_aidata_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_oper_basic_aidata_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dws.dws_oper_basic_aidata_1d · ai组 新增、活跃、留存基础数据汇总

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_oper_basic_aidata_1d` |
| 粒度 | 日期+产品+国家+版本 |
| 主键/去重键 | 日期+产品+国家+版本；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `traffic_src_type` | STRING | NULLABLE | 投放渠道类型 | 飞书 |
| `traffic_src_name` | STRING | NULLABLE | 投放渠道名称 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `app_version` | STRING | NULLABLE | app客户端版本号 | 飞书 |
| `vip_type` | INTEGER | NULLABLE | 是否vip | 飞书 |
| `dnu` | INTEGER | NULLABLE | 新增用户 | 飞书 |
| `dau` | INTEGER | NULLABLE | dau | 飞书 |
| `retention` | RECORD | NULLABLE | 留存用户数，针对新用户 | schema |
| `retention.day1` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day2` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day3` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day4` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day5` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day6` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day7` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day8` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day9` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day10` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day11` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day12` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day13` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day14` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day15` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day16` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day17` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day18` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day19` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day20` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day21` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day22` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day23` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day24` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day25` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day26` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day27` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day28` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day29` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retention.day30` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe` | RECORD | NULLABLE | 订阅用户数，针对新用户 | schema |
| `subscribe.day1` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day2` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day3` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day4` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day5` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day6` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day7` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day8` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day9` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day10` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day11` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day12` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day13` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day14` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day15` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day16` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day17` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day18` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day19` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day20` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day21` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day22` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day23` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day24` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day25` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day26` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day27` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day28` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day29` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscribe.day30` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `adjust_src_type` | STRING | NULLABLE | adjust渠道类型 | 飞书 |

## 定义差异与补充

- retention: 飞书补充解释：N日留存信息
- retention: 旧文档补充解释：N日留存信息
- subscribe: 飞书补充解释：N日订阅信息
- subscribe: 旧文档补充解释：N日订阅信息

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_user_basic_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdws!3sdws_oper_basic_aidata_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdws%2Fdaily%2Fh_dws_oper_basic_aidata_1d.sqlx?project=aidata2025) |
| 看板 | AI基础数据看板 |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dws/daily/h_dws_oper_basic_aidata_1d.sqlx`；仓库 `aidata`，路径 `definitions/dws/daily/h_dws_oper_basic_aidata_1d.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:55.026404+00:00`。同一 SQLX 的产出：`aidata2025.dws.dws_oper_basic_aidata_1d`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 0) AS day1,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 1) AS day2,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 2) AS day3,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 3) AS day4,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 4) AS day5,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 5) AS day6,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 6) AS day7,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 7) AS day8,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 8) AS day9,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 9) AS day10,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 10) AS day11,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 11) AS day12,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 12) AS day13,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 13) AS day14,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 14) AS day15,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 15) AS day16,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 16) AS day17,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 17) AS day18,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 18) AS day19,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 19) AS day20,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 20) AS day21,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 21) AS day22,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 22) AS day23,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 23) AS day24,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 24) AS day25,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 25) AS day26,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 26) AS day27,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 27) AS day28,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 28) AS day29,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 29) AS day30 ) AS retention,
AND DATE_DIFF(a.event_date, b.event_date, DAY) = 29) AS day30 ) AS subscribe,
INNER JOIN (
AND to_date
AND is_new=TRUE
AND a.package_name=b.package_name
AND to_date ) t
LEFT JOIN (
AND COALESCE(a.traffic_src_name, '') = COALESCE(b.traffic_src_name, '')
AND COALESCE(a.traffic_src_type, '') = COALESCE(b.traffic_src_type, '')
AND COALESCE(a.country, '') = COALESCE(b.country, '')
AND COALESCE(a.app_version, '') = COALESCE(b.app_version, '')
AND COALESCE(a.vip_type, 0) = COALESCE(b.vip_type, 0)
AND COALESCE(a.package_name, '') = COALESCE(b.package_name, '')
AND COALESCE(a.adjust_src_type, '') = COALESCE(b.adjust_src_type, '')
where a.package_name<>'collart_web';
```

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_oper_user_basic_di
