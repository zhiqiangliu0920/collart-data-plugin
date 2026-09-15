-- DATE start_date/end_date. Historical first_open_date from the existing profile, not a raw seven-day window.
-- Internal-user device exclusion is an explicit optional scope; validate the authorized list separately.
SELECT user_pseudo_id, user_id, user_ids, first_open_date
FROM `aidata2025.ads_collartweb.ads_oper_user_profile_df`
WHERE first_open_date BETWEEN @start_date AND @end_date;
