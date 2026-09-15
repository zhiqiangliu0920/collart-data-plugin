# Collart 数据分析插件

**0.5.0** 将 Collart Android、iOS/VidArt、Web 和 Fashion 的业务定义、表结构、埋点、指标及分析方法组织成统一知识，供同事在 Codex 中按需查询和分析。

- [安装与使用](INSTALL.md)
- [新结构与文件作用](maintainer/STRUCTURE.md)
- [知识入口](plugins/collart-data-assistant/knowledge/INDEX.md)
- [迁移清单](maintainer/MIGRATION.md)、[验证结果](maintainer/VALIDATION.md)、[知识缺口](maintainer/KNOWLEDGE-GAPS.md)

数据只读，原始逐条行为仅最近 **7 天**；长期分析使用已有汇总、画像、收入或成本表。插件没有数据连接凭证；同事使用各自授权连接。数据库 IAM/网关负责强制访问控制，插件文档不是数据库权限开关。

## 目录

```text
.agents/plugins/marketplace.json  Codex marketplace 入口
plugins/collart-data-assistant/   安装给同事的完整分析包
  .codex-plugin/plugin.json      名称、版本与技能入口
  skills/                       分析与知识维护两个轻量入口
  knowledge/                    项目 → 五类知识；相关长 SQL
  sources/                      SQLX、必要依赖、schema/飞书证据
  _meta/                        索引、来源和旧 ID 映射
  config/                       检索意图规则
  scripts/                      search/read 与只读 SQL 模板生成
maintainer/                     维护流程、变更记录、验收与缺口
scripts/                        确定性构建、来源复核与分发工具
tests/                          结构、检索、查询边界与同步测试
.github/workflows/               GitHub 自动校验
```

原 ai-knowledge 仍是来源之一，原目录未改动；插件正文是维护中的规范知识，不再自动镜像原始资料目录。来源变动先定位受影响条目，复核后构建发布；[维护流程](maintainer/MAINTENANCE.md)。
