---
id: "table:aidata2025.ads_collartfashion.ads_oper_user_revenue_di"
title: "aidata2025.ads_collartfashion.ads_oper_user_revenue_di"
project: "collart_fashion"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_fashion/tables/aidata2025.ads_collartfashion.ads_oper_user_revenue_di.md", "dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_user_revenue_di.sqlx", "schema:aidata2025.ads_collartfashion.ads_oper_user_revenue_di"]
tags: ["ads_oper_user_revenue_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartfashion.ads_oper_user_revenue_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartfashion.ads_oper_user_revenue_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartfashion.ads_oper_user_revenue_di` |
| 粒度 | Stripe 订单，交易键去重（缺 ID 时源码使用降级键） |
| 主键/去重键 | transaction_id；缺失时 user_id + event_timestamp；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date", "requirePartitionFilter": true} |
| 聚簇 | user_id, transaction_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | Stripe 收入日期 | schema |
| `event_timestamp` | INTEGER | NULLABLE | Stripe 事件 unix 秒 | schema |
| `transaction_id` | STRING | NULLABLE | Stripe 交易 ID | schema |
| `app_name` | STRING | NULLABLE | Stripe app_name，Fashion 订单一般为 collart_web | schema |
| `charge_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `currency` | STRING | NULLABLE | 未说明 | 缺口 |
| `stripe_customer_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `amount` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `fee` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revneue` | FLOAT | NULLABLE | 实收美元，字段名与上游一致 | schema |
| `description_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `order_status` | STRING | NULLABLE | 未说明 | 缺口 |
| `product_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `product_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `subscription_status` | STRING | NULLABLE | 未说明 | 缺口 |
| `user_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `payment_channel` | STRING | NULLABLE | 未说明 | 缺口 |
| `package_name` | STRING | NULLABLE | Fashion 归属包名 collart_fashion | schema |
| `user_pseudo_id` | STRING | NULLABLE | 匹配支付成功事件的 GA4 用户 ID | schema |
| `first_fashion_succeed_date` | DATE | NULLABLE | 该 user_id 窗口内首次 Fashion 支付成功日 | schema |
| `succeed_date` | DATE | NULLABLE | 匹配到的 vip_subscribe_succeed 日期 | schema |
| `match_diff_seconds` | INTEGER | NULLABLE | Stripe 与支付成功事件的秒差绝对值 | schema |
| `etl_time` | TIMESTAMP | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

## 2. 核心作用
Fashion 付费订单明细。Stripe 字段原样同步，再用前后 10 分钟 `vip_subscribe_succeed` 判定是否归属 Fashion。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_fashion/ads_oper_user_revenue_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_fashion/ads_oper_user_revenue_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:50.958386+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartfashion.ads_oper_user_revenue_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - ${cfg.REVENUE_BACKFILL_DAYS};
DECLARE to_date   DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN DATE_SUB(from_date, INTERVAL 1 DAY) AND DATE_ADD(to_date, INTERVAL 1 DAY)
AND event_name = "vip_subscribe_succeed"
AND NULLIF(user_id, "") IS NOT NULL
AND user_id NOT IN (SELECT user_id FROM internal_users)
WHERE event_date BETWEEN from_date AND to_date
AND app_name = "collart_web"
AND revneue > 0
QUALIFY ROW_NUMBER() OVER (
PARTITION BY COALESCE(
ORDER BY event_timestamp DESC
JOIN payment_events AS e
ON s.user_id = e.user_id
AND ABS(TIMESTAMP_DIFF(e.succeed_time, TIMESTAMP_SECONDS(s.event_timestamp), SECOND)) <= 600
ORDER BY match_diff_seconds, e.succeed_time
WHERE package_name = "${cfg.PACKAGE_NAME}"
GROUP BY user_id
JOIN fashion_first_succeed AS f USING (user_id)
WHERE n.package_name = "${cfg.PACKAGE_NAME}";
```
- 物理上游：`aidata2025.dm.dm_collart_web_user_event_di`
- 物理上游：`pubdata2025.dwd.dwd_cdct_revenue_stripe_di`

### Fashion 当前源码的交易归属

Stripe app_name=collart_web 且 revneue>0；有效 user_id；交易 ID 缺失时按 user_id+event_timestamp 降级去重。对同 user_id 前后 600 秒的所有支付成功事件选最近一条，再筛 package_name=collart_fashion；不是先只筛 Fashion 再匹配。最近距离相同的事件须看 ORDER BY 的完整规则，未有唯一次序时需做歧义检查。内部名单用于事件侧，无法匹配事件的订单不会进入本表。来源为正额收入，不代表已抵扣所有退款。

Fashion 与 Web Stripe 总量存在交集；要计算整体收入，按交易集合并去重。不能把曾访问 Fashion 用户的全部终身交易都归 Fashion。
