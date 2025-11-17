SELECT *
FROM (
    SELECT 'US' AS location, * FROM ussales WHERE price > 50.00
    UNION ALL
    SELECT 'EU' AS location, * FROM eusales WHERE price > 50.00
) AS sales
ORDER BY location DESC, id;
