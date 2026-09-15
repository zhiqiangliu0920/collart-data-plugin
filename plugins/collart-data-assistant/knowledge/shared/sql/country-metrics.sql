-- GoogleSQL script; DATE parameters: start_date, end_date, as_of_date.
-- as_of_date = last complete and successfully refreshed business date, not the wall-clock date.
-- Web country grain; inspect schema and upstream internal-user exclusion before use.
SELECT
  event_date,
  country,
  SUM(dau) AS dau,
  SUM(dnu) AS dnu,
  SUM(IF(DATE_ADD(event_date, INTERVAL 1 DAY) <= @as_of_date, retain.d2, NULL)) AS retained_d2_new,
  SUM(IF(DATE_ADD(event_date, INTERVAL 1 DAY) <= @as_of_date, dnu, NULL)) AS mature_d2_new_users,
  SAFE_DIVIDE(SUM(IF(DATE_ADD(event_date, INTERVAL 1 DAY) <= @as_of_date, retain.d2, NULL)), SUM(IF(DATE_ADD(event_date, INTERVAL 1 DAY) <= @as_of_date, dnu, NULL))) AS retention_d2_new,
  SUM(revenue.purchase_revenue) AS purchase_revenue,
  SUM(revenue.new_subscribe_uv) AS first_subscription_payers
FROM `aidata2025.ads_collartweb.ads_oper_basic_indicator_country_di`
WHERE event_date BETWEEN @start_date AND @end_date
GROUP BY event_date, country
ORDER BY event_date, dau DESC;
-- first_subscription_payers may contain returning visitors; it is not a new-visitor conversion numerator.
-- Multi-day rates must SUM mature numerators / SUM mature denominators, never AVG daily rates.
