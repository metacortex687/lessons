--https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true

SELECT
    s.hacker_id,
    H.name,
    sum(S.score) AS score
FROM
    (
        SELECT
            hacker_id,
            challenge_id,
            max(score) as score
        FROM
            SUBMISSIONS
        GROUP BY
            hacker_id, challenge_id    
    ) S --Scores
JOIN
    HACKERS H
ON 
    H.hacker_id = S.hacker_id
GROUP BY 
    s.hacker_id, H.name
HAVING
    sum(S.score) > 0
ORDER BY
    score DESC, s.hacker_id

