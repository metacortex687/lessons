--- https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true
SELECT 
    C.company_code,
    C.founder,
    COUNT(DISTINCT LM.lead_manager_code),
    COUNT(DISTINCT SM.senior_manager_code),
    COUNT(DISTINCT M.manager_code),
    COUNT(DISTINCT E.employee_code)
FROM
    COMPANY C
LEFT JOIN
    LEAD_MANAGER LM
ON
    C.company_code = LM.company_code
LEFT JOIN
    SENIOR_MANAGER SM
ON
  LM.company_code = SM.company_code
  AND LM.lead_manager_code = SM.lead_manager_code 
LEFT JOIN
    MANAGER M
ON
  SM.company_code = M.company_code
  AND SM.lead_manager_code = M.lead_manager_code
  AND SM.senior_manager_code = M.senior_manager_code
LEFT JOIN
    EMPLOYEE E
ON
  M.company_code = E.company_code
  AND M.lead_manager_code = E.lead_manager_code
  AND M.senior_manager_code = E.senior_manager_code
  AND M.manager_code = E.manager_code 
GROUP BY
    C.company_code, C.founder    
ORDER BY
    c.company_code    

