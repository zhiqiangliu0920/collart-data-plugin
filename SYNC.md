# 知识库同步到插件

同步方向为 **本仓库 `main` → 本机插件源码 → Codex 已安装插件缓存**。知识与两个 skill 本来就在同一仓库中；同步后对插件全部文件逐一比较哈希，不能只看安装命令是否成功。

## 已配置的方式

维护者电脑由当前 Codex 任务的周期检查每 30 分钟检查一次 GitHub 提交。使用已连接的 GitHub 插件读取私有仓库，不在脚本中保存令牌，不要求 Git 命令另行登录。只有检查通过的更新才进入本机插件。

这是本机配置，不会替同事开启后台任务。电脑离线、Codex 未运行或账号额度/连接不可用时可能延后，恢复后再检查。安装更新后请开启新 Codex 任务使用；正在运行的任务不会强制重启。

同事可以克隆本仓库后按 INSTALL.md 更新插件；要自动同步，需要在各自电脑上配置同样的周期检查和各自的 GitHub 访问权限。不要复制维护者的登录态或同步状态目录。

## 主版本与本地修改

- `main` 是共享发布版本。已验证的知识修改提交到本仓库后，周期检查会分发到本机插件。
- 本地源码如有未发布修改，自动同步会停止该次更新并保留修改。先审阅并提交或合并，再重新建立与共享版本一致的基线；不得通过删状态、强制覆盖或改哈希绕过冲突。
- 本流程不自动把原始 ai-knowledge、历史报告或私人配置上传。把分析结果沉淀为知识仍需保留来源、适用窗口和验证状态。
- 本地安装版本使用 Codex 官方 helper 添加 `+codex.<时间戳>` 缓存后缀。该后缀留在本地，不需要反向提交到共享仓库。

## 同步工具

`scripts/sync_plugin.py` 使用 Python 3.10+ 标准库，要求本机已有 Codex CLI、已安装启用的 `collart-data-assistant@personal` 和官方 plugin-creator helpers。工具不会自动启用已禁用插件或改变 marketplace 来源。

维护者先确认已注册的 marketplace 对应工作副本，初始化一次基线：

```powershell
python scripts/sync_plugin.py init --root "<发行目录>"
python scripts/sync_plugin.py status --root "<发行目录>"
python scripts/sync_plugin.py apply --root "<发行目录>" --snapshot "<已验证的仓库快照.json>"
```

同步状态默认保存在当前用户的 `.codex/collart-knowledge-sync`，包括最后成功提交、源码哈希、已安装版本和更新前备份；它不进入仓库。`status` 比较实际源码与基线，同时核对已安装缓存。`apply` 检查本地冲突、快照哈希、基础凭证模式及知识结构，调用官方 helper 刷新缓存版本，通过 Codex CLI 重装，再验证缓存。失败时恢复源码并尝试重装之前的版本；失败详情和备份保留供处理。

快照采用 UTF-8 JSON，结构如下；`files` 必须来自指定提交的完整递归 Git 树，不能用代码搜索结果代替：

```json
{
  "repository": "zhiqiangliu0920/collart-ai-knowledge",
  "commit": "完整40位提交SHA",
  "files": [
    {"path": "仓库内相对路径", "sha": "Git blob SHA", "content": "完整UTF-8正文"}
  ]
}
```

GitHub 连接器负责确认仓库为 private、读取 `refs/heads/main`、该提交的 tree 和全部 blob。仅接受普通文本文件；拒绝截断的树、符号链接和 submodule。可复用本地上次快照中 blob SHA 相同的正文，只读取变化内容。完整校验后将快照交给同步脚本。

无新提交且源码和缓存一致时无需安装。出现本地修改、连接失败、marketplace 变更或检查失败时保留现有可用版本并报告。每次更新完成记录提交 SHA 和安装版本。

## 验证

```sh
python -B -m unittest discover -s tests -v
python -B plugins/collart-data-assistant/scripts/kb.py check
```

本工具的文件名和常见凭证模式检查不是完整保密审查；知识来源和业务正确性仍按维护规范处理。插件更新生效边界参见 [OpenAI 插件文档](https://learn.chatgpt.com/docs/plugins)。
