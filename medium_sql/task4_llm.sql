--Вариант 1

WITH dates AS (
  -- даты, которые встречаются только как конец
  SELECT DISTINCT end_date AS dt FROM projects
  EXCEPT
  SELECT DISTINCT start_date FROM projects

  UNION ALL

  -- даты, которые встречаются только как старт
  SELECT DISTINCT start_date AS dt FROM projects
  EXCEPT
  SELECT DISTINCT end_date FROM projects
),
grouped AS (
  SELECT
    dt,
    (ROW_NUMBER() OVER (ORDER BY dt) - 1) / 2 AS pos
  FROM dates
)
SELECT
  MIN(dt) AS start_date,
  MAX(dt) AS end_date
FROM grouped
GROUP BY pos
ORDER BY (MAX(dt) - MIN(dt)), MIN(dt);


--- Вариант 2

WITH dates AS (
  SELECT DISTINCT p1.end_date AS dt
  FROM projects p1
  WHERE NOT EXISTS (
    SELECT 1 FROM projects p2 WHERE p2.start_date = p1.end_date
  )
  UNION ALL
  SELECT DISTINCT p1.start_date AS dt
  FROM projects p1
  WHERE NOT EXISTS (
    SELECT 1 FROM projects p2 WHERE p2.end_date = p1.start_date
  )
),
grouped AS (
  SELECT
    dt,
    (ROW_NUMBER() OVER (ORDER BY dt) - 1) / 2 AS pos
  FROM dates
)
SELECT
  MIN(dt) AS start_date,
  MAX(dt) AS end_date
FROM grouped
GROUP BY pos
ORDER BY (MAX(dt) - MIN(dt)), MIN(dt);


--- Вариант 3

WITH events AS (
  SELECT start_date AS dt, +1 AS delta FROM projects
  UNION ALL
  SELECT end_date   AS dt, -1 AS delta FROM projects
),
timeline AS (
  SELECT
    dt,
    SUM(delta) OVER (ORDER BY dt ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cov,
    LAG(SUM(delta) OVER (ORDER BY dt)) OVER () AS prev_cov
  FROM events
),
gaps AS (
  -- конец занятого блока (cov меняется с >0 на 0) — это начало «дыры»
  SELECT dt AS gap_start
  FROM timeline
  WHERE prev_cov > 0 AND cov = 0

  UNION ALL

  -- начало занятого блока (cov меняется с 0 на >0) — это конец «дыры»
  SELECT dt AS gap_end
  FROM timeline
  WHERE prev_cov = 0 AND cov > 0
),
paired AS (
  SELECT
    dt,
    (ROW_NUMBER() OVER (ORDER BY dt) - 1) / 2 AS pos
  FROM gaps
)
SELECT
  MIN(dt) AS start_date,
  MAX(dt) AS end_date
FROM paired
GROUP BY pos
ORDER BY (MAX(dt) - MIN(dt)), MIN(dt);
