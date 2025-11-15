-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true

WITH GOOD_WANDS AS (
    SELECT 
        W.id,
        WP.age,
        W.coins_needed,
        W.power
    FROM
        WANDS W
    JOIN
        WANDS_PROPERTY WP
    ON
        W.code = WP.code
    WHERE
        WP.is_evil = 0
)
SELECT
    GW.id,
    GW.age,
    GW.coins_needed,
    GW.power
FROM
    GOOD_WANDS GW
JOIN
    (
        SELECT
            age,
            power,
            min(coins_needed) coins_needed
        FROM
            GOOD_WANDS 
        GROUP BY
            age, power          
    ) GP --Good price
ON
    GP.age = GW.age 
    AND GP.power = GW.power 
    AND GP.coins_needed = GW.coins_needed
ORDER BY
    GW.power DESC,  GW.age DESC


--Вариант 2. попросил с использованием оконных функций

WITH good_wands AS (
    SELECT
        w.id,
        wp.age,
        w.coins_needed,
        w.power,
        MIN(w.coins_needed) OVER (
            PARTITION BY
                wp.age,
                w.power
        ) AS min_coins_needed
    FROM
        WANDS AS w
        JOIN WANDS_PROPERTY AS wp
          ON w.code = wp.code
    WHERE
        wp.is_evil = 0
)
SELECT
    id,
    age,
    coins_needed,
    power
FROM
    good_wands
WHERE
    coins_needed = min_coins_needed
ORDER BY
    power DESC,
    age  DESC;
