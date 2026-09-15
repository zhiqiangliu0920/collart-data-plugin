---
id: "shared.diagnosis"
title: "趋势变化、对账与质量检查"
project: "shared"
kind: "playbook"
status: "documented"
sources: ["ai-knowledge:1company/analysis_playbooks/data-analysis-skill.md", "ai-knowledge:1company/analysis_playbooks/ga4_new_product_discovery.md", "previous:company-ga4-product-discovery", "previous:shared-analysis-playbook"]
tags: ["分析", "对账", "异常", "质量"]
tables: []
---

# 趋势变化、对账与质量检查

## 固定问题与检查质量

先明确产品、业务问题、对照周期、时区、用户/订单/事件粒度和决策，再按[表路由](../business/routing.md)及指标定义选源。检查日期覆盖、新鲜度、唯一键、NULL、重复、单位和枚举；缺失、真实零和未覆盖分别记录。

JOIN 前后核对行数和关键总量，先在适当粒度聚合，避免一对多关系放大金额。去重必须有业务键和保留依据；不默认均值填充、dropna 或用 IQR 删除异常。比率按同一人群和窗口计算，跨组汇总使用总分子/总分母。

## 问题与分析步骤

| 问题 | 步骤与判断依据 |
|---|---|
| 周复盘 | daily/country 看核心指标与上周同星期几，按 sort_id/metric_name 对齐四端；先排除缺数，再拆国家、渠道、新老结构的变化量及贡献 |
| DAU/新增异常 | 总量 → 国家 → 渠道 traffic_src_type/platform → 新增与回访 → 功能漏斗；分清规模变化与结构占比变化 |
| 收入与目标差距 | 使用当前明确目标，比较 DAU × ARPDAU 的量价贡献；分别检查广告/IAP、付费率、付费用户收入，观察完整周期均值而非单日尖峰 |
| 新功能 | 映射真实流程事件，比较渗透率与逐步转化；排除区域 timeout、事件缺失及版本上报变化后再解释差异 |
| 单用户 | 先查画像与可靠身份映射，再查合适用户日汇总或允许窗口内明细；明确历史覆盖，最少返回个人信息 |
| 投放/ROAS | 以获客 cohort 固定成本与收入范围，区分新增量与后续绑定、AI 启动、付费质量；D180 等只比较完整成熟 cohort |
| 看板对账 | 按[公司看板方法](../../company/analysis/dashboard.md)检查唯一键、漏行、额外行、舍入及字段差异 |

日期以[业务日与成熟窗口](../metrics/report-windows.md)为准；收入发布滞后不能变成随意平移 event_date。广告与支付定义见[收入指标](../metrics/revenue.md)，ASA 见[iOS 归因](../../collart_ios/metrics/asa.md)，DeepClick 等见[Web 渠道](../../collart_web/metrics/channel.md)。

## 事件摸底

先确认权限、产品过滤、表覆盖和用户键。事件按名称 × 参数 key × 类型查看覆盖，检查 string/int/double/float；候选名称不等于已确认触发语义。窗口内首次观察不能称为终身首次使用；D7/D30 需成熟 cohort，不足时使用汇总或说明缺口。

访问失败不等于无数据，LIMIT 不能约束原始扫描。原始事件及行为明细服从[只读、最近 7 天](../business/access.md)，不能为了长期分析拆批读取更早记录。

## 结论与沉淀

交付关键结论、指标对比、变化贡献、异常和行动依据，附实际覆盖日期、来源、已执行检查及可复现查询。样本小、归属不清、窗口未完整或事件缺失时标记证据不足；相关性和渠道差异不能单独证明因果，不使用无产品依据的固定合格线。

报告、结果快照和一次性 SQL 留在本次分析交付物中。知识库只沉淀稳定定义、业务规则、验证方法或明确范围的数据问题。
