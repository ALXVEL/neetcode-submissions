-- Write your query below
SELECT DISTINCT
    s.seller_name
FROM seller s
LEFT JOIN orders o
    ON o.seller_id = s.seller_id
WHERE s.seller_id NOT IN (
    SELECT DISTINCT
        seller_id
    FROM orders
    WHERE sale_date < '2021-01-01' AND sale_date >= '2020-01-01'
)
ORDER BY s.seller_name