---
id: "android.activity"
title: "Android DAU、新增与留存"
project: "collart_android"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:collart_android/indicators/dau.md", "ai-knowledge:collart_android/indicators/retention.md"]
tags: ["Android", "DAU", "DNU", "留存"]
tables: []
---

# Android DAU、新增与留存

## 活跃与新增

统一公式与成熟窗口见[公共活动指标](../../shared/metrics/activity.md)；选表见[路由](../../shared/business/routing.md)，默认 ads_collartandroid 的 daily/country/active。

日活跃按自然日、产品及明确用户键去重，新老用户均可计入且不要求登录。读取 active 按 `is_active` 计活跃，排除仅收入骨架行。设备 `user_pseudo_id` 与登录 `user_id` 不可混作一个键；跨国家、渠道或版本的 UV 不能直接相加。

正式新增、首次安装、首次观察和 active 的 `is_new` 需依据具体加工定义选择，不能相互替代。GA4 嵌套字段与加工表扁平字段按[表字典](../tables/README.md)分别读取。

## 留存与回访

新增留存以指定日新用户为 cohort；活跃回访以指定日活跃用户为 cohort。比率为 cohort 中目标日活跃人数 / cohort 人数；产品、用户键和活跃定义保持一致。

分析术语 D1 表示 cohort_date + 1，D7/D30 类推；不能据此推定物理 `retain_2`、`retain_7` 等字段后缀相同。必须核查 SQLX 的日序，公共字段映射见[公共活动指标](../../shared/metrics/activity.md)。

只比较完整观察的 cohort，零回访补零；未成熟和零分母为 NULL，不能当作流失。跨 cohort 汇总按总回访人数/总 cohort 人数重算，不平均日留存百分比。

## 趋势

不预置固定 DAU 或通用百分比告警阈值。按[活跃与首订诊断](../analysis/acquisition.md)分解规模、获客和回访，时间窗按[公共日期规则](../../shared/metrics/report-windows.md)。长期留存需要汇总或充分历史 cohort，不能通过扫描更早原始事件绕过七天限制。
