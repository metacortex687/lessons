-- https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true

WITH RANKED_F AS(
SELECT
    ROW_NUMBER() OVER (ORDER BY x) as row_num,
    x,
    y
FROM
    FUNCTIONS   
)
SELECT
    F1.x,
    F1.y
FROM
    RANKED_F F1
JOIN
    RANKED_F F2
ON
    ((F1.x = F2.y AND F1.y = F2.x) OR (F1.y = F2.x AND F1.x = F2.y)) 
    AND F1.row_num < F2.row_num        
