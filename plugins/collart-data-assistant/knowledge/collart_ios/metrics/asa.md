---
id: "ios.asa"
title: "VidArt ASA 归因、关键词成本与历史边界"
project: "collart_ios"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_ios/indicators/asa_delivery.md", "sql:asa-cost"]
tags: ["ASA", "关键词", "投放", "VidArt"]
tables: ["aidata2025.dws.dws_oper_asa_delivery_di"]
review_required: true
---

# VidArt ASA 归因、关键词成本与历史边界

## 使用场景

经营成本使用当前 cdct / country.delivery 口径；关键词归因诊断使用 aidata2025.dws.dws_oper_asa_delivery_di（已捕获该表 schema 与 SQLX）。两者粒度不同，不按文档日期简单替换。旧“ads_collartios 为空”是 2026-07 快照，当前已有表元数据，仍未验证业务日期全覆盖。

## 关键词成本

资料定义粒度 event_date × campaign_id × adgroup_id × keyword_id × country，使用 cost_usd / cost_cny，包含 is_keyword_attributed=FALSE 的无关键词投放。VidArt 使用 bundle package_name 过滤；旧 ASA 账号混有其他产品，仅看到最近无别的投放不能取消过滤。campaign 历史名字用 VidArt% 辅助判断，不替代当前产品映射。

源 ODS 曾存在整行重报。直读旧 ODS 时按日期、adgroup、keyword、country 排序取**整行**，不可分别 MAX 各指标。Max Conversion 无关键词时用 campaign 合计减关键词合计核对残差，避免漏计。当前 DWS 已把去重、币种和残差纳入加工，使用前查对应源码。

## 币种与关联

ASA local_spend 为人民币，GA4 event_value_in_usd 为美元。手动换汇用 exchange_rate_days 的 currency='CNY'，不是 RMB；stats_date 按实际类型转换。没有汇率的日期不得因 INNER JOIN 或 SUM NULL 静默丢失；当日用最近有效汇率须明确标注。

keyword_id / country 可能 NULL；使用统一 no_keyword 占位再关联。用户归因先收敛为一用户一行，不能按 user × date × keyword 构造 NULL 行后再按 user 连接导致收入双算。成本与用户来源可能有彼此独有国家/日期，使用并集骨架避免丢收入。ASA country_region 是两位码；GA4 geo.country 是英文国家名，维表字段名 country_name_3 历史虽称 3 实为该两位映射，需验证实际值。

## 用户侧三级归因

user_properties.campaignID/keywordID → firebase_campaign 参数 campaign/term → traffic_source.name（source='Apple'）。属性不保证在 first_open 上。已写入 DM traffic_src.campaign_id/keyword_id 和 active 的归因快照时优先读取；不能为“全生命周期回填”扫描七天以外的原始埋点。超出范围需要既有汇总，缺失就保留归因缺口。

资料边界：成本起点记为 2026-05-19；用户级归因 2026-07-20 前无信号；DWD 参数/属性 2026-07-26 起才较完整；2026-07-01～07-06 的部分成本缺 keyword_id。均为历史证据，不能推断后续日期一直完整。旧 dws_oper_asa_collart_1d / dws_oper_asa_keyword_collart_1d 本次元数据未找到，退出当前推荐。

## 收入与执行入口

IAP event_value_in_usd 是客户端毛额；资料中订阅×0.85、点数包×0.70 仅历史净额估算，Apple 实际结算另核。vip_subscribe_succeed 无金额只能计数。ROI/ROAS 保持成本币种、cohort、归因和收入窗口一致。

`sql:asa-cost` 是参数化关键词成本 SELECT；表字典见[ASA 成本](../tables/aidata2025.dws.dws_oper_asa_delivery_di.md)。原始探查仅最近 7 天且限定 VidArt bundle、排除 manual_install/debug。
