SELECT
    n AS node,
    CASE
        WHEN p IS NULL THEN 'Root'
        WHEN EXISTS (
            SELECT 1
            FROM bst AS b2
            WHERE b2.p = b1.n
        ) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM bst AS b1
ORDER BY n;
--- в случае EXISTS система сама сделает внутри LIMIT 1

--- варинат 2 с количеством потомков

SELECT
    b1.n AS node,
    COUNT(b2.p) AS children_count,
    CASE
        WHEN b1.p IS NULL THEN 'Root'
        WHEN COUNT(b2.p) > 0 THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM bst AS b1
LEFT JOIN bst AS b2 ON b1.n = b2.p
GROUP BY b1.n, b1.p
ORDER BY b1.n;
