-- https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true

SELECT
    CONCAT(H.hacker_id,' ',H.name)
FROM
    HACKERS H
JOIN
    SUBMISSIONS S
ON
    H.hacker_id = S.hacker_id
JOIN
    CHALLENGES C
ON
    C.challenge_id = S.challenge_id
JOIN
    DIFFICULTY D
ON
    D.difficulty_level = C.difficulty_level
GROUP BY
    H.hacker_id, H.name
HAVING
    COUNT(CASE WHEN D.score = S.score THEN C.challenge_id ELSE NULL END) > 1
ORDER BY
    COUNT(CASE WHEN D.score = S.score THEN C.challenge_id ELSE NULL END) DESC, H.hacker_id

