# 同事安装与使用说明

## 安装

先在终端执行以下命令，直接从 GitHub 注册并安装本仓库，不必复制知识文件：

```text
codex plugin marketplace add zhiqiangliu0920/collart-data-plugin --ref main
codex plugin add collart-data-assistant@personal
```

也可以注册来源后，重新打开客户端，在 Plugins Directory 选择该 marketplace，安装 **Collart 团队数据助手**。marketplace 的 Git 来源与刷新方式见 [OpenAI 官方说明](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli)。安装命令已在本机 Codex CLI 核对；客户端可用入口可能因版本不同而变化。

先用 `codex plugin marketplace list` 检查 personal 是否已指向其他来源；存在同名冲突时不要覆盖。仓库为私有时，每位同事需自己的 GitHub 权限。安装插件不自动授予数据权限。Windows 也可在克隆后的仓库运行 `install.ps1`，脚本默认注册 GitHub 来源并检查冲突。

插件更新后执行 `codex plugin marketplace upgrade personal`，再执行 `codex plugin add collart-data-assistant@personal` 安装最新版，最后用 `codex plugin list` 查看版本。新建一个 Codex 任务使用；旧任务可能仍保留旧技能上下文。不要手改安装缓存。

## 使用

可直接提出问题：

- “使用 Collart 插件，分析 Android 最近七个完整日收入变化。”
- “Web 画像表 user_ids 和 user_id 有什么区别？”
- “Fashion 收入和 Web 有交集吗？”
- “ADS 查不到这个漏斗时，能否用最近七天埋点补充？”
- “把已确认的口径修正沉淀到团队知识。”

复杂问题请给出项目、时间范围、指标和希望支持的决策。插件先读取相关口径和表字段，再使用你本人已有授权的数据连接；无连接时只能给出说明和待执行 SQL，不会假装获得结果。

## 约定

仅允许只读查询，禁止写入、删除、改表及运行 Dataform SQLX。原始 GA4 与逐条行为 DWD/DM 仅允许最近 **7 天**：默认最近七个完整日，含今天时窗口最多今天及前六天；不能分批读取更早日期。原始查询同时限定日期与产品。已有汇总、画像、收入/成本表可做更长期分析。

Web/Fashion 内部账号名单来自授权的数据源，不随本插件公开分发；名单未取得时需说明过滤缺口。数据 IAM 或查询网关才能强制限制数据库能力，安装插件不会改变你现有连接的权限。

## 高效查阅

通常一次 search、一次主题 read、必要字段 read 即可。默认 search 3 条、read 正文 2800 字符；确有需要时按章节、字段或 offset 继续。SQLX、完整 schema 与来源原件只在追溯时读取。

```text
python -X utf8 scripts/kb.py search "收入" --project collart_android --kind metric
python -X utf8 scripts/kb.py read android.revenue
python -X utf8 scripts/kb.py read aidata2025.ads_collartweb.ads_oper_user_profile_df --field user_ids
python -X utf8 scripts/query.py raw-events --project collart_fashion
```

以上命令从插件根目录执行，需要 Python 3.10+。脚本不需要第三方依赖，不自动连接数据库。
