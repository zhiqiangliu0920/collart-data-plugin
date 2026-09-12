# Collart 团队数据助手 · 安装包

一个插件，两个入口，共享同一份业务知识。仅公司内部使用。插件正文位于 [plugins/collart-data-assistant](plugins/collart-data-assistant/README.md)。

## 同事安装

1. 将完整 ZIP 解压到自己长期保留的目录，路径可以与作者不同；不要只复制 skills 子目录。
2. 使用已登录且支持 plugin 命令的 Codex。PowerShell 进入本目录后运行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

这仅对本次脚本进程设定执行策略。安装脚本先注册本地 marketplace，再安装 `collart-data-assistant`，不下载 Python 或数据库凭证。若公司策略禁止运行脚本，可按脚本中的两条 Codex 命令手动安装。

3. 开启一个新 Codex 任务，例如：“使用 Collart 数据分析，分析 Web 最近 7 个完整日的收入变化”。要沉淀时说：“使用 Collart 知识维护，把这份字段说明更新到团队知识”。可在技能列表选择对应入口。
4. 数据查询使用同事自己的已有连接与权限；没有连接仍能阅读知识、生成 SQL。检索和维护脚本使用 Python 3.10+ 标准库；没有 Python 时可直接读知识索引。

## 更新和维护

维护者改 [统一源码](plugins/collart-data-assistant/README.md)，运行检查、记录版本后发布新包；同事替换自己的发行副本并重新运行 install.ps1，然后开新任务。旧安装是缓存版本，不会随 OneDrive 文件变化即时更新。安装目录应长期保留以供后续更新。

维护者电脑已配置从本私有仓库到插件的周期同步，默认每 30 分钟检查；详见 [同步说明](SYNC.md)。此配置不会自动部署到其他同事电脑，同事仍可按本页手动更新，或在自己的 Codex 中设置同样的周期检查。

marketplace 的本地标识由脚手架默认设为 `personal`，只是安装来源名称，并不意味着对外公开。若同事已有同名 marketplace 指向其他目录，安装脚本会拒绝覆盖；由同事与维护者先确认来源命名冲突，再处理安装配置。

避免在同一次分析里同时选择旧 collart-biz-analysis、旧 team-data-knowledge 和新插件。原两个目录保留用于历史对照，新知识维护集中在此插件。未自动卸载或改动任何旧技能。

当前版本通过本私有仓库分发，未发布到公共市场。无需 node_modules、虚拟环境或大型构建目录。

## 手动安装顺序

```powershell
$distributionRoot = (Get-Location).Path
$marketplaceName = (Get-Content .agents/plugins/marketplace.json -Raw | ConvertFrom-Json).name
codex plugin marketplace add "$distributionRoot"
# 上一步成功后再执行：
codex plugin add "collart-data-assistant@$marketplaceName"
```

安装命令按本机 Codex CLI 的 plugin help 核对。插件支持范围参见 [整合记录](plugins/collart-data-assistant/docs/integration.md)，维护机制参见 [维护说明](plugins/collart-data-assistant/docs/maintenance.md)。
