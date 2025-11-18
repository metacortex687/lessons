-- llm
WITH sends_with_stats AS (
  SELECT
    cs.id,
    cs.user_id,
    cs.sent_at,
    -- сколько отправок было за предыдущие 7 дней
    COUNT(csb.id) AS prior_touches,
    -- был ли engagement в течение 24 часов
    EXISTS (
      SELECT 1
      FROM engagement_events ee
      WHERE ee.user_id     = cs.user_id
        AND ee.campaign_id = cs.campaign_id
        AND ee.event_time BETWEEN cs.sent_at
                             AND cs.sent_at + INTERVAL '1 day'
    ) AS engaged_24h
  FROM
    campaign_sends cs
  LEFT JOIN
    campaign_sends csb
      ON  csb.user_id   = cs.user_id
      AND csb.sent_at  < cs.sent_at
      AND csb.sent_at >= cs.sent_at - INTERVAL '7 days'
  GROUP BY
    cs.id, cs.user_id, cs.sent_at
)
SELECT
  s.prior_touches,
  COUNT(*) AS sends,
  SUM(s.engaged_24h::int) AS engagements,
  TO_CHAR(
    ROUND(
      SUM(s.engaged_24h::int)::numeric * 100 / COUNT(*),
      2
    ),
    'FM990.00'
  ) AS engagement_rate_pct
FROM
  sends_with_stats s
GROUP BY
  s.prior_touches
ORDER BY
  s.prior_touches;




-- Best Practices
select 
  prior_touches,
  count(*) sends,
  sum(engagement) engagements,
  to_char(sum(engagement)*100.0/count(*), 'FM990.00') engagement_rate_pct 
from (
  select  
  count(*) over (partition by user_id order by sent_at range '7 day' preceding exclude group) prior_touches,
  exists(
    select 1 from engagement_events 
    where engagement_events.user_id = campaign_sends.user_id and engagement_events.campaign_id = campaign_sends.campaign_id
      and event_time >= sent_at and event_time < sent_at +'1 day'::interval)::int engagement
  from campaign_sends) t
group by prior_touches  
order by prior_touches
