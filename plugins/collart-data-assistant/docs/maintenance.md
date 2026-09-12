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

本机每 30 分钟任务采用上述流程。同事更新安装或自行配置其授权与任务；更新后开启新任务使用新版。插件本身不启动定时器、不运行生产查询、不发送外部消息。
