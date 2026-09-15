---
name: collart-knowledge-maintain
description: 将已确认的 Collart 表字段、业务规则、指标口径、事件语义、分析经验及来源变化沉淀或纠正到团队知识；普通查数走 collart-analysis。
---

# Collart 知识维护

只编辑获授权的团队知识源码。安装缓存是分发副本，不是长期编辑源；无法访问源码时在当前任务整理可审阅的 Markdown 变更。数据权限仍只读，原始事件最多最近 **7 天**，不得修改生产表或 Dataform 任务。

## 最小维护流程

1. 用 search/read 找到已有条目，优先修正其正文；不要另建一份近义说明。
2. 按项目的业务、表字典、埋点、指标、分析方法归位；公共规则/物理表只维护一份。公式与边界放指标，分析方法引用它们，完整字段与 SQLX 关联放表字典。
3. 记录来源 ID、相对定位、版本/捕获日期和哈希；区分 schema 已观察、源码静态依据与生产结果验证。缺失或冲突标 review_required，不能靠整理日期宣称 verified。
4. 保留旧 ID 到新条目的机器映射。来源变化先进入 review queue，核对受影响知识再更新证据；构建不得重新导入 library/presets/provenance。
5. 源码仓库运行 `python -X utf8 scripts/build.py`、`python -m unittest discover -s tests` 和 `python -X utf8 scripts/build.py --check`；发布与本机安装遵循已获得的用户授权。

不沉淀经营数据快照、单次报告、内部账号、凭证、私人路径和一次性运行脚本。完整流程和迁移历史位于 [GitHub maintainer](https://github.com/zhiqiangliu0920/collart-data-plugin/tree/main/maintainer)，无需分析时加载。
