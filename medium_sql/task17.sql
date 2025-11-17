-- https://www.hackerrank.com/challenges/weather-observation-station-15/problem?isFullScreen=true

SELECT
    ROUND(S.LONG_W,4)
FROM
    STATION S
JOIN
    (
        SELECT
            max(lat_n) as lat_n
        FROM
            STATION
        WHERE
            lat_n < 137.2345
    ) MLN -- max lat_n
ON
    MLN.lat_n = S.lat_n