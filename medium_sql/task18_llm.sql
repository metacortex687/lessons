WITH PAIRS AS (
    SELECT
        LEAST(x, y) AS x,
        GREATEST(x, y) AS y,
        COUNT(*)      AS cnt
    FROM
        FUNCTIONS
    GROUP BY
        LEAST(x, y), GREATEST(x, y)
)
SELECT
    x,
    y
FROM
    PAIRS
WHERE
    cnt > 1
ORDER BY
    x, y;
