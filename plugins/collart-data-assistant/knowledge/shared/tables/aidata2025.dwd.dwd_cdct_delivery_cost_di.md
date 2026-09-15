---
id: "table:aidata2025.dwd.dwd_cdct_delivery_cost_di"
title: "aidata2025.dwd.dwd_cdct_delivery_cost_di · 全公司分产品分campaign投放花费明细数据"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_cdct_delivery_cost_di.md", "dataform:aidata/definitions/dwd/daily/h_dwd_cdct_delivery_cost_di.sqlx", "feishu:aidata2025.dwd.dwd_cdct_delivery_cost_di", "schema:aidata2025.dwd.dwd_cdct_delivery_cost_di"]
tags: ["dwd_cdct_delivery_cost_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_cdct_delivery_cost_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_cdct_delivery_cost_di · 全公司分产品分campaign投放花费明细数据

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_cdct_delivery_cost_di` |
| 粒度 | 每天，每个产品每个campagin每个广告组一行 |
| 主键/去重键 | event_Date+ adgroup_id；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | package_name, campaign_name |
| 更新 | T+1 8:30；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | REQUIRED | 业务日期，用于分区 | schema |
| `delivery_type` | STRING | REQUIRED | 投放渠道类型:ga,tt,fb,asa | schema |
| `app_name` | STRING | NULLABLE | App名称 | schema |
| `package_name` | STRING | NULLABLE | 应用包名 | schema |
| `country` | STRING | NULLABLE | 国家或地区代码 | schema |
| `campaign_id` | STRING | NULLABLE | 广告系列 ID | schema |
| `campaign_name` | STRING | NULLABLE | 广告系列名称 | schema |
| `adgroup_id` | STRING | NULLABLE | 广告组 ID | schema |
| `adgroup_name` | STRING | NULLABLE | 广告组名称 | schema |
| `ad_id` | STRING | NULLABLE | 素材/广告 ID | schema |
| `ad_name` | STRING | NULLABLE | 素材/广告名称 | schema |
| `keyword` | STRING | NULLABLE | 搜索关键词 (主要用于ASA) | schema |
| `impressions` | INTEGER | NULLABLE | 展示次数 | schema |
| `clicks` | INTEGER | NULLABLE | 点击次数 (ASA对应taps) | schema |
| `cost` | FLOAT | NULLABLE | 标准消耗成本 | schema |
| `installs` | INTEGER | NULLABLE | 安装转化数 (GA/ASA对应Installs, TT对应SKAN等) | schema |
| `conversions` | INTEGER | NULLABLE | 通用转化事件数 (如GA中的Conversions) | schema |
| `actions` | RECORD | REPEATED | 复杂结构字段，通常包含嵌套对象或数组信息。 | 飞书 |
| `actions.action_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `actions.action_count` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `country_name` | STRING | NULLABLE | 未说明 | 缺口 |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- delivery_type: 飞书补充解释：投放平台
- delivery_type: 旧文档补充解释：投放平台
- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- package_name: 飞书补充解释：包名
- package_name: 旧文档补充解释：包名
- country: 飞书补充解释：国家
- country: 旧文档补充解释：国家
- campaign_id: 飞书补充解释：投放campaign id
- campaign_id: 旧文档补充解释：投放campaign id
- campaign_name: 飞书补充解释：投放campaign名称
- campaign_name: 旧文档补充解释：投放campaign名称
- adgroup_id: 飞书补充解释：广告组id
- adgroup_id: 旧文档补充解释：广告组id
- adgroup_name: 飞书补充解释：投放广告组
- adgroup_name: 旧文档补充解释：投放广告组
- ad_id: 飞书补充解释：广告id
- ad_id: 旧文档补充解释：广告id
- ad_name: 飞书补充解释：广告名称
- ad_name: 旧文档补充解释：广告名称
- keyword: 飞书补充解释：关键词
- keyword: 旧文档补充解释：关键词
- impressions: 飞书补充解释：投放广告展示次数
- impressions: 旧文档补充解释：投放广告展示次数
- clicks: 飞书补充解释：点击次数
- clicks: 旧文档补充解释：点击次数
- cost: 飞书补充解释：投放花费
- cost: 旧文档补充解释：投放花费
- installs: 飞书补充解释：安装量
- installs: 旧文档补充解释：安装量
- conversions: 飞书补充解释：转化次数
- conversions: 旧文档补充解释：转化次数

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.dws.dws_cdct_cost_google_1h,aidata2025.dws.dws_oper_tiktok_ad_1d,aidata2025.dws.dws_oper_fb_delivery_1d,aidata2025.dws.dws_oper_asa_keyword_collart_1d |
| 是否需要展示血缘 | 是 |
| 数据来源 | 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdwd!3sdwd_cdct_delivery_cost_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdwd%2Fdaily%2Fh_dwd_cdct_delivery_cost_di.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_cdct_delivery_cost_di.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_cdct_delivery_cost_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:54.413572+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_cdct_delivery_cost_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
WHERE event_date BETWEEN from_date
AND to_date
WHERE event_date BETWEEN from_date AND to_date
left join aidata2025.dim.dim_country_info b
on a.country = b.country_name_3
```

飞书登记上游（不保证当前依赖）：pubdata2025.dws.dws_cdct_cost_google_1h,aidata2025.dws.dws_oper_tiktok_ad_1d,aidata2025.dws.dws_oper_fb_delivery_1d,aidata2025.dws.dws_oper_asa_keyword_collart_1d
- 物理上游：`aidata2025.dws.dws_oper_tiktok_ad_1d`
- 物理上游：`pubdata2025.dws.dws_cdct_cost_delivery_fb_1d`
- 物理上游：`pubdata2025.dws.dws_cdct_cost_google_1h`
