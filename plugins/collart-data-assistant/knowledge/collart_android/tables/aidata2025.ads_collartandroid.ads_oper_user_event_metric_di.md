---
id: "table:aidata2025.ads_collartandroid.ads_oper_user_event_metric_di"
title: "aidata2025.ads_collartandroid.ads_oper_user_event_metric_di"
project: "collart_android"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads_collartandroid.ads_oper_user_event_metric_di.md", "dataform:aidata/definitions/ads/collart/collart_android/ads_oper_user_event_metric_di.sqlx", "feishu:aidata2025.ads_collartandroid.ads_oper_user_event_metric_di", "schema:aidata2025.ads_collartandroid.ads_oper_user_event_metric_di"]
tags: ["ads_oper_user_event_metric_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartandroid.ads_oper_user_event_metric_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartandroid.ads_oper_user_event_metric_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartandroid.ads_oper_user_event_metric_di` |
| 粒度 | event_date × user_pseudo_id（源码说明；需验唯一性） |
| 主键/去重键 | event_date, user_pseudo_id；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | user_pseudo_id |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `user_pseudo_id` | STRING | NULLABLE | 未说明 | 缺口 |
| `home_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_template_click_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `album_show_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_ready_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_save_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `image_save_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_success_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

## 2. 核心作用

热漏斗用户日 `*_pv`。下游 attr / country / daily 上卷。冷指标不进本表。

## 3. 字段口径

- 列名 = 规则 `metric_name`，一律 `*_pv`。
- `count_events` → `COUNTIF`；`count_distinct_task_id` → `COUNT(DISTINCT IF(..., task_id, NULL))`。
- 上卷 UV：`COUNTIF(*_pv > 0)`。
- `is_new` / `is_vip` 不落本表，JOIN active。

2026-09-02 热列 27 个，与 Sheet 对齐。冷：`ai_tool_execute_start_pv`。

## 5. 数据质量

- 稀疏：当日无热事件的活跃用户不出行；DAU 分母用 active。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_android/ads_oper_user_event_metric_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_android/ads_oper_user_event_metric_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:50.018673+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartandroid.ads_oper_user_event_metric_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Android 第八张表：用户 × 日 事件行为宽表
  Dataform: definitions/ads/collart/collart_android/ads_oper_user_event_metric_di.sqlx
  目标表  : aidata2025.ads_collartandroid.ads_oper_user_event_metric_di

  口径（已确认）:
  - 粒度: event_date × user_pseudo_id；INNER JOIN active 且 is_active=TRUE，仅活跃用户
    （active 表含「付费-only」行 is_active=FALSE，这类行不产生事件行为指标）
  - 列由规则表 aidata2025.ads_collart.ads_dim_metric_rule 中 is_materialized=true 的规则驱动生成
    （本文件由 _scratch/gen_event_metric_sqlx.py 产出，勿手改）
  - 用户×日只存次数列，列名=metric_name（一律 *_pv；上卷 UV 用 COUNTIF(pv>0)）
  - *_pv = COUNT 事件 或 COUNT DISTINCT task_id（见规则 agg_type）
  - is_new / is_vip 派生不入本表，由下游表达
  - event_params 任意 params_info key，比较前 LOWER()
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 30;
DECLARE to_date   DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date;
WHERE event_date BETWEEN from_date AND to_date
AND user_pseudo_id IS NOT NULL
AND is_active
INNER JOIN act AS a
WHERE e.event_date BETWEEN from_date AND to_date
AND e.event_name IN ('Home_Template_Click', 'Home_show', 'ai_service_download_start', 'ai_service_start', 'ai_service_success', 'album_show', 'generate_pro_create', 'generate_watch_ad')
GROUP BY event_date, user_pseudo_id;
```
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_user_active_di`
- 物理上游：`aidata2025.dm.dm_collart_android_user_event_di`

稀疏表：无热事件命中不出行。*_pv 汇总 PV、COUNTIF(*_pv>0) 汇总 UV；DAU/功能使用率分母来自完整 active/cohort。规则修改不等于 SQLX/物化列更新。
