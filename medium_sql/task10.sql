-- https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true
SELECT
    CEIL(
        AVG(salary)-
        AVG(CAST(REPLACE(CAST(salary AS CHAR),'0','') AS UNSIGNED)  
    ))  
FROM
    EMPLOYEES