-- Универсально (MySQL/PostgreSQL/SQL Server)
SELECT
  ROUND(
    SQRT(
      POWER(lat_max - lat_min, 2) +
      POWER(lon_max - lon_min, 2)
    ),
    4
  ) AS distance
FROM (
  SELECT
    MIN(LAT_N)  AS lat_min,
    MAX(LAT_N)  AS lat_max,
    MIN(LONG_W) AS lon_min,
    MAX(LONG_W) AS lon_max
  FROM STATION
) AS ext;
