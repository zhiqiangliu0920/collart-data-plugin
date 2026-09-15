---
id: "table:aidata2025.dim.dim_collart_asa_keyword_info"
title: "aidata2025.dim.dim_collart_asa_keyword_info · ASA投放campagin id与name映射表"
project: "collart_ios"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.dim.dim_collart_asa_keyword_info.md", "dataform:aidata/definitions/dim/dim_collart_asa_keyword_info.sqlx", "feishu:aidata2025.dim.dim_collart_asa_keyword_info", "schema:aidata2025.dim.dim_collart_asa_keyword_info"]
tags: ["dim_collart_asa_keyword_info", "字段", "schema", "SQLX"]
tables: ["aidata2025.dim.dim_collart_asa_keyword_info"]
review_required: false
applies_to: []
---

# aidata2025.dim.dim_collart_asa_keyword_info · ASA投放campagin id与name映射表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dim.dim_collart_asa_keyword_info` |
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
| `stats_date` | DATE | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `keyword_id` | STRING | NULLABLE | 用于唯一标识记录或业务实体的关键字段。 | 飞书 |
| `keyword` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `adgroup_id` | STRING | NULLABLE | 广告组id | 飞书 |
| `adgroup_name` | STRING | NULLABLE | 投放广告组 | 飞书 |
| `campaign_id` | STRING | NULLABLE | 投放campaign id | 飞书 |
| `campaign_name` | STRING | NULLABLE | 投放campaign名称 | 飞书 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.ods.ods_apple_campaigns_reports_1d,pubdata2025.ods.ods_apple_adgroups_reports_1d,pubdata2025.ods.ods_apple_keyword_reports_1d |
| 是否需要展示血缘 | 是 |
| 数据来源 | 投放后台 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sdim!3sdim_collart_asa_keyword_info) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdim%2Fdim_collart_asa_keyword_info.sqlx?project=aidata2025&supportedpurview=project) |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dim/dim_collart_asa_keyword_info.sqlx`；仓库 `aidata`，路径 `definitions/dim/dim_collart_asa_keyword_info.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.646803+00:00`。同一 SQLX 的产出：`aidata2025.dim.dim_collart_asa_keyword_info`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
where stats_date  between from_date and to_date
where stats_date between from_date and to_date
group by all
left join adgroup_info b on a.stats_date=b.stats_date and a.adgroup_id=b.adgroup_id
left join campaign_id_info c on a.stats_date=c.stats_date and b.campaign_id=c.campaign_id;
```

飞书登记上游（不保证当前依赖）：pubdata2025.ods.ods_apple_campaigns_reports_1d,pubdata2025.ods.ods_apple_adgroups_reports_1d,pubdata2025.ods.ods_apple_keyword_reports_1d
