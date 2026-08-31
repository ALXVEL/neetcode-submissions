-- Write your query below
SELECT
    ROUND(SUM(
        CASE WHEN customer_pref_delivery_date = order_date 
        THEN 1 ELSE 0 END
    )::numeric * 100 / COUNT(DISTINCT delivery_id),2) AS immediate_percentage
FROM delivery
