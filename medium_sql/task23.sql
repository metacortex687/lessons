--https://www.codewars.com/kata/58113a64e10b53ec36000293/train/sql
-- SQL Basics: Simple EXISTS
--6 kyu

SELECT
  id,
  name
FROM
  departments D
WHERE
  EXISTS (SELECT 1 FROM sales WHERE department_id = D.id AND price > 98)