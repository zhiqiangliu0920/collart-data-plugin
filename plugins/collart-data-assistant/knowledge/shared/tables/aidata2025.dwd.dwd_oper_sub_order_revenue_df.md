---
id: "table:aidata2025.dwd.dwd_oper_sub_order_revenue_df"
title: "aidata2025.dwd.dwd_oper_sub_order_revenue_df · 安卓账单粒度 订阅收入表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_oper_sub_order_revenue_df.md", "dataform:aidata/definitions/dwd/daily/h_dwd_oper_sub_order_revenue_df.sqlx", "feishu:aidata2025.dwd.dwd_oper_sub_order_revenue_df", "schema:aidata2025.dwd.dwd_oper_sub_order_revenue_df"]
tags: ["dwd_oper_sub_order_revenue_df", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_oper_sub_order_revenue_df"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_oper_sub_order_revenue_df · 安卓账单粒度 订阅收入表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_oper_sub_order_revenue_df` |
| 粒度 | 每个订单一行 |
| 主键/去重键 | order_id；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "order_date"} |
| 聚簇 | package_name, product_type, country, user_pseudo_id |
| 更新 | T+1 8:30；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `order_date` | DATE | NULLABLE | 订阅日期 | schema |
| `event_date` | DATE | NULLABLE | 埋点日期 | schema |
| `user_pseudo_id` | STRING | NULLABLE | 用户ID | schema |
| `package_name` | STRING | NULLABLE | 包名称 | schema |
| `app_name` | STRING | NULLABLE | app名称 | schema |
| `order_id` | STRING | NULLABLE | 订单ID | schema |
| `product_title` | STRING | NULLABLE | 订阅产品类型 | schema |
| `product_type` | STRING | NULLABLE | 产品类型 | schema |
| `country` | STRING | NULLABLE | 国家 | schema |
| `financial_status` | STRING | NULLABLE | 交易状态 | schema |
| `subscribe_type` | STRING | NULLABLE | 订阅类型 | schema |
| `item_price` | FLOAT | NULLABLE | 产品价格 | schema |
| `charged_amount` | FLOAT | NULLABLE | 交易金额 | schema |
| `taxes_collected` | FLOAT | NULLABLE | 税收金额 | schema |
| `sku_id` | STRING | NULLABLE | 产品ID | schema |
| `google_fee_rate` | FLOAT | NULLABLE | Google 收费比率 | schema |
| `rate` | FLOAT | NULLABLE | 汇率 | schema |
| `charged_amount_usd` | FLOAT | NULLABLE | 汇率计算后的交易金额 | schema |
| `taxes_collected_usd` | FLOAT | NULLABLE | 汇率计算后的税收金额 | schema |
| `revenue_without_VAT` | FLOAT | NULLABLE | 税后收入 | schema |
| `google_fee` | FLOAT | NULLABLE | 税后 Google 收费金额 | schema |
| `revenue` | FLOAT | NULLABLE | 最终收入 | schema |
| `order_type` | STRING | NULLABLE | 购买产品类型(年/月/日/点数包） | schema |
| `original_transaction_id` | STRING | NULLABLE | 原始订单号 | schema |
| `order_num` | INTEGER | NULLABLE | 续订单数(第几次续订） | schema |
| `traffic_src_type` | STRING | NULLABLE | 用户流量渠道 | schema |
| `user_id` | STRING | NULLABLE | 用户id(woolong) | schema |
| `expires_date` | DATE | NULLABLE | 到期日期 | schema |
| `subscribe_status` | STRING | NULLABLE | 订阅状态（到期续订、到期未续订、未到期、一次性购买) | schema |
| `adjust_id` | STRING | NULLABLE | adjust平台对应id | schema |
| `login_user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |

## 定义差异与补充

- order_date: 飞书补充解释：订单发生日期
- order_date: 旧文档补充解释：订单发生日期
- event_date: 飞书补充解释：日期
- event_date: 旧文档补充解释：日期
- user_pseudo_id: 飞书补充解释：用户id，firebase分配的唯一id
- user_pseudo_id: 旧文档补充解释：用户id，firebase分配的唯一id
- package_name: 飞书补充解释：包名
- package_name: 旧文档补充解释：包名
- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- order_id: 飞书补充解释：订单id
- order_id: 旧文档补充解释：订单id
- product_title: 飞书补充解释：商品名称
- product_title: 旧文档补充解释：商品名称
- product_type: 飞书补充解释：商品类型
- product_type: 旧文档补充解释：商品类型
- item_price: 飞书补充解释：商品价格
- item_price: 旧文档补充解释：商品价格
- charged_amount: 飞书补充解释：商品交易金额
- charged_amount: 旧文档补充解释：商品交易金额
- taxes_collected: 飞书补充解释：商品税收金额
- taxes_collected: 旧文档补充解释：商品税收金额
- sku_id: 飞书补充解释：商品SKUid
- sku_id: 旧文档补充解释：商品SKUid
- google_fee_rate: 飞书补充解释：google 收税比率
- google_fee_rate: 旧文档补充解释：google 收税比率
- rate: 飞书补充解释：货币汇率
- rate: 旧文档补充解释：货币汇率
- charged_amount_usd: 飞书补充解释：商品交易金额（美元）
- charged_amount_usd: 旧文档补充解释：商品交易金额（美元）
- revenue_without_VAT: 飞书补充解释：税前订阅收入
- revenue_without_VAT: 旧文档补充解释：税前订阅收入
- google_fee: 飞书补充解释：税后google 收费金额
- google_fee: 旧文档补充解释：税后google 收费金额
- revenue: 飞书补充解释：订阅收入
- revenue: 旧文档补充解释：订阅收入
- traffic_src_type: 飞书补充解释：投放渠道类型
- traffic_src_type: 旧文档补充解释：投放渠道类型
- user_id: 飞书补充解释：用户id，内部平台分配的唯一id
- user_id: 旧文档补充解释：用户id，内部平台分配的唯一id
- expires_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- expires_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- adjust_id: 飞书补充解释：adjust id
- adjust_id: 旧文档补充解释：adjust id

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.dwd.dwd_cdct_revenue_google_di,aidata2025.dwd.dwd_oper_user_order_event_di,pubdata2025.ods.ods_woolong_subscription_1d |
| 是否需要展示血缘 | 是 |
| 数据来源 | 谷歌商店 / 服务端 / 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdwd!3sdwd_oper_sub_order_revenue_df) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdwd%2Fdaily%2Fh_dwd_oper_sub_order_revenue_df.sqlx?project=aidata2025) |
| 看板 | 用于查询订单粒度、用户粒度收入数据 |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_oper_sub_order_revenue_df.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_oper_sub_order_revenue_df.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:54.569357+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_oper_sub_order_revenue_df`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
declare from_date date default ${dataform.projectConfig.vars.biz_date}-30;
declare to_date date default ${dataform.projectConfig.vars.biz_date}+1;
where Order_Charged_Date between from_date and to_date
WHERE `date` between from_date and to_date
and `date` is not null
where event_date >= from_date-60
and advertising_id is not null
and advertising_id != '__REDACTED_ID__'
where activity_kind = 'install'
group by all
group by original_transaction_id
order by CASE WHEN financial_status='Charged' THEN 0 ELSE 1 END,order_num,order_number) as rk,
left join woolong_original w
on sub_tab.original_transaction_id = w.original_transaction_id
left join user_tab u1
on a.original_transaction_id = u1.event_order_id
and a.package_name = u1.package_name
left join user_tab2 u2
on a.advertising_id  = u2.advertising_id
and a.package_name = u2.package_name
and a.advertising_id != '__REDACTED_ID__'
and u2.advertising_id != '__REDACTED_ID__'
left join dim.dim_product_info d
on a.package_name = d.package_name
left join adjust_tab e
on coalesce(u1.package_name,u2.package_name) = e.package_name
and coalesce(u1.adjust_id,u2.adjust_id) = e.adid
WHERE a.user_id = b.guest_uid
AND a.app_name = 'collart_android'
AND b.user_id IS NOT NULL;
```

飞书登记上游（不保证当前依赖）：pubdata2025.dwd.dwd_cdct_revenue_google_di,aidata2025.dwd.dwd_oper_user_order_event_di,pubdata2025.ods.ods_woolong_subscription_1d
- 物理上游：`aidata2025.ods.au_guest_binding`
- 物理上游：`pubdata2025.dwd.dwd_cdct_revenue_google_adjust_di`
- 物理上游：`pubdata2025.dwd.dwd_cdct_revenue_google_di`
- 物理上游：`pubdata2025.ods.ods_woolong_subscription_1d`
