-- Write your query below
WITH sub_orders AS (
    SELECT
        c.customer_id,
        c.customer_name,
        SUM(CASE WHEN o.product_name = 'A' THEN 1 ELSE 0 END) AS a_purchased,
        SUM(CASE WHEN o.product_name = 'B' THEN 1 ELSE 0 END) AS b_purchased,
        SUM(CASE WHEN o.product_name = 'C' THEN 1 ELSE 0 END) AS c_purchased
    FROM customers c
    LEFT JOIN orders o
        ON o.customer_id = c.customer_id
    GROUP BY c.customer_id, c.customer_name
)

SELECT
    customer_id,
    customer_name
FROM sub_orders
WHERE a_purchased > 0 AND b_purchased > 0 AND c_purchased = 0
ORDER BY customer_name
