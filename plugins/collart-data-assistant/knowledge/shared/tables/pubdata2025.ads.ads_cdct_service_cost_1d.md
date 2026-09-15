---
id: "table:pubdata2025.ads.ads_cdct_service_cost_1d"
title: "pubdata2025.ads.ads_cdct_service_cost_1d · 分产品服务器成本"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.ads.ads_cdct_service_cost_1d.md", "dataform:pubdata/definitions/ads/h_ads_cdct_service_cost_1d.sqlx", "feishu:pubdata2025.ads.ads_cdct_service_cost_1d", "schema:pubdata2025.ads.ads_cdct_service_cost_1d"]
tags: ["ads_cdct_service_cost_1d", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ads.ads_cdct_service_cost_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ads.ads_cdct_service_cost_1d · 分产品服务器成本

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ads.ads_cdct_service_cost_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `event_date` | DATE | NULLABLE | 日期 | 飞书 |
| `billing_month` | DATE | NULLABLE | 账单月份呢 | 飞书 |
| `region` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `billing_from` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `resource_type` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `billing_type` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `atlasv_app_name` | STRING | NULLABLE | 应用或产品相关属性字段，用于产品识别、分类或归属分析。 | 飞书 |
| `allocate_rate` | FLOAT | NULLABLE | 比率指标字段，用于表示转化率、留存率或占比。 | 飞书 |
| `allocate_from` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |
| `cost` | FLOAT | NULLABLE | 投放花费 | 飞书 |
| `project_name` | STRING | NULLABLE | 项目名称 | schema |

## 定义差异与补充

- project_name: 飞书补充解释：文本属性字段，用于补充业务描述、分类或标签信息。
- project_name: 旧文档补充解释：文本属性字段，用于补充业务描述、分类或标签信息。

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | pubdata2025.ods.ods_billing_aws_cost_1d pubdata2025.ods.ods_billing_azure_cost_1d pubdata2025.ods.ods_billing_gcs_cost_1d pubdata2025.ods.ods_log_aws_cdn_1d pubdata2025.ods.ods_billing_third_cost_1d pubdata2025.dwd.dwd_cdct_cost_aws_billing_di pubdata2025.dwd.dwd_cdct_cost_azure_billing_di... pubdata2025.dwd.dwd_cdct_cost_gcp_billing_di pubdata2025.dwd.dwd_cdct_log_aws_cdn_di pubdata2025.dwd.dwd_cdct_cost_third_billing_di pubdata2025.dws.dws_cdct_cost_billing_1d pubdata2025.dws.dws_cdct_log_aws_cdn_1d pubdata2025.dws.dws_cdct_log_ai_record_1d hzdw2024.ods.ai_base_record_store pubdata2025.ads.ads_cdct_service_cost_1d aidata2025.dim.dim_ai_service_cost_unit |
| 是否需要展示血缘 | 是 |
| 数据来源 | - |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sads!3sads_cdct_service_cost_1d) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:pubdata/definitions/ads/h_ads_cdct_service_cost_1d.sqlx`；仓库 `pubdata`，路径 `definitions/ads/h_ads_cdct_service_cost_1d.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.042524+00:00`。同一 SQLX 的产出：`pubdata2025.ads.ads_cdct_service_cost_1d`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND billing_from ='gcp'
AND billing_from like '%aws%'
GROUP BY all
LEFT JOIN (
AND app_name<>''
AND a.atlasv_app_name='woolong'
AND billing_from ='azure'
AND billing_from ='do'
```

飞书登记上游（不保证当前依赖）：pubdata2025.ods.ods_billing_aws_cost_1d<br>pubdata2025.ods.ods_billing_azure_cost_1d<br>pubdata2025.ods.ods_billing_gcs_cost_1d <br>pubdata2025.ods.ods_log_aws_cdn_1d<br>pubdata2025.ods.ods_billing_third_cost_1d<br><br>pubdata2025.dwd.dwd_cdct_cost_aws_billing_di<br>pubdata2025.dwd.dwd_cdct_cost_azure_billing_di...<br>pubdata2025.dwd.dwd_cdct_cost_gcp_billing_di<br>pubdata2025.dwd.dwd_cdct_log_aws_cdn_di<br>pubdata2025.dwd.dwd_cdct_cost_third_billing_di<br><br>pubdata2025.dws.dws_cdct_cost_billing_1d<br>pubdata2025.dws.dws_cdct_log_aws_cdn_1d<br>pubdata2025.dws.dws_cdct_log_ai_record_1d<br>hzdw2024.ods.ai_base_record_store<br>pubdata2025.ads.ads_cdct_service_cost_1d<br><br>aidata2025.dim.dim_ai_service_cost_unit
- 物理上游：`pubdata2025.dws.dws_cdct_cost_billing_1d`
