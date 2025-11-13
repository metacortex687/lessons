--https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true
SELECT
    CASE WHEN G.grade< 8 THEN NULL ELSE S.name END as name,
    G.grade,
    S.marks 
FROM
    STUDENTS S
LEFT JOIN
    GRADES G
ON 
    S.marks BETWEEN G.min_mark AND G.max_mark
ORDER BY
    G.grade DESC, CASE WHEN G.grade< 8 THEN NULL ELSE S.name END, S.marks 
 