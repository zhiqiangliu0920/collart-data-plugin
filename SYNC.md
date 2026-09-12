# 三来源整合、发布与安装

`ai-knowledge + cursor_summary + codex_summary → 暂存整合 → private GitHub main → 本机插件`

维护者沿用现有每 30 分钟 Codex heartbeat。原目录继续维护。任务使用已连接 GitHub 访问私有仓库，脚本不持有令牌。电脑离线、Codex 未运行或连接不可用时延后，恢复后重试。新任务使用更新后的插件。

## 本机配置和基线

源路径配置放在用户本机 `.codex/collart-knowledge-sync/inputs.json`：sources 指定三个互不重叠的输入根，distribution 指向已安装来源。reviews 按源文件 SHA-256 保存复核决定，内容改变后失效。不把配置和原始审核台账上传。

- state.json：最后成功安装提交、源码与缓存哈希、版本和备份。保留现有同步历史，禁止删除或重置来消除差异。
- release-proposal.json：本次候选文件、远端基准与冲突。
- release-status.json：已发布提交、来源指纹、快照位置及独立的 installation 状态。
- snapshots：GitHub 完整文本快照，可复用 blob SHA 相同的正文。

## 每次运行的顺序

1. 获取本机互斥运行锁；读取 release-status 与 state。若已发布但未安装，先读取已保存且哈希有效的快照重试安装，成功后记录 installed。网络不可用不阻止使用已验证快照重试安装。
2. sync_plugin.py status 核对源码与缓存。有未发布本地改动时保留原件，不覆盖，转入三方审查。有缓存故障时保留独立失败状态，不重复发布。
3. 通过 GitHub 连接读取 main、commit、递归 tree；确认 private、无截断、仅普通文件。变化 blob 必须读取正文并核对 Git blob SHA，未变正文可复用上次快照。不能用代码搜索代替完整树。
4. 在输入目录之外建立暂存发行目录，以本机上次快照、当前远端和本地修改做三方比较。保留远端新增与修改。碰撞文件保留双方并进入待处理；main 不是旧基线时先纳入远端变更再构建。
5. 运行 source_pipeline.py --config <inputs.json> --stage <暂存发行目录> --audit <本机审核输出>。完整读取可用文本，排除凭证、个人配置、原始用户明细、临时产物、目录链接及插件/发布/索引输出。生成全文资料、去重映射、日期与来源图，保留旧来源证据。
6. 阅读新增/变化原文、pending 与 topic_impacts。主题事实改变或互相矛盾时保留旧证据并标记待复核，不能凭更新时间认定新口径正确。无歧义内容自动整合；无独立证据不提升为 verified。必要时改暂存 knowledge，再运行 kb.py index。更新本机目录用 build_local_catalog.py，索引不是输入。
7. 运行 kb.py check、受影响测试及整包凭证检查。正式主题引用的旧摘录必须保留；全文引用按 source ID 映射解析。待处理项不包含敏感正文。
8. release_state.py prepare 与最新远端快照比较。没有差异就结束，不制造时间戳或版本提交。冲突影响关联索引/主题时隔离整个关联变更；只有合成结果再次通过完整检查的无冲突部分可以发布。
9. GitHub create_tree 基于刚读取的远端 tree，仅写实际差异；create_commit 的 parent 为该远端提交。更新 ref 前重新读取 main；若变化则重新三方合并与验证。update_ref 必须 force=false。权限或断网失败保留候选，不推进发布/安装基线。
10. 重新读取发布树并核对全部 path/blob SHA，保存完整 snapshot。先用 release_state.py published 保存发布成功与 installation=pending，再调用 sync_plugin.py apply；成功后 release_state.py installed。

## 命令入口

- `python -B scripts/source_pipeline.py --config <本机配置> --stage <暂存目录> --audit <本机审计.json>`
- `python -B plugins/collart-data-assistant/scripts/kb.py check`
- `python -B scripts/release_state.py prepare --state-root <状态目录> --stage <暂存目录> --snapshot <最新远端快照> --fingerprint <来源指纹>`
- `python -B scripts/release_state.py published --state-root <状态目录> --snapshot <发布后快照> --fingerprint <来源指纹>`
- `python -B scripts/sync_plugin.py apply --root <发行目录> --snapshot <发布后快照>`
- `python -B scripts/release_state.py installed --state-root <状态目录>`

sync_plugin.py 使用官方 plugin-creator helper 更新本机缓存后缀，再通过 Codex CLI 安装，最后逐文件核对缓存。失败时恢复旧源码与安装基线并重装旧版。发布状态不回退，因此下次只重试安装同一个已发布版本。

快照格式：`{repository, commit, files:[{path, sha, content}]}`，commit 为 40 位 Git SHA，sha 是 UTF-8 正文对应的 Git blob SHA。没有密钥、登录态或本机路径配置。

## 通知与验收

无变化安静结束。仅报告实际更新、故障状态变化和新增待处理事项；同一已知故障或未解决事项不每半小时重复提醒。通知摘要指纹保存在本机，失败后恢复也视为状态变化。

测试覆盖三个输入新增/修改、幂等、去重、生成目录有效资料、循环拦截、敏感内容、三方冲突、历史保留、独立引用解析、安装失败回滚和状态分离。失败场景使用可控故障注入，不关闭用户真实网络或破坏现有插件。业务正确性仍依赖原日期、证据与实际复核。
