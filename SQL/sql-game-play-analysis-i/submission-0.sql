-- Write your query below
WITH login_date_rankings AS (
    SELECT
        *,
        ROW_NUMBER() OVER(
            PARTITION BY player_id
            ORDER BY event_date ASC
        ) AS login_date_rank
    FROM activity
)

SELECT
    player_id,
    event_date AS first_login
FROM login_date_rankings
WHERE login_date_rank = 1