-- Write your query below
WITH latest_login AS (
    SELECT
        *,
        ROW_NUMBER() OVER(
            PARTITION BY user_id
            ORDER BY time_stamp DESC
        ) AS latest_rank
    FROM logins
    WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
)

SELECT 
    user_id, 
    time_stamp AS last_stamp
FROM latest_login 
WHERE latest_rank = 1