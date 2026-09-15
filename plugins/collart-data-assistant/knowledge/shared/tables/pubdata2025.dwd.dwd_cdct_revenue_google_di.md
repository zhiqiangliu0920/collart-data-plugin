---
id: "table:pubdata2025.dwd.dwd_cdct_revenue_google_di"
title: "pubdata2025.dwd.dwd_cdct_revenue_google_di · google商店订单明细"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.dwd.dwd_cdct_revenue_google_di.md", "dataform:pubdata/definitions/dwd/revenue/h_dwd_cdct_revenue_google_di.sqlx", "feishu:pubdata2025.dwd.dwd_cdct_revenue_google_di", "schema:pubdata2025.dwd.dwd_cdct_revenue_google_di"]
tags: ["dwd_cdct_revenue_google_di", "字段", "schema", "SQLX"]
tables: ["pubdata2025.dwd.dwd_cdct_revenue_google_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.dwd.dwd_cdct_revenue_google_di · google商店订单明细

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.dwd.dwd_cdct_revenue_google_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "Order_Charged_Date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `stats_mon` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `Product_ID` | STRING | NULLABLE | 未说明 | 缺口 |
| `Order_Number` | STRING | NULLABLE | 未说明 | 缺口 |
| `Order_Charged_Date` | DATE | NULLABLE | 未说明 | 缺口 |
| `Product_Title` | STRING | NULLABLE | 未说明 | 缺口 |
| `Product_Type` | STRING | NULLABLE | 未说明 | 缺口 |
| `Country_of_Buyer` | STRING | NULLABLE | 未说明 | 缺口 |
| `Currency_of_Sale` | STRING | NULLABLE | 未说明 | 缺口 |
| `Financial_Status` | STRING | NULLABLE | 未说明 | 缺口 |
| `Item_Price` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `Charged_Amount` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `Taxes_Collected` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `SKU_ID` | STRING | NULLABLE | 未说明 | 缺口 |
| `google_fee_rate` | FLOAT | NULLABLE | 比率指标字段，用于表示转化率、留存率或占比。 | 飞书 |
| `rate` | FLOAT | NULLABLE | 比率指标字段，用于表示转化率、留存率或占比。 | 飞书 |
| `Charged_Amount_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `Taxes_Collected_usd` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `Revenue_Without_VAT` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `Google_Fee` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `Revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `expiration_date` | DATE | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `region` | STRING | NULLABLE | 地区：hz或gz | schema |
| `Base_Plan_ID` | STRING | NULLABLE | 未说明 | 缺口 |
| `Order_Charged_Timestamp` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `base_plan_id` | string | 用于唯一标识记录或业务实体的关键字段。 |
| `charged_amount` | float | 商品交易金额 |
| `charged_amount_usd` | float | 商品交易金额（美元） |
| `country_of_buyer` | string | 付费用户的国家 |
| `currency_of_sale` | string | 汇率 |
| `financial_status` | string | 交易状态 |
| `google_fee` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `item_price` | float | 商品价格 |
| `order_charged_date` | date | 用于记录事件发生、数据生成或分区时间的时间字段。 |
| `order_charged_timestamp` | int | 用于记录事件发生、数据生成或分区时间的时间字段。 |
| `order_number` | string | 文本属性字段，用于补充业务描述、分类或标签信息。 |
| `product_id` | string | 用于唯一标识记录或业务实体的关键字段。 |
| `product_title` | string | 商品名称 |
| `product_type` | string | 商品类型 |
| `revenue` | float | 订阅收入 |
| `revenue_without_vat` | float | 税前订阅收入 |
| `sku_id` | string | 商品skuid |
| `taxes_collected` | float | 税收金额 |
| `taxes_collected_usd` | float | 浮点型指标字段，用于统计金额、比率或均值。 |

## 定义差异与补充

- region: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- region: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.ods.ods_googleplay_sales_download2025_1d pubdata2025.ods.ods_googleplay_sales_downloader_1d pubdata2025.ods.ods_googleplay_sales_etm_1d pubdata2025.ods.ods_googleplay_sales_lifestyle_1d pubdata2025.ods.ods_googleplay_sales_new_downloader_1d |
| 是否需要展示血缘 | 是 |
| 数据来源 | 谷歌商店 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sdwd!3sdwd_cdct_revenue_google_di) |
| 任务地址 | dwd/revenue/h_dwd_cdct_revenue_google_di.sqlx |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:pubdata/definitions/dwd/revenue/h_dwd_cdct_revenue_google_di.sqlx`；仓库 `pubdata`，路径 `definitions/dwd/revenue/h_dwd_cdct_revenue_google_di.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.605718+00:00`。同一 SQLX 的产出：`pubdata2025.dwd.dwd_cdct_revenue_google_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
WHERE rate IS NOT NULL
AND to_date
LEFT JOIN (-- 用于关联25年的数据
ON SUBSTRING(CAST(Order_Charged_Date AS string),1,7)=b.stats_mon
AND a.Currency_of_Sale=b.currency
LEFT JOIN ( -- 计算每日新增的数据
ON a.Order_Charged_Date=b1.stats_date
AND a.Currency_of_Sale=b1.currency
LEFT JOIN latest_daily_rate b2 -- 如果当日分区没产出 用最新一天有数的分区
ON a.Currency_of_Sale = b2.currency
```

飞书登记上游（不保证当前依赖）：pubdata2025.ods.ods_googleplay_sales_download2025_1d<br>pubdata2025.ods.ods_googleplay_sales_downloader_1d<br>pubdata2025.ods.ods_googleplay_sales_etm_1d<br>pubdata2025.ods.ods_googleplay_sales_lifestyle_1d<br>pubdata2025.ods.ods_googleplay_sales_new_downloader_1d
- 物理上游：`gzdw2024.gz_dim.exchange_rate`
- 物理上游：`gzdw2024.gz_dim.exchange_rate_days`
- 物理上游：`pubdata2025.ods.ods_googleplay_sales_download2025_1d`
- 物理上游：`pubdata2025.ods.ods_googleplay_sales_downloader_1d`
- 物理上游：`pubdata2025.ods.ods_googleplay_sales_etm_1d`
- 物理上游：`pubdata2025.ods.ods_googleplay_sales_lifestyle_1d`
- 物理上游：`pubdata2025.ods.ods_googleplay_sales_new_downloader_1d`
- 物理上游：`pubdata2025.ods.ods_googleplay_sales_text_1d`
- 物理上游：`pubdata2025.ods.ods_googleplay_sales_vidma_1d`
