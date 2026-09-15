---
id: "company.dashboard"
title: "公司看板聚合与只读对账"
project: "company"
kind: "playbook"
status: "documented"
sources: ["ai-knowledge:1company/analysis_playbooks/dashboard_reconciliation.md", "ai-knowledge:1company/lineage/dashboard_pipeline.md"]
tags: ["公司", "看板", "对账"]
tables: ["pubdata2025.ads.ads_atlasv_basic_data_daily_1h"]
---

# 公司看板聚合与只读对账

## 血缘与聚合

[公司数据源](../tables/pubdata2025.ads.ads_atlasv_basic_data_daily_1h.md) → 日期/团队/产品聚合 → product/group/line/company 四层 → `daily_metric` → 看板。`sync_run` 是同步批次元数据，不是业务事实表；本方法只读取并对比，不执行写入或回填。

源表按 `stats_date × team × app_name` 聚合。四组为 downloader、ai_photo、guangzhou_tool、guangzhou_game；广州游戏按 TTG_ / FBG_ 分线。遇到其他团队或不属于两线的游戏产品应报告未映射范围，不静默漏掉。

产品/组/线分别汇总 revenue、cost、else_cost、active_users、new_users。公共费用来自 `(team='guangzhou', app_name='gz')` 与 `(team='hangzhou', app_name='hz')`，仅在 company 层加一次。净收入 = 收入 − 投放花费 − 其他花费，不能把多个层级总计相加。

次留以有效 `retan_2` 的新增人数加权：`SUM(retan_2 * new_users)` / 有效 retan_2 行的 `SUM(new_users)`。空留存不是 0；当前日序和刷新覆盖需按表字典核实。

## 对账

1. 固定相同源日期、环境和过滤，先查数据新鲜度和日期覆盖。目标 `daily_metric` 的业务键为日期 × level × group_name × line_name × product_name × data_mode。
2. 预期与实际均先检验键唯一，再比较缺失键、额外键、同键字段差异。字典覆盖重复键会掩盖异常，分页或截断也会造成假缺失。
3. 当前方法约定金额差容忍 0.01、人数相等；留存先 ROUND_HALF_UP 到 4 位再比较。若目标存储或舍入规则不同，应先对齐，不擅自放宽阈值。
4. 报告覆盖范围、异常键和最大差异；旧验收结果不能代替本次检查。具体数据读取遵守[只读规范](../../shared/business/access.md)。
