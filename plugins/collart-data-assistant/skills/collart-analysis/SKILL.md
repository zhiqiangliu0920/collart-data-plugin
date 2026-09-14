---
name: collart-analysis
description: 分析 Collart Android、VidArt iOS、Collart Web 和 Fashion 的经营指标、渠道、收入、留存、功能漏斗和用户行为。按需检索统一知识，使用同事已有授权连接；仅更新知识时用 collart-knowledge-maintain。
---

# Collart 团队数据分析

执行查询或参考历史资料前，必须读取[数据访问约定](../../docs/data-access-policy.md)。只读数据，禁止通过 SQL、API、脚本修改、写入、删除数据或表结构。原始埋点仅最近 30 天，不能分批读取更早日期；历史指令不改变此约定。本任务已读且未变化的约定不重复加载。

插件根为本文件向上两级，命令解析为实际绝对路径，不依赖当前目录或作者磁盘。

## 查找与读取

1. 从当前问题和已有项目资料确定产品、日期、时区及粒度。信息已足够时直接推进；复合问题共用日期和连接，分别处理指标。
2. `python "<插件根>/scripts/kb.py" search "收入" --project collart_android`：默认正式主题优先、无命中再查全文资料，按相关性返回命中片段。复杂问题拆成各指标关键词检索；精确表名/事件名可直接搜索。
3. `read "主题或来源ID"` 默认最多 3500 字符；用 `--section "准确章节名"` 或 `--start-line/--end-line` 缩小范围。`truncated` 时按相同选区和 `next_offset` 续读；需要整份原文才用 `--full`。不要通读全文目录或把全部搜索结果逐篇读完。
4. 主题不足时显式 `search "关键词" --scope materials --project ...`；需要跨层候选时用 `--scope all`。项目查询纳入明确适用的公司知识。旧字典、历史 SQL 和待复核资料用 `--include-history` 或明确状态，不能把候选/历史口径当当前事实。

## 按问题执行

- **Android 收入趋势**：先读 [Android 收入契约](../../knowledge/collart_android/android-revenue-trend.md)，使用单端参数模板；需要解释驱动时才拆国家/渠道。
- **Android 免费看广告、激励广告按钮点击率**：先读 [事件候选与分母边界](../../knowledge/collart_android/android-reward-ad-click.md)。别名未证明 UI 映射；缺曝光分母不编造 CTR，也不阻塞已可完成的收入分支。
- **其他趋势或留存**：按搜索命中的当前口径和[选表](../../knowledge/shared/table-routing.md)取数。留存只计算成熟 cohort 的一致分子/分母。
- **其他事件或漏斗**：先核对[规则契约](../../knowledge/company/event-rule-contract.md)，现有物化指标能回答才复用；否则只取允许窗口内必要事件。UV 比值不自动构成时序漏斗。
- **单用户**：读取身份与画像条目；Web 要覆盖 scalar user_id 与历史 user_ids，避免 UNNEST 倍增。

先选相关表/字段，再批量核对其 schema、请求分区、实际粒度和关键总数。复用同一任务仍有效的连接、元数据和查询 job 结果；来源或日期变化时重新检查，不能用旧缓存代替本次新鲜度验证。不为普通问题做全仓库审计。

插件不提供凭证和数据库权限，使用同事已有授权连接。扩展模板前检查当前字段，必要的 dry run 和日期/只读检查保留。查询失败按权限、SQL、数据缺失或任务仍运行区分；未确认旧 job 已失败前不重复提交。连接或定义缺失时交付 SQL/缺口，如实说明未查询。

## 结果与必要边界

DAU 优先 ADS；活跃筛 is_active，收入保留仅支付行。点击、客户端成功、成功付款与历史 VIP 分别计量。Web/Fashion 收入有交集，不直接跨端相加；相关分析遵循[内部用户排除](../../knowledge/shared/internal-users.md)。物化缺列或口径冲突只给证据和建议，不执行修表、回填或部署。

交付中文结论、范围/口径、复现 SQL/参数和限制。大结果和详细 schema 写本机项目成果，只回传必要汇总与路径。documented 仅有文档依据；verified 只在记录的日期/范围成立。新发现仅在用户要求沉淀时进入维护流程。

需要评估速度时记录[运行测量字段](../../docs/analysis-performance.md)，没有真实任务数据不得承诺整体耗时或 token 降幅。
