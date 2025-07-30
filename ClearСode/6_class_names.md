```


3.1.
RuleManager - Rule
//Метод получения актуального правила начисления баллов, перенес в метод класса  Rule

BulkPointsCalculator - Awarder
//Награда


UserReportGenerator - UserReport
//Отчет пользователя

GenerateReport - WeekReport
//Отчет за неделю

DiscourseManager - DiscourseAPI
//выполняет запросы к API


3.2 

fetch_events_by_user - get_events_by_user
//Получает запросы сгруппированные по пользователям
//Везде в других местах используется get

add_events - create_events
//метод создает объекты в базе данных

_make_dataexplorer_request - discourse_api_data_explorer_post
//post запрос к api

get_like_events - get_events
//из контекста понятно что это за события

get_post_events - get_events
//аналогично выше

get_comment_events - getevents
//аналогично выше

sync_all - sync_event_in_period
//Синхронизация событий через загрузку и проверку уже загруженных за период

send_posthog_query - send_query
//Из контекста понятно

calculate_award_for_date - award_for_date
//метод не только считает, но и выполняет запись данных о награде в базу данных

calculate_bulk_for_date - award_for_period
//начисляет за период


```