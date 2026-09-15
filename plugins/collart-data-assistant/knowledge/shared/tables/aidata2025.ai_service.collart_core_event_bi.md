---
id: "table:aidata2025.ai_service.collart_core_event_bi"
title: "aidata2025.ai_service.collart_core_event_bi · Collart ios/android ai服务事件的uv、pv"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ai_service.collart_core_event_bi.md", "feishu:aidata2025.ai_service.collart_core_event_bi", "schema:aidata2025.ai_service.collart_core_event_bi"]
tags: ["collart_core_event_bi", "字段", "schema", "SQLX"]
tables: ["aidata2025.ai_service.collart_core_event_bi"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ai_service.collart_core_event_bi · Collart ios/android ai服务事件的uv、pv

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ai_service.collart_core_event_bi` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `event_name` | STRING | NULLABLE | 事件名/事件英文名 | 飞书 |
| `key` | STRING | NULLABLE | 参数名 | 飞书 |
| `value` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `event_module` | STRING | NULLABLE | 事件分类 | 飞书 |
| `event_name_chinese` | STRING | NULLABLE | 事件中文名 | 飞书 |
| `is_vip` | BOOLEAN | NULLABLE | 是否新老用户，true代表付费用户、false代表免费用户 | 飞书 |
| `is_new` | BOOLEAN | NULLABLE | 是否新老用户，true代表新用户、false代表老用户 | 飞书 |
| `traffic_src_type` | STRING | NULLABLE | 投放渠道类型 | 飞书 |
| `country` | STRING | NULLABLE | 国家 | 飞书 |
| `event_num` | INTEGER | NULLABLE | pv，统计某事件的触发次数 | 飞书 |
| `user_num` | INTEGER | NULLABLE | uv，统计某事件的触发人数 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | 埋点表 aidata2025.dwd.dwd_oper_user_collart_di aidata2025.dim.dim_collart_core_event |
| 是否需要展示血缘 | 否 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sai_service!3scollart_core_event_bi) |
| 任务地址 | collart_co…t_1d.sqlx – Code – Dataform – BigQuery – AIDATA – Google Cloud 控制台 |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：埋点表<br>aidata2025.dwd.dwd_oper_user_collart_di<br>aidata2025.dim.dim_collart_core_event
