---
id: "web.activity"
title: "Web 活跃、新增与成熟留存"
project: "collart_web"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_web/indicators/dau.md", "ai-knowledge:collart_web/indicators/new_user_pseudo_id.md", "ai-knowledge:collart_web/indicators/retention.md", "sql:web-cohort"]
tags: ["Web", "DNU", "DAU", "新增", "留存"]
tables: ["aidata2025.ads_collartweb.ads_oper_user_active_di", "aidata2025.ads_collartweb.ads_oper_user_profile_df"]
---

# Web 活跃、新增与成熟留存

## 当前经营入口

DAU / DNU / 留存先用 ads_collartweb 的 daily、country 和 active。DAU 计 is_active=TRUE 的去重 pseudo，收入骨架不计活跃；成熟留存公式见[公共指标](../../shared/metrics/activity.md)。旧 session_start UV 只命名为会话启动用户，不能覆盖经营 DAU。

## 首次发现与正式新增

设备首次发现 = 该 user_pseudo_id 在目标业务范围的最早已知事件日；first_visit 是事件线索，可能漏报、迟报、跨域或清 Cookie 重置，不能单凭最近窗口证明终身新增。正式 is_new 以当前 active 的加工规则为准，专题“首次发现新人”与经营 DNU 不完全一致时须分别命名。

首落地页 = 第一次 page_view 的完整 page_location，首落地路径为其 path；事件参数、日时区和最早时间排序需明确。旧 DWD 的 event_page 曾不含 page_view URL，不能假定可替代原始参数。长期首次记录优先读已维护的画像与历史汇总；当前七天原始扫描仅能产出“窗口首次观察”，不能用作 lifetime cohort。

## 身份、范围与分母

UV 按设备 pseudo；user_id 仅补充账号/收入关联，二者多对多。账号查画像同时匹配 user_id 和 user_ids，不能仅按数组或只按最后账号。主站原始过滤需要 app_info.id IS NULL **且**页面不属于 studio/fashion；空页面归属单列。加工层 collart_web 与旧 collartweb 拼写的差异需查对应表。

cohort_date=target_date 为该日新人；在 [start,end] 为窗口新人；此前首次发现为老用户。渠道/国家/版本按同一归因时点，不能用未来登录映射改变历史 cohort。

## 历史替代与查询

旧 ads_oper_user_new_collartweb_di / dwd_oper_user_collartweb_di 及有界 MIN(event_date) 脚本退出默认推荐。旧 latest_user_id 按字符串排序不等于末次登录。采用 `sql:web-cohort` 从当前画像按 first_open_date 取设备 cohort 时，仍需先核验该字段的首次发现定义、历史覆盖和内部用户范围。

相关表：[画像字典](../tables/aidata2025.ads_collartweb.ads_oper_user_profile_df.md)、[active 字典](../tables/aidata2025.ads_collartweb.ads_oper_user_active_di.md)。
