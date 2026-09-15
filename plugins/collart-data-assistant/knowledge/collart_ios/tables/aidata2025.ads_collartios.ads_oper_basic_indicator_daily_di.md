---
id: "table:aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di"
title: "aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di"
project: "collart_ios"
kind: "table"
status: "documented"
sources: ["dataform:aidata/definitions/ads/collart/collart_ios/ads_oper_basic_indicator_daily_di.sqlx", "feishu:aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di", "schema:aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di"]
tags: ["ads_oper_basic_indicator_daily_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | {"type": "DAY", "field": "event_date"} |
| 聚簇 | package_name |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `package_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `app_name` | STRING | NULLABLE | 未说明 | 缺口 |
| `event_date` | DATE | NULLABLE | 未说明 | 缺口 |
| `dau` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `vip_dau` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `churn_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `return_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_vip` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_free` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source` | RECORD | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.organic` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.delivery` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.kol` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `dnu_by_source.inhouse` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain` | RECORD | NULLABLE | 未说明 | 缺口 |
| `retain.d2` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d3` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d4` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d5` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d6` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d7` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d8` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d9` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d10` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d11` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d12` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d13` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d14` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d15` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d16` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d17` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d18` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d19` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d20` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d21` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d22` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d23` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d24` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d25` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d26` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d27` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d28` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d29` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain.d30` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_vip` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_free` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source` | RECORD | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.organic` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.delivery` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.kol` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `retain2_by_source.inhouse` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain` | RECORD | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d2` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d3` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d4` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d5` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d6` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d7` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d8` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d9` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d10` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d11` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d12` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d13` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d14` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d15` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d16` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d17` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d18` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d19` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d20` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d21` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d22` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d23` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d24` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d25` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d26` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d27` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d28` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d29` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `rolling_retain.d30` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription` | RECORD | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv_1d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv_old` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.subscribe_uv_7d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv_1d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv_old` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_uv_7d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_pack_cnt` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.credit_amount` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.purchase_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `subscription.purchase_uv_1d` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue` | RECORD | NULLABLE | 未说明 | 缺口 |
| `revenue.purchase_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.resub_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.new_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.trial_conver_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.credit_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.ad_revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `revenue.new_subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue.renew_subscribe_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue.credit_pack_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue.ad_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `revenue.revenue` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `delivery` | RECORD | NULLABLE | 未说明 | 缺口 |
| `delivery.cost` | FLOAT | NULLABLE | 未说明 | 缺口 |
| `delivery.impressions` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `delivery.clicks` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `delivery.installs` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `home_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_show.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_template_click` | RECORD | NULLABLE | 未说明 | 缺口 |
| `home_template_click.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_template_click.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `home_template_click.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `album_show` | RECORD | NULLABLE | 未说明 | 缺口 |
| `album_show.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `album_show.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `album_show.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_ready` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_ready.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_ready.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_ready.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save` | RECORD | NULLABLE | 未说明 | 缺口 |
| `generate_save.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `generate_save.new_uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
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
| `video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_start.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `referencetovideo_video_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success` | RECORD | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `img2img_generate_success.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_save` | RECORD | NULLABLE | 未说明 | 缺口 |
| `video_save.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `video_save.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `image_save` | RECORD | NULLABLE | 未说明 | 缺口 |
| `image_save.uv` | INTEGER | NULLABLE | 未说明 | 缺口 |
| `image_save.pv` | INTEGER | NULLABLE | 未说明 | 缺口 |
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

## 加工依据与关联关系

- 加工源码：`dataform:aidata/definitions/ads/collart/collart_ios/ads_oper_basic_indicator_daily_di.sqlx`；仓库 `aidata`，路径 `definitions/ads/collart/collart_ios/ads_oper_basic_indicator_daily_di.sqlx`，版本 `9af2cc4ed39c61edb920c7ceba68425d366924a8`，捕获 `2026-09-14T13:18:51.562437+00:00`。同一 SQLX 的产出：`aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di`。

源码说明摘录（保留原定义日期；不能当作本次运行验证）：

```text
Collart iOS 第七张表：日总览
  Dataform: definitions/ads/collart/collart_ios/ads_oper_basic_indicator_daily_di.sqlx
  目标表  : aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di

  口径:
  - 粒度: event_date × package_name（iOS 包）
  - 行为/留存/订阅/收入/花费: SUM(aidata2025.ads_collartios.ads_oper_basic_indicator_country_di)
  - 事件漏斗: SUM(aidata2025.ads_collartios.ads_oper_event_metric_country_di)，列名与 country 一致（含 new_uv 等分层字段）
  - 本文件由 _scratch/gen_indicator_daily_sqlx_ios.py 产出，勿手改事件列
```

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT ${dataform.projectConfig.vars.biz_date} - 30;
DECLARE to_date   DATE DEFAULT ${dataform.projectConfig.vars.biz_date};
PARTITION BY event_date
WHERE event_date BETWEEN from_date AND to_date
AND package_name = 'ai.photo.video.generator.fotos.ai.image.picture.editor.app.free';
GROUP BY event_date
```
- 物理上游：`aidata2025.ads_collartios.ads_oper_basic_indicator_country_di`
- 物理上游：`aidata2025.ads_collartios.ads_oper_event_metric_country_di`
