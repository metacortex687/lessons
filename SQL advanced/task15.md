Рефлексия

1. В этот раз получилось, лучше подготовить таблицы в разделе "WITH". Решения отличаются во многом из-за различия в понимании предметной области, и того что эталонное решение более полное чем пример возможного ответа. 

2. Распишу пути получения данных в эталонном решении.

```
civilization_trade_history
    civilization_type = CARAVANS.civilization_type  
    trade_year = CARAVAN_GOODS.EXTRACT_YEAR(trade_year)
    caravan_count = CARAVANS.COUNT_DISTINCT(caravan_id)  
    total_trade_value = TRADE_TRANSACTIONS.SUM(value)
    import_value = CARAVAN_GOODS.SUM(value ).WHERE(type = 'Import')
    export_value = CARAVAN_GOODS.SUM(value ).WHERE(type = 'Export')
    unique_goods_traded = CARAVAN_GOODS.COUNT_DISTINCT(goods_id) 
    unique_imports = CARAVAN_GOODS.COUNT_DISTINCT(goods_id).WHERE(type = 'Import')
    unique_exports = CARAVAN_GOODS.COUNT_DISTINCT(goods_id).WHERE(type = 'Export')
CARAVANS.JOIN_ON(caravan_id).TRADE_TRANSACTIONS.JOIN_ON(caravan_id).CARAVAN_GOODS
GROUPBY(civilization_type, trade_year)

fortress_resource_dependency
    material_type = CARAVAN_GOODS.material_type
    times_imported = CARAVAN_GOODS.COUNT_DISTINCT(goods_id)
    total_imported = CARAVAN_GOODS.SUM(quantity) 
    total_imported_value = CARAVAN_GOODS.SUM(value)
    caravans_importing = CARAVANS.COUNT_DISTINCT(caravan_id)
    avg_price_fluctuation = CARAVAN_GOODS.AVG(price_fluctuation)
    dependency_score = CARAVAN_GOODS.COUNT_DISTINCT(goods_id)*CARAVAN_GOODS.SUM(quantity)*(1/CARAVANS.COUNT_DISTINCT(civilization_type))
CARAVAN_GOODS.JOIN_ON(caravan_id).CARAVANS.WHERE(CARAVAN_GOODS.type = "Import")
GROUPBY(material_type)

diplomatic_trade_correlation
    civilization_type = CARAVANS.civilization_type
    diplomatic_events = DIPLOMATIC_EVENTS.COUNT_DISTINCT(event_id)
    positive_events = DIPLOMATIC_EVENTS.COUNT_DISTINCT(event_id).WHERE(outcome = 'Positive')
    negative_events = DIPLOMATIC_EVENTS.COUNT_DISTINCT(event_id).WHERE(outcome = 'Negative')
    total_trade_value = TRADE_TRANSACTIONS.SUM(value)
    trade_diplomacy_correlation = CORR(DIPLOMATIC_EVENTS.relationship_change, TRADE_TRANSACTIONS.value)  
CARAVANS.JOIN_ON(caravan_id).TRADE_TRANSACTIONS.JOIN_ON(civilization_type).DIPLOMATIC_EVENTS
GROUPBY(civilization_type)

workshop_export_effectiveness
    product_type = PRODUCTS.type
    workshop_type = WORKSHOPS.type
    products_created = PRODUCTS.COUNT_DISTINCT(product_id)
    products_exported = PRODUCTS.COUNT_DISTINCT(product_id).WHERE(PRODUCTS.product_id =  CARAVAN_GOODS.original_product_id)
    total_production_value = PRODUCTS.SUM(VALUE)
    export_value = CARAVAN_GOODS.SUM(value)
    avg_export_markup = AVG(CARAVAN_GOODS.value/PRODUCTS.value)
PRODUCTS.JOIN_ON(workshop_id ).WORKSHOPS.LEFTJOIN(product_id = original_product_id, type = 'Export')
GROUPBY(product_type,workshop_type)

trade_timeline
    year = CARAVANS.YEAR(arrival_date)
    quarter = CARAVANS.QUARTER(arrival_date)
    quarterly_trade_value = TRADE_TRANSACTIONS.SUM(value)
    trading_civilizations = CARAVANS.COUNT_DISTINCT(civilization_type)    
    import_value = TRADE_TRANSACTIONS.SUM(value).WHERE(balance_direction = 'Import')
    export_value = TRADE_TRANSACTIONS.SUM(value).WHERE(balance_direction = 'Export')
    previous_quarter_value = TRADE_TRANSACTIONS.LAG.ORDER_BY(year,quarter).SUM(value)
CARAVANS.JOIN_ON(caravan_id).TRADE_TRANSACTIONS
GROUP_BY(year,quarter)

```


3. Отличия

civilization_type = DIPLOMATIC_EVENTS.civilization_type (у меня)
civilization_type = CARAVANS.civilization_type (эталонное решение)


