**Пример 1**

```python
# Тип данных для идентификации объекта EDBase в базе данных
@dataclass(frozen=True)
class EDIdentity:
    type_name: str
    reference: str | None = None
    components: tuple[tuple[str, Hashable], ...] = ()
    parent: "EDIdentity | None" = None
    name: str | None = None
    position: int | None = None
```

По факту он оказался излишен, в базовой иерархии типов не хватало класса, который содержит ключевые поля, вместо него был класс для группировки полей. 
По которому нельзя было определить, можно ли его использовать для идентификации объекта в строке таблицы базы данных (в качестве ключа).

**Пример 2.**

```python
# базовый тип для объектов загружаемых из EnterpriseData
class EDBase:
    def __setattr__(self, name: str, value: object) -> None:
        raise AttributeError("Значения EnterpriseData неизменяемы")

    def __delattr__(self, name: str) -> None:
        raise AttributeError("Значения EnterpriseData неизменяемы")

```

Решил сделать полностью иммутабельными объекты


**Пример 3**

```python
# Состояние архива от пользователя на этапе загружки и проверки  
class UploadPhase(TextChoices):
    WAITING = "waiting", "Ожидает начала"
    UPLOADING = "uploading", "Получение частей"
    UPLOADED = "uploaded", "Все части получены"
    VALIDATING = "validating", "Проверка начата"
    VALIDATED = "validated", "Проверка завершена"
```

Рефлексия: 
Можно было использовать паттерн "Состояние" рассматривая в том числе и ошибку при загрузке как одно из состояний.


**Пример 4.**

```python
# Фабрика объектов EnterpriseData. Проверяет одинаковость существующих реквизитов для объектов с одним ключом уникальности в рамках одной загрузки.
class EDObjectFactory:
    def __init__(self) -> None:
        self._objects: dict[Hashable, EDObject] = {}

    def get_or_create(
        self, key: Hashable, properties: Mapping[str, object]
    ) -> EDObject:
        candidate = EDObject(properties)
        existing = self._objects.get(key)
        if existing is not None:
            if existing != candidate:
                raise ValueError(f"Противоречивые данные объекта {key!r}")
            return existing
        self._objects[key] = candidate
        return candidate
```

Рефлексия: изначально использовал словарь, чтобы при загрузке были уникальные объекты. Но когда понял, что сильно удобнее, если эти объекты будут иммутабельными, определив для них операцию сравнения, то уникальность объектов не нужна, она теперь определяется не по идентичности, а по значению. Оставил для проверки на непротиворечивость загружаемых данных.


Общая рефлексия: 
Код в проекте стал сильно лучше. В правилах закрепил, что это ООП-проект и не должно быть свободных функций по возможности. И каждый класс подписан. Классы стали сильно компактнее.

Плюс к этому стало сильно проще оценивать как корректность реализации, так и интерфейса класса. Сразу видны части реализации, которые относятся скорее к оптимизации и без них можно обойтись. И методы, которые или непонятно дял чего нужны, или выразимы через другие методы.