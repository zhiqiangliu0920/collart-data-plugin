---
id: "company-dashboard-pipeline"
title: "公司看板数据流与对账边界"
project: "company"
kind: "lineage"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-538c697a64e8"]
tags: ["公司看板", "血缘", "加权", "对账"]
supersedes: []
verification_evidence: []
---

# 公司看板数据流与对账边界

已记录的数据流为 `pubdata2025.ads.ads_atlasv_basic_data_daily_1h` → 日期/团队/产品聚合 → product/group/line/company 四层 → daily_metric → 看板。

公共费用只在 company 层附加；源留存按新增人数加权。sync_run 记录批次，不是业务事实表。只读对账应从同一源按相同业务键生成预期，与已有目标比较，不执行原脚本的写入步骤。

来源窗口为 2026-05-23～08-21，原脚本只查 dev 与最新日期。该链路记录不证明当前生产调度与完整覆盖。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [1company/lineage/dashboard_pipeline.md](../../library/text/cd0889b6ee8b78f9a63519ed3d481d86339912a2229dd0acbb5f0ba80f92c212.txt)
