WITH ext AS (
  SELECT
    MIN(LAT_N)  AS lat_min,
    MAX(LAT_N)  AS lat_max,
    MIN(LONG_W) AS lon_min,
    MAX(LONG_W) AS lon_max
  FROM STATION
)
SELECT
  ROUND( (lat_max - lat_min) + (lon_max - lon_min), 4 ) AS manhattan_distance
FROM ext;
