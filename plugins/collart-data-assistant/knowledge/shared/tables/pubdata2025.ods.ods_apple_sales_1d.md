---
id: "table:pubdata2025.ods.ods_apple_sales_1d"
title: "pubdata2025.ods.ods_apple_sales_1d · 苹果商店收入与订阅事件报告"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.ods.ods_apple_sales_1d.md", "feishu:pubdata2025.ods.ods_apple_sales_1d", "schema:pubdata2025.ods.ods_apple_sales_1d"]
tags: ["ods_apple_sales_1d", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ods.ods_apple_sales_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ods.ods_apple_sales_1d · 苹果商店收入与订阅事件报告

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ods.ods_apple_sales_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "stats_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `stats_date` | DATE | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `revenue_usd` | FLOAT | NULLABLE | 收入 | 飞书 |
| `provider` | STRING | NULLABLE | 服务提供方或供应商标识字段。 | 飞书 |
| `provider_country` | STRING | NULLABLE | 计数指标字段，用于统计人数、次数或记录量。 | 飞书 |
| `sku` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `developer` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `title` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `version` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `product_type_identifier` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `units` | FLOAT | NULLABLE | 浮点型指标字段，用于统计金额、比率或均值。 | 飞书 |
| `developer_proceeds` | FLOAT | NULLABLE | 收入 | 飞书 |
| `begin_date` | DATE | NULLABLE | 订阅开始日期 | 飞书 |
| `end_date` | DATE | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `customer_currency` | STRING | NULLABLE | 汇率 | 飞书 |
| `country_code` | STRING | NULLABLE | 国家代码 | 飞书 |
| `currency_of_proceeds` | STRING | NULLABLE | 汇率 | 飞书 |
| `apple_identifier` | FLOAT | NULLABLE | 浮点型指标字段，用于统计金额、比率或均值。 | 飞书 |
| `customer_price` | FLOAT | NULLABLE | 订阅价格 | 飞书 |
| `promo_code` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `parent_identifier` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `subscription` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `period` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `category` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `cmb` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `device` | STRING | NULLABLE | 设备 | 飞书 |
| `supported_platforms` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `proceeds_reason` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `preserved_pricing` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `client` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `order_type` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `region` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `project` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 是 |
| 数据来源 | 苹果商店 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sods!3sods_apple_sales_1d) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。
- 旧说明把币种字段写作“汇率”；币种代码与换算比率应分别确认，不直接用该列作除数。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
