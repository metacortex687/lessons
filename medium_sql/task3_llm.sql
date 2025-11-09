--- Вариант 1

SELECT 
    c.company_code,
    c.founder,
    COUNT(DISTINCT lm.lead_manager_code)   AS lead_managers,
    COUNT(DISTINCT sm.senior_manager_code) AS senior_managers,
    COUNT(DISTINCT m.manager_code)         AS managers,
    COUNT(DISTINCT e.employee_code)        AS employees
FROM company AS c
LEFT JOIN lead_manager AS lm 
    USING (company_code)
LEFT JOIN senior_manager AS sm 
    USING (company_code, lead_manager_code)
LEFT JOIN manager AS m 
    USING (company_code, lead_manager_code, senior_manager_code)
LEFT JOIN employee AS e 
    USING (company_code, lead_manager_code, senior_manager_code, manager_code)
GROUP BY c.company_code, c.founder
ORDER BY c.company_code;


--- Враиант 2 (когда много таблиц лучше)
WITH 
  lm AS (SELECT company_code, COUNT(DISTINCT lead_manager_code) AS lead_managers FROM lead_manager GROUP BY company_code),
  sm AS (SELECT company_code, COUNT(DISTINCT senior_manager_code) AS senior_managers FROM senior_manager GROUP BY company_code),
  m  AS (SELECT company_code, COUNT(DISTINCT manager_code) AS managers FROM manager GROUP BY company_code),
  e  AS (SELECT company_code, COUNT(DISTINCT employee_code) AS employees FROM employee GROUP BY company_code)
SELECT
    c.company_code,
    c.founder,
    COALESCE(lm.lead_managers, 0)   AS lead_managers,
    COALESCE(sm.senior_managers, 0) AS senior_managers,
    COALESCE(m.managers, 0)         AS managers,
    COALESCE(e.employees, 0)        AS employees
FROM company AS c
LEFT JOIN lm USING (company_code)
LEFT JOIN sm USING (company_code)
LEFT JOIN m  USING (company_code)
LEFT JOIN e  USING (company_code)
ORDER BY c.company_code;
