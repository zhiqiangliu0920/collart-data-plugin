---
id: "table:pubdata2025.ads.ads_data_report_1d"
title: "pubdata2025.ads.ads_data_report_1d"
project: "company"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.ads.ads_data_report_1d.md", "dataform:aidata/definitions/ads/reports/h_pubdata_ads_data_report_1d.sqlx", "feishu:pubdata2025.ads.ads_data_report_1d", "schema:pubdata2025.ads.ads_data_report_1d"]
tags: ["ads_data_report_1d", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ads.ads_data_report_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ads.ads_data_report_1d

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ads.ads_data_report_1d` |
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
| `app_name` | STRING | NULLABLE | app名称 | schema |
| `package_name` | STRING | NULLABLE | 包名 | schema |
| `dnu` | INTEGER | NULLABLE | 新增 | schema |
| `dau` | INTEGER | NULLABLE | 活跃 | schema |
| `retention` | FLOAT | NULLABLE | 留存率 | schema |
| `dnu_organic` | INTEGER | NULLABLE | 自然渠道新增 | schema |
| `dnu_others` | INTEGER | NULLABLE | 其它渠道新增 | schema |
| `dnu_inhouse` | INTEGER | NULLABLE | 内部带量新增 | schema |
| `cost` | FLOAT | NULLABLE | 成本 | schema |
| `data_from` | STRING | NULLABLE | 文本属性字段，用于补充业务描述、分类或标签信息。 | 飞书 |

## 定义差异与补充

- app_name: 飞书补充解释：产品名
- app_name: 旧文档补充解释：产品名
- dnu: 飞书补充解释：新增用户
- dnu: 旧文档补充解释：新增用户
- dau: 飞书补充解释：dau
- dau: 旧文档补充解释：dau
- retention: 飞书补充解释：浮点型指标字段，用于统计金额、比率或均值。
- retention: 旧文档补充解释：浮点型指标字段，用于统计金额、比率或均值。
- dnu_organic: 飞书补充解释：自然新增
- dnu_organic: 旧文档补充解释：自然新增
- dnu_others: 飞书补充解释：其他新增
- dnu_others: 旧文档补充解释：其他新增
- cost: 飞书补充解释：投放花费
- cost: 旧文档补充解释：投放花费

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 是 |
| 数据来源 | - |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=pubdata2025&ws=!1m5!1m4!4m3!1spubdata2025!2sads!3sads_data_report_1d) |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/reports/h_pubdata_ads_data_report_1d.sqlx`；仓库 `aidata`，路径 `definitions/ads/reports/h_pubdata_ads_data_report_1d.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:52.880425+00:00`。同一 SQLX 的产出：`pubdata2025.ads.ads_data_report_1d`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND run_date
AND data_from='aidata';
LEFT JOIN (
ON a.event_date = b.event_date
AND a.package_name = b.package_name
ON a.event_date=c.event_date
AND a.package_name=c.package_name
WHERE dau>0
```
- 物理上游：`aidata2025.dwd.dwd_cdct_delivery_cost_di`
