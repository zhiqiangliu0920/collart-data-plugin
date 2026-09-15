---
id: "android.product"
title: "Android 产品流程与维度"
project: "collart_android"
kind: "business"
status: "documented"
sources: ["ai-knowledge:collart_android/lineage/lineage.md", "ai-knowledge:collart_android/product/core_metrics.md", "ai-knowledge:collart_android/product/home_screenshots.md"]
tags: ["首页", "产品", "功能", "Android"]
tables: []
---

# Android 产品流程与维度

## 产品与商业模式

Android 是图片/视频生成与编辑应用，含图生视频 img2video、文生视频 text2video、图生图 img2img、文生图 text2img、video_edit、AI Edit、移除、增强和动作同步。商业分析区分订阅、点数包及广告，成功收入定义见[支付与收入](../../shared/metrics/revenue.md)。

## 用户流程与维度

Discover 首页 → 分类/Banner/模板或功能入口 → 输入/配置 → 生成准备（VIP/广告）→ 任务开始与终态 → 结果展示/下载 → 付费。顶部含搜索、点数和设置；底部为 Discover、AI Video、AI Photo、Projects。源文未给出当前发布版本，不能把旧截图位置视为所有版本相同。

入口 home_feature_click 的 feature 与 service_type 是不同维度；完整对应放在[首页与服务事件](../events/events.md)。分析按国家、渠道、版本、新老、VIP、服务类型及入口拆分，不能从位置直接推断转化因果。

包名 free.ai.photo.generator.collart.ai，使用 aidata2025.ads_collartandroid。设备 pseudo 与登录账号分开。原始事件共享 storytemplate 库，必须按包名过滤且只读最近 7 天。旧“功能使用最高/最低”“固定 DAU 规模”和截图内点数不是稳定知识，已退出本页。

## 加工链路与渠道边界

GA4 → DWD → Android DM → active / 热事件表 → profile 与 attr/country/daily。连接行为与收入前分别收敛到业务键，事件 × 订单直接多对多会放大金额；留存按 cohort 起点与目标活跃日期连接，不只按用户。

traffic_src_type 为 delivery/inhouse/kol/nature，traffic_src_platform 为 ga_delivery/fb_delivery/x_delivery/tt_delivery/other_delivery 等。Instagram 归 fb_delivery；sptt- / tt_official 为 KOL，不是 TT 付费。资料中的 profile 首次非空/历史 delivery 优先策略需以对应版本源码为准；type/name/platform 必须来自同一来源行。
