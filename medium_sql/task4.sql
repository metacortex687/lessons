--- https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true
WITH DATES AS
    (
        SELECT
            end_date AS date
        FROM
            PROJECTS
        WHERE
            not end_date in (SELECT start_date FROM PROJECTS)

        UNION ALL

        SELECT
            start_date
        FROM
            PROJECTS
        WHERE
            not start_date in (SELECT end_date FROM PROJECTS) 
    ),
GROUP_DATES AS
    (
        SELECT
            date AS date,
            FLOOR((ROW_NUMBER() OVER (ORDER BY date) - 1) / 2) AS position  
        FROM
            DATES
    )
SELECT
    min(gd.date) AS start_date,
    max(gd.date) AS end_date
FROM
    GROUP_DATES gd
GROUP BY
    position  
ORDER BY
    max(gd.date)-min(gd.date), min(gd.date) 