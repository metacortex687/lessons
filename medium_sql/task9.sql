--https://www.hackerrank.com/challenges/population-density-difference/problem?isFullScreen=true
-- Формально задача в medium

SELECT
    max(population)-min(population)
FROM
    CITY