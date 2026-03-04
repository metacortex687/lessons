SELECT
  p.customer_id ,
  c.email,
  p.payments_count,
  p.total_amount::float
FROM
  (
    SELECT
      customer_id,
      COUNT(payment_id) AS payments_count,
      SUM(amount) AS total_amount
    FROM
      payment
    GROUP BY
      customer_id
    ORDER BY
      total_amount DESC  
    LIMIT 10    
  ) p --payment
LEFT JOIN
  (
    SELECT
      lr.customer_id,
      c.email
    FROM
      (
        SELECT
          customer_id,
          max(last_update) AS last_update
        FROM
          customer
        WHERE
          active = 1
        GROUP BY
          customer_id 
      ) lr --last record
    JOIN customer c
    ON c.customer_id = lr.customer_id AND c.last_update = lr.last_update 
  ) c --customer
ON
  p.customer_id = c.customer_id
ORDER BY
  total_amount DESC



--лучшее решение
SELECT
  customer.customer_id,
  customer.email,
  COUNT(payment.payment_id) AS payments_count,
  CAST(SUM(payment.amount) AS float) AS total_amount
FROM customer
JOIN payment
  ON customer.customer_id = payment.customer_id
GROUP BY customer.customer_id
ORDER BY total_amount DESC
LIMIT 10

--усложнилось так как предполагал, что записи о email пользователя хранятся несколько и актуальна последняя. 