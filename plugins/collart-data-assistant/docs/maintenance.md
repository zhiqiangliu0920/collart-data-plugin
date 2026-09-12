# 知识维护与发布

分析和维护读取同一份 knowledge。日常只更新这套规范正文；provenance 的快照冻结来源，旧版两个独立 skill 不再作为新插件的第二套运行入口。

## 状态与证据

- draft：提议或冲突未解决，不作已确认口径。
- documented：有来源依据，未独立查询或负责人确认。本次整理的正常条目均为此状态。
- verified：记录具体核验范围、负责人、核验人、日期、到期日及本地证据。结构校验不能把条目自动变成 verified。
- deprecated：保留旧定义与失效范围，用 supersedes 指向被替代的稳定 ID；同一个 ID 的一般修订保留在版本历史。

元数据值使用 JSON 字面量的 YAML 子集，例 `sources: ["source-id"]`、`verified_at: null`。来源登记位于 [sources.json](../provenance/sources.json)，每项保留 source_path、source_sha256、captured_at、locator、excerpt、excerpt_sha256。source_path 相对于团队原知识库根，运行时不依赖这些原文件。

## 操作

在作者的插件源码根执行以下 PowerShell 命令；不要在安装缓存中编辑：

```powershell
$pluginRoot = (Get-Location).Path
python scripts/kb.py --root "$pluginRoot" --authoring new --id sample-rule --project shared --kind metric --title "新规则"
# 编辑 knowledge 中对应正文，补充来源，再生成索引。
python scripts/kb.py --root "$pluginRoot" --authoring index
python scripts/kb.py --root "$pluginRoot" check
python -B -m unittest discover -s tests -v
python scripts/kb.py source-check --source-root "<原始 ai-knowledge 根目录>"
```

new 只用于新主题；修改已有主题直接编辑原条目。search 从实时正文检索，check 能发现索引未更新。`check --strict` 会对 draft 和到期条目返回非零，适合复核提醒；发布是否允许已标明的 draft 由维护者明确记录。

source-check 只报告变动，不自动覆盖知识；需核实变动与分析结论的关联。若来源不可访问，报告 missing，不宣称已同步。历史摘录变更需说明原因并重新记录哈希，不以改哈希代替事实核验。

## 团队更新

选择一份公司内部源码作为主版本，每次修改记录变更说明和版本。其他同事提交修改建议或在独立分支修改，避免同时编辑 OneDrive 同一文件。当前只交付本地目录和 ZIP；尚未创建公司 Git 远端或定时同步。

正式内容更新提升语义版本；仅开发缓存刷新可用 `版本+codex.时间戳`。检查后重新打包 marketplace 根，排除 .git、缓存、依赖目录和私密内容。将新包交给同事后，由同事更新其解压源码，并重新执行根目录 install.ps1，随后开新任务。

推荐在一次分析结束、一个表结构或指标规则改动后更新知识；运行 check 查看到期项。自动巡检或生产同步需要另行配置，本版本不会自行启动。
