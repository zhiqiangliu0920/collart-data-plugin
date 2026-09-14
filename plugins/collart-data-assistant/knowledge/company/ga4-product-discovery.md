---
id: "company-ga4-product-discovery"
title: "新产品 GA4 摸底与诊断边界"
project: "company"
kind: "playbook"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-8dfb0b7e3a2a"]
tags: ["新产品", "GA4", "Vibedance", "数据质量"]
supersedes: []
verification_evidence: []
---

# 新产品 GA4 摸底与诊断边界

先确认数据权限、产品归属、表日期覆盖、用户键和事件参数类型；访问失败不等于无数据，LIMIT 不能控制原始扫描范围。旧 Vibedance 资料属于独立产品，放在 Android 历史目录不代表 Collart Android。

窗口内首次观察不能直接称首次使用或终身新增。D7/D30 留存需足够成熟的同一 cohort，分组比率按人数加权。用户行为步骤从真实产品流程映射事件，缺失事件保留待核验；参数同时检查 string/int/double/float。

比较版本、国家、渠道及同星期几，区分缺数、上报变化、投放变化与产品变化。通用 DAU、留存、漏斗合格线没有产品依据，不作为默认规则。报告和一次性 SQL 留在对应 Codex/Cursor 项目，长期定义和经验再提炼入知识库。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [1company/analysis_playbooks/ga4_new_product_discovery.md](../../library/text/1b3c0101426b1757cbaa9e2f0fec60380b77bb1650ffe2a33f1847a4220ea84d.txt)
