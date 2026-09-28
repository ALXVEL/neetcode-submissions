-- Write your query below
SELECT
    wh.name AS warehouse_name,
    SUM((p.width * p.length * p.height)* wh.units)  AS volume
FROM warehouse wh
LEFT JOIN products p
    ON wh.product_id = p.product_id
GROUP BY wh.name