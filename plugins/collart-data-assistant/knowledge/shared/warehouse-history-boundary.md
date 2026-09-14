---
id: "shared-warehouse-history-boundary"
title: "仓库历史依赖与当前选表"
project: "shared"
kind: "lineage"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-3e325ef95b0e", "review-20260914-f1c2cc9a24d3", "review-20260914-6acb9bd4c056", "review-20260914-d827082c2233", "review-20260914-c862ce5dbfc5", "review-20260914-2ec5522ed31b"]
tags: ["血缘", "仓库", "历史字典", "schema"]
supersedes: []
verification_evidence: []
---

# 仓库历史依赖与当前选表

公司、Android、iOS 与 Web 新增 warehouse_sources 入口，汇总 2026-05-21 字典的显式上游依赖。它们用于定位加工关系，不能证明任务仍在调度、表仍在写入或字段仍然可用。未声明的依赖不推断，二段表名不擅自补项目。

当前分析先查对应产品现有 ADS 定义、schema、分区和口径；历史表和已废弃规则表不作为默认入口。旧链接目标移除时保留缺口，不能随便换成名字相近的新表。读取原始事件明细的历史血缘不构成超过最近 30 天限制的理由。

新增 iOS/Web tables README 用于导航，实际字段与业务范围仍以表正文及本次元数据为准。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [1company/lineage/warehouse_sources.md](../../library/text/60b1b4269ed67e442a40ae428e9bd582bc0708b15204182636d63bc298f03d8e.txt)
- [collart_android/lineage/warehouse_sources.md](../../library/text/0f4124de0ed893d232d583fed3e1078933922da2beaddd694b198388c75be4de.txt)
- [collart_ios/lineage/warehouse_sources.md](../../library/text/7efe570fe1392a1427fdbbb6bfdaeeb4f6b4ceedd02d239559d60aecab960e12.txt)
- [collart_web/lineage/warehouse_sources.md](../../library/text/83471c22d9ea913d755581b25a322d92c198c42a9f98505344e220d9751138c4.txt)
- [collart_ios/tables/README.md](../../library/text/524a00cb75dfe6ffb8476b2743f56bf420ccfb215adc021de2f4d4a58c5dc799.txt)
- [collart_web/tables/README.md](../../library/text/08ff43b677473c97c75baba271aa9ea0b879230d71c961c7d0e13707e684a90e.txt)
