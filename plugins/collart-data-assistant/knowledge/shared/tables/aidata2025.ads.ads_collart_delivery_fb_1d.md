---
id: "table:aidata2025.ads.ads_collart_delivery_fb_1d"
title: "aidata2025.ads.ads_collart_delivery_fb_1d · collart fb、tt-adjust投放看板底表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads.ads_collart_delivery_fb_1d.md", "feishu:aidata2025.ads.ads_collart_delivery_fb_1d", "schema:aidata2025.ads.ads_collart_delivery_fb_1d"]
tags: ["ads_collart_delivery_fb_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_collart_delivery_fb_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_collart_delivery_fb_1d · collart fb、tt-adjust投放看板底表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_collart_delivery_fb_1d` |
| 粒度 | 每个产品、每天每个投放渠道每个国家一行 |
| 主键/去重键 | 日期+包名+投放渠道名+国家；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | country |
| 更新 | T+1 8:30；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 安装日期 分区字段 | schema |
| `package_name` | STRING | NULLABLE | 应用包名 | schema |
| `platform` | STRING | NULLABLE | 投放平台 | schema |
| `campaign_name` | STRING | NULLABLE | 广告系列名称 | schema |
| `adgroup_name` | STRING | NULLABLE | 广告组名称 | schema |
| `country` | STRING | NULLABLE | 国家 | schema |
| `cost` | FLOAT | NULLABLE | 投放消耗金额 | schema |
| `install` | INTEGER | NULLABLE | 投放侧安装数 | schema |
| `installed_cnt` | INTEGER | NULLABLE | Adjust安装数 | schema |
| `subscribe_cnt` | INTEGER | NULLABLE | 付费订阅设备数 | schema |
| `revenue_usd_1` | FLOAT | NULLABLE | D1(安装当日)累计收入 | schema |
| `revenue_usd_2` | FLOAT | NULLABLE | D2累计收入 | schema |
| `revenue_usd_3` | FLOAT | NULLABLE | D3累计收入 | schema |
| `revenue_usd_4` | FLOAT | NULLABLE | D4累计收入 | schema |
| `revenue_usd_5` | FLOAT | NULLABLE | D5累计收入 | schema |
| `revenue_usd_6` | FLOAT | NULLABLE | D6累计收入 | schema |
| `revenue_usd_7` | FLOAT | NULLABLE | D7累计收入 | schema |
| `revenue_usd_14` | FLOAT | NULLABLE | D14累计收入 | schema |
| `revenue_usd_21` | FLOAT | NULLABLE | D21累计收入 | schema |
| `revenue_usd_30` | FLOAT | NULLABLE | D30累计收入 | schema |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- package_name: 飞书补充解释：包名
- package_name: 旧文档补充解释：包名
- platform: 飞书补充解释：投放平台，如FB/TT
- platform: 旧文档补充解释：投放平台，如FB/TT
- campaign_name: 飞书补充解释：投放campaign名称
- campaign_name: 旧文档补充解释：投放campaign名称
- adgroup_name: 飞书补充解释：投放广告组
- adgroup_name: 旧文档补充解释：投放广告组
- cost: 飞书补充解释：投放花费
- cost: 旧文档补充解释：投放花费
- install: 飞书补充解释：投放平台统计的安装量
- install: 旧文档补充解释：投放平台统计的安装量
- installed_cnt: 飞书补充解释：安装量
- installed_cnt: 旧文档补充解释：安装量
- subscribe_cnt: 飞书补充解释：adjust统计的订阅量
- subscribe_cnt: 旧文档补充解释：adjust统计的订阅量
- revenue_usd_1: 飞书补充解释：adjust统计的投放用户首日收入
- revenue_usd_1: 旧文档补充解释：adjust统计的投放用户首日收入
- revenue_usd_2: 飞书补充解释：adjust统计的投放用户前2日收入
- revenue_usd_2: 旧文档补充解释：adjust统计的投放用户前2日收入
- revenue_usd_3: 飞书补充解释：adjust统计的投放用户前3日收入
- revenue_usd_3: 旧文档补充解释：adjust统计的投放用户前3日收入
- revenue_usd_4: 飞书补充解释：adjust统计的投放用户前4日收入
- revenue_usd_4: 旧文档补充解释：adjust统计的投放用户前4日收入
- revenue_usd_5: 飞书补充解释：adjust统计的投放用户前5日收入
- revenue_usd_5: 旧文档补充解释：adjust统计的投放用户前5日收入
- revenue_usd_6: 飞书补充解释：adjust统计的投放用户前6日收入
- revenue_usd_6: 旧文档补充解释：adjust统计的投放用户前6日收入
- revenue_usd_7: 飞书补充解释：adjust统计的投放用户前7日收入
- revenue_usd_7: 旧文档补充解释：adjust统计的投放用户前7日收入
- revenue_usd_14: 飞书补充解释：adjust统计的投放用户前14日收入
- revenue_usd_14: 旧文档补充解释：adjust统计的投放用户前14日收入
- revenue_usd_21: 飞书补充解释：adjust统计的投放用户前21日收入
- revenue_usd_21: 旧文档补充解释：adjust统计的投放用户前21日收入
- revenue_usd_30: 飞书补充解释：adjust统计的投放用户前30日收入
- revenue_usd_30: 旧文档补充解释：adjust统计的投放用户前30日收入

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_cdct_delivery_cost_di,dwd.dwd_oper_delivery_adjust_user_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | adjust / 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_collart_delivery_fb_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Fdaily%2Fh_ads_collart_delivery_fb_1d.sqlx?project=aidata2025) |
| 看板 | collart andrtoid GA投放看板 |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_cdct_delivery_cost_di,dwd.dwd_oper_delivery_adjust_user_di
