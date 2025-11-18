-- https://www.codewars.com/kata/686e88bcedcbf29af056f499/train/sql
-- SQL for Marketing – Episode 1: Measuring Engagement Fatigue
-- 5 kyu (уменьшу сложность до 6 kyu, времени много уходит, иногда на эту лсожность буду заглядывать)

WITH PRIOR_7D_TOUCHES AS (
  SELECT
    CS.id,
    CS.user_id,
    CS.sent_at,
    COUNT(CSB.id) AS prior_touches  
  FROM
    campaign_sends CS
  LEFT JOIN
    campaign_sends CSB -- campaign_sends befor
  ON
    CS.user_id = CSB.user_id 
    AND CSB.sent_at < CS.sent_at 
    AND CS.sent_at - CSB.sent_at <= INTERVAL '7 days'
  GROUP BY
    CS.id, CS.user_id, CS.sent_at 
),
ENGADED_24H_SENDS AS (
    SELECT
      CS.id
    FROM
      campaign_sends CS
    WHERE 
      EXISTS (SELECT * FROM engagement_events 
                WHERE 
                  user_id = CS.user_id 
                  AND campaign_id  = CS.campaign_id 
                  AND event_time > CS.sent_at AND event_time - CS.sent_at <= INTERVAL '1 days')
)
SELECT
  PT.prior_touches,
  COUNT(PT.id) AS sends,
  COUNT(ES.id) AS engagements,
  TO_CHAR(ROUND(COUNT(ES.id)::numeric/COUNT(PT.id)*100,2),'FM990.00') AS engagement_rate_pct  
FROM
  PRIOR_7D_TOUCHES PT
LEFT JOIN
  ENGADED_24H_SENDS ES 
ON 
  PT.id = ES.id 
GROUP BY
  PT.prior_touches
ORDER BY
  PT.prior_touches    


