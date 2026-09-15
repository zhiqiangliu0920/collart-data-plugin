---
id: "table:aidata2025.revenue.vip_event_data_ios"
title: "aidata2025.revenue.vip_event_data_ios · 苹果商店收入与订阅事件报告清洗"
project: "collart_ios"
kind: "table"
status: "historical"
sources: ["ai-knowledge:1company/tables/aidata2025.revenue.vip_event_data_ios.md", "feishu:aidata2025.revenue.vip_event_data_ios", "schema:aidata2025.revenue.vip_event_data_ios"]
tags: ["vip_event_data_ios", "字段", "schema", "SQLX"]
tables: ["aidata2025.revenue.vip_event_data_ios"]
review_required: true
applies_to: []
---

# aidata2025.revenue.vip_event_data_ios · 苹果商店收入与订阅事件报告清洗

## 使用边界

BigQuery 元数据返回 NOT_FOUND（2026-09-14）；可能为历史表/名称变化/不可见，不能作为默认当前入口。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.revenue.vip_event_data_ios` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未取得元数据 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: historical；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| — | — | — | 当前 schema 缺失，下面保留来源字段，不保证当前可用 | 缺口 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `cancellation_reason` | string | 取消原因 |
| `consecutive_paid_periods` | float | 续订次数 |
| `country` | string | 国家 |
| `event` | string | 事件名称 |
| `event_date` | date | 日期 |
| `original_start_date` | date | 用于记录事件发生、数据生成或分区时间的时间字段。 |
| `package_name` | string | 包名 |
| `quantity` | float | 浮点型指标字段，用于统计金额、比率或均值。 |
| `standard_subscription_duration` | string | 文本属性字段，用于补充业务描述、分类或标签信息。 |
| `subscription_name` | string | 文本属性字段，用于补充业务描述、分类或标签信息。 |

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 是 |
| 数据来源 | 苹果商店 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2srevenue!3svip_event_data_ios) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
