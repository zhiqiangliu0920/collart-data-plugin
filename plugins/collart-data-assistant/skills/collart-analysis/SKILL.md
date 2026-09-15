---
name: collart-analysis
description: 分析 Collart Android、iOS/VidArt、Web 与 Fashion 的经营指标、渠道、收入、留存、功能漏斗和用户行为；按项目检索统一知识，使用本人已有授权连接。仅维护知识时用 collart-knowledge-maintain。
---

# Collart 数据分析

先读[访问约定](../../knowledge/shared/business/access.md)：只读；原始 GA4 及逐条行为 DWD/DM 仅最近 **7 天**，有日期上下界与产品过滤，不得分批读更早数据。SQLX 只作为加工依据，不能执行。使用同事自己的授权连接；无连接时提供口径、SQL 草稿及待核验项。

## 按需读取

以下路径相对本插件根目录；在本地查找脚本后执行，Python 仅标准库。一次任务复用已读的口径、schema 和连接信息，不重复加载全库。

```text
python -X utf8 scripts/kb.py search "收入" --project collart_android --kind metric
python -X utf8 scripts/kb.py read android.revenue
python -X utf8 scripts/kb.py read aidata2025.ads_collartweb.ads_oper_user_profile_df --field user_ids
python -X utf8 scripts/kb.py read fashion.events --section "Step 4"
```

默认 search 最多 3 条；read 默认正文 2800 字符。只有确需后续内容才用 next_offset 续读，同一 section/field 条件保持一致；查看章节用 --toc，明确需要全篇才 --full。优先读命中的指标/表字段，不批量读取 sources、_meta 或项目全部正文。追溯加工时按表字典的 dataform: 来源 ID 读取 SQLX；无需默认加载。

## 分析步骤

1. 明确项目、日期、对照、设备/账号/cohort 与业务问题；不清楚时先利用已有上下文。
2. 按指标查表字典，只核对本次需要的字段、粒度、分区、连接与数据覆盖。优先 ADS；缺列/不可用时按 [回退路径](../../knowledge/shared/business/routing.md) 选规则 → DM → GA4。
3. 查询只读，原始扫描限最近 7 天。标准事件探查用 `python -X utf8 scripts/query.py raw-events --project collart_android`。Web/Fashion 需使用授权内部名单参数；无名单不声称完成过滤。汇总表允许更长历史。
4. 检查缺日、NULL、去重、金额毛净额、身份映射、成熟窗口。DAU 筛 is_active，金额保留 pay-only；purchase 已含 credit。Web/Fashion 收入有交集，不能直接加总。
5. 输出结果、实际覆盖、口径、关键 SQL 与限制。字段存在、源码捕获、静态校验均不代表已验证生产数据；不编造查询结果或固定告警阈值。

稳定规则或新证据需要沉淀时转 collart-knowledge-maintain。单次经营数据和用户明细留在当前任务交付物中。
