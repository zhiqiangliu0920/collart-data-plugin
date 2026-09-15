---
id: "table:pubdata2025.ads.ads_atlasv_basic_data_daily_1h"
title: "pubdata2025.ads.ads_atlasv_basic_data_daily_1h · 公司分产品收入等基础数据"
project: "company"
kind: "table"
status: "documented"
sources: ["ai-knowledge:1company/tables/pubdata2025.ads.ads_atlasv_basic_data_daily_1h.md", "dataform:pubdata/definitions/ads/h_ads_atlasv_basic_data_daily_1h.sqlx", "feishu:pubdata2025.ads.ads_atlasv_basic_data_daily_1h", "schema:pubdata2025.ads.ads_atlasv_basic_data_daily_1h"]
tags: ["ads_atlasv_basic_data_daily_1h", "字段", "schema", "SQLX"]
tables: ["pubdata2025.ads.ads_atlasv_basic_data_daily_1h"]
review_required: false
applies_to: ["collart_android", "collart_ios", "collart_web", "collart_fashion"]
---

# pubdata2025.ads.ads_atlasv_basic_data_daily_1h · 公司分产品收入等基础数据

## 使用边界

表元数据读取成功；未读取数据行，未验证完整日期覆盖、金额或最近任务运行。

只读；本页 SQLX 是加工依据，不可执行。原始事件及逐条行为 DWD/DM 均限最近 7 天并有日期与产品过滤；汇总、画像和收入表可按适用范围分析更长历史。字段语义未经线上业务值验证。

## 表结构与粒度

| 项 | 定义及来源 |
|---|---|
| 物理表 | `pubdata2025.ads.ads_atlasv_basic_data_daily_1h` |
| 粒度 | 未说明 |
| 主键/去重键 | 未说明；BigQuery 未声明即不代表强制唯一约束 |
| 分区 | 未声明时间/范围分区 |
| 聚簇 | 未说明 |
| 更新 | 未说明；具体重写/MERGE 窗口见加工依据 |
| 捕获状态 | schema: documented；Dataform releaseConfig 源码与实际运行版本分开 |

## 完整字段

字段名/类型/mode 以本次 schema 为准，含所有嵌套层级；解释优先 schema 描述，其次飞书，再用旧文档。来源都未解释时明确未知，不把字段名翻译当验证。存在语义冲突时需复核。

| 字段 | 类型 | Mode | 解释 | 解释来源 |
|---|---|---|---|---|
| `stats_date` | DATE | NULLABLE | 用于记录事件发生、数据生成或分区时间的时间字段。 | 飞书 |
| `team` | STRING | NULLABLE | 负责该产品或数据维护的团队。 | 飞书 |
| `package_name` | STRING | NULLABLE | 包名 | 飞书 |
| `app_name` | STRING | NULLABLE | 产品名 | 飞书 |
| `platform` | STRING | NULLABLE | 应用所属平台，如 iOS、Android、Web。 | 飞书 |
| `app_type` | STRING | NULLABLE | 产品类型 | 飞书 |
| `city` | STRING | NULLABLE | 产品所在城市 | 飞书 |
| `revenue` | FLOAT | NULLABLE | 收入 | 飞书 |
| `vip_revenue` | FLOAT | NULLABLE | 订阅收入 | 飞书 |
| `ad_revenue` | FLOAT | NULLABLE | 广告收入 | 飞书 |
| `new_users` | INTEGER | NULLABLE | 新增用户数 | 飞书 |
| `new_users_organic` | INTEGER | NULLABLE | 自然新增用户数 | 飞书 |
| `active_users` | INTEGER | NULLABLE | dau | 飞书 |
| `cost` | FLOAT | NULLABLE | 投放花费 | 飞书 |
| `else_cost` | FLOAT | NULLABLE | 服务器成本 | 飞书 |
| `revenue_last` | FLOAT | NULLABLE | 收入数值字段。 | 飞书 |
| `new_users_last` | INTEGER | NULLABLE | 新增用户数 | 飞书 |
| `active_users_last` | INTEGER | NULLABLE | 前一天的dau | 飞书 |
| `cost_last` | FLOAT | NULLABLE | 前一天的投放花费 | 飞书 |
| `else_cost_last` | FLOAT | NULLABLE | 服务器成本 | 飞书 |
| `retan_2` | FLOAT | NULLABLE | 浮点型指标字段，用于统计金额、比率或均值。 | 飞书 |
| `retan_7` | FLOAT | NULLABLE | 浮点型指标字段，用于统计金额、比率或均值。 | 飞书 |
| `revenue_level` | STRING | NULLABLE | 收入数值字段。 | 飞书 |

## 表专属业务说明

> 业务状态：historical；复核：reviewed_static。以下完整字段定义来自 2026-05-21 导出，未经本次生产验证。

### 上游与来源

| 项目 | 内容 |
|---|---|
| 上层表 | aidata2025.ads.ads_ad_sub_revenue_1h （ai组收入） downloaddata2025.ads.ads_ad_sub_revenue_1h（下载器收入） aidata2025.dws.dws_oper_basic_aidata_1d（ai组新增活跃） downloaddata2025.ads.ads_dau_retain_90_1d（下载器新增活跃） `hzdata.firebase.prefect_total_metrics_20*`（老产品新增活跃） pubdata2025.dws.dws_cdct_cost_google_1h（GA投放成本） aidata2025.dws.dws_oper_tiktok_ad_1d（TT投放成本） aidata2025.dws.dws_oper_fb_delivery_1d（FB投放成本） aidata2025.dws.dws_oper_asa_keyword_collart_1d（ASA投放成本） gzdw2024.gz_bi.dws_daily_app_reports（广州数据） pubdata2025.ads.ads_atlasv_basic_data_daily_2024（杭州2024数据） |
| 是否需要展示血缘 | 是 |
| 数据来源 | - |
| 数据表地址 | - |
| 任务地址 | 定时计划：pubdata2025.ads.ads_atlasv_basic_data_daily_1h |
| 看板 | 公司层收入看板 |

### 使用限制

- 行粒度未填写；聚合前需确认唯一键及重复记录处理。
- 主键未填写；字段角色中的“主键”不等于已验证唯一约束。
- 部分字段说明为导出模板的通用解释，不是已确认业务口径；金额单位、去重键、观察窗口仍需业务证据。

## 加工依据与关联关系

- 加工源码：`dataform:pubdata/definitions/ads/h_ads_atlasv_basic_data_daily_1h.sqlx`；仓库 `pubdata`，路径 `definitions/ads/h_ads_atlasv_basic_data_daily_1h.sqlx`，版本 `8dfbd362d9f3435b7f5d6f5febdc87b93639ceb9`，捕获 `2026-09-14T13:18:56.095928+00:00`。同一 SQLX 的产出：`pubdata2025.ads.ads_atlasv_basic_data_daily_1h`。

releaseConfig 指向的编译源码已捕获；未读取当前工作区编辑，也未核验最新 workflow invocation 的实际执行版本。引用的 includes 保存在 sources/dataform，可按源码相对路径追溯。原始哈希与分发文件哈希分别记录在 _meta/sources.json；若隐私常量脱敏，则分发版不是字节级原件。

### 过滤、关联、去重与窗口线索

下列为静态语句定位片段，顺序和完整表达式以源码为准，不是可执行查询。

```text
DECLARE from_date DATE DEFAULT  "2025-01-01";
WHERE  stats_date >= '2025-01-01';
join (select package_name,app_name,platform,app_type,city,team from `aidata2025.dim.dim_product_info`) on 1=1
where event_date>='2025-01-01'
group by 1,2
left join aidata2025.dim.dim_product_info_copy b on a.package_name=b.package_name
where event_date >= "2025-01-01"
and b.team<>'ai_photo'
where _TABLE_SUFFIX between '250101' and  '250630'
and country='TOTAL'
and package_name not in('instagram.video.downloader.story.saver',
where a.event_date>='2025-01-01'
and package_name in (
and traffic_source_name like '%ga%'
on a.stats_date=b.stats_date
and a.package_name=b.package_name
and package_name<>'ai.headshot.photo.generator.face.app.free'
left join hangzhou_active_info b on a.package_name=b.package_name and a.stats_date=b.stats_date
left join hangzhou_revenue_info c on a.package_name=c.package_name and a.stats_date=c.stats_date
left join pubdata2025.ads.ads_atlasv_deliver_cost_daily d on a.package_name=d.package_name and a.stats_date=d.event_date
left join (
group by all) f on  a.app_name=f.app_name and a.stats_date=f.event_Date
where a.city='hangzhou'
left join gzdw2024.gz_bi.dws_daily_app_reports b on a.package_name=b.package_name and a.stats_date=b.stats_date
where a.city='guangzhou'
and b.stats_date>='2025-01-01'
where stats_date<'2025-01-01'),
where stats_Date between date_sub(current_date, INTERVAL 8 day) and date_sub(current_date, INTERVAL 2 day)
group by app_name
left join revenue_level_info  using(app_name)
```

飞书登记上游（不保证当前依赖）：aidata2025.ads.ads_ad_sub_revenue_1h （ai组收入）<br>downloaddata2025.ads.ads_ad_sub_revenue_1h（下载器收入）<br><br>aidata2025.dws.dws_oper_basic_aidata_1d（ai组新增活跃）<br>downloaddata2025.ads.ads_dau_retain_90_1d（下载器新增活跃）<br>`hzdata.firebase.prefect_total_metrics_20*`（老产品新增活跃）<br><br>pubdata2025.dws.dws_cdct_cost_google_1h（GA投放成本）<br>aidata2025.dws.dws_oper_tiktok_ad_1d（TT投放成本）<br>aidata2025.dws.dws_oper_fb_delivery_1d（FB投放成本）<br>aidata2025.dws.dws_oper_asa_keyword_collart_1d（ASA投放成本）<br><br>gzdw2024.gz_bi.dws_daily_app_reports（广州数据）<br>pubdata2025.ads.ads_atlasv_basic_data_daily_2024（杭州2024数据）
- 物理上游：`aidata2025.dim.dim_product_info`
- 物理上游：`hzdata.firebase.prefect_total_metrics_20*`
