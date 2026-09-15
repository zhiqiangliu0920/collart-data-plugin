---
id: "table:aidata2025.ads.ads_user_subscribe_daily_1d"
title: "aidata2025.ads.ads_user_subscribe_daily_1d · 分产品分国家分渠道分商品订阅收入"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ads.ads_user_subscribe_daily_1d.md", "feishu:aidata2025.ads.ads_user_subscribe_daily_1d", "schema:aidata2025.ads.ads_user_subscribe_daily_1d"]
tags: ["ads_user_subscribe_daily_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_user_subscribe_daily_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_user_subscribe_daily_1d · 分产品分国家分渠道分商品订阅收入

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_user_subscribe_daily_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 日期+包名+国家+商品+渠道；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "order_date"} |
| 聚簇 | package_name, country, product_type |
| 更新 | T+1 8:30；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `order_date` | DATE | NULLABLE | 订单日期 | schema |
| `package_name` | STRING | NULLABLE | 包名 | schema |
| `country` | STRING | NULLABLE | 国家代码 | schema |
| `country_name` | STRING | NULLABLE | 国家名称 | schema |
| `sku_id` | STRING | NULLABLE | SKU ID | schema |
| `product_type` | STRING | NULLABLE | 产品类型 | schema |
| `traffic_src_type` | STRING | NULLABLE | 流量来源类型 | schema |
| `charged_money` | FLOAT | NULLABLE | 已支付金额 | schema |
| `refunded_money` | FLOAT | NULLABLE | 退款金额 | schema |
| `vip_revenue` | FLOAT | NULLABLE | 订阅总收入 | schema |
| `order_num` | INTEGER | NULLABLE | 订单数量 | schema |
| `renew_order_num` | INTEGER | NULLABLE | 续订订单数量 | schema |
| `new_order_num` | INTEGER | NULLABLE | 首订订单数量 | schema |
| `renew_user_num` | INTEGER | NULLABLE | 续订用户数量 | schema |
| `new_user_num` | INTEGER | NULLABLE | 首订用户数量 | schema |
| `renew_vip_revenue` | FLOAT | NULLABLE | 续订收入 | schema |
| `new_vip_revenue` | FLOAT | NULLABLE | 首订收入 | schema |
| `first_order_num` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `trial_conver_order_num` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `first_user_num` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `trial_conver_user_num` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `first_vip_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `trial_conver_vip_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |

## 定义差异与补充

- order_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- order_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- country: 飞书补充解释：国家
- country: 旧文档补充解释：国家
- country_name: 飞书补充解释：国家
- country_name: 旧文档补充解释：国家
- sku_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- sku_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- product_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- product_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- traffic_src_type: 飞书补充解释：投放渠道类型
- traffic_src_type: 旧文档补充解释：投放渠道类型
- charged_money: 飞书补充解释：商品交易金额（美元）
- charged_money: 旧文档补充解释：商品交易金额（美元）
- refunded_money: 飞书补充解释：浮点型指标字段，用于统计金额、比率或均值。
- refunded_money: 旧文档补充解释：浮点型指标字段，用于统计金额、比率或均值。
- vip_revenue: 飞书补充解释：订阅收入
- vip_revenue: 旧文档补充解释：订阅收入
- order_num: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- order_num: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_num: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_num: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- new_order_num: 飞书补充解释：首次订阅订单数
- new_order_num: 旧文档补充解释：首次订阅订单数
- renew_user_num: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_user_num: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- new_user_num: 飞书补充解释：新增用户数
- new_user_num: 旧文档补充解释：新增用户数
- new_vip_revenue: 飞书补充解释：首次订阅收入
- new_vip_revenue: 旧文档补充解释：首次订阅收入

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_sub_order_revenue_df |
| 是否需要展示血缘 | 是 |
| 数据来源 | 苹果商店 / 谷歌商店 / 服务端 / 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_user_subscribe_daily_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Frevenue%2Fads_user_subscribe_daily_1d.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_oper_sub_order_revenue_df
