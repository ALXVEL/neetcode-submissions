-- Write your query below
WITH score_rnk AS (
    SELECT
        student_id,
        exam_id,
        score,
        ROW_NUMBER() OVER(
            PARTITION BY student_id
            ORDER BY score DESC, exam_id ASC
        ) as best_score
    FROM exam_results
)

SELECT
    student_id,
    exam_id,
    score
FROM score_rnk
WHERE best_score = 1
ORDER BY student_id