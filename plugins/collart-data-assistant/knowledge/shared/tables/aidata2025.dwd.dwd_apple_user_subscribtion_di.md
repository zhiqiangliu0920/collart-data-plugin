---
id: "table:aidata2025.dwd.dwd_apple_user_subscribtion_di"
title: "aidata2025.dwd.dwd_apple_user_subscribtion_di · iOS账单粒度 账单表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_apple_user_subscribtion_di.md", "dataform:aidata/definitions/dwd/daily/h_dwd_apple_user_subscribtion_di.sqlx", "feishu:aidata2025.dwd.dwd_apple_user_subscribtion_di", "schema:aidata2025.dwd.dwd_apple_user_subscribtion_di"]
tags: ["dwd_apple_user_subscribtion_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_apple_user_subscribtion_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_apple_user_subscribtion_di · iOS账单粒度 账单表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_apple_user_subscribtion_di` |
| 粒度 | 每个账单id一行 |
| 主键/去重键 | transaction_id；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | package_name, sku, storefront |
| 更新 | T+1  12:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 订阅日期（分区字段） | schema |
| `transaction_id` | STRING | NULLABLE | 交易唯一标识符 | schema |
| `package_name` | STRING | NULLABLE | 应用包名 | schema |
| `user_id` | STRING | NULLABLE | 用户ID | schema |
| `user_pseudo_id` | STRING | NULLABLE | firebase用户ID | schema |
| `sku` | STRING | NULLABLE | 商品SKU | schema |
| `purchase_date` | DATETIME | NULLABLE | 购买时间 | schema |
| `original_purchase_date` | DATETIME | NULLABLE | 原始购买时间 | schema |
| `expires_date` | DATETIME | NULLABLE | 订阅过期时间 | schema |
| `quantity` | INTEGER | NULLABLE | 购买数量 | schema |
| `sub_type` | STRING | NULLABLE | 订阅类型(是否自动续订） | schema |
| `transaction_type` | STRING | NULLABLE | 交易类型(RENEWAL/PURCHASE) | schema |
| `storefront` | STRING | NULLABLE | 商店区域代码 | schema |
| `country_code` | STRING | NULLABLE | 国家/地区代码 | schema |
| `country_name` | STRING | NULLABLE | 国家/地区名称 | schema |
| `price` | FLOAT | NULLABLE | 交易价格 | schema |
| `currency` | STRING | NULLABLE | 货币类型 | schema |
| `revenue_apple` | FLOAT | NULLABLE | Apple 收入 | schema |
| `login_user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `aidata2025.dwd.dwd_apple_user_subscribtion_di` | exists | 2026-09-13T09:53:37.982288+00:00 |

## 定义差异与补充

- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- transaction_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- transaction_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- package_name: 飞书补充解释：包名
- package_name: 旧文档补充解释：包名
- user_id: 飞书补充解释：用户id，内部平台分配的唯一id
- user_id: 旧文档补充解释：用户id，内部平台分配的唯一id
- user_pseudo_id: 飞书补充解释：用户id，firebase分配的唯一id
- user_pseudo_id: 旧文档补充解释：用户id，firebase分配的唯一id
- sku: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- sku: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- purchase_date: 飞书 类型 timestamp；schema 类型 DATETIME
- purchase_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- purchase_date: 旧文档 类型 timestamp；schema 类型 DATETIME
- purchase_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- original_purchase_date: 飞书 类型 timestamp；schema 类型 DATETIME
- original_purchase_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- original_purchase_date: 旧文档 类型 timestamp；schema 类型 DATETIME
- original_purchase_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- expires_date: 飞书 类型 timestamp；schema 类型 DATETIME
- expires_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- expires_date: 旧文档 类型 timestamp；schema 类型 DATETIME
- expires_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- quantity: 飞书补充解释：整型指标字段，用于统计数量、金额或次数。
- quantity: 旧文档补充解释：整型指标字段，用于统计数量、金额或次数。
- sub_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- sub_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- transaction_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- transaction_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- storefront: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- storefront: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- country_code: 飞书补充解释：国家代码
- country_code: 旧文档补充解释：国家代码
- country_name: 飞书补充解释：国家
- country_name: 旧文档补充解释：国家
- price: 飞书补充解释：价格字段，用于记录商品、服务或订阅价格。
- price: 旧文档补充解释：价格字段，用于记录商品、服务或订阅价格。
- currency: 飞书补充解释：汇率
- currency: 旧文档补充解释：汇率
- revenue_apple: 飞书补充解释：订阅收入
- revenue_apple: 旧文档补充解释：订阅收入

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.ods.ods_apple_sales_1d,aidata2025.dwd.dwd_oper_user_event_di,aidata2025.dwd.dwd_oper_user_basic_di,pubdata2025.ods.ods_woolong_subscription_1d,aidata2025.dwd.dwd_oper_user_transaction_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 苹果商店 / 服务端 / 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdwd!3sdwd_apple_user_subscribtion_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdwd%2Fdaily%2Fh_dwd_apple_user_subscribtion_di.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。
- 旧说明把币种字段写作“汇率”；币种代码与换算比率应分别确认，不直接用该列作除数。
- 2026-09-13 用户确认：这是苹果订阅表；原 Android 分类错误。作为公司共用苹果/iOS 订阅源维护，不限定为 VidArt 独占。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_apple_user_subscribtion_di.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_apple_user_subscribtion_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.792800+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_apple_user_subscribtion_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
AND revenue_usd <>0
AND units <>0
where event_date between from_date-30 and to_date
and lower(app_name) in ('looksart','vidart','vibedance_ios')
GROUP BY user_id
WHERE DATE(TIMESTAMP_MILLIS(CAST(ti_purchasedate AS INT64))) between from_date and to_date
AND rd_environment = 'Production'
AND notificationtype not IN (
AND a.sku = c.sku
AND a.package_name = c.package_name
on a.original_transaction_id = d.original_transaction_id
left join user_map
on a.user_id = user_map.user_id
left join dim.dim_product_info e
on a.package_name = e.package_name
WHERE a.user_id = b.guest_uid
AND lower(a.app_name) = 'vidart'
AND b.user_id IS NOT NULL;
```

飞书登记上游（不保证当前依赖）：pubdata2025.ods.ods_apple_sales_1d,aidata2025.dwd.dwd_oper_user_event_di,aidata2025.dwd.dwd_oper_user_basic_di,pubdata2025.ods.ods_woolong_subscription_1d,aidata2025.dwd.dwd_oper_user_transaction_di
- 物理上游：`aidata2025.ods.au_guest_binding`
- 物理上游：`aidata2025.ods.ods_apple_subscription_muselab_df`
- 物理上游：`aidata2025.ods.ods_apple_subscription_vibedance_df`
- 物理上游：`aidata2025.ods.ods_apple_subscription_vidart_df`
- 物理上游：`pubdata2025.ods.ods_woolong_subscription_1d`
