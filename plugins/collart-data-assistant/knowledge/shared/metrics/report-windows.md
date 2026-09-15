---
id: "shared.report-windows"
title: "经营日报日期与比较窗口"
project: "shared"
kind: "metric"
status: "documented"
sources: ["ai-knowledge:1company/indicators/collart_daily_report_date_windows.md"]
tags: ["日期", "T-2", "T-1", "日报"]
tables: []
---

# 经营日报日期与比较窗口

> 生效确认：2026-08-06  
> 适用：Collart Android / Web / iOS 项目经营日报

## 1. 收入与留存指标

对比值使用前天（T-2）：

```text
对比值：T-2
前7日均值：T-9 至 T-3
```

适用指标：

- 收入
- 广告收入
- 首次订阅收入
- 续订收入
- 点数包收入
- ARPU
- 次日留存
- 免费用户次留
- 付费用户次留
- Web 登录用户次留

## 2. 其他指标

对比值使用昨天（T-1）：

```text
对比值：T-1
前7日均值：T-8 至 T-2
```

- DAU
- 新增、自然新增、投放新增
- 订阅/点数包转化率
- 新用户转化
- AI 服务与内容指标

## 3. SQL 实现

源表必须扫描：

```text
WHERE event_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 9 DAY)
                     AND DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)
```

收入和留存指标执行：

```text
DATE_ADD(event_date, INTERVAL 1 DAY)
```

再统一提取：

```text
yestoday = CURRENT_DATE() - 1
avg_7days = AVG(CURRENT_DATE() - 8 至 CURRENT_DATE() - 2)
```

这样日期平移指标实际对应 T-2 与 T-9~T-3；普通指标仍对应 T-1 与 T-8~T-2。

## 4. 红线

若源表仅从 T-8 开始扫描，收入和留存会缺少 T-9，`AVG()` 实际只计算 6 天。
