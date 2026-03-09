--# write your SQL statement here: 
-- you are given a table 'fibo' with column 'n'.
-- return a table with:
--   this column and your result in a column named 'res'
--   ordered ascending by 'n'
--   distinct results (remove duplicates)

WITH RECURSIVE numbers AS (
  SELECT 
    0::BIGINT AS f0,
    1::BIGINT AS f1,
    1 AS n,
    (SELECT max(n) FROM fibo) AS max_n  
  
  UNION

  SELECT 	
    f1 AS f0,
    f1+f0 AS f1,
    n + 1 AS n,
    max_n AS max_n
  FROM
    numbers
  WHERE
    n <= max_n
)

SELECT DISTINCT
	fibo.n AS n,
	numbers.f0 AS res 
FROM
    fibo
LEFT JOIN 
    numbers
ON
  fibo.n = numbers.n
ORDER BY n


---- Лучшее решение:
with recursive cte_fibo as
(
  SELECT 1 n, 0::BIGINT x, 1::BIGINT fibo
  union all
  select n+1, fibo, x + fibo
  from cte_fibo
  where n < 50
)

select n, x as res 
from cte_fibo 
WHERE n in (SELECT n FROM fibo)
ORDER BY n

--- В условиях задачи нет ограничение на n=50, 51-й элемент фибоначи 20 365 011 074 а BIGINT максимальное значение 9223372036854775807 а INT 4 294 967 295
--  наименование переменных в лучшем решении лучше