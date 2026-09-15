---
id: "table:aidata2025.dwd.dwd_oper_delivery_adjust_user_di"
title: "aidata2025.dwd.dwd_oper_delivery_adjust_user_di · adjust数据归因明细表-ai产品"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_oper_delivery_adjust_user_di.md", "feishu:aidata2025.dwd.dwd_oper_delivery_adjust_user_di", "schema:aidata2025.dwd.dwd_oper_delivery_adjust_user_di"]
tags: ["dwd_oper_delivery_adjust_user_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_oper_delivery_adjust_user_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_oper_delivery_adjust_user_di · adjust数据归因明细表-ai产品

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_oper_delivery_adjust_user_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | package_name, country, campaign_name, adid |
| 更新 | T+1  9:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 事件日期，分区字段 | schema |
| `package_name` | STRING | NULLABLE | 应用包名 | schema |
| `app_name` | STRING | NULLABLE | 产品名 | schema |
| `event_name` | STRING | NULLABLE | 事件名称 | schema |
| `activity_kind` | STRING | NULLABLE | install, event, reattribution等 | schema |
| `created_at` | STRING | NULLABLE | 原始创建时间戳 | schema |
| `created_time` | DATETIME | NULLABLE | 转换后的创建时间 | schema |
| `installed_at` | STRING | NULLABLE | 原始安装时间戳 | schema |
| `installed_time` | DATETIME | NULLABLE | 转换后的安装时间 | schema |
| `platform` | STRING | NULLABLE | 归因平台ga, fb, tt, asa等 | schema |
| `country` | STRING | NULLABLE | 国家代码 | schema |
| `adid` | STRING | NULLABLE | Adjust 唯一设备 ID | schema |
| `campaign_id` | STRING | NULLABLE | 渠道原始广告系列 ID | schema |
| `campaign_name` | STRING | NULLABLE | 渠道原始广告系列名称 | schema |
| `adgroup_id` | STRING | NULLABLE | 渠道原始广告组 ID | schema |
| `adgroup_name` | STRING | NULLABLE | 渠道原始广告组名称 | schema |
| `tracker_name` | STRING | NULLABLE | Adjust 追踪器全名 | schema |
| `revenue_usd` | FLOAT | NULLABLE | 收入金额 | schema |
| `product_id` | STRING | NULLABLE | 内购产品 ID | schema |
| `currency` | STRING | NULLABLE | 币种 (默认 USD) | schema |
| `gclid` | STRING | NULLABLE | Google Click ID | schema |
| `network_type` | STRING | NULLABLE | 网络类型 (Search, Display等) | schema |
| `engagement_type` | STRING | NULLABLE | 交互类型 (click, impression) | schema |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- package_name: 飞书补充解释：包名
- package_name: 旧文档补充解释：包名
- event_name: 飞书补充解释：事件名/事件英文名
- event_name: 旧文档补充解释：事件名/事件英文名
- activity_kind: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- activity_kind: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- created_at: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- created_at: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- created_time: 飞书 类型 timestamp；schema 类型 DATETIME
- created_time: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- created_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- created_time: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- installed_at: 飞书补充解释：安装时间
- installed_at: 旧文档补充解释：安装时间
- installed_time: 飞书 类型 timestamp；schema 类型 DATETIME
- installed_time: 飞书补充解释：安装时间
- installed_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- installed_time: 旧文档补充解释：安装时间
- platform: 飞书补充解释：应用所属平台，如 iOS、Android、Web。
- platform: 旧文档补充解释：应用所属平台，如 iOS、Android、Web。
- country: 飞书补充解释：国家
- country: 旧文档补充解释：国家
- adid: 飞书补充解释：用户的广告id身份，也是一种唯一id
- adid: 旧文档补充解释：用户的广告id身份，也是一种唯一id
- campaign_id: 飞书补充解释：投放campaign id
- campaign_id: 旧文档补充解释：投放campaign id
- campaign_name: 飞书补充解释：投放campaign名称
- campaign_name: 旧文档补充解释：投放campaign名称
- adgroup_id: 飞书补充解释：广告组id
- adgroup_id: 旧文档补充解释：广告组id
- adgroup_name: 飞书补充解释：投放广告组
- adgroup_name: 旧文档补充解释：投放广告组
- tracker_name: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- tracker_name: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- revenue_usd: 飞书补充解释：收入
- revenue_usd: 旧文档补充解释：收入
- product_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- product_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- currency: 飞书补充解释：汇率
- currency: 旧文档补充解释：汇率
- gclid: 飞书补充解释：一种用户的身份id
- gclid: 旧文档补充解释：一种用户的身份id
- network_type: 飞书补充解释：设备网络类型
- network_type: 旧文档补充解释：设备网络类型
- engagement_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- engagement_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | fx-editor.analytics_263446298.daily_adjust_report_*， ods.ods_adjust_collart_android_1d， |
| 是否需要展示血缘 | 否 |
| 数据来源 | adjust |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_delivery_adjust_user_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdwd%2Fdaily%2Fh_dwd_oper_delivery_adjust_user_di.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。
- 旧说明把币种字段写作“汇率”；币种代码与换算比率应分别确认，不直接用该列作除数。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：fx-editor.analytics_263446298.daily_adjust_report_*， ods.ods_adjust_collart_android_1d，
