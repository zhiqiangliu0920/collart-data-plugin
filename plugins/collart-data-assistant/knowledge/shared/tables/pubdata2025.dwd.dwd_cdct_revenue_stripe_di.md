---
id: "table:pubdata2025.dwd.dwd_cdct_revenue_stripe_di"
title: "pubdata2025.dwd.dwd_cdct_revenue_stripe_di · collart web收入表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_fashion/tables/pubdata2025.dwd.dwd_cdct_revenue_stripe_di.md", "ai-knowledge:collart_web/tables/pubdata2025.dwd.dwd_cdct_revenue_stripe_di.md", "dataform:pubdata/definitions/dwd/revenue/h_dwd_cdct_revenue_stripe_di.sqlx", "feishu:pubdata2025.dwd.dwd_cdct_revenue_stripe_di", "schema:pubdata2025.dwd.dwd_cdct_revenue_stripe_di"]
tags: ["dwd_cdct_revenue_stripe_di", "字段", "schema", "SQLX"]
tables: ["pubdata2025.dwd.dwd_cdct_revenue_stripe_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.dwd.dwd_cdct_revenue_stripe_di · collart web收入表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.dwd.dwd_cdct_revenue_stripe_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | app_name, country, product_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期分区 | schema |
| `event_timestamp` | INTEGER | NULLABLE | 交易发生时间戳 | schema |
| `transaction_id` | STRING | NULLABLE | Stripe 流水唯一 ID | schema |
| `app_name` | STRING | NULLABLE | 所属应用名称 | schema |
| `charge_type` | STRING | NULLABLE | 交易类型 | schema |
| `country` | STRING | NULLABLE | 支付账户国家代码 | schema |
| `currency` | STRING | NULLABLE | 结算币种  | schema |
| `stripe_customer_id` | STRING | NULLABLE | Stripe 客户 ID  | schema |
| `amount` | FLOAT | NULLABLE | 交易总金额 | schema |
| `fee` | FLOAT | NULLABLE | Stripe 收取的手续费 | schema |
| `revneue` | FLOAT | NULLABLE | 净收入 (Amount - Fee) | schema |
| `description_type` | STRING | NULLABLE | 交易描述信息 | schema |
| `order_status` | STRING | NULLABLE | 流水订单状态 | schema |
| `product_id` | STRING | NULLABLE | 产品唯一 ID  | schema |
| `product_name` | STRING | NULLABLE | 产品名称 | schema |
| `subscription_id` | STRING | NULLABLE | 关联的订阅 ID | schema |
| `subscription_status` | STRING | NULLABLE | 该订阅目前的实时状态 | schema |
| `user_id` | STRING | NULLABLE | 用户user_id | schema |
| `payment_channel` | STRING | NULLABLE | 付款平台 | schema |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `cancel_at_period_end` | boolean | 布尔标记字段，用于表示是/否状态。 |
| `current_period_end` | int | 订阅结束日期 |
| `current_period_start` | int | 订阅开始日期 |
| `sub_price_id` | string | 用于唯一标识记录或业务实体的关键字段。 |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- event_timestamp: 飞书补充解释：事件触发时间
- event_timestamp: 旧文档补充解释：事件触发时间
- transaction_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- transaction_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- charge_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- charge_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- country: 飞书补充解释：国家
- country: 旧文档补充解释：国家
- currency: 飞书补充解释：汇率
- currency: 旧文档补充解释：汇率
- stripe_customer_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- stripe_customer_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- amount: 飞书补充解释：交易金额
- amount: 旧文档补充解释：交易金额
- fee: 飞书补充解释：浮点型指标字段，用于统计金额、比率或均值。
- fee: 旧文档补充解释：浮点型指标字段，用于统计金额、比率或均值。
- revneue: 飞书补充解释：浮点型指标字段，用于统计金额、比率或均值。
- revneue: 旧文档补充解释：浮点型指标字段，用于统计金额、比率或均值。
- description_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- description_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- order_status: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- order_status: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- product_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- product_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- product_name: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- product_name: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- subscription_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- subscription_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- subscription_status: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- subscription_status: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- user_id: 飞书补充解释：用户id，内部平台分配的唯一id
- user_id: 旧文档补充解释：用户id，内部平台分配的唯一id
- payment_channel: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- payment_channel: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。

## 表专属业务说明

## 2. 核心作用
本表主要用于以下场景：
- 计算每日收入、首次订阅收入、点数包收入、续订收入使用
- 分析收入的国家分布
- **2026-08-28 起**：Web 用户粒度收入、移动端俄罗斯支付（`currency='RUB'`）用户粒度收入的 T+1 真值。不再用 `ods.orders`。
- **2026-09-06**：Android/iOS `ads_oper_user_active_di` 已叠加本表 RUB（进 `purchase_revenue`/`credit_revenue`）；四端 profile 都是 `SUM(active.revenue)`。country/daily 未改。
- **2026-09-07**：`dwd_cdct_orders_revenue_hi` 是空表，不要当当天补洞源。

## 6. 数据质量与风险提示
-此表有重复数据，因此在分析计算前以transaction_Id为基础，进行去重处理
- 每日约北京 8 点刷新到昨天；查「今天」本表会空。不要用 `dwd_cdct_orders_revenue_hi` 补（0 行）。当天未进 T+1 就等次日，或说明是 T+1 口径。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 是 |
| 数据来源 | 第三方支付平台（stripe等） |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sdwd!3sdwd_cdct_revenue_stripe_di) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。
- 旧说明把币种字段写作“汇率”；币种代码与换算比率应分别确认，不直接用该列作除数。

## 2. 核心作用
本表主要用于以下场景：
- 计算每日收入、首次订阅收入、点数包收入、续订收入使用
- 分析收入的国家分布

## 6. 数据质量与风险提示
-此表有重复数据，因此在分析计算前以transaction_Id为基础，进行去重处理
- Fashion 收入需限定 `app_name = 'collart_web' AND revneue > 0`，再按 `user_id` 关联 Fashion succeed 用户；不能直接使用 Web 全站收入。
- 当前 Fashion 订单入口为 `aidata2025.ads_collartfashion.ads_oper_user_revenue_di`；旧用户日表已于 2026-09-09 停写。交易按前后 600 秒最近支付成功事件确定场景，见收入定义。

## 加工依据与关联关系

- 加工源码：`dataform:pubdata/definitions/dwd/revenue/h_dwd_cdct_revenue_stripe_di.sqlx`；仓库 `pubdata`，路径 `definitions/dwd/revenue/h_dwd_cdct_revenue_stripe_di.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.815295+00:00`。同一 SQLX 的产出：`pubdata2025.dwd.dwd_cdct_revenue_stripe_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
LEFT JOIN `pubdata2025.dim.dim_payinsider_product_price` AS b
ON a.event_date = b.event_date
AND a.app_name = b.app_name
AND a.product_id = b.product_id
AND a.currency = b.currency
WHERE a.event_date BETWEEN from_date AND to_date
AND a.transaction_status = 'Approved'
AND a.response_code = 'Success'
LEFT JOIN (
ON a.subscription_id = b.subscription_id
LEFT JOIN `pubdata2025.dim.dim_stripe_product_info_df` AS c
ON a.product_id = c.product_id
AND a.type IN ('charge', 'payment')
WHERE acquirer = 'Payssion'
LEFT JOIN product_tab AS b
ON a.payment_intent_id = b.gateway_id
group by all
LEFT JOIN `aidata2025.dim.exchange_rate_days` AS c
on a.event_date = date(c.stats_date)
and a.currency = c.currency
WHERE a.acquirer = 'Payssion'
LEFT JOIN `aidata2025.dim.exchange_rate_days` AS b
ON DATE(a.updated_at) = DATE(b.stats_date)
WHERE a.payment_channel = 'enjoypay'
AND a.status = 'paid'
and DATE(a.updated_at) between from_date and to_date
```
- 物理上游：`aidata2025.dim.exchange_rate_days`
- 物理上游：`aidata2025.ods.orders`
- 物理上游：`pubdata2025.dim.dim_payinsider_product_price`
- 物理上游：`pubdata2025.dim.dim_stripe_product_info_df`
- 物理上游：`pubdata2025.ods.ods_payinsider_order_report_1d`
- 物理上游：`pubdata2025.ods.ods_stripe_balance_transactions_1d`
- 物理上游：`pubdata2025.ods.ods_stripe_subscriptions_1d`
