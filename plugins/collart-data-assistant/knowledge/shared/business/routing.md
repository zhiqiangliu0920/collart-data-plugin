---
id: "shared.routing"
title: "项目范围、选表与 ADS 回退"
project: "shared"
kind: "business"
status: "documented"
sources: ["policy:20260914", "previous:shared-project-overview", "previous:shared-table-routing", "previous:shared-warehouse-lineage", "sql:four-platform-daily", "sql:country-metrics"]
tags: ["ADS", "回退", "选表", "原始埋点", "无连接"]
tables: ["aidata2025.ads_collart.ads_dim_metric_rule"]
---

# 项目范围、选表与 ADS 回退

## 四端标识

| 项目 | ADS 数据集 | 加工层产品值 | 原始产品过滤 |
|---|---|---|---|
| Android | aidata2025.ads_collartandroid | free.ai.photo.generator.collart.ai | app_info.id 为该包 |
| iOS / VidArt | aidata2025.ads_collartios | ai.photo.video.generator.fotos.ai.image.picture.editor.app.free | app_info.id 为该 bundle；排除 manual_install / debug |
| Web | aidata2025.ads_collartweb | collart_web | app_info.id IS NULL，再限定主站页面归属 |
| Fashion | aidata2025.ads_collartfashion | collart_fashion | app_info.id IS NULL，再限定 studio/fashion |

Web/Fashion 共用物理事件、Stripe 与 Web DM 表，公共表只保存一份字典；各端说明边界差异。

## 按问题选表

| 问题 | 表族 | 粒度与检查 |
|---|---|---|
| 总量趋势 | ads_oper_basic_indicator_daily_di | 日期 × 项目；核对完整日 |
| 国家贡献 | ads_oper_basic_indicator_country_di | 日期 × 国家；不要重复加总计行 |
| 渠道、版本、新老、VIP | ads_oper_basic_indicator_attr_di | 日期 × 维度组合；UV 不跨桶随意相加 |
| 用户日行为/收入 | ads_oper_user_active_di | 日期 × pseudo；DAU 筛 is_active，金额不过滤 |
| 设备画像/历史账号 | ads_oper_user_profile_df | pseudo 一行；账号多对多，滚动字段需看刷新逻辑 |
| 热事件漏斗 | ads_oper_user_event_metric_di / event_metric_attr / event_metric_country | 稀疏事件表，完整分母来自 active/cohort |
| 冷事件或参数 | ads_collart.ads_dim_metric_rule → 项目 DM → GA4 | 校验事件参数；逐条行为均限最近 7 天 |

## ADS 无法使用时

先区分无权限、无表/字段、缺日、粒度不适用和口径冲突。不要把失败或空结果当成业务为零。相关表字典列出实际 schema 捕获状态与来源。

规则表优先使用 `aidata2025.ads_collart.ads_dim_metric_rule`，按 app_name 过滤；is_materialized 不证明线上已有列。检查对应项目 DM 是否有需要的参数；仍缺才查 GA4。Android/Web/Fashion 用 storytemplate 事件库，VidArt 用 vidart 事件库。每个扫描遵守最近 7 天、产品和日期上下界。

超过最近 7 天且没有合适汇总时，明确不能完成这段历史的原始重算，交付可用汇总范围与缺口。不能偷偷放宽原始限制。没有连接时按只读约定交付查询草稿。

## 来源可信度

当前表 schema 来自 2026-09-14 BigQuery 元数据。Dataform 使用 releaseConfig 指向的已编译版本源码，不是工作区未发布编辑；这不等于已经确认最近一次生产工作流成功执行了该版本。字段业务解释来自源码/飞书/本地知识，冲突处分别保留来源，分析前按需要核验。

## 关联查询

- [四端日报](../sql/four-platform-daily.sql)（sql:four-platform-daily）
- [国家指标](../sql/country-metrics.sql)（sql:country-metrics）

执行前检查参数、字段、日期覆盖和金额/人群范围。
