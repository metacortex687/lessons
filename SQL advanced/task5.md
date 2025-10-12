1. Получение информации о крепости. 

``` sql
SELECT
	f.*,
	json_build_object(
		'dwarf_ids', (
			SELECT json_agg(d.dwarf_id)
			FROM dwarves d
			WHERE d.fortress_id = f.fortress_id
		),
		'resource_ids', (
			SELECT json_agg(fr.resource_id)
			FROM fortress_resources fr
			WHERE fr.fortress_id = f.fortress_id
		),		
		'workshop_ids', (
			SELECT json_agg(w.workshop_id)
			FROM workshops  w
			WHERE w.fortress_id = f.fortress_id
		),
		'squad_ids', (
			SELECT json_agg(m.squad_id)
			FROM military_squads  m
			WHERE m.fortress_id = f.fortress_id
		)
	) AS related_entities
FROM
	fortresses f
```

Рефлексия: 

Решение почти идентичное с примером. Вместо JSON_OBJECT использую json_build_object и вместо JSON_ARRAYAGG использую json_agg, которые используются в PostgreSQL.

JSON_ARRAYAGG — агрегатная функция, которая принимает одно значение и создает JSON.

JSON_OBJECT — создает JSON-объект, аргументы в нечетных позициях используя как ключ, а из четной позиции беря аргумент.

Рассматривал вариант обернуть строку запроса в JSON_OBJECT, а далее эти строки агрегировать с помощью JSON_ARRAYAGG, но в этом случае, если пустой результат запроса, то возвращаются [NULL], что странно.

Для получения серверного ответа в виде REST-выдачи в формате JSON использовал бы VIEW, созданные на основании этого запроса, и PostgREST.
