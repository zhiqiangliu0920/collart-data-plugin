---
id: "shared-data-access-policy"
title: "只读查询与原始埋点最近30天限制"
project: "shared"
kind: "sql"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: null
owner: null
verified_by: null
effective_from: "2026-09-14"
sources: ["maintainer-data-access-20260914"]
tags: ["只读", "禁止写入", "禁止删表", "原始埋点", "最近30天"]
supersedes: []
verification_evidence: []
---

# 只读查询与原始埋点最近30天限制

维护者于 2026-09-14 明确：只读数据，禁止写入、删除和修改数据表；原始埋点只能查询过去 30 天的数据。

执行前读取 [完整约定](../../docs/data-access-policy.md)。默认最近 30 个完整日，不能选任意历史 30 天、分批扫更早分片、通过视图或原始明细副本绕过。长历史分析使用合适的既有汇总表；无法回答时说明限制，不建表回填。知识维护仅涉及授权的文档编辑，不授予数据库写权限。

来源：[维护者本次要求](../../provenance/excerpts/maintainer-data-access-20260914.txt)。这是插件使用约定，不表示账号权限已在数据库中配置。
