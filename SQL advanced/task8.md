Задача 1*: Анализ эффективности экспедиций

``` sql
SELECT
	e_val.expedition_id,
	e_val.destination,
	e_val.status,
	e_val.survival_rate,
	e_val.artifacts_value,
	e_val.discovered_sites,
	e_val.encounter_success_rate,
	e_val.skill_improvement,
	e_val.expedition_duration,
	GREATEST(0, LEAST(
		0.800655 * ((e_val.survival_rate + e_val.encounter_success_rate) / 200.0)
		+ 0.187619 * LEAST(e_val.discovered_sites / 4.0, 1.0)
		+ 0.100000 * GREATEST(1.0 - e_val.expedition_duration / 62.0, 0.0)
		+ 0.015000 * LEAST(e_val.artifacts_value / 56000.0, 1.0)
		+ 0.015000 * LEAST(e_val.skill_improvement / 23.0, 1.0)
		+ 0.040636
	  , 1.0)) AS overall_success_score,
	JSON_BUILD_OBJECT (
		'member_ids', (
			SELECT JSON_AGG(em.dwarf_id)
			FROM EXPEDITION_MEMBERS em
			WHERE e_val.expedition_id = em.expedition_id
			ORDER BY em.dwarf_id
		),
		'artifact_ids', (
			SELECT JSON_AGG(ea.artifact_id)
			FROM EXPEDITION_ARTIFACTS ea
			WHERE e_val.expedition_id = ea.expedition_id
			ORDER BY ea.artifact_id
		),
		'site_ids', (
			SELECT JSON_AGG(es.site_id)
			FROM EXPEDITION_SITES es
			WHERE e_val.expedition_id = es.expedition_id
			ORDER BY es.site_id
		)		
	) AS related_entities	
FROM
(
	SELECT 
		e.expedition_id AS expedition_id,
		e.destination AS destination,
		e.status AS status,
		em.survival_rate AS survival_rate,
		COALESCE(ea.artifacts_value,0) AS artifacts_value,
		COALESCE(es.discovered_sites,0) AS discovered_sites,
		COALESCE(ec.encounter_success_rate,0) AS encounter_success_rate,
		COALESCE(skils.skill_improvement,0) as skill_improvement,
		e.return_date - e.departure_date as expedition_duration
	FROM EXPEDITIONS e	
	LEFT JOIN
		(
			select 
				expedition_id,
				AVG(survived::int) as survival_rate
			FROM
				expedition_members
			group by
				expedition_id		
		) em
	ON
		e.expedition_id = em.expedition_id
	LEFT JOIN
		(
			select 
				expedition_id,
				SUM(value) as artifacts_value
			FROM
				EXPEDITION_ARTIFACTS
			group by
				expedition_id		
		) ea
	ON
		e.expedition_id = ea.expedition_id
	LEFT JOIN
		(
			SELECT 
				expedition_id,
				COUNT(site_id) AS discovered_sites
			FROM EXPEDITION_SITES
			GROUP BY
				expedition_id					
		) es
	ON
		e.expedition_id = es.expedition_id
	LEFT JOIN
		(
			select 
				expedition_id,
				AVG(
					CASE
						WHEN outcome IN ('GOOD') then 1
						ELSE 0
					END
				) as encounter_success_rate
			FROM
				EXPEDITION_CREATURES
			group by
				expedition_id		
		) ec
	ON
		e.expedition_id = EC.expedition_id	
	LEFT JOIN
		(
			SELECT 
				count(skill_id) AS skill_improvement,
			FROM
				EXPEDITION_MEMBERS em
			JOIN 
				DWARF_SKILLS ds
			ON
				em.dwarf_id = ds.dwarf_id 
			WHERE
				em.expedition_id = e.expedition_id
				AND ds.date >= e.departure_date
				AND ds.date < e.return_date
		) skils
	ON
		e.expedition_id = skils.expedition_id	
	WHERE
		e.departure_date IS NOT NULL
		AND e.return_date IS NOT NULL
) e_val	
ORDER BY
	overall_success_score DESC
	
```


Описание решения: 

Поскольку overall_success_score может вычисляться по сложной формуле, которую предоставит игровой дизайнер, то все параметры, которые могут понадобится для расчёта, оберну в запрос.

В этом запросе буду использовать подзапросы, которые присоединю через левое соединения к EXPEDITIONS через expedition_id. При этом некоторые ответы оберну COALESCE , так как могут быть NULL.

Для получения уровней считаю, что если они были получены гномами, которые в отряде, во время экспедиции, значит эти уровни были получены в экспедиции.

В целом в данном решении, можно придумать входящие условия при которых запрос будет некорректным. Например, есть допущение что 'outcome' в случае успеха "GOOD", хотя я этого не знаю.