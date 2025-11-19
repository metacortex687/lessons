--https://www.codewars.com/kata/649421e15e89dc1ca27e5fb3/train/sql
--Students who excel in Science over Math
-- 6 kyu

SELECT
  sc.student_id,
  st.name,
  sc.score_science-sc.score_math AS score_difference
FROM
  (
    SELECT
      student_id,  
      SUM(CASE WHEN course_name = 'Math' THEN score ELSE 0 END) AS score_math,
      SUM(CASE WHEN course_name = 'Science' THEN score ELSE 0 END) AS score_science
    FROM
      courses
    GROUP BY
      student_id    
  ) sc -- scores
JOIN
  students st
ON
  sc.student_id = st.id 
WHERE
  sc.score_science-sc.score_math > 0
ORDER BY
  score_difference DESC,  student_id
