-- MySQL 8+
SELECT ROUND(AVG(LAT_N), 4) AS MEDIAN
FROM (
  SELECT
    LAT_N,
    ROW_NUMBER() OVER (ORDER BY LAT_N) AS rn,
    COUNT(*) OVER () AS cnt
  FROM STATION
) AS ordered
WHERE rn IN (FLOOR((cnt + 1) / 2), CEIL((cnt + 1) / 2));
