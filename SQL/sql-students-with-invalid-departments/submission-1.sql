-- Write your query below
SELECT
    s.id,
    s.name
FROM students s
WHERE s.department_id NOT IN (
    SELECT DISTINCT id FROM departments
) OR s.department_id IS NULL