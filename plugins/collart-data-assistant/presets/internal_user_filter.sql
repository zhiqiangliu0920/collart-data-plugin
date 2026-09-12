-- ARRAY<STRING> internal_user_ids: load config/internal-user-ids.json:user_ids, never silently use [].
-- Web example: conservative whole-device exclusion on current profile historical bindings.
-- This can exclude shared devices used by both employees and customers; state the chosen policy.
ASSERT ARRAY_LENGTH(@internal_user_ids) > 0 AS 'Internal-account exclusion configuration is required';
SELECT p.*
FROM `aidata2025.ads_collartweb.ads_oper_user_profile_df` p
WHERE NOT EXISTS (
  SELECT 1 FROM UNNEST(@internal_user_ids) internal_id
  WHERE UPPER(internal_id) = UPPER(p.user_id)
     OR EXISTS (SELECT 1 FROM UNNEST(IFNULL(p.user_ids, ARRAY<STRING>[])) historic_id WHERE UPPER(historic_id) = UPPER(internal_id))
);
-- For event-time exclusion use reliable event-time login mappings instead, and name that distinct policy.
