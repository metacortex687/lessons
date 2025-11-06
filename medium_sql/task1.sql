--https://www.hackerrank.com/challenges/occupations/problem?isFullScreen=true
WITH D AS
(
        SELECT
            ROW_NUMBER() OVER (ORDER BY name) AS _rank,
            name
        FROM
            OCCUPATIONS
        WHERE
            OCCUPATION = "Doctor"    
),
P AS
(
        SELECT
            ROW_NUMBER() OVER (ORDER BY name) AS _rank,
            name
        FROM
            OCCUPATIONS
        WHERE
            OCCUPATION = "Professor"      
),
S AS
(
        SELECT
            ROW_NUMBER() OVER (ORDER BY name) AS _rank,
            name
        FROM
            OCCUPATIONS
        WHERE
            OCCUPATION = "Singer"      
),
A AS
(
        SELECT
            ROW_NUMBER() OVER (ORDER BY name) AS _rank,
            name
        FROM
            OCCUPATIONS
        WHERE
            OCCUPATION = "Actor"      
),
RANKS AS
(
    SELECT DISTINCT
        res._rank
    FROM
        (
            SELECT
                D._rank
            FROM
                D
            UNION ALL
            SELECT
                P._rank
            FROM
                P
            UNION ALL          
            SELECT
                S._rank
            FROM
                S
            UNION ALL
            SELECT
                A._rank
            FROM
                A
         ) res
    ORDER BY
        _rank        
)
SELECT
    D.name,
    P.name,
    S.name,
    A.name
FROM
    RANKS RS
LEFT JOIN
    D
ON
    RS._rank = D._rank
LEFT JOIN
    P
ON
    RS._rank = P._rank
LEFT JOIN