```
6.1

//Переменные в классе который агрегирует данные из различных источников и сохраняет их
//1. Получает события из различных источников
//2. Преобразует их в те которые надо сохранить
//3. Сохраняет их в базу данных

EventAggregator:
    event_sources 
    event_translator
    event_writer 
	 

//Ещё два примера названий переменных (name, properties), в классе Event 
Event: 
    name
    properties


6.2
//В событие для даты добавил информацию о формате хранимой даты,
//а для свойств - формат хранимых в ней данных
Event: 
    date_iso
    properties_json

wallet_id_sha256
//ид кошелька с указаним алгоритма хэширования которым был получен

hogql_query_text
//указан используемый вариант SQL и тип данных в переменной


6.3 
//Здесь контекст указывает что это дата события, имя события и свойства события
Event: 
    name
    date_iso    
    properties_json


6.4
name - type_event 
//тип события, это точнее

events - award_points
//начисленные баллы

css - default_style_css
//стиль используемый по умолчанию

event_ids - awarded_event_ids
//идентификаторы событий по которым уже  начисленны баллы

api_key - personal_api_key
//Персональный ключ доступа к базе данных, это важно так как этот тип ключа позволяет делать только запросы


