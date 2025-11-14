WITH full_scores AS (
    SELECT
        H.hacker_id,
        H.name,
        SUM(
            CASE 
                WHEN S.score = D.score THEN 1 
                ELSE 0 
            END
        ) AS full_count
    FROM
        HACKERS     AS H
    JOIN
        SUBMISSIONS AS S
        ON H.hacker_id = S.hacker_id
    JOIN
        CHALLENGES  AS C
        ON C.challenge_id = S.challenge_id
    JOIN
        DIFFICULTY  AS D
        ON D.difficulty_level = C.difficulty_level
    GROUP BY
        H.hacker_id,
        H.name
)
SELECT
    CONCAT(hacker_id, ' ', name)
FROM
    full_scores
WHERE
    full_count > 1
ORDER BY
    full_count DESC,
    hacker_id;

--llm: улучшена читабельность запроса
