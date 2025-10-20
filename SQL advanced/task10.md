
```sql
SELECT
	w.workshop_id AS workshop_id,
	w.name AS workshop_name,
	w.type AS workshop_type,
	wc.num_craftsdwarves AS num_craftsdwarves,
	wp.total_quantity_produced AS total_quantity_produced,
	p.total_production_value AS total_production_value,
	p.total_production_value/IFNULL(p.duration_work,0) AS daily_production_rate,
	p.total_production_value/p.material_unit AS value_per_material_unit,
	NULL AS workshop_utilization_percent,
	NULL AS material_conversion_ratio,
	ds.average_craftsdwarf_skill AS average_craftsdwarf_skill,
	CORR(ds.average_craftsdwarf_skill,w.quality) AS skill_quality_correlation,
	JSON_BUILD_OBJECT (
		'craftsdwarf_ids', (
			SELECT JSON_AGG(_wc.dwarf_id)
			FROM WORKSHOP_CRAFTSDWARVES _wc
			WHERE w.workshop_id  = _wc.workshop_id 
		),
		'product_ids', (
			SELECT JSON_AGG(_wp.product_id)
			FROM WORKSHOP_PRODUCTS _wp
			WHERE w.workshop_id  = _wp.workshop_id 
		),
		'material_ids', (
			SELECT JSON_AGG(_p.material_id)
			FROM PRODUCTS _p
			WHERE w.workshop_id  = _p.workshop_id 
		),
		'project_ids', (
			SELECT JSON_AGG(_p.project_id)
			FROM PROJECTS _p
			WHERE w.workshop_id  = _p.workshop_id 
		)		
	) AS related_entities		

FROM
	WORKSHOPS w
JOIN
	(
		SELECT
			workshop_id,		
			COUNT(DISTINCT dwarf_id) AS num_craftsdwarves 
		FROM
			WORKSHOP_CRAFTSDWARVES
		GROUP BY
			workshop_id			
	) wc
ON
	w.workshop_id = wc.workshop_id
LEFT JOIN
	(
		SELECT
			workshop_id, 
			SUM(quantity) AS total_quantity_produced
		FROM
			WORKSHOP_PRODUCTS
		GROUP BY 
			workshop_id		
	) wp	
ON
	w.workshop_id = wp.workshop_id
LEFT JOIN
	(
		SELECT 
			_wp.workshop_id,
			COUNT(*) AS material_unit,
			EXTRACT(DAY FROM (MAX(_wp.created_by) - MIN(_p.production_date))) AS duration_work
			SUM(_wp.quantity*_p.value) AS total_production_value
		FROM
			WORKSHOP_PRODUCTS _wp
		JOIN 
			PRODUCTS _p
		ON
			_wp.workshop_id = _p.workshop_id
			AND _wp.product_id = _p.product_id
		GROUP BY 
			_wp.workshop_id			
	) p
ON
	w.workshop_id = p.workshop_id
LEFT JOIN
	(
		SELECT 
			_wc.workshop_id,
			AVG(level) AS average_craftsdwarf_skill
		FROM
			WORKSHOP_CRAFTSDWARVES _wc
		JOIN
			(
				SELECT 
					MAX(level),
					dwarf_id
				FROM
					DWARF_SKILLS			
			) _ds
		ON
			_wc.dwarf_id = _ds.dwarf_id
	) ds	
ON
	w.workshop_id = ds.workshop_id 	
		

```

Предварительная рефлексия:

1. workshop_id, workshop_name, workshop_type - беру из таблицы WORKSHOPS, к которой в основном через левое соединение буду добавлять данные.
2. num_craftsdwarves — считаю количество гномов через COUNT(DISTINCT dwarf_id), группируя по workshop_id. Использую DISTINCT, так как до конца не понятно, может ли гном переназначаться на другую role.
3. total_quantity_produced - беру из WORKSHOP_PRODUCTS, суммируя там quantity и группируя по workshop_id.
4. total_production_value - получаю через соединение таблиц WORKSHOP_PRODUCTS и PRODUCTS и суммируя value из таблицы PRODUCTS.
5. daily_production_rate - определяю время работы duration_work через min(production_date) из таблицы WORKSHOP_PRODUCTS, считая это временем назначения.
И max(created_by) из таблицы PRODUCTS, считая это временем выпуска. После чего делю total_production_value на duration_work. Хотя могу и ошибатся об created_by.

6. value_per_material_unit — непонятно откуда брать число единиц материалов, предположил, что это для каждой единицы материала в таблице PRODUCTS отдельная запись.
7. workshop_utilization_percent - не считаю. по идее я могу получить для product_id, считая production_date из WORKSHOP_PRODUCTS датой начала, а максимальный created_by из PRODUCTS — это дата окончания работы по product_id. Далее их надо как-то объединить, исключить пересечения. А после сложить сумму длительностей интервалов.
8. material_conversion_ratio - не понимаю, как считать.
9. average_craftsdwarf_skill - считаю для гномов максимальный level из DWARF_SKILLS уровнем и считаю от этого среднее.
10. skill_quality_correlation - использую встроенную функцию корреляций.
