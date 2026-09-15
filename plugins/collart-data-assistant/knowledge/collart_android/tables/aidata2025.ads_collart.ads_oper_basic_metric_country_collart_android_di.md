---
id: "table:aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di"
title: "aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di"
project: "collart_android"
kind: "table"
status: "historical"
sources: ["ai-knowledge:collart_android/tables/aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di.md", "feishu:aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di", "schema:aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di"]
tags: ["ads_oper_basic_metric_country_collart_android_di", "字段", "schema", "SQLX"]
tables: ["aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di"]
review_required: true
applies_to: []
---

# aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di

## 使用边界

BigQuery 元数据返回 NOT_FOUND（2026-09-14）；可能为历史表/名称变化/不可见，不能作为默认当前入口。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `aidata2025.ads_collart.ads_oper_basic_metric_country_collart_android_di` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未取得元数据 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: historical；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| — | — | — | 当前 schema 缺失，下面保留来源字段，不保证当前可用 | 缺口 |

## 来源有而当前 schema 未见的字段

可能是历史列、旧嵌套命名或缺失 schema，未自动映射到相似新字段。

| 字段 | 来源类型 | 来源说明 |
|---|---|---|
| `ad_revenue` | float | 广告收入 |
| `aiGeneral_generate_start_num` | int | 图生图开始生成次数 |
| `aiGeneral_generate_start_user` | int | 图生图开始生成人数 |
| `aiGeneral_generate_success_num` | int | 图生图生成成功次数 |
| `aiGeneral_save_num` | int | 图生图保存次数 |
| `country` | string | 国家 |
| `country_type` | string | 国家 |
| `dau` | int | dau |
| `delivery_new_user` | int | 投放新增用户 |
| `delivery_retain2_new_user` | int | 投放新增用户在次日仍然活跃的用户数 |
| `event_date` | date | 日期 |
| `first_7_vip_pack_user` | int | 前7日购买点数包用户数 |
| `first_7_vip_user` | int | 前7日订阅用户数 |
| `free_generate_start_user` | int | 免费ai服务开始使用人数 |
| `free_generate_success_num` | int | 免费ai服务生成成功次数 |
| `free_new_user` | int | 免费新用户 |
| `generate_start_num` | int | 开始生成次数 |
| `generate_start_user` | int | 开始生成人数 |
| `generate_success_num` | int | 生成成功次数 |
| `headshot_generate_start_num` | int | headshot开始生成次数 |
| `headshot_generate_start_user` | int | headshot开始生成人数 |
| `headshot_generate_success_num` | int | headshot生成成功次数 |
| `headshot_save_num` | int | headshot保存次数 |
| `mau` | int | 月活 |
| `month` | string | 月份 |
| `new_Home_Template_Click_user` | int | 点击模板的新用户数 |
| `new_album_show_user` | int | 进入相册页的新用户数 |
| `new_generate_ready_user` | int | 准备开始生成的新用户数 |
| `new_generate_save_user` | int | 保存生成结果的新用户数 |
| `new_generate_start_user` | int | 开始生成的新用户数 |
| `new_generate_success_num` | int | 新用户数生成成功次数 |
| `new_generate_success_user` | int | 生成成功的新用户数 |
| `new_home_show_user` | int | 进入主页的新用户数 |
| `new_revenue` | float | 首次订阅收入 |
| `new_user` | int | 新增用户数 |
| `old_generate_start_user` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `organic_new_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `organic_retain2_new_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `pack_revenue` | float | 点数包收入 |
| `package_name` | string | 包名 |
| `renew_revenue` | float | 续订算收入 |
| `retain2_free_new_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `retain2_new_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `retain2_vip_new_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `rolling_retain_7_free_new_user` | int | 滚动留存指标 |
| `rolling_retain_7_new_user` | int | 滚动留存指标 |
| `rolling_retain_7_vip_new_user` | int | 滚动留存指标 |
| `temp_content_click_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `text2image_generate_start_num` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `text2image_generate_start_user` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `text2image_generate_success_num` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `text2image_save_num` | int | 计数指标字段，用于统计人数、次数或记录量。 |
| `total_revenue` | float | 收入 |
| `video_generate_start_num` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `video_generate_start_user` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `video_generate_success_num` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `video_save_num` | int | 计数指标字段，用于统计人数、次数或记录量。 |
| `vip_dau` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `vip_generate_start_user` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `vip_generate_success_num` | int | 比率指标字段，用于表示转化率、留存率或占比。 |
| `vip_new_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `vip_pack_credit_count` | int | 计数指标字段，用于统计人数、次数或记录量。 |
| `vip_pack_num` | int | 计数指标字段，用于统计人数、次数或记录量。 |
| `vip_pack_user` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `vip_pack_user_0` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `vip_pack_user_old` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `vip_revenue` | float | 订阅收入 |
| `vip_user_0` | int | 整型指标字段，用于统计数量、金额或次数。 |
| `week_end` | string | 文本属性字段，用于补充业务描述、分类或标签信息。 |
| `week_range` | string | 文本属性字段，用于补充业务描述、分类或标签信息。 |
| `week_start` | string | 文本属性字段，用于补充业务描述、分类或标签信息。 |

## 表专属业务说明

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | storytemplate-10a27.analytics_232977577.events_*,aidata2025.ads_collart.ads_oper_basic_indicator_collart_di,pubdata2025.ods.ods_apple_sales_1d,aidata2025.dwd.dwd_oper_user_basic_di,aidata2025.ai_service.ai_cost_data,aidata2025.dws.dws_oper_fb_delivery_1d,aidata2025.dws.dws_oper_asa_keyword_collart_1d |
| 是否需要展示血缘 | 是 |
| 数据来源 | 客户端埋点 |
| 数据表地址 | [BigQuery](https://console.cloud.google.com/bigquery?project=aidata2025&ws=!1m5!1m4!4m3!1saidata2025!2sads_collart!3sads_oper_basic_metric_country_collart_android_di) |
| 任务地址 | [任务](https://console.cloud.google.com/bigquery/dataform/locations/us-east1/repositories/aidata/workspaces/script/files/definitions%2Fads%2Fcollart%2Fads_oper_basic_metric_collart_di.sqlx?project=aidata2025&supportedpurview=project) |
| 看板 | collart android周报分析用 |

### 使用限制

- 表名包含 country，但登记粒度仅写“每天一行”；国家维度是否参与唯一键需核对。
- retain_2 的历史说明为次日；其他 retain_N 的自动解释可能偏移一天，不能按字段后缀直接认定 Dn。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

未捕获对应 SQLX：可能由外部导入、计划查询或未收录仓库生成。只保留已知 schema 与来源；加工过滤、去重及增量规则不能推定。
