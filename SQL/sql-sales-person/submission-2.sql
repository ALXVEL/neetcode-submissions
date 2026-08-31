-- Write your query below
SELECT
    sp.name AS name
FROM sales_person sp
LEFT JOIN orders o
    ON sp.sales_id = o.sales_id
LEFT JOIN company c
    ON o.com_id = c.com_id
GROUP BY sp.sales_id
HAVING
    SUM(CASE WHEN c.name = 'CRIMSON' THEN 1 ELSE 0 END) = 0

