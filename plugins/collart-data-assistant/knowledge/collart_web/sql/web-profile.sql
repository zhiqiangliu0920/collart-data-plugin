-- STRING uid. One row per device; a login account can match several devices.
SELECT p.user_pseudo_id, p.user_id AS last_login_user_id, p.user_ids, p.first_open_date, p.last_active_date, p.country, p.is_vip
FROM `aidata2025.ads_collartweb.ads_oper_user_profile_df` p
WHERE UPPER(p.user_id) = UPPER(@uid)
   OR EXISTS (SELECT 1 FROM UNNEST(IFNULL(p.user_ids, ARRAY<STRING>[])) historic_id WHERE UPPER(historic_id) = UPPER(@uid));
-- VIP status is not proof of a successful payment during a requested date window.
-- Inspect current schema before adding traffic_src/revenue/active_days fields.
