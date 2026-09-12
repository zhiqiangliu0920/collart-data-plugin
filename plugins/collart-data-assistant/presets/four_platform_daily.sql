-- DATE parameters start_date/end_date: an explicit complete business-day range.
-- Per-platform comparison only. Web/Fashion overlap; do not SUM these rows into company revenue or users.
-- Verify each endpoint's schema, dates, currency and upstream internal exclusions before running.
ASSERT @start_date <= @end_date AS 'Invalid date window';
WITH daily AS (
  SELECT event_date, 'collart_android' AS platform, dau, dnu, revenue.purchase_revenue AS purchase_revenue, revenue.ad_revenue AS ad_revenue
  FROM `aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_di`
  WHERE event_date BETWEEN @start_date AND @end_date
  UNION ALL
  SELECT event_date, 'collart_ios', dau, dnu, revenue.purchase_revenue, revenue.ad_revenue
  FROM `aidata2025.ads_collartios.ads_oper_basic_indicator_daily_di`
  WHERE event_date BETWEEN @start_date AND @end_date
  UNION ALL
  SELECT event_date, 'collart_web', dau, dnu, revenue.purchase_revenue, revenue.ad_revenue
  FROM `aidata2025.ads_collartweb.ads_oper_basic_indicator_daily_di`
  WHERE event_date BETWEEN @start_date AND @end_date
  UNION ALL
  SELECT event_date, 'collart_fashion', dau, dnu, revenue.purchase_revenue, revenue.ad_revenue
  FROM `aidata2025.ads_collartfashion.ads_oper_basic_indicator_daily_di`
  WHERE event_date BETWEEN @start_date AND @end_date
)
SELECT event_date, platform, SUM(dau) AS dau, SUM(dnu) AS dnu, SUM(purchase_revenue) AS purchase_revenue, SUM(ad_revenue) AS ad_revenue
FROM daily
GROUP BY event_date, platform
ORDER BY event_date, platform;
