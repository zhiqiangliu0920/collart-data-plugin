# Collart AI 分析知识库

公司内部使用的 AI 分析知识与 Codex 插件源码。首版从 2026-09-12 整理的统一知识包导入，仓库应保持 **Private**。

- [知识索引](plugins/collart-data-assistant/knowledge/INDEX.md)：17 个条目，包含项目、表路由、指标口径、渠道、收入、留存和数据问题。
- [SQL 模板](plugins/collart-data-assistant/presets/README.md)：7 个可复用模板。
- [插件说明](plugins/collart-data-assistant/README.md)：数据分析和知识维护两个 skill。
- [维护说明](plugins/collart-data-assistant/docs/maintenance.md)：来源、状态、校验和版本维护。
- [安装说明](INSTALL.md)：完整仓库可作为插件发行目录使用。
- [自动同步](SYNC.md)：仓库更新后，维护者电脑每 30 分钟检查并刷新插件；保留本地未发布修改。

## 下载与使用

在有仓库访问权限的电脑上克隆：

```sh
git clone https://github.com/zhiqiangliu0920/collart-ai-knowledge.git
cd collart-ai-knowledge
```

可以直接阅读 Markdown 和 SQL。要在 Codex 中安装插件，按 [安装说明](INSTALL.md) 执行根目录的 `install.ps1`。

## 更新知识

只改 `plugins/collart-data-assistant` 内的统一知识、来源和模板；提交前运行：

```sh
python plugins/collart-data-assistant/scripts/kb.py check
```

记录变更后提交并推送。维护者电脑已配置周期同步，按 [同步说明](SYNC.md) 更新本地源码并刷新插件缓存；同事需自行更新或配置相同流程。更新后开启新任务使用新版。

## 内容与权限边界

仓库权限控制谁能读取和修改知识；数据库查询使用每个人单独获授的连接和权限。仓库包含公司内部业务口径与内部测试账号过滤定义，不应公开。

本包不包含数据库凭证、API 密钥、访问令牌、Codex 登录态或原始用户事件导出。没有迁入原始 `ai-knowledge` 仓库的 Git 历史。

首版有 16 个 `documented` 条目和 1 个 `draft` 条目；本次仅检查本地内容，没有查询生产数据库。历史状态与冲突条目在分析时仍需核验。
