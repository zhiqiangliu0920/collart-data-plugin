---
id: "table:aidata2025.dwd.dwd_oper_user_transaction_di"
title: "aidata2025.dwd.dwd_oper_user_transaction_di · iOS账单粒度 账单表（原始表）"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_oper_user_transaction_di.md", "feishu:aidata2025.dwd.dwd_oper_user_transaction_di", "schema:aidata2025.dwd.dwd_oper_user_transaction_di"]
tags: ["dwd_oper_user_transaction_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_oper_user_transaction_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_oper_user_transaction_di · iOS账单粒度 账单表（原始表）

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_oper_user_transaction_di` |
| 粒度 | 每个账单id一行 |
| 主键/去重键 | transactionid；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | bundleId, productId, storefront |
| 更新 | 每小时刷新；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 订阅日期（分区字段） | schema |
| `transactionId` | STRING | NULLABLE | 交易唯一标识符 | schema |
| `originalTransactionId` | STRING | NULLABLE | 原始交易ID | schema |
| `webOrderLineItemId` | STRING | NULLABLE | 网页订单行项目ID | schema |
| `bundleId` | STRING | NULLABLE | 应用包标识符 | schema |
| `productId` | STRING | NULLABLE | 产品ID | schema |
| `subscriptionGroupIdentifier` | STRING | NULLABLE | 订阅组标识符 | schema |
| `purchaseDate` | TIMESTAMP | NULLABLE | 购买时间戳(毫秒) | schema |
| `originalPurchaseDate` | TIMESTAMP | NULLABLE | 原始购买时间戳(毫秒) | schema |
| `expiresDate` | TIMESTAMP | NULLABLE | 订阅过期时间戳(毫秒) | schema |
| `quantity` | INTEGER | NULLABLE | 购买数量 | schema |
| `type` | STRING | NULLABLE | 交易类型(Auto-Renewable Subscription/Consumable) | schema |
| `user_id` | STRING | NULLABLE | 应用账户令牌(UUID格式) | schema |
| `inAppOwnershipType` | STRING | NULLABLE | 应用内购买所有权类型 | schema |
| `signedDate` | TIMESTAMP | NULLABLE | 数据签名时间戳 | schema |
| `offerType` | INTEGER | NULLABLE | 优惠类型标识 | schema |
| `environment` | STRING | NULLABLE | 环境类型(Production/Sandbox) | schema |
| `transactionReason` | STRING | NULLABLE | 交易原因 | schema |
| `storefront` | STRING | NULLABLE | 商店区域代码 | schema |
| `storefrontId` | STRING | NULLABLE | 商店区域数字代码 | schema |
| `price` | FLOAT | NULLABLE | 交易价格 | schema |
| `currency` | STRING | NULLABLE | 货币类型(ISO代码) | schema |
| `offerDiscountType` | STRING | NULLABLE | 优惠折扣类型 | schema |
| `appTransactionId` | STRING | NULLABLE | 应用交易ID | schema |
| `offerPeriod` | STRING | NULLABLE | 优惠期限(如P24D表示24天) | schema |
| `revocationDate` | TIMESTAMP | NULLABLE | 撤销时间 | schema |
| `revocationReason` | STRING | NULLABLE | 撤销原因 | schema |
| `event_type` | STRING | NULLABLE | 推理出的事件类型 | schema |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- transactionId: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- transactionId: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- originalTransactionId: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- originalTransactionId: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- webOrderLineItemId: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- webOrderLineItemId: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- bundleId: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- bundleId: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- productId: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- productId: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- subscriptionGroupIdentifier: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- subscriptionGroupIdentifier: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- purchaseDate: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- purchaseDate: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- originalPurchaseDate: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- originalPurchaseDate: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- expiresDate: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- expiresDate: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- quantity: 飞书补充解释：整型指标字段，用于统计数量、金额或次数。
- quantity: 旧文档补充解释：整型指标字段，用于统计数量、金额或次数。
- type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- user_id: 飞书补充解释：用户id，内部平台分配的唯一id
- user_id: 旧文档补充解释：用户id，内部平台分配的唯一id
- inAppOwnershipType: 飞书补充解释：应用或产品相关属性字段，用于产品识别、分类或归属分析。
- inAppOwnershipType: 旧文档补充解释：应用或产品相关属性字段，用于产品识别、分类或归属分析。
- signedDate: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- signedDate: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- offerType: 飞书补充解释：整型指标字段，用于统计数量、金额或次数。
- offerType: 旧文档补充解释：整型指标字段，用于统计数量、金额或次数。
- environment: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- environment: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- transactionReason: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- transactionReason: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- storefront: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- storefront: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- storefrontId: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- storefrontId: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- price: 飞书补充解释：价格字段，用于记录商品、服务或订阅价格。
- price: 旧文档补充解释：价格字段，用于记录商品、服务或订阅价格。
- currency: 飞书补充解释：汇率
- currency: 旧文档补充解释：汇率
- offerDiscountType: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- offerDiscountType: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- appTransactionId: 飞书补充解释：应用或产品相关属性字段，用于产品识别、分类或归属分析。
- appTransactionId: 旧文档补充解释：应用或产品相关属性字段，用于产品识别、分类或归属分析。
- offerPeriod: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- offerPeriod: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- revocationDate: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- revocationDate: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- revocationReason: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- revocationReason: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- event_type: 飞书补充解释：事件属性字段，用于标识行为名称、事件分类或事件补充信息。
- event_type: 旧文档补充解释：事件属性字段，用于标识行为名称、事件分类或事件补充信息。

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.ods.ods_apple_transaction_1d |
| 是否需要展示血缘 | 否 |
| 数据来源 | 苹果商店 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m10!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_delivery_adjust_user_di!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_user_transaction_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdwd%2Fdaily%2Fh_dwd_oper_user_transaction_di.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。
- 旧说明把币种字段写作“汇率”；币种代码与换算比率应分别确认，不直接用该列作除数。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：aidata2025.ods.ods_apple_transaction_1d
