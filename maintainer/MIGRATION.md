# 0.4 → 0.5 迁移清单

| 旧内容 | 新归属 | 处理 |
|---|---|---|
| 37 个 knowledge 主题 | 项目五类知识及 shared 公共规则 | 收入口径、身份、事件与分析方法分别整合；旧 ID 映射 |
| library 中有效当前知识 | 对应业务/指标/事件/方法/表字典 | 正文合并，不保留第二份材料入口 |
| library 中历史报告/运行数字/无引用残留 | 旧 Git 版本 + 迁移元数据 | 退出发行包 |
| 原始表字段、飞书字段 | 每物理表一份 tables 字典 + 必要来源记录 | 与当前 schema 对齐，旧字段单列 |
| Dataform SQLX 与 includes | sources/dataform | 按 releaseConfig 编译版本捕获，多产出共用一份 |
| presets | knowledge/<project>/sql + 原始查询生成器 | 保留安全查询意图，替换旧日期/旧金额模板 |
| provenance/catalog/search 多入口 | _meta 机器元数据 | 不展示庞大原始目录 |
| docs 中维护、集成、性能、旧更新记录 | maintainer/history | 退出安装包；新流程在 MAINTENANCE |
| 原 source_pipeline 等镜像导入器 | build.py + source_review.py | 来源变化触发复核，不恢复旧目录 |

精确到来源路径及旧 ID 的状态见 [migration.json](migration.json)，含 integrated / relations-integrated / replaced / archived / excluded；旧 ID 读取可返回新条目或归档原因，不静默定位到相似但无关的表。

内部账号列表改由授权数据源提供，发行包不含个人账号。Dataform 中识别到的账号/邮箱常量脱敏，origin_sha256 与 sha256 分别记录。ai-knowledge 原始目录、生产表、Dataform 调度均未修改。
