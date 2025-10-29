```sql
WITH CARAVAN_STATS AS
(
    SELECT
        cg.caravan_id AS caravan_id,
        SUM(CASE WHEN cg.type = 'Import' THEN cg.quantity*cg.value) AS import_value,
        SUM(CASE WHEN cg.type = 'Export' THEN cg.quantity*cg.value) AS export_value,
        SUM(cg.quantity*cg.value) AS total_trade_value,
        de.trade_relationship AS trade_relationship,
        de.civilization_type AS civilization_type,
        c.fortress_id AS fortress_id,
        EXTRACT(YEAR FROM c.arrival_date) AS year,
        EXTRACT(QUARTER FROM c.arrival_date) AS quarter
    FROM
        CARAVAN_GOODS cg
    JOIN
        DIPLOMATIC_EVENTS de
    ON
        cg.caravan_id = cd.caravan_id
    JOIN
        CARAVANS c
    ON
        cg.caravan_id = c.caravan_id
    GROUP BY
        caravan_id,fortress_id, trade_relationship, civilization_type, year,
),
GOODS_STATS
(
    SELECT
        cg.goods_id AS goods_id
        cg.material_type AS material_type,
        SUM(CASE WHEN cg.type = 'Import' THEN cg.quantity*cg.value ELSE 0 END) AS import_value,
        SUM(CASE WHEN cg.type = 'Export' THEN cg.quantity*cg.value ELSE 0 END) AS export_value,
        SUM(CASE WHEN cg.type = 'Export' THEN cg.quantity ELSE 0 END) AS export_quantity,
        c.fortress_id AS fortress_id,
        cg.original_product_id AS product_id
    FROM
        CARAVAN_GOODS cg
    JOIN
        CARAVANS c
    ON
        cg.caravan_id = c.caravan_id
),
WORKSHOP_PRODUCTS_STATS
(
    SELECT
        w.workshop_id AS workshop_id,
        p.product_id AS product_id,
        w.type AS workshop_type,
        p.type AS product_type,
        SUM(wp.quantity) AS quantity_product,
        SUM(wp.quantity*p.value) AS prime_value
    FROM
        WORKSHOPS w
    LEFT JOIN
        WORKSHOP_PRODUCTS wp
    ON
        w.workshop_id = wp.workshop_id
    LEFT JOIN
        PRODUCTS p
    ON
        wp.product_id = p.product_id
    GROUP BY
        w.workshop_id, p.product_id, w.type, p.type
)
SELECT
    (SELECT COUNT(DISTINCT cs.fortress_id) FROM CARAVAN_STATS) AS total_trading_partners,
    (SELECT SUM(cs.total_trade_value) FROM CARAVAN_STATS) AS all_time_trade_value,
    (SELECT SUM(cs.export_value) - SUM(cs.import_value) FROM CARAVAN_STATS) AS all_time_trade_balance,
    json_build_object("civilization_trade_data",
        SELECT
            json_agg(
                jsonb_build_object(
                    "civilization_type", cs.civilization_type,
                    "total_caravans", COUNT(cs.caravan_id),
                    "total_trade_value", SUM(cs.total_trade_value),
                    "trade_balance", SUM(cs.export_value) - SUM(cs.import_value),
                    "trade_relationship", cs.trade_relationship,
                    "diplomatic_correlation", CORR(cs.total_trade_value, CASE WHEN cs.trade_relationship = "Favorable" THEN 1 ELSE 0 END),
                    "caravan_ids", (
                        SELECT json_agg(_cs.caravan_id)
                        FROM
                            CARAVAN_STATS _cs
                        WHERE
                            _cs.civilization_type = cs.civilization_type
                    )
                )
            )
        FROM
            CARAVAN_STATS cs
        GROUP BY cs.civilization_type
    ) AS civilization_data,
    json_build_object("resource_dependency",
        SELECT
            json_agg(
                jsonb_build_object(
                    "material_type", gs.material_type,
                    "dependency_score", SUM(gs.export_value) - SUM(gs.import_value),
                    "total_imported", SUM(gs.import_value),
                    "import_diversity", COUNT(DISTINCT gs.fortress_id),
                    "resource_ids", (
                        SELECT json_agg(DISTINCT _gs.goods_id)
                        FROM
                            GOODS_STATS _gs
                        WHERE
                            _gs.material_type = gs.material_type
                    )
                )
            )
        FROM
            GOODS_STATS gs
    ) AS critical_import_dependencies,
    json_build_object("export_effectiveness",
        SELECT
            json_agg(
                jsonb_build_object(
                    "workshop_type", wp.workshop_type,
                    "product_type", wp.product_type,
                    "export_ratio", ROUND(export.export_quantity/wp.quantity_product*100),
                    "avg_markup", ROUND(export.export_value*wp.quantity_product/NULLIF(export.export_quantity*wp.prime_value) ,2),
                    "workshop_ids", (
                        SELECT json_agg(DISTINCT _wp.workshop_id)
                        FROM
                            WORKSHOP_PRODUCTS_STATS _wp
                        WHERE
                            _wp.workshop_type = wp.workshop_type
                    )
                )
            )
        FROM
            WORKSHOP_PRODUCTS_STATS wp
        LEFT JOIN
            (
                SELECT
                    export_value,
                    export_quantity
                FROM
                    GOODS_STATS
                GROUP BY
                    product_id
            ) export
        ON
            wp.product_id = export.product_id
    ) AS export_effectiveness,
    json_build_object("trade_growth",
        SELECT
            json_agg(
                jsonb_build_object(
                    "year", year,
                    "quarter", quarter,
                    "quarterly_value", SUM(total_trade_value),
                    "quarterly_balance", SUM(export_value) - SUM(import_value),
                    "trade_diversity", COUNT(DISTINCT fortress_id)
                )
            )
        FROM
            CARAVAN_STATS
        GROUP BY
            year, quarter
        ORDER BY
            year, quarter
    ) AS trade_timeline


```
