Рефлексия:

1. При решении задания в этот раз делал код для того, что понимаю как получить. Для того что не знаю как сделать, описывал затруднения.

2. defense_structures_used - было непонятно что это за поле, и какой оно имеет тип. По тому что в эталонном решении используется 
`ds.structure_id = ANY(ca.defense_structures_used)`. Означает, что данное поле имеет тип массив.

3. Таблица defense_structures, в задании 5 есть описание текстом, но не было описания полей, поэтому воссоздам её структуру по тексту запроса.

| DEFENCE_STRUCTURES    |
| --------------------- |
| structure_id (PK)     |
| type                  |
| location_id (FK)      |
| construction_date     |
| last_maintenance_date |
| quality               |
| material_id (FK)      |

Непонятно, про material_id, как будто, только один материал у одной защитной структуры. Если материал имеет тип тогда и один тип материала. При этом это внешний аналогично ключ используется во многих других таблицах.
Возможно это что-то составное из ресурсов.

4. Для таблица squad_movement, поля что упоминаются в звпросах

| SQUAD_MOVEMENT        |
| --------------------- |
| patrol_zone_id (FK)   |
| squad_id (FK)         |

5. Для таблицы Squad_Battle_Participation, поля что упоминаются в звпросах 

| SQUAD_BATTLE_PARTICIPATION|
| ---------------------     |
| attack_id (FK)            |
| squad_id (FK)             |

6. fortress_events, аналогично поля что упоминаются в запросе 

| FORTRESS_EVENTS           |
| ---------------------     |
| date                      |
| resource_allocation       |
| fortress_casualties       |
| event_type                |


5. Теперь сравню часть полей, что пробовал получить:

Для JSON-объектов данные готовлю по возможности в почти одноименных CTE-таблицах. При сравнении путей получения данных буду протягивать до таблиц БД, из которых получаю, не упоминая CTE-таблицы.



| Поле                          | Эталонное решение                                                                                                            | Мое решение                                                                                           | Рефлексия                                                                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| total_recorded_attacks        | `CREATURE_ATTACKS.COUNT(*)                                                                                                   | `CREATURE_ATTACKS.COUNT(attack_id)                                                                    | +                                                                                                                                                            |
| unique_attackers              | `CREATURE_ATTACKS.COUNT_DISTINCT(creature_id)                                                                                | `CREATURES.COUNT_DISTINCT(creature_id)                                                                | - <br>не все существа атакуют                                                                                                                                |
| count_win                     | `CREATURE_ATTACKS.COUNT(*).WHERE(outcome = 'Repelled')                                                                       | `CREATURE_ATTACKS.COUNT(attack_id).WHERE(outcome = 'Win')                                             | +<br>в эталонном решении нет такого поля, но схожее выражение используется при рассчете overall_defense_success_rate                      |
| overall_defense_success_rate  | count_win/total_recorded_attacks                                                                                             | count_win/total_recorded_attacks                                                                      | +                                                                                                                                                            |
| current_threat_level          | Определяется количеством атак за последний месяц. И в зависимости от их количества это или 'Critical', 'High' или 'Moderate' | Определяется CREATURES.AVG(threat_level)<br>и в зависимости от значения это 'High', 'Moderate', 'Low' |                                                                                                                                                              |
| threat_level                  | CREATURES.threat_level                                                                                                       | CREATURES.threat_level                                                                                | +                                                                                                                                                            |
| territory_proximity           | CREATURE_TERRITORIES.distance_to_fortress                                                                                    | CREATURE_TERRITORIES.AVG(distance_to_fortress)                                                        | использую среднее поскольку, предположил что у существ с одним creature_id может быть несколько территорий. <br>Если это не так, то эталонное решение лучше. |
| estimated_numbers             | CREATURES.estimated_population                                                                                               | CREATURES.SUM(estimated_population).GROUP_BY(type)                                                    | Предполагал, что для одного type могут быть различные creature_id.                                                                                           |
| В целом записи active_threats | делается отбор по active = TRUE                                                                                              | нет отбора                                                                                            | -<br>стоило бы сделать, было понятно из контекста                                                                                                            |



