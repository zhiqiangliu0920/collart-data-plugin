# 0.4 维护资料归档

此文件只用于维护历史，不作为 0.5 分析指令；新流程见维护说明。

# 知识维护与发布

原始业务资料在 ai-knowledge、cursor_summary、codex_summary 中维护。通过 library/catalog.json 的 source 与 path 定位来源；安装缓存和插件生成的 library 不是原始维护入口。

## 证据与状态

统一主题保留 draft / documented / verified / deprecated。verified 必须有负责人、核验人、日期、范围和证据，全文扫描或结构校验不自动授予 verified。

来源资料分别记录 included、historical、duplicate、excluded、pending。完全相同正文共用一份文本并保留所有来源；同名不同内容分开保存。凭证、个人配置、原始用户明细不发布。只针对明确复核的源文件哈希做示例脱敏或聚合资料放行，内容变化后重新复核。

原始 provenance 的 source_path 与哈希保留历史记录；origin_source/origin_path 指向迁移后的逻辑来源。新资料在 library 中完整保存。topic_impacts.json 标明统一主题引用的原文已变化，旧主题检索会提醒 source_review_required。

## 维护动作

1. 先检索稳定主题 ID、完整资料和待处理项，确认项目、日期和粒度。
2. 在已授权的原来源修改或添加文档。需要调整统一主题时，在暂存发行目录编辑；保留旧摘录，添加新来源与适用范围。
3. 冲突不能自动变成已确认口径。保留双方版本并写入待处理清单；可独立发布的无冲突资料继续处理。
4. 运行 kb.py index/check、受影响脚本测试和来源扫描。文件链接及文本哈希必须一致。
5. 按仓库 SYNC.md 非强制发布，再通过 Codex CLI 安装并核对全部缓存文件。发布与安装是两个独立状态；不能重置旧基线掩盖差异。

同步流程不代表调度已启用。2026-09-13 来源维护约定记载原每 30 分钟任务已暂停；只有核查实际任务状态后才能宣称自动同步运行。同事更新安装或自行配置其授权与任务；更新后开启新任务使用新版。插件本身不启动定时器、不运行生产查询、不发送外部消息。

## 目录整理后的标识与检索

ai-knowledge 的正式正文按公司/四端维护，0global/knowledge_registry.json 记录持久 ID、旧路径别名及精确正文哈希。两个历史包的标识表由 inputs.source_registries 指向本机状态文件。纯迁移更新 path/aliases 并保留 id；内容变化必须审阅差异后更新记录，禁止只重设哈希。

收录 status、业务 business_status、复核 review_status 分开。默认 search 返回正式主题和 documented + reviewed_static 全文；--include-history 包含历史、废弃与待核对资料；--business-status 可精确筛选。read 接受持久 ID 和新旧路径别名，返回来源状态与完整正文。旧档案按带内容哈希的版本 ID 读取，不能冒充当前版本。

主题来源重新捕获时新增 source ID 和摘录，旧证据记录 tracking_status=historical 并保留哈希。它们不参与当前来源漂移报警，但仍接受包内证据完整性校验。新日期仅为整理/捕获日，不是业务生效日。

