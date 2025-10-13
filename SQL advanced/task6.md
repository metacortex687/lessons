
Задача 2: Получение данных о гноме с навыками и назначениями

``` sql

SELECT 
	JSON_BUILD_OBJECT(
		'dwarf_id', d.dwarf_id,
		'name', d.name,
		'age', d.age,
		'profession', d.profession,
		'related_entities', 
			JSON_BUILD_OBJECT (
				'skill_ids', (
					SELECT JSON_AGG(ds.skill_id)
					FROM DWARF_SKILLS ds
					WHERE ds.dwarf_id = d.dwarf_id
				),
				'assignment_ids', (
					SELECT JSON_AGG(da.assignment_id)
					FROM DWARF_ASSIGNMENTS da
					WHERE da.dwarf_id = d.dwarf_id
				),
				'squad_ids', (
					SELECT JSON_AGG(sm.squad_id)
					FROM SQUAD_MEMBERS sm
					WHERE sm.dwarf_id = d.dwarf_id
				),			
				'equipment_ids', (
					SELECT JSON_AGG(de.equipment_id)
					FROM DWARF_EQUIPMENT de
					WHERE de.dwarf_id = d.dwarf_id
				)			
			)
	)
FROM
	DWARVES d

```



Задача 3: Данные о мастерской с назначенными рабочими и проектами

``` sql

SELECT 
	JSON_BUILD_OBJECT(
		'workshop_id', w.workshop_id,
		'name', w.name,
		'type', w.type,
		'quality', w.quality,
		'related_entities', 
			JSON_BUILD_OBJECT (
				'craftsdwarf_ids', (
					SELECT JSON_AGG(wc.dwarf_id)
					FROM WORKSHOP_CRAFTSDWARVES wc
					WHERE wc.workshop_id = w.workshop_id
				),
				'project_ids', (
					SELECT JSON_AGG(p.project_id)
					FROM PROJECTS p
					WHERE p.workshop_id = w.workshop_id
				),
				'input_material_ids', (
					SELECT JSON_AGG(wm.material_id)
					FROM WORKSHOP_MATERIALS wm
					WHERE wm.workshop_id = w.workshop_id AND wm.is_input
				),		
				'output_product_ids', (
					SELECT JSON_AGG(wm.material_id)
					FROM WORKSHOP_MATERIALS wm
					WHERE wm.workshop_id = w.workshop_id AND NOT wm.is_input
				)		
			)
	)
FROM
	WORKSHOPS w

```


Задача 4: Данные о военном отряде с составом и операциями

``` sql

SELECT 
	JSON_BUILD_OBJECT(
		'squad_id', ms.squad_id,
		'name',ms.name,
		'formation_type', ms.formation_type,
		'leader_id', ms.leader_id,
		'related_entities', 
			JSON_BUILD_OBJECT (
				'member_ids', (
					SELECT JSON_AGG(sm.dwarf_id)
					FROM SQUAD_MEMBERS sm
					WHERE sm.squad_id = ms.squad_id
				),
				'equipment_ids', (
					SELECT JSON_AGG(se.equipment_id)
					FROM SQUAD_EQUIPMENT se
					WHERE se.squad_id = ms.squad_id
				),
				'operation_ids', (
					SELECT JSON_AGG(so.operation_id)
					FROM SQUAD_OPERATIONS so
					WHERE so.squad_id = ms.squad_id
				),		
				'training_schedule_ids', (
					SELECT JSON_AGG(st.schedule_id)
					FROM SQUAD_TRAINING st
					WHERE st.squad_id = ms.squad_id
				),	
				'battle_report_ids', (
					SELECT JSON_AGG(sb.report_id)
					FROM SQUAD_BATTLES sb
					WHERE sb.squad_id = ms.squad_id
				)		
			)
	)
FROM
	MILITARY_SQUADS ms

```

Рефлексия:

1. При всей сложности описываемой ситуации данными, запросы оказалось писать не сложно. Оформляя при этом запрос отступами.

2. В этот раз решил строки обернуть `JSON_BUILD_OBJECT`, хотя до конца не уверен в этом решении. Возможно, механизм, который будет создавать REST API, сделает это лучше.

3. Как вариант можно использовать 'COALESCE'. 
Например так:

``` sql

...

'equipment_ids', COALESCE(
					(
						SELECT JSON_AGG(se.equipment_id)
						FROM SQUAD_EQUIPMENT se
						WHERE se.squad_id = ms.squad_id
					),
						'[]'::json
				),
				
...

```
В ответах был бы результат вида `'equipment_ids': []`, а не `'equipment_ids': NULL` как сейчас в PostgreSQL.

4. В JSON_AGG решил не заворачивать, но тогда странно использовать и JSON_BUILD_OBJECT для строк.


