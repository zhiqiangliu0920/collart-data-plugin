-- GoogleSQL script. DATE end_date: last requested complete business day.
-- Offline template: verify actual schema, currency, gross/net scope and daily grain.
-- Query only Android. No extra Stripe/RUB addition to these ADS amounts.
ASSERT @end_date < CURRENT_DATE('Asia/Shanghai') AS 'End date must be complete';
WITH days AS (
  SELECT event_date, IF(event_date > DATE_SUB(@end_date, INTERVAL 7 DAY), 'current', 'previous') AS period
  FROM UNNEST(GENERATE_DATE_ARRAY(DATE_SUB(@end_date, INTERVAL 13 DAY), @end_date)) AS event_date
), daily AS (
  SELECT event_date, COUNT(*) AS source_rows,
    COUNTIF(revenue.purchase_revenue IS NULL OR revenue.ad_revenue IS NULL) AS null_revenue_rows,
    SUM(revenue.purchase_revenue) AS purchase_revenue, SUM(revenue.ad_revenue) AS ad_revenue
  FROM `aidata2025.ads_collartandroid.ads_oper_basic_indicator_daily_di`
  WHERE event_date BETWEEN DATE_SUB(@end_date, INTERVAL 13 DAY) AND @end_date
  GROUP BY event_date
), aligned AS (
  SELECT days.*, daily.source_rows, daily.null_revenue_rows, daily.purchase_revenue, daily.ad_revenue,
    daily.source_rows IS NOT NULL AND daily.null_revenue_rows = 0 AS data_present
  FROM days LEFT JOIN daily USING (event_date)
), totals AS (
  SELECT period, COUNTIF(data_present) AS populated_days,
    IF(COUNTIF(data_present) = 7, SUM(purchase_revenue), NULL) AS purchase_revenue,
    IF(COUNTIF(data_present) = 7, SUM(ad_revenue), NULL) AS ad_revenue
  FROM aligned GROUP BY period
), comparison AS (
  SELECT c.populated_days AS current_days, p.populated_days AS previous_days,
    c.purchase_revenue AS current_purchase_revenue, p.purchase_revenue AS previous_purchase_revenue,
    c.ad_revenue AS current_ad_revenue, p.ad_revenue AS previous_ad_revenue,
    c.purchase_revenue - p.purchase_revenue AS purchase_change,
    SAFE_DIVIDE(c.purchase_revenue - p.purchase_revenue, p.purchase_revenue) AS purchase_change_rate,
    c.ad_revenue - p.ad_revenue AS ad_change,
    SAFE_DIVIDE(c.ad_revenue - p.ad_revenue, p.ad_revenue) AS ad_change_rate
  FROM totals c CROSS JOIN totals p WHERE c.period = 'current' AND p.period = 'previous'
)
SELECT ARRAY(SELECT AS STRUCT * FROM aligned ORDER BY event_date) AS daily,
       (SELECT AS STRUCT * FROM comparison) AS comparison;
-- Populated days do not establish source freshness or absence of placeholder zeroes.
-- Confirm package grain/duplicates and amounts before combining purchase + ad revenue.
