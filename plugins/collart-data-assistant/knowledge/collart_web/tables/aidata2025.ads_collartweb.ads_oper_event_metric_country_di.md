---
id: "table:aidata2025.ads_collartweb.ads_oper_event_metric_country_di"
title: "aidata2025.ads_collartweb.ads_oper_event_metric_country_di"
project: "collart_web"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_web/ads_oper_event_metric_country_di.sqlx", "feishu:aidata2025.ads_collartweb.ads_oper_event_metric_country_di", "schema:aidata2025.ads_collartweb.ads_oper_event_metric_country_di"]
tags: ["ads_oper_event_metric_country_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartweb.ads_oper_event_metric_country_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartweb.ads_oper_event_metric_country_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartweb.ads_oper_event_metric_country_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | country |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `country` | STRING | NULLABLE | 未说明 | 缺口 |
| `page_view` | RECORD | NULLABLE | 未说明 | 缺口 |
| `page_view.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `page_view.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `session_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `session_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `session_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `first_visit` | RECORD | NULLABLE | 未说明 | 缺口 |
| `first_visit.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `first_visit.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `user_engagement` | RECORD | NULLABLE | 未说明 | 缺口 |
| `user_engagement.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `user_engagement.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start.old_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start.free_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success.new_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success.free_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_success.vip_pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_page_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `explore_page_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_page_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_page_show.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_card_click` | RECORD | NULLABLE | 未说明 | 缺口 |
| `explore_card_click.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_card_click.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_card_click.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_content_click` | RECORD | NULLABLE | 未说明 | 缺口 |
| `explore_content_click.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_content_click.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_content_click.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_content_generate_click` | RECORD | NULLABLE | 未说明 | 缺口 |
| `explore_content_generate_click.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_content_generate_click.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `explore_content_generate_click.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `feature_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `feature_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `feature_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `feature_show.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `photo_add` | RECORD | NULLABLE | 未说明 | 缺口 |
| `photo_add.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `photo_add.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `photo_add.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `photo_add_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `photo_add_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `photo_add_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `photo_add_success.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_click` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_click.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_click.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_click.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `login_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_show.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_account_choose` | RECORD | NULLABLE | 未说明 | 缺口 |
| `login_account_choose.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_account_choose.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_account_choose.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `login_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `login_success.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `vip_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_show.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe` | RECORD | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe_succeed` | RECORD | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe_succeed.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe_succeed.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_subscribe_succeed.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_save.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `valid_user` | RECORD | NULLABLE | 未说明 | 缺口 |
| `valid_user.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `valid_user.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `valid_user.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `framestransition_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `motioncontrol_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `text2video_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_start.vip_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_web/ads_oper_event_metric_country_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_web/ads_oper_event_metric_country_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:52.456671+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartweb.ads_oper_event_metric_country_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart Web：日 × 国家 事件指标汇总
  Dataform: definitions/ads/collart/collart_web/ads_oper_event_metric_country_di.sqlx
  目标表  : aidata2025.ads_collartweb.ads_oper_event_metric_country_di

  口径:
  - 粒度: event_date × country；全量国家（不 top_country）
  - 列名=metric_name 去 *_pv 后缀；STRUCT 内区分 uv/pv
  - 上游: 从表 9 aidata2025.ads_collartweb.ads_oper_event_metric_attr_di 按 country SUM(uv/pv)
  - 列由 aidata2025.ads_collart.ads_dim_metric_rule is_materialized=true 驱动
    （本文件由 _scratch/gen_event_metric_country_sqlx_web.py 产出，勿手改）
  - 与表 6 basic_indicator_country 并行：本表只管事件漏斗，不管 DAU/收入/花费
  - 旧 country metric 所需的 new/old/free/vip 切片直接放在对应事件 STRUCT 内：
      如 generate_start.new_uv / vip_uv、generate_success.new_pv / vip_pv
  - 凡指标名含 generate_start 的列，STRUCT 必有 vip_uv（= attr.is_vip 的 uv）
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
AND country IS NOT NULL
GROUP BY event_date, country;
```
- 物理上游：`aidata2025.ads_collartweb.ads_oper_event_metric_attr_di`
