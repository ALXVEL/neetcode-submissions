-- Write your query below
SELECT
    e.*,
    (CASE
        WHEN e.operator = '<' AND v1.value < v2.value THEN 'true'
        WHEN e.operator = '>' AND v1.value > v2.value THEN 'true'
        WHEN e.operator = '=' AND v1.value = v2.value THEN 'true'
        ELSE 'false'
    END) AS value
FROM expressions e
LEFT JOIN variables v1
    ON v1.name = e.left_operand
LEFT JOIN variables v2
    ON v2.name = e.right_operand
