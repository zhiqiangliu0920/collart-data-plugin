---
id: "table:aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di"
title: "aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di"
project: "collart_android"
kind: "table"
status: "documented"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di.md", "dataform:aidata/definitions/ads/collart/collart_android/ads_oper_event_metric_attr_di.sqlx", "feishu:aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di", "schema:aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di"]
tags: ["ads_oper_event_metric_attr_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | country, app_version, is_new |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `is_new` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `is_vip` | BOOLEAN | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_type` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_platform` | STRING | NULLABLE | 未说明 | 缺口 |
| `traffic_src_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_version` | STRING | NULLABLE | 未说明 | 缺口 |
| `home_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `home_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_template_click` | RECORD | NULLABLE | 未说明 | 缺口 |
| `home_template_click.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_template_click.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `album_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `album_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `album_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_ready` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_ready.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_ready.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_save.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `aiedit_img2img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `multireference_img2img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_save` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_save.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_save.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `image_save` | RECORD | NULLABLE | 未说明 | 缺口 |
| `image_save.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `image_save.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 表专属业务说明

## 2. 核心作用

漏斗按新老 / VIP / 国家 / 渠道 / 版本切分。

## 5. 数据质量

冷指标不进本表。2026-09-02 与 Sheet 27 个热指标对齐。

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_android/ads_oper_event_metric_attr_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_android/ads_oper_event_metric_attr_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:49.973653+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Android 第九张表：日 × 默认维度 事件指标汇总
  Dataform: definitions/ads/collart/collart_android/ads_oper_event_metric_attr_di.sqlx
  目标表  : aidata2025.ads_collartandroid.ads_oper_event_metric_attr_di

  口径（已确认）:
  - 维度对齐表 5：is_new / is_vip / country / traffic_src_type /
    traffic_src_platform / traffic_src_name / app_version
  - 不加 city / package_name
  - app_version：按当日 active DAU Top5（仅 is_active 用户），其余折叠为 'other'
  - 维度源 active_base 仅取 is_active=TRUE 行：付费-only 行（is_active=FALSE）无事件行为，
    也不参与 DAU / 版本排名；本表无收入列，故整表按 is_active 过滤
  - 每个热指标一列 STRUCT<uv,pv>；列名=metric_name 去 *_pv 后缀
  - 表8列=metric_name(*_pv)：uv=COUNTIF(pv>0)，pv=SUM(pv)
  - 列由 aidata2025.ads_collart.ads_dim_metric_rule is_materialized=true 驱动生成
    （本文件由 _scratch/gen_event_metric_attr_sqlx.py 产出，勿手改）
  - 仅汇总表 8 有行的用户（稀疏；无行为的维度组合不出行）
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
ORDER BY COUNT(DISTINCT user_pseudo_id) DESC, app_version
GROUP BY event_date, app_version
WHERE rn <= 5
INNER JOIN active_base AS a
LEFT JOIN top_version AS tv
ON a.event_date = tv.event_date
AND a.app_version = tv.app_version
WHERE m.event_date BETWEEN from_date AND to_date
```
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_user_active_di`
- 物理上游：`aidata2025.ads_collartandroid.ads_oper_user_event_metric_di`
