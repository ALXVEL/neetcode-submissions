-- Write your query below
SELECT
    t.*,
    COALESCE(SUM(
        CASE 
            WHEN t.team_id = m.host_team AND 
            m.host_goals > m.guest_goals THEN 3

            WHEN t.team_id = m.guest_team AND 
            m.host_goals < m.guest_goals THEN 3

            WHEN m.host_goals = m.guest_goals THEN 1

            ELSE 0
        END
    ),0) AS num_points
FROM teams t
LEFT JOIN matches m
    ON m.host_team = t.team_id
    OR m.guest_team = t.team_id
GROUP BY t.team_id, t.team_name
ORDER BY num_points DESC
