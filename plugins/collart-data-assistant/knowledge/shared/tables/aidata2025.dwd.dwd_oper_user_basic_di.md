---
id: "table:aidata2025.dwd.dwd_oper_user_basic_di"
title: "aidata2025.dwd.dwd_oper_user_basic_di · ai组每日活跃用户id表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_oper_user_basic_di.md", "dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_basic_di.sqlx", "feishu:aidata2025.dwd.dwd_oper_user_basic_di", "schema:aidata2025.dwd.dwd_oper_user_basic_di"]
tags: ["dwd_oper_user_basic_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_oper_user_basic_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_oper_user_basic_di · ai组每日活跃用户id表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_oper_user_basic_di` |
| 粒度 | 每天每个user_pseudo_Id一行 |
| 主键/去重键 | event_Date,user_pseudo_id；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | app_name, package_name, country, user_pseudo_id |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 同步日期 | schema |
| `app_name` | STRING | NULLABLE | 项目名称 | schema |
| `user_pseudo_id` | STRING | NULLABLE | firebase上报的用户id | schema |
| `user_id` | STRING | NULLABLE | userid | schema |
| `adjust_id` | STRING | NULLABLE | adjust_id | schema |
| `atlasv_uid` | STRING | NULLABLE | 技术团队给用户定义的唯一id | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | schema |
| `traffic_src_type` | STRING | NULLABLE | 投放来源（nature/delivery） | schema |
| `traffic_src_name` | STRING | NULLABLE | 投放来源名称 | schema |
| `country` | STRING | NULLABLE | 国家 | schema |
| `country_level` | INTEGER | NULLABLE | 国家等级 | schema |
| `city` | STRING | NULLABLE | 城市 | schema |
| `device_language` | STRING | NULLABLE | 设备语言 | schema |
| `device_total_ram` | STRING | NULLABLE | 设备内存 | schema |
| `mobile_brand_name` | STRING | NULLABLE | 手机品牌 | schema |
| `mobile_model_name` | STRING | NULLABLE | 机型 | schema |
| `app_version` | STRING | NULLABLE | 版本号 | schema |
| `network_type` | STRING | NULLABLE | 网络环境 | schema |
| `is_new` | BOOLEAN | NULLABLE | 是否新客 | schema |
| `is_active` | BOOLEAN | NULLABLE | 是否活跃 | schema |
| `register_time` | DATETIME | NULLABLE | 注册时间 | schema |
| `mobile_marketing_name` | STRING | NULLABLE | 设备型号 | 飞书 |
| `vip_type` | STRING | NULLABLE | 是否VIP | 飞书 |
| `subscribe_time` | DATETIME | NULLABLE | 订阅时间 | schema |
| `subscribe_product_id` | STRING | NULLABLE | 订阅ID | schema |
| `os_classify` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `os_cpu_info` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `subscriptions` | RECORD | REPEATED | 复杂结构字段，通常包含嵌套对象或数组信息。 | 飞书 |
| `subscriptions.product_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscriptions.sub_time` | DATETIME | NULLABLE | 未说明 | 缺口 |
| `advertising_id` | STRING | NULLABLE | 用户标识 每个用户唯一 | schema |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- user_pseudo_id: 飞书补充解释：用户id，firebase分配的唯一id
- user_pseudo_id: 旧文档补充解释：用户id，firebase分配的唯一id
- user_id: 飞书补充解释：用户id，内部平台分配的唯一id
- user_id: 旧文档补充解释：用户id，内部平台分配的唯一id
- adjust_id: 飞书补充解释：adjust id
- adjust_id: 旧文档补充解释：adjust id
- traffic_src_type: 飞书补充解释：投放渠道类型
- traffic_src_type: 旧文档补充解释：投放渠道类型
- traffic_src_name: 飞书补充解释：投放渠道名称
- traffic_src_name: 旧文档补充解释：投放渠道名称
- country_level: 飞书补充解释：国家T级；比如T1/T2/T3
- country_level: 旧文档补充解释：国家T级；比如T1/T2/T3
- city: 飞书补充解释：用户所在城市
- city: 旧文档补充解释：用户所在城市
- mobile_brand_name: 飞书补充解释：设备品牌名
- mobile_brand_name: 旧文档补充解释：设备品牌名
- mobile_model_name: 飞书补充解释：设备型号
- mobile_model_name: 旧文档补充解释：设备型号
- app_version: 飞书补充解释：app客户端版本号
- app_version: 旧文档补充解释：app客户端版本号
- network_type: 飞书补充解释：设备网络类型
- network_type: 旧文档补充解释：设备网络类型
- is_new: 飞书补充解释：是否新老用户，true代表新用户、false代表老用户
- is_new: 旧文档补充解释：是否新老用户，true代表新用户、false代表老用户
- is_active: 飞书补充解释：布尔标记字段，用于表示是/否状态。
- is_active: 旧文档补充解释：布尔标记字段，用于表示是/否状态。
- register_time: 飞书 类型 timestamp；schema 类型 DATETIME
- register_time: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- register_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- register_time: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- subscribe_time: 飞书 类型 timestamp；schema 类型 DATETIME
- subscribe_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- subscribe_product_id: 飞书补充解释：订阅商品
- subscribe_product_id: 旧文档补充解释：订阅商品
- advertising_id: 飞书补充解释：用户的广告id身份，也是一种唯一id
- advertising_id: 旧文档补充解释：用户的广告id身份，也是一种唯一id

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_user_event_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_user_basic_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdwd%2Fdaily%2Fh_dwd_oper_user_basic_di.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_oper_user_basic_di.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_oper_user_basic_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:54.599379+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_oper_user_basic_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
AND to_date) a
where event_date between from_date-29 and to_date
group by all
left join adjust_tab b
on u.adjust_id = b.adid
and u.package_name = b.package_name
and u.app_name = b.app_name
```

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_oper_user_event_di
