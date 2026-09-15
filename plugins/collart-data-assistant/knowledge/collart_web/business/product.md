---
id: "web.product"
title: "Web 页面流程、账号与站点边界"
project: "collart_web"
kind: "business"
status: "documented"
sources: ["ai-knowledge:collart_web/indicators/fashion_vs_main_site_user.md", "ai-knowledge:collart_web/lineage/lineage.md", "ai-knowledge:collart_web/product/core_metrics.md", "ai-knowledge:collart_web/product/page_structure.md"]
tags: ["Web", "产品", "页面", "身份"]
tables: ["storytemplate-10a27.analytics_232977577.events_*"]
---

# Web 页面流程、账号与站点边界

提供 AI 图片/视频生成和编辑；用户与设备关联见[身份映射](identity.md)，购买见[收入指标](../metrics/revenue.md)。以下功能和事件来自静态产品定义，使用前按实际版本核对。

## 页面层级

```
首页 (Home)
    │
    ├── AI Video 功能页
    │       ├── img2video
    │       ├── text2video
    │       └── frames_transition
    │
    ├── AI Image 功能页
    │       ├── img2img
    │       └── text2img
    │
    ├── AI Edit 功能页
    │       ├── faceretouch
    │       ├── improve
    │       └── remove
    │
    └── 其他工具页
            ├── AI Remove
            └── AI Upscale
```

## 埋点事件对应

| 页面 | 进入事件 | 参数 |
|------|---------|------|
| 首页 | page_view | page_location |
| AI Video | aivideo_edit_show | type |
| AI Image | aiimage_edit_show | type |
| AI Edit | aiedit_show | - |

## 先区分分析对象

| 对象 | 判定 | 使用限制 |
|---|---|---|
| 单次事件/页面 | page_location 命中 studio 或 fashion | 只说明该事件发生页面，不能代替用户全历史标签 |
| 指定窗口内的用户到访标签 | 按 user_pseudo_id 汇总是否至少有一次命中 | 未命中仅表示窗口内未观察到，不能写“从未到访” |
| 有充分历史覆盖的用户标签 | 曾命中过 Fashion 页面即带该到访标签 | 需要说明历史覆盖起点和缺失；不代表此人全部支付都属于 Fashion |
| 加工表产品行 | 按该表实际 package_name | 该行产品归属不等于用户终身归属 |
| 首次落地 cohort | 按经确认的首次页面来源 | 与任意一次到访标签分别计算，不能替换 |

共用原始表为 `storytemplate-10a27.analytics_232977577.events_*`，Web/App 区分使用 `app_info.id IS NULL`，主站还须排除下述 Fashion 页面。用户键采用 user_pseudo_id；user_id 映射仅在来源可靠时补充。新增定义见[活动指标](../metrics/activity.md)。

## 原始页面规则与覆盖

原记录的页面匹配为大小写不敏感的子串 `studio` 或 `fashion`。从 event_params 中提取 page_location，再在所需粒度聚合：

```text
REGEXP_CONTAINS(LOWER(COALESCE(page_location, '')), r'(studio|fashion)')
-- 用户窗口标签：按已固定窗口和 user_pseudo_id 使用 LOGICAL_OR 聚合。
```

提取缺失、空 URL 与明确主站页面应分别检查；NULL 经 COALESCE 后不命中，不能据此证明用户属于主站。新页面分类需核对真实 URL，保留旧报告的原匹配方法，不凭目录整理修改历史口径。

## 加工表版本

新四端 ADS/cdct 的本地文档和现有模板使用主站 `collart_web`，Fashion 使用 `collart_fashion`。2026-07-22 旧共享表文档出现主站值 `collartweb`，只作为具体旧表版本的历史枚举，不能全库替换或混用。

当前分析按具体表字典选择来源与过滤。旧 DWD 用户表及 ADS 同名表 已由用户确认废弃，不能继续作为推荐入口。

## 关联粒度

Web/Fashion 共用 DM 后按 package 分流，用户日 active / 热事件上卷指标，画像基于设备。原始事件内 user_properties 是参数集合，不是独立用户属性表。先按用户日、交易或会话聚合再关联，不能将多条事件直接 JOIN 多笔 orders。旧 Web 血缘里的 orders 示例与无日期上界 SQL 已退出，成功收入走 Stripe/ADS，原始逐条行为仍仅最近 7 天。
