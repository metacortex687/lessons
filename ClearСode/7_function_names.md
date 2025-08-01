```
get_id — get_user_id_by_email
// получаю id пользователя по email

get_email — get_email_by_user_id
// получаю email по id пользователя 

check_existing_events — find_events_by_sync_key
//ищет события, которые уже были загружены 

get_events — get_awardable_events
// получить события для начисления награды

start — start_bot
// Стартуею бота

ask_participation — send_participation_request
// отправить запрос об участии

participation_response — handle_participation_response
// обработчик ответа пользователя, вызывается как callback


notify_empty_username — notify_username_required
// оповещает пользователя об необходимости заполнить в Telegram имя пользователя

feedback_off_command — handle_feedback_disable
// обработчик команды, которой вызывается, когда отказываешься от получения обратной связи

feedback_on_command — handle_feedback_enable
// обработчик команды, которой вызывается, когда включаешь получение обратной связи

meeting_rating_response — handle_meeting_rating, save_meeting_rating
// обрабатывает оценку встречи пользователем, разбил на две функции: `handle_meeting_rating` является callback-обработчиком, `save_meeting_rating` сохраняет данные рейтинга

sum_linked_list — add_elementwise
складывает два списка поэлементно и возвращает третий, тип понятен из контекста.



```