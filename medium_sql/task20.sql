-- https://www.hackerrank.com/challenges/print-prime-numbers/problem?isFullScreen=true
WITH NUMS AS (
SELECT TOP (1000)
    ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
FROM 
    master..spt_values a
    CROSS JOIN master..spt_values b
),
NOT_PRIME_NUMS AS
(
    SELECT DISTINCT
        N1.n
    FROM
        NUMS N1
    JOIN
        NUMS N2
    ON
        N1.n <> N2.n AND N1.n % N2.n = 0 AND N2.n>1 
)
SELECT
    STRING_AGG(CAST(n AS VARCHAR(3)),'&')
FROM
    nums
WHERE
    n > 1
    AND n NOT IN (SELECT n FROM NOT_PRIME_NUMS)


-- была проблема получения 1000 чисел, RECURSIVE версия SQL сервера не поддерживала