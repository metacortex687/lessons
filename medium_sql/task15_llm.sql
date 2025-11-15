-- ответ тот же самый
-- попросил вариант с оконными функциями


-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true

WITH HackerCreatedChallenges AS (
    SELECT
        base.hacker_id,
        base.name,
        base.created_count,
        MAX(base.created_count) OVER ()                         AS max_created_count,
        COUNT(*)             OVER (PARTITION BY base.created_count) AS hackers_with_same_count
    FROM (
        SELECT
            C.hacker_id,
            H.name,
            COUNT(C.challenge_id) AS created_count
        FROM
            CHALLENGES AS C
            JOIN HACKERS AS H
              ON H.hacker_id = C.hacker_id
        GROUP BY
            C.hacker_id,
            H.name
    ) AS base
)
SELECT
    hacker_id,
    name,
    created_count
FROM
    HackerCreatedChallenges
WHERE
    created_count = max_created_count          -- максимальное число задач
    OR hackers_with_same_count = 1            -- или уникальное значение
ORDER BY
    created_count DESC,
    hacker_id;
