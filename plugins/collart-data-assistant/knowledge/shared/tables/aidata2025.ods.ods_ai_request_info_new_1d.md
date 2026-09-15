---
id: "table:aidata2025.ods.ods_ai_request_info_new_1d"
title: "aidata2025.ods.ods_ai_request_info_new_1d · 用户ai服务  输入输出明细表（提示词）"
project: "shared"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/aidata2025.ods.ods_ai_request_info_new_1d.md", "feishu:aidata2025.ods.ods_ai_request_info_new_1d", "schema:aidata2025.ods.ods_ai_request_info_new_1d"]
tags: ["ods_ai_request_info_new_1d", "字段", "schema", "SQLX"]
tables: ["aidata2025.ods.ods_ai_request_info_new_1d"]
review_required: true
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# aidata2025.ods.ods_ai_request_info_new_1d · 用户ai服务  输入输出明细表（提示词）

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ods.ods_ai_request_info_new_1d` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | app_name, country, ai_type, atlas_uid |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `id` | STRING | NULLABLE | 自增id | schema |
| `event_date` | DATE | NULLABLE | 事件触发日期 | schema |
| `prompt` | STRING | NULLABLE | 正向提示词 | schema |
| `negative_prompt` | STRING | NULLABLE | 反向提示词 | schema |
| `app_name` | STRING | NULLABLE | 应用包名/名称 | schema |
| `country` | STRING | NULLABLE | 国家代码 | schema |
| `version` | STRING | NULLABLE | 应用版本号 | schema |
| `client_task_id` | STRING | NULLABLE | 客户端任务ID | schema |
| `task_id` | STRING | NULLABLE | 服务端任务ID | schema |
| `mode_type` | STRING | NULLABLE | 模式类型 | schema |
| `third_name` | STRING | NULLABLE | 第三方服务名称 | schema |
| `atlas_uid` | STRING | NULLABLE | 内部用户UID | schema |
| `ai_type` | STRING | NULLABLE | AI类型(如 video_gen) | schema |
| `request` | STRING | NULLABLE | 请求参数(JSON字符串) | schema |
| `style` | STRING | NULLABLE | 风格参数 | schema |
| `sub_mode_type` | STRING | NULLABLE | 子模式类型 | schema |
| `cost_point` | FLOAT | NULLABLE | 消耗点数 | schema |
| `ai_home_design_type` | STRING | NULLABLE | AI家居设计类型标识 | schema |
| `status` | STRING | NULLABLE | 状态 | schema |
| `created_at` | TIMESTAMP | NULLABLE | 创建时间 | schema |
| `updated_at` | TIMESTAMP | NULLABLE | 更新时间 | schema |
| `filter_date` | TIMESTAMP | NULLABLE | 过滤/分区日期(带时间戳) | schema |
| `start_resource_moderation` | STRING | NULLABLE | 开始资源/机器审核JSON | schema |
| `at_uid` | STRING | NULLABLE | at_uid | schema |
| `resource_type` | STRING | NULLABLE | 资源类型 | schema |
| `resource_category` | STRING | NULLABLE | 资源分类 | schema |
| `resource_severity` | STRING | NULLABLE | 资源安全级别/严重程度 | schema |
| `start_two_resource` | STRING | NULLABLE | 二级起点资源 | schema |
| `request_resource` | STRING | NULLABLE | 请求资源 | schema |
| `service_task_id` | STRING | NULLABLE | 服务端具体任务ID | schema |
| `result_path` | STRING | NULLABLE | 最终结果路径 | schema |
| `user_status` | STRING | NULLABLE | 用户状态 | schema |
| `function_type` | STRING | NULLABLE | 功能分类 | schema |
| `scene` | STRING | NULLABLE | 类型 | schema |
| `business_tag` | STRING | NULLABLE | 是否有 前置检查, pre_check | schema |
| `business_tag_2` | STRING | NULLABLE | 业务场景标签 | schema |
| `group_task_id` | STRING | NULLABLE | 批量任务 id | schema |
| `service_req_status` | INTEGER | NULLABLE | 服务侧状态调和结果：0=未知，1=成功(completed)，2=失败(failed/nsfw)，3=未找到。 | schema |
| `failed_reason` | STRING | NULLABLE | 失败原因；6010 表示后置检测拦截 | schema |

## 定义差异与补充

- app_name: 旧文档补充解释：产品关联范围
- client_task_id: 旧文档补充解释：仅用于核查，不直接作多对多回退连接
- task_id: 旧文档补充解释：请求侧任务ID候选关联键
- atlas_uid: 旧文档补充解释：用于查 VIP 表的内部用户ID候选
- request: 旧文档补充解释：从 moderation_text 数组提取 sexual 类评分
- at_uid: 旧文档补充解释：旧服务记录用户ID的候选映射
- service_task_id: 旧文档补充解释：具体服务任务ID候选关联键，不能忽略
- service_req_status: 旧文档补充解释：schema 说明：0未知、1成功、2失败(failed/nsfw)、3未找到；本次不替换 DWD 状态
- failed_reason: 旧文档补充解释：schema 说明中 6010 表示后置检测拦截；不自行扩展过滤规则

## 表专属业务说明

## 评分提取与关联要求

（旧执行片段已退出发行包；加工依据见 SQLX，只读查询见关联指标。）

- 用原始数值判断 `> 0.6`，ROUND 仅用于展示。无法解析、类别缺失、无请求关联等情况保留原始 NULL 和缺失标志；按用户规则，非大R过滤时可用 `COALESCE(sexual, 0) <= 0.6` 默认纳入。身份、任务归属或评分冲突仍走质量核查，不作为普通缺失评分回退。
- 请求数组不可直接在服务任务事实表上 CROSS JOIN 后计数；应先提取并归并为任务级维度，再 LEFT JOIN。
- 先验证 `service_task_id`，再验证 `task_id`；必须约束产品、身份一致性，避免 OR JOIN 放大任务数。
- 新数据主要可用服务 `user_id = atlas_uid` 核对；旧数据有 `user_id = at_uid` 的情况，应验证映射后再用 `atlas_uid` 查大R。
- 先尝试经任务验证的身份映射；多个候选身份不一致或仍无唯一映射时保留身份问题标记，但按用户追加规则归为非大R，不因此丢弃任务。
- 评分、身份、状态有冲突的任务不静默选择有利结果；归入质量核查。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | - |
| 是否需要展示血缘 | 否 |
| 数据来源 | 服务端 |
| 数据表地址 | - |
| 任务地址 | - |
| 看板 | - |

### 使用限制

- 导出没有字段明细，不能据此编写字段查询。
- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
