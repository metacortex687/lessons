1. Получить информацию о всех гномах, которые входят в какой-либо отряд, вместе с информацией об их отрядах.

``` sql
SELECT d.dwarf_id, d.name dwarf_name, sq.squad_id, sq.name squad_name 
FROM dwarves d INNER JOIN squads sq ON d.squad_id = sq.squad_id
```



2. Найти всех гномов с профессией "miner", которые не состоят ни в одном отряде.
 ```sql
 SELECT * FROM dwarves  WHERE profession = 'miner' and squad_id is NULL
   
   ```

3. Получить все задачи с наивысшим приоритетом, которые находятся в статусе "pending"
``` sql
SELECT * FROM tasks WHERE status = 'pending' and priority = (SELECT max(priority) FROM tasks)

```

4. Для каждого гнома, который владеет хотя бы одним предметом, получить количество предметов, которыми он владеет.
``` sql

SELECT d.dwarf_id, d.name dwarf_name, count(*) count_items 
FROM dwarves d INNER JOIN items itm 
ON d.dwarf_id = itm.owner_id or itm.owner_id is NULL 
GROUP BY d.dwarf_id, d.name

Описание решения: Использую внутреннее соединение, если у предмета owner_id NULL, это значит, что им владеют все гномы. 
Далее эту таблицу, содержащую уникальные строки гном-предмет, группирую по гномам и считаю количество строк.

```

5. Получить список всех отрядов и количество гномов в каждом отряде. Также включите в выдачу отряды без гномов.
 ``` sql 
 SELECT sq.squad_id, sq.name as squad_name, count(d.dwarf_id) as count_members 
 FROM squads sq LEFT JOIN dwarves d 
 ON d.squad_id = sq.squad_id
 GROUP BY sq.squad_id, sq.name
   
   ```
Описание решения: Использую левое соединение. Левая таблица - отряды, правая таблица - гномы. Это гарантирует, что в выборку попадут все отряды. Чтобы считалось количество гномов, использую агрегатную функцию count(d.dwarf_id). 
Это гарантирует, если d.dwarf_id будет NULL, то число будет 0, в отличие от count(*).


6. Получить список профессий с наибольшим количеством незавершённых задач ("pending" и "in_progress") у гномов этих профессий.

``` sql
WITH profession_incomplete AS
(
SELECT d.profession, count(*) count_incomplete 
FROM tasks t INNER JOIN dwarves d 
ON t.assigned_to = d.dwarf_id  
WHERE t.status in ('pending','in_progress') GROUP BY d.profession
)
SELECT * FROM profession_incomplete 
WHERE count_incomplete = (SELECT max(count_incomplete) FROM profession_incomplete)
```

Описание решения: Поскольку таблица, в которой содержится количество незавершенных задач для профессии, используется дважды, раз для получения результата и другой для определения максимального количества незавершенных задач, использую для этой таблицы `WITH`, что повышает читаемость запроса. `WITH`  в одних базах данных может быть макросом, в других
временной таблицей.


7. Для каждого типа предметов узнать средний возраст гномов, владеющих этими предметами.

```sql
SELECT item_type, avg(age_dwarf) average_age_owner FROM 
(SELECT DISTINCT itm.type item_type, dwarf_id, d.age age_dwarf 
FROM Items itm INNER JOIN Dwarves  d 
ON itm.owner_id = d.dwarf_id or itm.owner_id is NULL) 
GROUP BY item_type  
``` 

Описание решения: Через внутреннее соединение получаю таблицу: тип предмета, гном. Учитывая что если "owner_id" NULL значит у этого предмета владельцы все гномы.  Поскольку в этой таблице содержатся повторяющиеся записи использую директиву DISTINCT. И уже по этой таблице считаю средний возраст. 

8. Найти всех гномов старше среднего возраста (по всем гномам в базе), которые не владеют никакими предметами.

```sql
SELECT d.dwarf_id, d.name dwarf_name 
FROM Dwarves d LEFT JOIN Items itm ON itm.owner_id = d.dwarf_id 
WHERE itm.item_id is NULL and d.age > (SELECT avg(age) FROM dwarves)   
```