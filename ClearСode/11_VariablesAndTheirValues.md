````md

1. Инварианты

assert 1 <= day <= 31, "День должен быть в диапазоне 1..31"

2. Инварианты

assert 0 <= hour < 24, "Час должен быть в диапазоне 0..23"


3. Инварианты

def add_edge(graph: dict, u, v):
    assert u != v, "Петли запрещены"


4. Инварианты

while True:
    assert 0 <= i < len(_list), "Индекс должен быть внутри списка"


5. Инварианты

def split_array(arr: list[int]) -> tuple[list[int], list[int]]:
    # arr1, arr2 нужно получить из arr
    arr1, arr2 = ..., ...
    assert len(arr1) + len(arr2) == len(arr), "Сумма длин должна совпадать"
    return arr1, arr2


6. Инварианты

assert left_index < right_index, "Левый индекс должен быть меньше правого"


7. Инварианты

assert 0 <= left_index < len(lst), "Левый индекс вне диапазона"


8. Инварианты

assert 0 <= right_index < len(lst), "Правый индекс вне диапазона"


9. Инварианты

assert all(lst[i] <= lst[i+1] for i in range(len(lst)-1)), "Массив должен быть отсортирован"


10. Инварианты

assert balance >= 0, "Баланс всегда неотрицательный"


11. Инварианты

assert 0 <= agent.x < MAP_WIDTH and 0 <= agent.y < MAP_HEIGHT, "Координаты должны быть внутри карты"


12. Инварианты

assert (agent.health > 0) == agent.is_alive, "Статус жизни не соответствует здоровью"


13. Инварианты

assert len({agent.id for agent in population}) == len(population), "Идентификаторы агентов должны быть уникальными"


14. Инварианты

assert area > 0, "Площадь должна быть положительной"


15. Инварианты

assert all(emp.department_id is not None for emp in employees), "У всех сотрудников должен быть указан отдел"


16. Инициализация переменной

int agent_x = window_x + agent_offset_x;


17. Инициализация переменной

int agent_y = window_y + agent_offset_y;

18. Завершение работы с переменными

sum = None
//теперь эту переменную нельзя будет использовать в арифметических операциях

```
```
