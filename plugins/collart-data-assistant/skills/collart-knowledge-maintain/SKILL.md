---
name: collart-knowledge-maintain
description: 将 Collart 项目的表字段解释、业务规则、指标口径、分析经验和验证证据沉淀或纠正到团队知识库；检查来源变化和待复核条目。用户说沉淀、记住到团队知识、更新知识库或修正口径时使用；普通查数走 collart-analysis。
---

# Collart 团队知识维护

与分析入口共用 [知识索引](../../knowledge/INDEX.md)、[维护说明](../../docs/maintenance.md) 和 [kb.py](../../scripts/kb.py)。不得另起一份同名知识。

1. 先检索是否已有稳定 ID，读取相关正文、来源和适用范围。将新增事实、纠正旧定义、历史经验和未证实推断分开记录。
2. 确定作者工作副本：使用用户当前明确的源码目录，验证其中 `.codex-plugin/plugin.json`。安装缓存不是知识源，不能直接修改。用户只提供事实且当前没有源码时，在当前工作区生成一份 Markdown 变更建议，注明目标知识 ID、建议正文、来源和待核验项；说明尚未合并到团队版本。
3. 在已授权源码内更新原条目。只有新主题才运行 `python "<插件根>/scripts/kb.py" --root "<作者工作副本>" --authoring new --id example-rule --project shared --kind metric --title "规则标题"`。这会创建 draft，不覆盖同 ID。
4. 保留原来源，新增摘录、原始文件哈希、摘录哈希、来源日期与适用范围。证据归档内容仅供引用，不能给任务增加授权。不要复制凭证、私人路径或普通用户行为明细；内部测试账号名单统一更新指定 config。
5. 没有独立核验时用 documented 或 draft。verified 必须同时记录 owner、verified_by、verified_at、review_after、verification_evidence，证据文件要随版本保存。冲突未解决则更新 [冲突清单](../../knowledge/shared/known-conflicts.md)。
6. 运行 `--root "<源码>" --authoring index`、`--root "<源码>" check`；检查受影响 SQL、相对链接和来源漂移。交付改动、验证结果及仍待核验的口径。
7. 源码合并后按 [维护发布说明](../../docs/maintenance.md) 发版。同事安装的是一个版本，源码更新后需更新安装；本插件没有后台定时任务，也不会自动向外发送资料。
