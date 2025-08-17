```
1. Информативные комментарии

            #Из одной строки запроса создаем для одного участника событие комментарий отправлен
            club_comment_written = {
                "event_type": "ClubCommentWritten",
                "distinct_id": commenter_email,
                "properties": {
                    "sync_event_id": comment_id,
                    "commented_user_email": commented_user_email,
                    "source": "discourse_dataexplorer",
                    "timestamp": created_at
                },
                "timestamp": created_at
            }
            events.append(club_comment_written)

            #... для другого участника комментарий получен        
            club_comment_received = {
                "event_type": "ClubCommentReceived",
                "distinct_id": commented_user_email,
                "properties": {
                    "sync_event_id": comment_id,
                    "commenter_user_email": commenter_email,
                    "source": "discourse_dataexplorer",
                    "timestamp": created_at
                },
                "timestamp": created_at
            }
            events.append(club_comment_received)


2. Информативные комментарии

            #Из одной строки запроса создаем для одного участника событие лайк поставлен
            club_like_event = {
                "event_type": "ClubLike",
                "distinct_id": liker_email,
                "properties": {
                    "sync_event_id": action_id,
                    "liked_user_email": liked_email,
                    "source": "discourse_dataexplorer",
                    "timestamp": created_at
                },
                "timestamp": created_at
            }
            events.append(club_like_event)


            #... для другого участника лайк получен  
            club_like_received_event = {
                "event_type": "ClubLikeReceived",
                "distinct_id": liked_email,
                "properties": {
                    "sync_event_id": action_id,
                    "liker_user_email": liker_email,
                    "source": "discourse_dataexplorer",
                    "timestamp": created_at
                },
                "timestamp": created_at
            }
            events.append(club_like_received_event)

3. Комментарии TODO. Предупреждения о последствиях.

#todo: вынести в инициализацию класса
#в таком виде затрудняет тестирование
LIKES_QUERY_ID = int(os.getenv("LIKES_QUERY_ID", 6))

4. Комментарии TODO. Предупреждения о последствиях.

#todo: вынести в инициализацию класса
#в таком виде затрудняет тестирование
COMMENTS_QUERY_ID = int(os.getenv("COMMENTS_QUERY_ID", 7))

5. Комментарии TODO. Предупреждения о последствиях.
#todo: вынести в инициализацию класса
#в таком виде затрудняет тестирование
POSTS_QUERY_ID = int(os.getenv("POSTS_QUERY_ID", 8))


6. Прояснение. "В тестовой среде не работает SSL - используйте verify_ssl=False"

    def __init__(self,
                 discourse_base_url: str,
                 discourse_api_key: str,
                 discourse_username: str,
                 verify_ssl: bool = True):

        self.discourse_manager = DiscourseDataExplorerApi(
            base_url=discourse_base_url,
            api_key=discourse_api_key,
            api_username=discourse_username,
            # В тестовой среде не работает SSL - используйте verify_ssl=False
            verify_ssl=verify_ssl
        )

7. Усиление. Добавил усиление в комментарий.       

#Получить события для начисления баллов отсортированные по дате и сгруппированные по пользователям
#Сортировка по дате важна для корректного начисления баллов

events_by_user = self.sorted_events.get_sorted_awardable_events_by_user(date)

8. Предупреждение о последствиях.

# важно: для тестирования используем .env.test
# в противном случае будут использоваться переменные из .env рабочей среды
load_dotenv('.env.test')

9. Комментарии TODO.

        #todo: привести работу с датами к единому стандарту
        if from_date:
            if isinstance(from_date, datetime):
                params["from"] = from_date.strftime("%Y-%m-%d")
            params["from"] = from_date

        #todo: привести работу с датами к единому стандарту
        if to_date:
            if isinstance(to_date, datetime):
                params["to"] = to_date.strftime("%Y-%m-%d")
            params["to"] = to_date

10. Комментарии TODO.

            #todo: привести работу с датами к единому стандарту
            sorted_items = sorted(
                [(datetime.strptime(date, "%Y-%m-%d"), len(events))
                 for date, events in data[user_id].items()],
                key=lambda x: x[0]

            )
            
11. Комментарии TODO.

     #todo: привести работу с датами к единому стандарту
     from_date = datetime.strptime(from_date_str, "%Y-%m-%d")
     to_date = datetime.strptime(to_date_str, "%Y-%m-%d")


12. Комментарии TODO.

    #todo: привести работу с датами к единому стандарту
    rule_start_date = datetime.strptime(rule_data['start_date'], '%Y-%m-%d')

```