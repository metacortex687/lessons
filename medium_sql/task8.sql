--https://www.hackerrank.com/challenges/weather-observation-station-20/problem?isFullScreen=true
SELECT
    ROUND(AVG(MEDIAN_BOUNDS.LAT_N),4) AS MEDIUM
FROM
    (
        SELECT
            CASE
                WHEN NUMBERED.count_row%2 = 1 THEN
                    CASE 
                        WHEN NUMBERED.N = (NUMBERED.count_row+1)/2 THEN NUMBERED.LAT_N
                        ELSE NULL
                    END
                ELSE
                    CASE 
                        WHEN NUMBERED.N = NUMBERED.count_row/2+1 THEN NUMBERED.LAT_N
                        WHEN NUMBERED.N = NUMBERED.count_row/2-1 THEN NUMBERED.LAT_N
                        ELSE NULL
                    END
            END AS LAT_N 
        FROM
            (
                SELECT
                    ID AS ID,
                    ROW_NUMBER() OVER (ORDER BY LAT_N) AS N,
                    LAT_N AS LAT_N,
                    COUNT(ID) OVER() AS count_row
                FROM
                    STATION
            ) NUMBERED
    ) MEDIAN_BOUNDS


