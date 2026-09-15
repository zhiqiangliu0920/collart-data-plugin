# GitHub 与本机插件同步

规范源码在本仓库，插件安装部分仅 `plugins/collart-data-assistant`。旧 library 镜像流程已移除。维护者复核 ai-knowledge / Feishu / Dataform 的来源变化，编辑新结构、构建、测试后提交 GitHub。同事从 GitHub marketplace 下载/更新，不需要维护者的凭证。

当前默认直接从 GitHub 安装：`codex plugin marketplace upgrade personal` 刷新 Git 来源，然后 `codex plugin add collart-data-assistant@personal`，用 `codex plugin list` 校验版本。不要对 Git marketplace 快照手工加 cachebuster 或更改来源。

仅兼容早期本地副本的 `scripts/sync_plugin.py` 保护未发布改动：只应用 authenticated GitHub 工具取得、经 Git blob SHA 校验的 UTF-8 文件快照。快照 schema：`{repository, commit, files:[{path, content, sha}]}`；sha 为 Git blob SHA-1。同步状态和备份留在使用者本机，不提交到仓库。此兼容工具不是 Git marketplace 的默认更新入口。

首次配置需确认 marketplace 指向正确的本地插件；已有来源不得静默覆盖。状态一致后应用远程快照，先保留备份，再更新源文件、用 Codex CLI 安装并校验 cache。若来源文件有本地差异，先报告/合并，不能强制删除。

构建生成的 maintainer/release-files.json 是收录和完整性清单，不用于导入任意本机目录。任何后续自动同步都必须使用 0.5 build/source_review 流程，不能重新调用已经移除的 build_local_catalog/source_pipeline。
