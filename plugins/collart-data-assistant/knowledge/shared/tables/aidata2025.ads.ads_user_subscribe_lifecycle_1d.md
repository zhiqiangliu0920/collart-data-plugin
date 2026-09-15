---
id: "table:aidata2025.ads.ads_user_subscribe_lifecycle_1d"
title: "aidata2025.ads.ads_user_subscribe_lifecycle_1d · 安卓侧续订率计算表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ads.ads_user_subscribe_lifecycle_1d.md", "feishu:aidata2025.ads.ads_user_subscribe_lifecycle_1d", "schema:aidata2025.ads.ads_user_subscribe_lifecycle_1d"]
tags: ["ads_user_subscribe_lifecycle_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_user_subscribe_lifecycle_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_user_subscribe_lifecycle_1d · 安卓侧续订率计算表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_user_subscribe_lifecycle_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 日期+包名+国家+商品+渠道；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "original_start_date"} |
| 聚簇 | package_name, product_type, country |
| 更新 | T+1 8:30；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `original_start_date` | DATE | NULLABLE | 首订日期 | schema |
| `package_name` | STRING | NULLABLE | 包名 | schema |
| `sku_id` | STRING | NULLABLE | SKU ID | schema |
| `product_type` | STRING | NULLABLE | 产品类型 | schema |
| `country` | STRING | NULLABLE | 国家代码 | schema |
| `country_name` | STRING | NULLABLE | 国家名称 | schema |
| `traffic_src_type` | STRING | NULLABLE | 流量来源类型 | schema |
| `subscribe_num` | INTEGER | NULLABLE | 首订数量 | schema |
| `renew_order_count1` | INTEGER | NULLABLE | 续订次数 1 | schema |
| `renew_order_count2` | INTEGER | NULLABLE | 续订次数 2 | schema |
| `renew_order_count3` | INTEGER | NULLABLE | 续订次数 3 | schema |
| `renew_order_count4` | INTEGER | NULLABLE | 续订次数 4 | schema |
| `renew_order_count5` | INTEGER | NULLABLE | 续订次数 5 | schema |
| `renew_order_count6` | INTEGER | NULLABLE | 续订次数 6 | schema |
| `renew_order_count7` | INTEGER | NULLABLE | 续订次数 7 | schema |
| `renew_order_count8` | INTEGER | NULLABLE | 续订次数 8 | schema |
| `renew_order_count9` | INTEGER | NULLABLE | 续订次数 9 | schema |
| `renew_order_count10` | INTEGER | NULLABLE | 续订次数 10 | schema |
| `renew_order_count11` | INTEGER | NULLABLE | 续订次数 11 | schema |
| `renew_order_count12` | INTEGER | NULLABLE | 续订次数 12 | schema |
| `is_new` | BOOLEAN | NULLABLE | 是否新客 | schema |
| `app_version` | STRING | NULLABLE | 版本 | schema |

## 定义差异与补充

- original_start_date: 飞书补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- original_start_date: 旧文档补充解释：用于记录事件发生、数据生成或分区时间的时间字段。
- sku_id: 飞书补充解释：用于唯一标识记录或业务实体的关键字段。
- sku_id: 旧文档补充解释：用于唯一标识记录或业务实体的关键字段。
- product_type: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- product_type: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- country: 飞书补充解释：国家
- country: 旧文档补充解释：国家
- country_name: 飞书补充解释：国家
- country_name: 旧文档补充解释：国家
- traffic_src_type: 飞书补充解释：投放渠道类型
- traffic_src_type: 旧文档补充解释：投放渠道类型
- subscribe_num: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- subscribe_num: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count1: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count1: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count2: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count2: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count3: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count3: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count4: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count4: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count5: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count5: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count6: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count6: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count7: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count7: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count8: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count8: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count9: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count9: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count10: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count10: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count11: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count11: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count12: 飞书补充解释：计数指标字段，用于统计人数、次数或记录量。
- renew_order_count12: 旧文档补充解释：计数指标字段，用于统计人数、次数或记录量。
- is_new: 飞书补充解释：是否新老用户，true代表新用户、false代表老用户
- is_new: 旧文档补充解释：是否新老用户，true代表新用户、false代表老用户
- app_version: 飞书补充解释：app客户端版本号
- app_version: 旧文档补充解释：app客户端版本号

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.dwd.dwd_oper_sub_order_revenue_df |
| 是否需要展示血缘 | 是 |
| 数据来源 | 苹果商店 / 谷歌商店 / 服务端 / 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_user_subscribe_lifecycle_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Frevenue%2Fads_user_subscribe_lifecycle_1d.sqlx?project=aidata2025) |
| 看板 | 计算续订率用 |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：aidata2025.dwd.dwd_oper_sub_order_revenue_df
