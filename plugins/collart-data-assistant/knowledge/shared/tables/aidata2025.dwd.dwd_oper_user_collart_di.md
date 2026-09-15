---
id: "table:aidata2025.dwd.dwd_oper_user_collart_di"
title: "aidata2025.dwd.dwd_oper_user_collart_di"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/dwd_oper_user_collart_di.md", "feishu:aidata2025.dwd.dwd_oper_user_collart_di", "schema:aidata2025.dwd.dwd_oper_user_collart_di"]
tags: ["dwd_oper_user_collart_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_oper_user_collart_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_oper_user_collart_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_oper_user_collart_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `user_pseudo_id` | STRING | NULLABLE | 用户id，firebase分配的唯一id | 飞书 |
| `user_id` | STRING | NULLABLE | 用户id，内部平台分配的唯一id | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `traffic_src_type` | STRING | NULLABLE | 投放渠道类型 | 飞书 |
| `traffic_src_name` | STRING | NULLABLE | 投放渠道名称 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `country_level` | INTEGER | NULLABLE | 国家T级；比如T1/T2/T3 | 飞书 |
| `city` | STRING | NULLABLE | 用户所在城市 | 飞书 |
| `device_language` | STRING | NULLABLE | 设备语言 | 飞书 |
| `device_total_ram` | STRING | NULLABLE | 设备内存 | 飞书 |
| `mobile_brand_name` | STRING | NULLABLE | 设备品牌名 | 飞书 |
| `mobile_model_name` | STRING | NULLABLE | 设备型号 | 飞书 |
| `app_version` | STRING | NULLABLE | app客户端版本号 | 飞书 |
| `network_type` | STRING | NULLABLE | 设备网络类型 | 飞书 |
| `is_new` | BOOLEAN | NULLABLE | 是否新老用户，true代表新用户、false代表老用户 | 飞书 |
| `register_time` | DATETIME | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `atlasv_uid` | STRING | NULLABLE | 技术团队给用户定义的唯一id | 飞书 |
| `mobile_marketing_name` | STRING | NULLABLE | 设备型号 | 飞书 |
| `is_vip` | BOOLEAN | NULLABLE | 是否新老用户，true代表付费用户、false代表免费用户 | 飞书 |
| `is_remove` | BOOLEAN | NULLABLE | 是否卸载用户，true代表新用户、false代表老用户 | 飞书 |
| `is_purchase` | BOOLEAN | NULLABLE | 是否新老用户，true代表新用户、false代表老用户 | 飞书 |
| `subscribe_time` | DATETIME | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `subscribe_product_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `device_id` | STRING | NULLABLE | 设备id | 飞书 |
| `advertising_id` | STRING | NULLABLE | 用户的广告id身份，也是一种唯一id | 飞书 |
| `is_active` | BOOLEAN | NULLABLE | 是否活跃 | schema |

## 定义差异与补充

- register_time: 飞书 类型 timestamp；schema 类型 DATETIME
- subscribe_time: 飞书 类型 timestamp；schema 类型 DATETIME
- is_active: 飞书补充解释：布尔标记字段，用于表示是/否状态。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
