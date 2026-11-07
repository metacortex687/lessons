# Добавлен класс Vector<T>
# Выполнена проверка типов с помощью mypy
# Тесты в блоке if __name__ == "__main__":


from copy import copy, deepcopy
import json
from typing import Generic, Self, Sequence, TypeVar, Union
from inspect import isfunction
from typing import final

class General(object):

    @final
    def copy(self)  -> Self:
        return copy(self)
    
    @final
    def deep_copy(self)  -> Self:
        return deepcopy(self)

    @final
    def __eq__(self, other: object) -> bool:
        return type(self) is type(other) and self.__dict__ == other.__dict__

    @final
    def serialize(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=True)

    @final
    @classmethod
    def deserialize(cls: type[Self], data: str) -> Self:
        fields = json.loads(data)
        return cls(**fields)

    @final
    def __repr__(self):
        fields = ", ".join(
            f"{name}={value!r}"
            for name, value in self.__dict__.items()
        )
        return f"{type(self).__name__}({fields})"
        
    @final
    def is_type(self, check_type: type) -> bool:
        return type(self) is check_type 

    @final
    def type(self) -> type:
        return type(self)

    def __add__(self, other:Self):
        raise NotImplementedError



class Any(General):
    pass


class Integer(Any):

    def __init__(self, value:int):
        self.__value = value

    def __add__(self, other:'Integer') -> 'Integer | Void':
        return Integer(self.__value+other.__value)


class String(Any):

    def __init__(self, value:str):
        self.__value = value

    def __add__(self, other:'String') -> 'String | Void':
        return String(self.__value+other.__value)


@final
class Void(Integer, String):
    def __init__(self):
        pass

        # Временно закоментировал, для корректной работы проверки типов методы надо явно переопределять

        # def return_void(self, *args, **kwargs):
        #     return Void()

        # cls = type(self)

        # for base in cls.__mro__[1:]:
        #     for name, value in vars(base).items():
        #         if isfunction(value) and not name.startswith("__"):
        #             setattr(cls, name, return_void)

    def __add__(self, other: General) -> 'Void':
        return Void()

    def __radd__(self, other: General) -> 'Void':
        return Void()

    def __len__(self):
        return 0






T = TypeVar("T", bound=General, covariant=True)

class Vector(Generic[T],General):
    def __init__(self, values:Sequence[General]): 
        self._values = values

    def __len__(self):
        return len(self._values)

    def __add__(self, other: 'Vector | Void') -> 'Vector | Void':
        if isinstance(other, Void):
            return Void()

        if len(self) != len(other):
            return Void()

        return Vector([value1 + value2 for value1, value2 in zip(self._values, other._values)])

# Запуск модуля
# uv run OOAP2\task15.py

# Запуск проверки типов
# uv run --with mypy  mypy "OOAP2\task14.py"

if __name__ == "__main__":
# Сложение векторов
    vector1: Vector[Integer] = Vector([Integer(1),Integer(2),Integer(3)])
    vector2: Vector[Integer] = Vector([Integer(4),Integer(5),Integer(6)])

    result1 = vector1 + vector2
    print(result1)

    expected1: Vector[Integer] = Vector([Integer(5),Integer(7),Integer(9)])
    
    assert result1 == expected1

# Сложение векторов разной длинны
    vector3: Vector[Integer] = Vector([Integer(7)])
    result2 = vector1 + vector3
    print(result2)

    expected2: Void = Void()
    
    assert result2 == expected2  

# Сложение составных векторов

    vector4: Vector[Vector[Vector[Integer]]] = Vector([
        Vector([
            Vector([Integer(1),Integer(2)])
            ])
        ])
    
    vector5: Vector[Vector[Vector[Integer]]] = Vector([
        Vector([
            Vector([Integer(3),Integer(4)])
            ])
        ])

    result3 = vector4 + vector5
    print(result3)

    expected3: Vector[Vector[Vector[Integer]]] = Vector([
        Vector([
            Vector([Integer(4),Integer(6)])
            ])
        ])

    assert result3 == expected3

# Сложение составных векторов где возможен Void
    vector6: Vector[Vector[Vector[Integer]]] = Vector([
        Vector([
            Vector([Integer(1),Integer(2)])
            ])
        ])
    
    vector7: Vector[Vector[Vector[Integer]]] = Vector([
        Vector([
            Vector([Integer(3)])
            ])
        ])

    result4 = vector6 + vector7
    print(result4)

    expected4: Vector[Vector[Void]] = Vector([
        Vector([
            Void()
            ])
        ])

    assert result4 == expected4




