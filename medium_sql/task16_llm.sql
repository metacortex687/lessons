
WITH max_scores AS (
    SELECT
        hacker_id,
        challenge_id,
        MAX(score) AS max_score
    FROM
        SUBMISSIONS
    GROUP BY
        hacker_id, challenge_id
),
leaderboard AS (
    SELECT
        ms.hacker_id,
        h.name,
        SUM(ms.max_score) AS total_score
    FROM
        max_scores AS ms
    JOIN
        HACKERS AS h
        ON h.hacker_id = ms.hacker_id
    GROUP BY
        ms.hacker_id, h.name
)
SELECT
    hacker_id,
    name,
    total_score AS score
FROM
    leaderboard
WHERE
    total_score > 0
ORDER BY
    total_score DESC,
    hacker_id;
