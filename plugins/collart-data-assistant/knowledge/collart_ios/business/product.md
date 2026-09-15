---
id: "ios.product"
title: "VidArt 产品、身份与渠道"
project: "collart_ios"
kind: "business"
status: "documented"
sources: ["ai-knowledge:collart_ios/indicators/asa_delivery.md", "previous:shared-project-overview"]
tags: ["VidArt", "iOS", "产品", "身份"]
tables: ["vidart-8b8ca.analytics_528583115.events_*"]
---

# VidArt 产品、身份与渠道

VidArt 是当前 iOS 分析范围，bundle 为 ai.photo.video.generator.fotos.ai.image.picture.editor.app.free，和旧 Collart iOS 包分开。AI 服务包含 aiVideoI2V/R2V/T2V/aiGeneral，订阅与点数包并存。设备 user_pseudo_id 与服务端账号 user_id 不等价；付费人群分析先确定成功交易和映射截止时间。

GA4 位于 vidart-8b8ca.analytics_528583115.events_*，过滤 bundle，并排除 manual_install / debug。ADS 使用 aidata2025.ads_collartios，2026-07“ADS 为空”旧快照已退出默认口径；当前已捕获其表结构，未证明分区最新或业务全量覆盖。ASA 渠道历史方法见 [ios.asa](../metrics/asa.md)，完整页面/UI 埋点定义仍有缺口。
