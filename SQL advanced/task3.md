1. Найдите все отряды, у которых нет лидера.

```sql
SELECT
	squad_id,
	name
FROM
	Squads
WHERE
	leader_id IS NULL
```



2. Получите список всех гномов старше 150 лет, у которых профессия "Warrior".

``` sql
SELECT
    name,
    age
FROM
    Dwarves
WHERE
    profession = 'Warrior' and age > 150
```

3. Найдите гномов, у которых есть хотя бы один предмет типа "weapon".

``` sql
SELECT
	D.name AS DvarfName
FROM
	Dwarves D
JOIN
    Items I
ON
    D.dwarf_id = I.owner_id 
WHERE
    I.type = 'weapon'
```


4. Получите количество задач для каждого гнома, сгруппировав их по статусу.

``` sql
SELECT
	D.name AS DwarfName,
	T.status AS TaskStatus,
	COUNT(T.task_id) AS TasksCount
FROM
	Dwarves D
LEFT JOIN
    Tasks T
ON
    D.dwarf_id = T.assigned_to
GROUP BY
    D.name, T.status
```

Описание решения:
В случае если у гнома нет назначенных на него задач, то количество будет 0 , а в колонке статус задачи будет NULL.

5. Найдите все задачи, которые были назначены гномам из отряда с именем "Guardians".

``` sql
SELECT
    T.description AS TaskDescription,
    T.status AS TaskStatus
FROM
    Tasks T
JOIN
	Dwarves D
ON
    T.assigned_to = D.dwarf_id
JOIN
	Squads S
ON
	D.squad_id = S.squad_id
WHERE
    S.name = 'Guardians'
```

Описание решения:
Непонятно, что делать если гном leader_id в таблице Squads, а в таблице Dwarves у него не указан этот squad_id. Предполагаю, что запрос должен возвращать данные, а проверка ошибок это не его ответственность.


6. Выведите всех гномов и их ближайших родственников, указав тип родственных отношений.

``` sql
SELECT
	D1.name AS LeftDwarfName,
	R.relationship AS Relationship,
	D2.name RightDwarfName
    
FROM 
	Dwarves D1
JOIN
	Relationships  R
ON
	D1.dwarf_id = R.dwarf_id
JOIN
    Dwarves D2
ON 
	R.related_to = D2.dwarf_id
WHERE
	R.relationship in ('Супруг','Родитель', 'Друг')


UNION

SELECT
	D2.name AS LeftDwarfName,
	CASE
		WHEN R.relationship = 'Родитель' THEN 'Ребенок'
		ELSE R.relationship
	END AS  Relationship
	D1.name RightDwarfName,
    
FROM 
	Dwarves D1
JOIN
	Relationships  R
ON
	D1.dwarf_id = R.dwarf_id
JOIN
    Dwarves D2
ON 
	R.related_to = D2.dwarf_id
WHERE
	R.relationship in ('Супруг', 'Родитель')
```

Описание решения:
Предполагаю что нужна таблица, вида LeftDwarfName, Relationship,  RightDwarfName. При этом есть отношения симметричные и не симметричные. То-есть если гном является родителем для  другого гнома, то этот другой гном является ребенком для этого. 
Для симметричных отношений вроде 'Супруг' и 'Друг', для однотипности представления данных, и поскольку у нас нет критерия выбора кого в какую колонку помещать, продублируем запись, симметрично поменяв содержимое колонок.