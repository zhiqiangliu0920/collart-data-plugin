---
id: "table:pubdata2025.ods.ods_woolong_subscription_1d"
title: "pubdata2025.ods.ods_woolong_subscription_1d"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.ods.ods_woolong_subscription_1d.md", "feishu:pubdata2025.ods.ods_woolong_subscription_1d", "schema:pubdata2025.ods.ods_woolong_subscription_1d"]
tags: ["ods_woolong_subscription_1d", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ods.ods_woolong_subscription_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ods.ods_woolong_subscription_1d

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ods.ods_woolong_subscription_1d` |
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
| `original_transaction_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `plan_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `is_in_trial_period` | BOOLEAN | NULLABLE | 布尔标记字段，用于表示是/否状态。 | 飞书 |
| `currency` | STRING | NULLABLE | 汇率 | 飞书 |
| `gclid` | STRING | NULLABLE | 一种用户的身份id | 飞书 |
| `adid` | STRING | NULLABLE | 用户的广告id身份，也是一种唯一id | 飞书 |
| `ip` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `idfa` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `install_timestamp` | INTEGER | NULLABLE | 安装时间 | 飞书 |
| `advertising_id` | STRING | NULLABLE | 用户的广告id身份，也是一种唯一id | 飞书 |
| `user_id` | STRING | NULLABLE | 用户id，内部平台分配的唯一id | 飞书 |
| `auto_renew` | BOOLEAN | NULLABLE | 是否自动续订商品 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `price` | NUMERIC | NULLABLE | 价格字段，用于记录商品、服务或订阅价格。 | 飞书 |
| `campaign` | STRING | NULLABLE | 投放campaign id | 飞书 |
| `introductory_price` | NUMERIC | NULLABLE | 价格字段，用于记录商品、服务或订阅价格。 | 飞书 |
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |

## 定义差异与补充

- price: 飞书 类型 float；schema 类型 NUMERIC
- price: 旧文档 类型 float；schema 类型 NUMERIC
- introductory_price: 飞书 类型 float；schema 类型 NUMERIC
- introductory_price: 旧文档 类型 float；schema 类型 NUMERIC

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 否 |
| 数据来源 | - |
| 数据表地址 | - |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。
- 旧说明把币种字段写作“汇率”；币种代码与换算比率应分别确认，不直接用该列作除数。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
