WITH NUMS AS (
    SELECT TOP (1000)
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM 
        master..spt_values a
        CROSS JOIN master..spt_values b
),
PRIMES AS (
    SELECT
        c.n
    FROM
        NUMS c
    WHERE
        c.n > 1
        AND NOT EXISTS (
            SELECT 1
            FROM NUMS d
            WHERE 
                d.n BETWEEN 2 AND FLOOR(SQRT(c.n))
                AND c.n % d.n = 0
        )
)
SELECT
    STRING_AGG(CAST(n AS varchar(4)), '&')
FROM
    PRIMES;


--Вариант с рекурсией, оказывается на SQL Server рекурсия включается автоматически безе директивы RECURSIVE

WITH N AS (
    SELECT 2 AS n
    UNION ALL
    SELECT n + 1
    FROM N
    WHERE n < 1000
),
PRIMES AS (
    SELECT
        c.n
    FROM
        N c
    WHERE
        NOT EXISTS (
            SELECT 1
            FROM N d
            WHERE 
                d.n BETWEEN 2 AND FLOOR(SQRT(c.n))
                AND c.n % d.n = 0
        )
)
SELECT
    STRING_AGG(CAST(n AS varchar(4)), '&')
FROM
    PRIMES
OPTION (MAXRECURSION 1000);
