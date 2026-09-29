-- Write your query below
WITH spending AS (
    SELECT
        c.customer_id,
        c.name,
        SUM(CASE
            WHEN o.order_date >= '2020-06-01' AND o.order_date < '2020-07-01'
            THEN (o.quantity * p.price)
            ELSE 0
        END) AS june_spending,
        SUM(CASE
            WHEN o.order_date >= '2020-07-01' AND o.order_date < '2020-08-01'
            THEN (o.quantity * p.price)
            ELSE 0
        END) AS july_spending
    FROM orders o
    LEFT JOIN customers c
        ON c.customer_id = o.customer_id
    LEFT JOIN product p
        ON p.product_id = o.product_id
    GROUP BY c.customer_id, c.name
)

SELECT
    customer_id,
    name
FROM spending
WHERE june_spending >= 100 AND july_spending >= 100


