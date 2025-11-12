--https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true
SELECT
    MAX((SELECT MAX(salary*months) FROM EMPLOYEE)),
    COUNT(*)
FROM
    EMPLOYEE    
WHERE 
    salary*months = (SELECT MAX(salary*months) FROM EMPLOYEE)