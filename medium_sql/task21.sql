--https://www.codewars.com/kata/58112f8004adbbdb500004fe/train/sql
--SQL Basics: Simple UNION ALL
--6 kyu

SELECT
  sales.*
FROM
  (  
    SELECT
      'US' as location,
      id,
      name,
      price,
      card_name,
      card_number,
      transaction_date
    FROM
      ussales
    WHERE
      price > 50.00  

    UNION ALL

    SELECT
      'EU',
      id,
      name,
      price,
      card_name,
      card_number,
      transaction_date
    FROM
      eusales 
    WHERE
      price > 50.00  
  ) sales
ORDER BY
  sales.location DESC, sales.id  

  
  