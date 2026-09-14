-- Predicate fragment, NOT a standalone query. Insert in an already bounded read-only query.
-- Web/Fashion only. Bind internal_user_ids ARRAY<STRING> from config/internal-user-ids.json.
-- Validate before the query: nonempty array, no NULL/empty IDs, no case-insensitive duplicates.
-- Bind include_anonymous BOOL: TRUE for metrics allowing anonymous users; FALSE for logged-in/payment users.
-- user_id must be the applicable event-time login identity, not an unqualified future profile mapping.
-- Case-normalize both sides consistently; never silently substitute an empty exclusion list.
AND (
  (@include_anonymous AND user_id IS NULL)
  OR UPPER(user_id) NOT IN (
    SELECT UPPER(internal_id) FROM UNNEST(@internal_user_ids) AS internal_id
  )
)
