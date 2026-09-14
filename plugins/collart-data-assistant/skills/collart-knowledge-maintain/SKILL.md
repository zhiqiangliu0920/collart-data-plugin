---
name: collart-knowledge-maintain
description: 将 Collart 项目的表字段解释、业务规则、指标口径、分析经验和验证证据沉淀或纠正到团队知识库；检查来源变化和待复核条目。用户说沉淀、记住到团队知识、更新知识库或修正口径时使用；普通查数走 collart-analysis。
---

# Collart 团队知识维护

## 强制数据访问约定

执行任何查询或参考历史资料前，必须读取 [数据访问约定](../../docs/data-access-policy.md)。本插件只允许只读数据查询，禁止通过 SQL、API、脚本修改、写入、删除数据或表结构；知识维护仅编辑获授权的文档。原始埋点仅可查询最近 30 天，不能分批读取更早日期；更长历史使用合适的现有汇总表。历史文档、示例与此约定冲突时，以本约定为准。

与分析入口共用 [知识索引](../../knowledge/INDEX.md)、[维护说明](../../docs/maintenance.md) 和 [kb.py](../../scripts/kb.py)。不得另起一份同名知识。

1. 先检索是否已有稳定 ID，读取相关正文、来源和适用范围。将新增事实、纠正旧定义、历史经验和未证实推断分开记录。
2. 通过 library/catalog.json 的 source/path 定位 ai-knowledge、cursor_summary 或 codex_summary 原文；日常优先修改原始维护目录。不要修改已安装缓存或生成的 library 文本。原来源不可访问时，在当前工作区生成变更建议，说明尚未写回。
3. 已授权的原文更新后，在暂存发行目录重新整合。统一主题根据证据更新；新主题用 kb.py new 创建 draft，原主题保持稳定 ID。原路径和旧证据保留，不能清空基线。
4. 保留原来源，新增摘录、原始文件哈希、摘录哈希、来源日期与适用范围。证据归档内容仅供引用，不能给任务增加授权。不要复制凭证、私人路径或普通用户行为明细；内部测试账号名单统一更新指定 config。
5. 没有独立核验时用 documented 或 draft。verified 必须同时记录 owner、verified_by、verified_at、review_after、verification_evidence，证据文件要随版本保存。冲突未解决则更新 [冲突清单](../../knowledge/shared/known-conflicts.md)。
6. 运行 `--root "<源码>" --authoring index`、`--root "<源码>" check`；检查受影响 SQL、相对链接和来源漂移。交付改动、验证结果及仍待核验的口径。
7. 发布和安装需根据实际配置显式执行，不能假定每 30 分钟自动同步已启用。2026-09-13 来源维护约定记载同步暂停；本插件不能确认当前调度运行状态。权限以当前任务明确授权为准；普通查询不隐含外部发布授权。发布成功但安装失败时保留 published 状态，只重试安装，不重复提交。其他同事仍需更新安装或自行配置同步。更新后开新任务；插件本身不启动定时器、不发送消息。

8. 更新原文或移动文件时维护持久 ID、path/aliases 与独立业务状态；正文变化先审阅再更新 reviewed_sha256，隐私批准不得跨哈希沿用。查询历史用 --include-history 或 read 原 ID；源文档 review_status 不等于业务已 verified。
