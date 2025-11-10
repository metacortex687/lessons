--https://www.hackerrank.com/challenges/weather-observation-station-19/problem?isFullScreen=true
SELECT
    ROUND(SQRT((max(LAT_N)-min(LAT_N))*(max(LAT_N)-min(LAT_N))+(max(LONG_W)-MIN(LONG_W))*(max(LONG_W)-MIN(LONG_W))),4)
FROM
    STATION