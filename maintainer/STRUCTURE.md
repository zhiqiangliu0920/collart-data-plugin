# 0.5 新结构与文件作用

## 同事会安装的内容

| 路径 | 作用 | 读取时机 |
|---|---|---|
| `.codex-plugin/plugin.json` | Codex 插件身份、版本和技能位置 | 安装/发现 |
| `skills/*/SKILL.md` | 分析、维护两种工作流；避免把全库塞进入口 | 技能被调用 |
| `skills/*/agents/openai.yaml` | Codex 展示名及默认提示 | 客户端元数据 |
| `knowledge/INDEX.md`、各级 README | 给人看的导航；不作为正文重复索引 | 手工浏览 |
| `knowledge/<project>/business` | 产品、用户、身份、范围；shared 另有访问约定 | 确认业务范围 |
| `knowledge/<project>/tables` | 一张物理表一份字典，完整嵌套字段、更新/加工、关联、状态 | 默认查表入口 |
| `knowledge/<project>/events` | 按业务流程组织事件、参数与测量缺口 | 分析功能漏斗 |
| `knowledge/<project>/metrics` | 合并同类指标公式、分母、筛选和查询入口 | 确定口径 |
| `knowledge/<project>/analysis` | 分析步骤和判断依据，引用指标/表 | 诊断业务问题 |
| `knowledge/<project>/sql` | 与指标或方法绑定的较长参数化 SELECT | 需要查询模板 |
| `sources/dataform` | SQLX 与 includes；同一源码只存一次，可关联多个产出 | 追溯加工，不执行 |
| `sources/schemas` | 捕获的 schema 或未找到状态，无业务数据行 | 查字段出处 |
| `sources/dictionaries` | 相关飞书表/字段记录，去掉维护人等无关列 | 查业务解释出处 |
| `_meta/catalog.json` | 知识元数据、ID/路径/hash，不含正文；项目/类型先筛选，再本地搜索对应规范正文 | search/read 定位，结果有界 |
| `_meta/sources.json` | 来源、版本、原始/分发哈希与产出表映射 | 追溯/完整性验证 |
| `_meta/aliases.json` | 旧 ID 兼容映射或明确归档原因 | 旧调用兼容 |
| `config/search-routing.json` | 小型意图词与排序加权 | search |
| `scripts/kb.py` | search/read；支持项目、类型、表名、字段、章节 | 按需检索 |
| `scripts/query.py` | 原始七天查询生成和保守只读语法检查 | 准备 SQL |

SQLX 含生产 DDL/DML 是来源证据，独立存储，永不进入查询模板目录。来源里的隐私常量脱敏时记录两种哈希，不声称分发版与原件字节相同。获取的 releaseConfig 版本不等于已核验生产最近成功运行版本。

## 只在仓库维护区使用

根目录 README/INSTALL 给同事看；CHANGELOG 记录版本。maintainer 的维护说明、迁移 JSON、来源输入清单、表覆盖、复核队列、发行清单、基准测试和验收结果给维护者使用。history 的旧维护资料不会被技能默认加载，也不在插件安装目录中。

scripts/build.py 只从新正文构建索引与发行清单；source_review.py 比较来源并标记受影响条目；sync_plugin.py 应用经过 GitHub 校验的快照并保护本地改动。tests 及 GitHub workflow 校验这些契约。

## 冗余的取舍

同类定义合并成一篇，物理表/schema/源码各只有一个规范位置。字段说明与机器 schema 两份表示分别服务阅读和校验；索引仅含机器元数据，不复制整篇正文。检索时本地读取经过项目/类型筛选的规范文件，只返回少量命中。旧 0.4 的 library、provenance、顶层 presets、重复摘要和历史报告不再是平行入口。

包大小不是 token 用量：只有实际读入模型的内容才消耗上下文。默认只输出少量命中/指定字段；真实性校验会本地读取和哈希文件，但不会把全文件返回模型。真实 token 节省必须由同一模型的 usage 记录验证，字符基准不能冒充 token 测量。
