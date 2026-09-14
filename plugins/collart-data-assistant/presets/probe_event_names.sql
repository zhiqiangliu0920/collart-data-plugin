-- GoogleSQL; DATE parameters start_date/end_date. Inclusive range <= 30 days.
-- Android example. Web requires app_info.id IS NULL plus reliable internal-account exclusions.
ASSERT DATE_DIFF(@end_date, @start_date, DAY) BETWEEN 0 AND 29 AS 'events query must cover 1 to 30 days';
-- Default: last 30 complete business dates, evaluated at execution time.
ASSERT @start_date >= DATE_SUB(CURRENT_DATE('Asia/Shanghai'), INTERVAL 30 DAY) AS 'raw events older than the past 30 days are forbidden';
ASSERT @end_date < CURRENT_DATE('Asia/Shanghai') AS 'this template only reads complete past dates';
SELECT event_name, COUNT(*) AS pv, COUNT(DISTINCT user_pseudo_id) AS uv
FROM `storytemplate-10a27.analytics_232977577.events_*`
WHERE _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', @start_date) AND FORMAT_DATE('%Y%m%d', @end_date)
  AND app_info.id = 'free.ai.photo.generator.collart.ai'
GROUP BY event_name
ORDER BY pv DESC
LIMIT 100;
