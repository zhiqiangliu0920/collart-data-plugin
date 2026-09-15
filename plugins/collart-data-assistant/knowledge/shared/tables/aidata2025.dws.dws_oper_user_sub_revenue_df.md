---
id: "table:aidata2025.dws.dws_oper_user_sub_revenue_df"
title: "aidata2025.dws.dws_oper_user_sub_revenue_df · 安卓用户粒度 收入表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dws.dws_oper_user_sub_revenue_df.md", "dataform:aidata/definitions/dws/daily/h_dws_oper_user_sub_revenue_df.sqlx", "feishu:aidata2025.dws.dws_oper_user_sub_revenue_df", "schema:aidata2025.dws.dws_oper_user_sub_revenue_df"]
tags: ["dws_oper_user_sub_revenue_df", "字段", "schema", "SQLX"]
tables: ["aidata2025.dws.dws_oper_user_sub_revenue_df"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dws.dws_oper_user_sub_revenue_df · 安卓用户粒度 收入表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dws.dws_oper_user_sub_revenue_df` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "order_date"} |
| 聚簇 | package_name, user_pseudo_id |
| 更新 | T+1 8:30；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `order_date` | DATE | NULLABLE | 订阅日期 | schema |
| `event_date` | DATE | NULLABLE | 埋点日期 | schema |
| `user_pseudo_id` | STRING | NULLABLE | 用户ID | schema |
| `app_name` | STRING | NULLABLE | App名称 | schema |
| `package_name` | STRING | NULLABLE | 包名称 | schema |
| `country` | STRING | NULLABLE | 国家 | schema |
| `last_subscribe_type` | STRING | NULLABLE | 最近订阅类型 | schema |
| `order_num` | INTEGER | NULLABLE | 订阅次数 | schema |
| `first_subscribe_date` | DATE | NULLABLE | 首订日期 | schema |
| `last_subscribe_date` | DATE | NULLABLE | 最近一次订阅日期 | schema |
| `user_id` | STRING | NULLABLE | 前端透传用户ID | schema |
| `is_new` | BOOLEAN | NULLABLE | 是否新客 | schema |
| `is_active` | BOOLEAN | NULLABLE | 是否活跃 | schema |
| `traffic_src_type` | STRING | NULLABLE | 用户渠道属性 | schema |
| `app_version` | STRING | NULLABLE | App版本 | schema |
| `total_revenue_today` | FLOAT | NULLABLE | 当日总收入 | schema |
| `resub_revenue_today` | FLOAT | NULLABLE | 当日续订收入 | schema |
| `new_revenue_today` | FLOAT | NULLABLE | 当日首订收入 | schema |
| `trial_conver_revenue_today` | FLOAT | NULLABLE | 当日试用转正收入 | schema |
| `total_revenue_all` | FLOAT | NULLABLE | 历史总收入 | schema |
| `resub_revenue_all` | FLOAT | NULLABLE | 历史续订收入 | schema |
| `new_revenue_all` | FLOAT | NULLABLE | 历史首订收入 | schema |
| `trial_conver_revenue_all` | FLOAT | NULLABLE | 历史试用转正收入 | schema |
| `new_order_num` | INTEGER | NULLABLE | 首订订单数 | schema |
| `renew_order_num` | INTEGER | NULLABLE | 续订订单数（转正+续订） | schema |
| `credit_revenue_today` | FLOAT | NULLABLE | 当日点数包收入 | schema |
| `credit_revenue_all` | FLOAT | NULLABLE | 累计点数包收入 | schema |

## 定义差异与补充

- order_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- order_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- user_pseudo_id: 飞书补充解释：用户id，firebase分配的唯一id
- user_pseudo_id: 旧文档补充解释：用户id，firebase分配的唯一id
- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- package_name: 飞书补充解释：包名
- package_name: 旧文档补充解释：包名
- last_subscribe_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- last_subscribe_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- order_num: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- order_num: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- first_subscribe_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- first_subscribe_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- last_subscribe_date: 飞书补充解释：最近订阅日期
- last_subscribe_date: 旧文档补充解释：最近订阅日期
- user_id: 飞书补充解释：用户id，内部平台分配的唯一id
- user_id: 旧文档补充解释：用户id，内部平台分配的唯一id
- is_new: 飞书补充解释：是否新老用户，true代表新用户、false代表老用户
- is_new: 旧文档补充解释：是否新老用户，true代表新用户、false代表老用户
- is_active: 飞书补充解释：布尔标记字段，用于表示是/否状态。
- is_active: 旧文档补充解释：布尔标记字段，用于表示是/否状态。
- traffic_src_type: 飞书补充解释：投放渠道类型
- traffic_src_type: 旧文档补充解释：投放渠道类型
- app_version: 飞书补充解释：app客户端版本号
- app_version: 旧文档补充解释：app客户端版本号
- total_revenue_today: 飞书补充解释：收入数值字段。
- total_revenue_today: 旧文档补充解释：收入数值字段。
- resub_revenue_today: 飞书补充解释：收入数值字段。
- resub_revenue_today: 旧文档补充解释：收入数值字段。
- new_revenue_today: 飞书补充解释：首次订阅收入
- new_revenue_today: 旧文档补充解释：首次订阅收入
- trial_conver_revenue_today: 飞书补充解释：收入数值字段。
- trial_conver_revenue_today: 旧文档补充解释：收入数值字段。
- total_revenue_all: 飞书补充解释：收入数值字段。
- total_revenue_all: 旧文档补充解释：收入数值字段。
- resub_revenue_all: 飞书补充解释：收入数值字段。
- resub_revenue_all: 旧文档补充解释：收入数值字段。
- new_revenue_all: 飞书补充解释：首次订阅收入
- new_revenue_all: 旧文档补充解释：首次订阅收入
- trial_conver_revenue_all: 飞书补充解释：收入数值字段。
- trial_conver_revenue_all: 旧文档补充解释：收入数值字段。
- new_order_num: 飞书补充解释：首次订阅订单数
- new_order_num: 旧文档补充解释：首次订阅订单数
- renew_order_num: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_num: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- credit_revenue_today: 飞书补充解释：点数包收入
- credit_revenue_today: 旧文档补充解释：点数包收入
- credit_revenue_all: 飞书补充解释：点数包收入
- credit_revenue_all: 旧文档补充解释：点数包收入

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_sub_order_revenue_df |
| 是否需要展示血缘 | 否 |
| 数据来源 | 谷歌商店 / 服务端 / 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m10!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_delivery_adjust_user_di!1m4!4m3!1saidata2025!2sdws!3sdws_oper_user_sub_revenue_df) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdws%2Fdaily%2Fh_dws_oper_user_sub_revenue_df.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dws/daily/h_dws_oper_user_sub_revenue_df.sqlx`；仓库 `aidata`，路径 `definitions/dws/daily/h_dws_oper_user_sub_revenue_df.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:55.363096+00:00`。同一 SQLX 的产出：`aidata2025.dws.dws_oper_user_sub_revenue_df`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
AND to_date
AND sub_tab.app_name = user_tab.app_name
AND sub_tab.event_date = user_tab.event_date
LEFT JOIN (
AND a.app_name = b.app_name
AND a.package_name = b.package_name
AND a.country = b.country
```

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_oper_sub_order_revenue_df
