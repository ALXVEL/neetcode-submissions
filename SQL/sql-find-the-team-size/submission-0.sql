-- Write your query below
WITH employee_team AS(
    SELECT
        team_id,
        COUNT(team_id) AS team_size
    FROM employee
    GROUP BY team_id
)

SELECT
    e.employee_id,
    t.team_size
FROM employee e
LEFT JOIN employee_team t
    ON e.team_id = t.team_id
