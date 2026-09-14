---
id: "shared-knowledge-maintenance-boundary"
title: "知识维护、项目产物与同步状态"
project: "shared"
kind: "playbook"
status: "documented"
updated_at: "2026-09-14"
verified_at: null
review_after: "2026-10-14"
owner: null
verified_by: null
effective_from: null
sources: ["review-20260914-17fea906079e"]
tags: ["知识维护", "同步", "报告", "SQL"]
supersedes: []
verification_evidence: []
---

# 知识维护、项目产物与同步状态

长期表定义、事件、指标、分析方法、血缘和可复用只读 SQL 维护在知识库。一次性 SQL、脚本、报告与结果留在对应 Codex/Cursor 项目，提炼长期规则后再入库；旧规范表格仍指向知识库 reports/sql-snippets 时，以 2026-09-13 的维护约定为准。

来源注册保留稳定 ID、旧路径别名、哈希及迁出记录；纯迁移与正文变化分开，后者重新审阅，不能沿用旧内容批准。备份、插件、安装缓存和项目产物不反向成为知识输入。

2026-09-13 来源明确每 30 分钟同步任务暂停。本次文档与插件更新不代表该任务恢复，也不代表 GitHub 发布或同事安装完成；三种状态分别记录。

以上为静态资料对齐，未执行本次生产查询。涉及原始埋点时还须遵循[只读与最近 30 天约定](../../docs/data-access-policy.md)。

## 2026-09-14 对齐依据

- [0global/KNOWLEDGE_MAINTENANCE.md](../../library/text/c9ce5c3d08ce5301677cfb9e479b55a7cad5f0c8fc979528251b8071edb2b83d.txt)
