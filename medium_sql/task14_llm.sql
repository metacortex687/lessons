WITH good_wands AS (
    SELECT
        w.id,
        wp.age,
        w.coins_needed,
        w.power
    FROM
        wands AS w
        JOIN wands_property AS wp
          ON w.code = wp.code
    WHERE
        wp.is_evil = 0
),
best_prices AS (
    SELECT
        age,
        power,
        MIN(coins_needed) AS min_coins_needed
    FROM
        good_wands
    GROUP BY
        age,
        power
)
SELECT
    gw.id,
    gw.age,
    gw.coins_needed,
    gw.power
FROM
    good_wands AS gw
    JOIN best_prices AS bp
      ON  bp.age             = gw.age
      AND bp.power           = gw.power
      AND bp.min_coins_needed = gw.coins_needed
ORDER BY
    gw.power DESC,
    gw.age   DESC;


--