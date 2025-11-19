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


