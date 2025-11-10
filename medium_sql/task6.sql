--https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true
SELECT
    ROUND(max(LAT_N)-min(LAT_N)+max(LONG_W)-MIN(LONG_W),4)
FROM
    STATION