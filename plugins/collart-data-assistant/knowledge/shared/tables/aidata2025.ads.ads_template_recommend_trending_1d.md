---
id: "table:aidata2025.ads.ads_template_recommend_trending_1d"
title: "aidata2025.ads.ads_template_recommend_trending_1d · collart android模板推荐（Trending)"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads.ads_template_recommend_trending_1d.md", "feishu:aidata2025.ads.ads_template_recommend_trending_1d", "schema:aidata2025.ads.ads_template_recommend_trending_1d"]
tags: ["ads_template_recommend_trending_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads.ads_template_recommend_trending_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ads.ads_template_recommend_trending_1d · collart android模板推荐（Trending)

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads.ads_template_recommend_trending_1d` |
| 粒度 | 每个国家每个渠道一组 |
| 主键/去重键 | country_code+ traffic_src_type；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | country_code |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `platform` | STRING | NULLABLE | 产品名称 | schema |
| `country_code` | STRING | NULLABLE | 国家代码 | schema |
| `traffic_src_type` | STRING | NULLABLE | 渠道 | schema |
| `temp_id_group` | STRING | NULLABLE | 模版列表 | schema |
| `temp_score_group` | STRING | NULLABLE | 模版分数列表 | schema |
| `temp_name_group` | STRING | NULLABLE | 模版名称列表 | schema |

## 定义差异与补充

- platform: 飞书补充解释：产品名
- platform: 旧文档补充解释：产品名
- traffic_src_type: 飞书补充解释：投放渠道类型
- traffic_src_type: 旧文档补充解释：投放渠道类型
- temp_id_group: 飞书补充解释：推荐的模板id列表
- temp_id_group: 旧文档补充解释：推荐的模板id列表
- temp_score_group: 飞书补充解释：模板id评分
- temp_score_group: 旧文档补充解释：模板id评分
- temp_name_group: 飞书补充解释：推荐的模板名称列表
- temp_name_group: 旧文档补充解释：推荐的模板名称列表

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | dws.dws_template_recommend_score_di |
| 是否需要展示血缘 | 否 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads!3sads_template_recommend_trending_1d) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Fdaily%2Fh_ads_template_recommend_trending_1d.sqlx?project=aidata2025) |
| 看板 | collart android模板推荐 |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。

飞书登记上游（不保证当前依赖）：dws.dws_template_recommend_score_di
