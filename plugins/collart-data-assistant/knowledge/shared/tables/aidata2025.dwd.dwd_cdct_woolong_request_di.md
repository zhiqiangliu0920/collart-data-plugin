---
id: "table:aidata2025.dwd.dwd_cdct_woolong_request_di"
title: "aidata2025.dwd.dwd_cdct_woolong_request_di · woolong表"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dwd.dwd_cdct_woolong_request_di.md", "dataform:aidata/definitions/dwd/daily/h_dwd_cdct_woolong_request_di.sqlx", "feishu:aidata2025.dwd.dwd_cdct_woolong_request_di", "schema:aidata2025.dwd.dwd_cdct_woolong_request_di"]
tags: ["dwd_cdct_woolong_request_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.dwd.dwd_cdct_woolong_request_di"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.dwd.dwd_cdct_woolong_request_di · woolong表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dwd.dwd_cdct_woolong_request_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "logged_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `logged_at` | TIMESTAMP | REQUIRED | 登录时间 | 飞书 |
| `owner_id` | STRING | REQUIRED | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `event_type` | STRING | REQUIRED | 事件属性字段，用于标识行为名称、事件分类或事件补充信息。 | 飞书 |
| `package_name` | STRING | REQUIRED | 包名 | 飞书 |
| `transaction_id` | STRING | REQUIRED | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `purchase_time` | DATETIME | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `cancellation_time` | DATETIME | NULLABLE | 取消时间 | 飞书 |
| `change_renewal_time` | DATETIME | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `auto_renew_product_id` | STRING | REQUIRED | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `original_transaction_id` | STRING | REQUIRED | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `is_trial_period` | BOOLEAN | REQUIRED | 布尔标记字段，用于表示是/否状态。 | 飞书 |
| `is_in_intro_offer_period` | BOOLEAN | REQUIRED | 布尔标记字段，用于表示是/否状态。 | 飞书 |
| `cancellation_date_ms` | INTEGER | REQUIRED | 整型指标字段，用于统计数量、金额或次数。 | 飞书 |
| `price_amount_micros` | INTEGER | REQUIRED | 价格字段，用于记录商品、服务或订阅价格。 | 飞书 |
| `price_currency_code` | STRING | REQUIRED | 价格字段，用于记录商品、服务或订阅价格。 | 飞书 |
| `campaign` | STRING | REQUIRED | 投放campaign id | 飞书 |
| `install_time` | DATETIME | NULLABLE | 安装时间 | 飞书 |
| `gclid` | STRING | REQUIRED | 一种用户的身份id | 飞书 |
| `logged_date` | DATE | NULLABLE | 登录日期 | 飞书 |
| `event_name` | STRING | NULLABLE | 事件名/事件英文名 | 飞书 |

## 定义差异与补充

- purchase_time: 飞书 类型 timestamp；schema 类型 DATETIME
- purchase_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- cancellation_time: 飞书 类型 timestamp；schema 类型 DATETIME
- cancellation_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- change_renewal_time: 飞书 类型 timestamp；schema 类型 DATETIME
- change_renewal_time: 旧文档 类型 timestamp；schema 类型 DATETIME
- install_time: 飞书 类型 timestamp；schema 类型 DATETIME
- install_time: 旧文档 类型 timestamp；schema 类型 DATETIME

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 是 |
| 数据来源 | 服务端 |
| 数据表地址 | - |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dwd/daily/h_dwd_cdct_woolong_request_di.sqlx`；仓库 `aidata`，路径 `definitions/dwd/daily/h_dwd_cdct_woolong_request_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:54.401159+00:00`。同一 SQLX 的产出：`aidata2025.dwd.dwd_cdct_woolong_request_di`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND to_date;
AND FORMAT_DATE('%Y%m%d', to_date)
AND transaction_id <> '0'
AND transaction_id <> '0' )) a;
```
- 物理上游：`fx-editor.analytics_263446298.woolong_events_*`
- 物理上游：`removeobjects-17cd7.analytics_348205064.woolong_events_*`
- 物理上游：`storytemplate-10a27.analytics_232977577.woolong_events_*`
