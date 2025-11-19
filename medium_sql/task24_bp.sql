-- Best Practices

SELECT
  s.id AS student_id,
  s.name,
  course_s.score - course_m.score AS score_difference
FROM students s
JOIN courses course_s ON s.id = course_s.student_id AND course_s.course_name = 'Science'
JOIN courses course_m ON s.id = course_m.student_id AND course_m.course_name = 'Math' AND course_s.score > course_m.score
GROUP BY s.id, course_s.score, course_m.score
ORDER BY score_difference DESC, s.id ASC