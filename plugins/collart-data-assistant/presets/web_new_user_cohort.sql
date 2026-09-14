-- Profile-observed device cohort, NOT a complete historical new-user list.
-- DATE start_date/end_date/as_of_date; ARRAY<STRING> internal_user_ids from config.
-- as_of_date must be the last complete and refreshed active partition date.
-- Validate profile uniqueness and coverage; use the maintained new-user source for full historical cohorts.
-- Opt-in conservative whole-device exclusion, NOT default event-time internal-user filtering.
ASSERT @start_date <= @end_date AND @end_date <= @as_of_date AS 'Invalid cohort window';
ASSERT ARRAY_LENGTH(@internal_user_ids) > 0 AS 'Internal-account exclusion configuration is required';
WITH cohort AS (
  SELECT p.user_pseudo_id, p.first_open_date AS cohort_date, p.country
  FROM `aidata2025.ads_collartweb.ads_oper_user_profile_df` p
  WHERE p.first_open_date BETWEEN @start_date AND @end_date
    AND NOT EXISTS (
      SELECT 1 FROM UNNEST(@internal_user_ids) internal_id
      WHERE UPPER(internal_id) = UPPER(p.user_id)
         OR EXISTS (SELECT 1 FROM UNNEST(IFNULL(p.user_ids, ARRAY<STRING>[])) historic_id WHERE UPPER(historic_id) = UPPER(internal_id))
    )
), active_days AS (
  SELECT DISTINCT user_pseudo_id, event_date
  FROM `aidata2025.ads_collartweb.ads_oper_user_active_di`
  WHERE event_date BETWEEN @start_date AND LEAST(DATE_ADD(@end_date, INTERVAL 1 DAY), @as_of_date)
    AND is_active = TRUE
)
SELECT
  n.cohort_date,
  n.country,
  COUNT(DISTINCT n.user_pseudo_id) AS profile_cohort_devices,
  IF(DATE_ADD(n.cohort_date, INTERVAL 1 DAY) <= @as_of_date, COUNT(DISTINCT a.user_pseudo_id), NULL) AS d2_retained,
  IF(DATE_ADD(n.cohort_date, INTERVAL 1 DAY) <= @as_of_date, SAFE_DIVIDE(COUNT(DISTINCT a.user_pseudo_id), COUNT(DISTINCT n.user_pseudo_id)), NULL) AS d2_retention
FROM cohort n
LEFT JOIN active_days a ON a.user_pseudo_id = n.user_pseudo_id AND a.event_date = DATE_ADD(n.cohort_date, INTERVAL 1 DAY)
GROUP BY n.cohort_date, n.country
ORDER BY n.cohort_date, profile_cohort_devices DESC;
