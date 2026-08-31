-- Write your query below
WITH score_ranking AS (
    SELECT
        *,
        RANK() OVER(
            PARTITION BY student_id
            ORDER BY score DESC, exam_id ASC
        ) AS score_rnk
    FROM exam_results
)

SELECT
    student_id,
    exam_id,
    score
FROM score_ranking
WHERE score_rnk = 1