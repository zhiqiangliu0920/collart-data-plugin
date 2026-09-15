---
id: "table:aidata2025.dim.dim_module_template_info_android"
title: "aidata2025.dim.dim_module_template_info_android · collart android模块内模板id表"
project: "collart_android"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/aidata2025.dim.dim_module_template_info_android.md", "dataform:aidata/definitions/dim/dim_module_template_info_android.sqlx", "feishu:aidata2025.dim.dim_module_template_info_android", "schema:aidata2025.dim.dim_module_template_info_android"]
tags: ["dim_module_template_info_android", "字段", "schema", "SQLX"]
tables: ["aidata2025.dim.dim_module_template_info_android"]
review_required: true
applies_to: []
---

# aidata2025.dim.dim_module_template_info_android · collart android模块内模板id表

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.dim.dim_module_template_info_android` |
| 粒度 | 每个模块每个国家一行 |
| 主键/去重键 | module_id+country_code；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | T+1  8:00；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `country_code` | STRING | NULLABLE | 国家代码 | schema |
| `module_id` | BIGNUMERIC | NULLABLE | 模块 ID | schema |
| `module_unique_id` | STRING | NULLABLE | 模块唯一标识 | schema |
| `template_id` | BIGNUMERIC | NULLABLE | 模板 ID | schema |
| `temp_unique_id` | STRING | NULLABLE | 模板唯一标识 | schema |
| `is_vip` | INTEGER | NULLABLE | 是否 VIP 用户（1 是，0 否） | schema |
| `from_type` | INTEGER | NULLABLE | 入口类型一级分类 | schema |
| `from_type2` | INTEGER | NULLABLE | 入口类型二级分类 | schema |
| `manual_priority` | INTEGER | NULLABLE | 人工调整后的优先级 | schema |
| `rn_in_group` | INTEGER | NULLABLE | 组内排序行号 | schema |
| `priority` | INTEGER | NULLABLE | 最终优先级 | schema |

## 定义差异与补充

- country_code: 飞书补充解释：国家
- country_code: 旧文档补充解释：国家
- module_id: 飞书 类型 int；schema 类型 BIGNUMERIC
- module_id: 飞书补充解释：模块名称
- module_id: 旧文档 类型 int；schema 类型 BIGNUMERIC
- module_id: 旧文档补充解释：模块名称
- module_unique_id: 飞书补充解释：模块数字id，唯一id
- module_unique_id: 旧文档补充解释：模块数字id，唯一id
- template_id: 飞书 类型 int；schema 类型 BIGNUMERIC
- template_id: 飞书补充解释：模板名称
- template_id: 旧文档 类型 int；schema 类型 BIGNUMERIC
- template_id: 旧文档补充解释：模板名称
- temp_unique_id: 飞书补充解释：模板数字id，唯一id
- temp_unique_id: 旧文档补充解释：模板数字id，唯一id
- is_vip: 飞书补充解释：是否vip
- is_vip: 旧文档补充解释：是否vip
- from_type: 飞书补充解释：from_type
- from_type: 旧文档补充解释：from_type
- from_type2: 飞书补充解释：from_type2
- from_type2: 旧文档补充解释：from_type2
- manual_priority: 飞书补充解释：模块的手动排序优先级
- manual_priority: 旧文档补充解释：模块的手动排序优先级
- rn_in_group: 飞书补充解释：rn_in_group
- rn_in_group: 旧文档补充解释：rn_in_group
- priority: 飞书补充解释：模块最终优先级
- priority: 旧文档补充解释：模块最终优先级

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.ods.module,aidata2025.ods.template,aidata2025.ods.module_template,aidata2025.dws.dws_template_recommend_score_di |
| 是否需要展示血缘 | 是 |
| 数据来源 | 服务端 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m10!1m4!4m3!1saidata2025!2sads_collart!3sads_high_value_user_Info!1m4!4m3!1saidata2025!2sdim!3sdim_module_template_info_android) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fdim%2Fdim_module_template_info_android.sqlx?project=aidata2025) |
| 看板 | - |

### 使用限制

- 仅有历史字典依据；当前表存在性、分区、写入状态与字段变更尚未重新验证。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/dim/dim_module_template_info_android.sqlx`；仓库 `aidata`，路径 `definitions/dim/dim_module_template_info_android.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:53.787917+00:00`。同一 SQLX 的产出：`aidata2025.dim.dim_module_template_info_android`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
AND (status='online'
AND deleted_at=0 ) a
LEFT JOIN (
AND status='online'
AND deleted_at=0) c
AND deleted_at = 0 ) d
where module_id<>110
WHERE platform = 'collart-android'
AND status = 'online'
AND deleted_at = 0
AND created_at IS NOT NULL
QUALIFY ROW_NUMBER() OVER (ORDER BY created_at DESC) <= 30
PARTITION BY a.country_name, a.traffic_src_type
ORDER BY a.temp_score DESC
JOIN `aidata2025.ods.template` b
ON a.temp_id = b.unique_id
WHERE b.platform = 'collart-android'
AND b.status = 'online'
AND b.deleted_at = 0
AND b.created_at IS NOT NULL
AND a.event_date =  current_date()-1
AND a.traffic_src_type = 'all'
AND a.country_code = 'all'
ON t.temp_id = s.temp_id
```

飞书登记上游（不保证当前依赖）：aidata2025.ods.module,aidata2025.ods.template,aidata2025.ods.module_template,aidata2025.dws.dws_template_recommend_score_di
- 物理上游：`aidata2025.dws.dws_template_recommend_score_di`
- 物理上游：`aidata2025.ods.module_template`
- 物理上游：`aidata2025.ods.template`
