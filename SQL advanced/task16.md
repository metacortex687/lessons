
``` sql
WITH THREAT_STATS AS
(
    SELECT 
        c.creature_id AS creature_id,
        c.creature_type AS creature_type,
        c.threat_level AS threat_level,
        last_cs.date AS last_sighting_date,
        avg_distance_to_fortress AS territory_proximity,
        SUM(c.estimated_population) AS estimated_numbers
    FROM
        CREATURES c
    JOIN
        (
            SELECT
                max(date) AS date,
                creature_id
            FROM
                CREATURE_SIGHTINGS
            GROUP BY
                creature_id    
        ) last_cs
    ON
        c.creature_id = last_cs.creature_id
    JOIN
        (
            SELECT
                AVG(distance_to_fortress) AS avg_distance_to_fortress,
                creature_id
            FROM
                CREATURE_TERRITORIES
            GROUP BY
                creature_id    
        ) ct
    ON
        c.creature_id = ct.creature_id 
    GROUP BY
        creature_id,creature_type,threat_level,last_sighting_date,territory_proximity            
),
ZONE_STATS AS
(
    SELECT
        l.zone_id AS zone_id,
        l.name AS zone_name,
        AVG((wall_integrity+trap_density)/2) AS vulnerability_score,
        SUM(ca.count_attack) AS historical_breaches,
        AVG(l.fortification_level) AS fortification_level,
        SUM(avg_military_response_time_minutes)/SUM(ca.count_attack)  AS military_response_time 
    FROM
        LOCATIONS l
    LEFT JOIN
    (
        SELECT
            COUNT(attack_id) AS count_attack,
            AVG(military_response_time_minutes) AS avg_military_response_time_minutes 
            location_id 
        FROM
            CREATURE_ATTACKS
        GROUP BY
            location_id    
    ) ca
    ON
        l.location_id  = ca.location_id
    GROUP BY
        l.zone_id, l.name    
),
SECURITY_EVOLUTION_STATS AS
(
    SELECT
        EXTRACT(YEAR FROM date) AS year,
        SUM(CASE WHEN outcome = 'Win' THEN 1 ELSE 0 END) AS count_win,
        ROUND(AVG(CASE WHEN outcome = 'Win' THEN 1 ELSE 0 END)*100/SUM(CASE WHEN outcome = 'Win' THEN 1 ELSE 0 END),2) AS defense_success_rate,
        COUNT(attack_id) AS total_attacks,
        SUM(casualties) AS casualties
    FROM
        CREATURE_ATTACKS
    GROUP BY
        year
),
CURRENT_THREAT_LEVEL AS
(
    SELECT
        CASE 
            WHEN avg_lvl >= 8 THEN 'High'
            WHEN avg_lvl >= 5 THEN 'Moderate'
            ELSE 'Low'
        END AS level 
    FROM
        (SELECT AVG(threat_level) avg_lvl FROM THREAT_STATS)
)
SELECT
    (SELECT COUNT(total_attacks) FROM SECURITY_EVOLUTION_STATS) AS total_recorded_attacks,
    (SELECT COUNT(DISTINCT creature_id) FROM THREAT_STATS) AS unique_attackers,
    (SELECT SUM(count_win)/NULLIF(SUM(total_attacks),0) FROM SECURITY_EVOLUTION_STATS) AS overall_defense_success_rate,
    json_build_object(
        'current_threat_level', (SELECT level FROM CURRENT_THREAT_LEVEL),
        'active_threats',
            (
                SELECT
                    json_agg(
                        jsonb_build_object(
                            'creature_type', ts.creature_type,    
                            'threat_level', AVG(ts.threat_level),
                            'last_sighting_date', MAX(ts.last_sighting_date),
                            'territory_proximity', AVG(ts.territory_proximity),
                            'estimated_numbers', SUM(ts.estimated_numbers),
                            'creature_ids', json_agg(SELECT _ts.creature_id FROM THREAT_STATS WHERE _ts.creature_type = ts.creature_type) 
                        )
                    )
                FROM 
                    THREAT_STATS ts
                GROUP BY
                    ts.creature_type
            ),
        "vulnerability_analysis",
            (
                SELECT
                    json_agg(
                        jsonb_build_object(
                            "zone_id",zone_id,
                            "zone_name",zone_name,
                            "vulnerability_score",vulnerability_score, 
                            "historical_breaches",historical_breaches,
                            "fortification_level",fortification_level,
                            "military_response_time", military_response_time
                        )
                    )
                FROM
                    ZONE_STATS       
            )
        "security_evolution",
            (
                SELECT
                    json_agg(
                        jsonb_build_object(
                            "year", year,
                            "defense_success_rate", defense_success_rate,
                            "total_attacks", total_attacks,
                            "casualties", casualties,
                            "year_over_year_improvement", defense_success_rate - LAG(defense_success_rate) OVER (ORDER BY year DESC)  
                        )
                    )
                FROM
                    SECURITY_EVOLUTION_STATS
            )
    ) AS security_analysis
FROM (SELECT 1) AS dummy
```

1. Разделы defense_effectiveness не заполнил так как нет описания таблицы Defense_Structures. Есть поле defense_structures_used в CREATURE_ATTACKS,  но непонятно что там хранится.

2. military_readiness_assessment - не заполнил так как с отярядами zone_id могу связать через location_id в SQUAD_TRAINING. Но атака существ и тренировки, как мне кажется это разные игровые ситуации.

3. В разделе "vulnerability_analysis" не заполнил "defense_coverage", так как непонятно откуда брать "structure_ids", предполагаю что это таблица Defense_Structures описания которой нет.
