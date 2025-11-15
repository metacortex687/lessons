--https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true

WITH HACKER_CREATED_CHALLANGES AS (
        SELECT
            C.hacker_id,
            COUNT(C.challenge_id) created_count,
            H.name
        FROM
            CHALLENGES C
        JOIN
            HACKERS H
        ON 
            H.hacker_id = C.hacker_id
        GROUP BY
            C.hacker_id, H.name 
)
SELECT
    HCC.hacker_id,
    HCC.name,
    HCC.created_count
FROM
    HACKER_CREATED_CHALLANGES HCC
JOIN
    (
        SELECT
            COUNT(hacker_id) AS count_hacker,
            created_count
        FROM
            HACKER_CREATED_CHALLANGES 
        GROUP BY
            created_count       
    ) SR --SAME RESULT
ON
    HCC.created_count = SR.created_count    
WHERE 
    HCC.created_count = (SELECT max(created_count) FROM HACKER_CREATED_CHALLANGES)
    OR SR.count_hacker = 1
ORDER BY
    HCC.created_count DESC, HCC.hacker_id    