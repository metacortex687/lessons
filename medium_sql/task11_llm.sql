SELECT
    MAX(salary*months),
    COUNT(*)
FROM
    EMPLOYEE    
WHERE 
    salary*months = (SELECT MAX(salary*months) FROM EMPLOYEE)


--по мотивам llm 