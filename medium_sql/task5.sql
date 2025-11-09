--- https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
SELECT
    S.name
FROM
    STUDENTS S
JOIN
    FRIENDS AS BF -- Best Friends
ON
    S.id = BF.id
JOIN
    PACKAGES AS SBF -- Salary Best Friends
ON
    BF.friend_id = SBF.id
JOIN
    PACKAGES AS SS -- Salary Student
ON
    S.id = SS.id
WHERE
    SS.salary < SBF.salary
ORDER BY
    SBF.salary    




