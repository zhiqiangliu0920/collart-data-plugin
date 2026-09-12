-- DATE start_date/end_date, STRING event_name/param_key. Android example, not an ordered funnel.
ASSERT DATE_DIFF(@end_date, @start_date, DAY) BETWEEN 0 AND 29 AS 'events query must cover 1 to 30 days';
WITH extracted AS (
  SELECT
    (SELECT AS STRUCT ep.value.string_value, ep.value.int_value, ep.value.float_value, ep.value.double_value
     FROM UNNEST(event_params) ep WHERE ep.key = @param_key LIMIT 1) AS param_value
  FROM `storytemplate-10a27.analytics_232977577.events_*`
  WHERE _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', @start_date) AND FORMAT_DATE('%Y%m%d', @end_date)
    AND app_info.id = 'free.ai.photo.generator.collart.ai'
    AND event_name = @event_name
)
SELECT TO_JSON_STRING(param_value) AS typed_value, COUNT(*) AS events
FROM extracted
GROUP BY typed_value
ORDER BY events DESC;
-- NULL means key absent; value types are preserved. If repeated identical keys exist, inspect them separately.
