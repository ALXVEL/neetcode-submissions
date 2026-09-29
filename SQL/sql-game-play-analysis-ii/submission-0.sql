-- Write your query below
WITH device_rank AS(
    SELECT
        player_id,
        device_id,
        ROW_NUMBER() OVER(
            PARTITION BY player_id
            ORDER BY event_date ASC
        ) AS rnk
    FROM activity
)

SELECT
    player_id,
    device_id
FROM device_rank
WHERE rnk = 1