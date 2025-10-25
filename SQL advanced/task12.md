
``` SQL

WITH squad_batle_dates AS (
	SELECT DISTINCT
		squad_id,
		date
	FROM
		SQUAD_BATTLES	
),
join_on_batle_date AS (
	SELECT DISTINCT
		sbd.squad_id,
		sbd.date,
		COUNT(sm.dwarf_id) AS count_join
	FROM
		squad_batle_dates sbd
	LEFT JOIN
		SQUAD_MEMBERS sm
	ON
		sbd.squad_id = sm.squad_id
		AND sm.join_date < sbd.date	
	GROUP BY sbd.squad_id,sbd.date		
),
exit_on_batle_date AS (
	SELECT DISTINCT
		sbd.squad_id,
		sbd.date,
		COUNT(sm.dwarf_id) AS count_exit
	FROM
		squad_batle_dates sbd
	LEFT JOIN
		SQUAD_MEMBERS sm
	ON
		sbd.squad_id = sm.squad_id
		AND sm.exit_date < sbd.date
	GROUP BY sbd.squad_id,sbd.date	
),
count_members_on_batle AS
(
	SELECT 
		sb.squad_id as squad_id,
		sb.report_id as report_id,
		jn.count_join AS join_count,
		COALESCE(ex.count_exit,0) AS exit_count
	FROM
		SQUAD_BATTLES sb
	LEFT JOIN
		join_on_batle_date jn	
	ON
		sb.squad_id = jn.squad_id
		AND sb.date = jn.date
	LEFT JOIN
		exit_on_batle_date ex	
	ON
		sb.squad_id = ex.squad_id
		AND sb.date = ex.date	
)
SELECT 
	ms.squad_id AS squad_id,
	ms.name AS squad_name,
	ms.formation_type AS formation_type,
	ldrs.name AS leader_name,
	sb.total_battles AS total_battles,
	sb.victories AS victories,
	ROUND(sb.victories/NULLIF(sb.total_battles,0)*100,2) AS victory_percentage,
	ROUND(sb.casualties/sb.count_on_statr_batle*100,2) AS casualty_rate,
	ROUND(sb.enemy_casualties/sb.casualties,2) AS casualty_exchange_ratio,
	sm.total_members_join AS total_members_ever,
	sm.total_members_join - sm.total_members_exit AS current_members,
	ROUND((sm.total_members_join - sm.total_members_exit)/NULLIF(sm.total_members_join,0)*100,2) AS retention_rate,
	se.avg_equipment_quality AS avg_equipment_quality,
	st.count_training_sessions AS  total_training_sessions,
	st.avg_effectiveness AS  avg_training_effectiveness,
	CORR(st.count_training_sessions, sb.victories ) AS training_battle_correlation,
	sti.count_improv_combat_skill/sm.total_members_join AS avg_combat_skill_improvement
	ROUND(
        (sb.victories::DECIMAL / sm.total_members) * 0.3 +
        (sb.enemy_casualties/sb.casualties * 0.15), 3 
    ) AS overall_effectiveness_score	
JSON_BUILD_OBJECT (
		'member_ids', (
			SELECT JSON_AGG(_ms.dwarf_id)
			FROM MILITARY_SQUADS _ms
			WHERE ms.squad_id  = _ms.squad_id 
		),
		'equipment_ids', (
			SELECT JSON_AGG(_se.equipment_id)
			FROM SQUAD_EQUIPMENT _se
			WHERE ms.squad_id  = _se.squad_id 
		),
		'battle_report_ids', (
			SELECT JSON_AGG(_sb.report_id)
			FROM SQUAD_BATTLES _sb
			WHERE ms.squad_id  = _sb.squad_id 
		),
		'training_ids', (
			SELECT JSON_AGG(_st.schedule_id)
			FROM SQUAD_TRAINING _st
			WHERE ms.squad_id  = _st.squad_id 
		)
	) AS related_entities		
FROM
	MILITARY_SQUADS ms	
LEFT JOIN 
	(
		SELECT
			dwarf_id,
			name
		FROM
			DWARVES	
	) ldrs
ON
	ms.leader_id = ldrs.dwarf_id
LEFT JOIN
	(
		SELECT
			_sb.squad_id,
			COUNT(_sb.report_id) AS total_battles,
			SUM(CASE _sb.outcome
				WHEN 'victory' THEN 1
				ELSE 0
			END) AS victories,
			SUM(_sb.casualties) AS casualties,
            SUM(_sb.enemy_casualties) AS enemy_casualties,
			SUM(c_on_btl.join_count - c_on_btl.exit_count) AS count_on_start_batle			
		FROM
			SQUAD_BATTLES _sb
		JOIN
			count_members_on_batle c_on_btl
		ON
			_sb.squad_id = c_on_btl.squad_id 
			AND _sb.report_id = c_on_btl.report_id
		GROUP BY
			_sb.squad_id	
	) sb
ON
	ms.squad_id = sb.squad_id	
LEFT JOIN
	(
		SELECT
            squad_id,
			COUNT(DISTINCT (dwarf_id, join_date)) AS total_members_join
			COUNT(DISTINCT (dwarf_id, exit_date)) AS total_members_exit	
		FROM
			SQUAD_MEMBERS
		GROUP BY
			squad_id	
	) sm
ON
	ms.squad_id = sm.squad_id	
LEFT JOIN
	(
		SELECT 
			_se.squad_id,
			AVG(e.quality) AS avg_equipment_quality
		FROM
			SQUAD_EQUIPMENT _se
		JOIN
			EQUIPMENT e
		ON
			_se.equipment_id = e.equipment_id
		GROUP BY
			_se.squad_id	
	) se
ON
	ms.squad_id = se.squad_id	
LEFT JOIN
	(
		SELECT
			squad_id,
			COUNT(schedule_id) AS count_training_sessions
			AVG(effectiveness) AS avg_effectiveness
		FROM
			SQUAD_TRAINING 
		GROUP BY
			squad_id			
	) st
ON
	ms.squad_id = st.squad_id		
LEFT JOIN
	(
		SELECT 
			_st.squad_id AS squad_id
			COUNT(1) AS count_improv_combat_skill	
		FROM
			SQUAD_TRAINING _st
		JOIN
			SQUAD_MEMBERS _sm
		ON
			_st.squad_id = _sm.squad_id
		JOIN
			DWARF_SKILLS _ds
		ON
			_sm.dwarf_id = _ds.dwarf_id
			AND _ds.date = _st.date
		JOIN
			SKILLS _s
		ON _ds.skill_id = _s.skill_id
		WHERE
			_s.category = 'comdat'	
		GROUP BY
			_st.squad_id		
	) sti
ON
	ms.squad_id = sti.squad_id	
	
```

