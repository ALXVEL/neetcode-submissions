-- Write your query below
SELECT
    sales_person.name
FROM sales_person
WHERE sales_person.sales_id NOT IN (
    SELECT DISTINCT
        o.sales_id
    FROM orders o
    LEFT JOIN company c
        ON c.com_id = o.com_id
    WHERE c.name = 'CRIMSON'
)