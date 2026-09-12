---
id: "shared-internal-users"
title: "内部用户过滤"
project: "shared"
kind: "metric"
status: "documented"
updated_at: "2026-09-12"
verified_at: null
review_after: "2026-10-12"
owner: null
verified_by: null
effective_from: null
sources: ["cursor-internal-users-md"]
tags: ["internal-users", "内部用户过滤"]
supersedes: []
verification_evidence: []
---

# 内部用户过滤

## 合并的业务细节

来源为 Cursor 资料，按项目与层级适用；尚未独立查询核验。历史状态须复核，上文约束与明确的修正说明优先。

## 内部测试账号排除

Web/Fashion 统计在有可靠登录账号映射时排除内部测试账号。名单统一维护在 [内部账号配置](../../config/internal-user-ids.json)，由原资料的 18 个账号迁入，原始提供日期为 2026-06-23。不得把配置缺失当作空名单。

设备画像同时检查最后登录 `user_id` 和历史 `user_ids`；使用 EXISTS 防止展开数组造成重复。设备关联过内部账号时整设备排除是一种保守规则，可能连带其他登录者，正式统计需声明。若有事件时点账号映射，可采用时点排除并单独命名口径。

只有聚合表、或匿名设备无法可靠映射时，说明是否上游已经排除及剩余限制，不能宣称已精确排除。不要直接从汇总收入扣掉另一套口径的测试账号收入。SQL 示例见 [过滤模板](../../presets/internal_user_filter.sql)。

来源快照：[cursor-internal-users-md](../../provenance/excerpts/cursor-internal-users-md.txt)。
