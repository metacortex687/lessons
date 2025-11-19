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
