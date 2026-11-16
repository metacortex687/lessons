
В решении рассмотрел полиморфное и контравариантное присваивание, а не полиморфное и ковариантное присваивание. В рефлексии рассмотрю оба варианта.

**Контравариантность**

Присваивание происходит от переменной одного типа, к переменной другого типа. Правило подстановки Барбары Лисков вводит определение тип-подтип. Согласно этому определению тогда, и тип стоит считать своим подтипом.

Кроме переменных и типов есть понятие экземпляра класса. Можно определение выше попробовать сформулировать как возможность переменной определенного типа  присваивать значение её подтипа, при этом под значением понимать экземпляр класса. Что не очень корректно, так как экземпляр класса это скорее объект физического мира, а переменная это некоторое описание.
Для таких конструкций `t:Cat = Cat()` проще говорить, что идет присваивание от неименованной переменной, к именованной. А неименованная переменная приобретает значение через инициализацию.

Класс - одновременно модуль и тип в случае если нет параметризации другим типом. Или модуль и шаблон типа в случае если есть параметризация другим типом.

В случая параметризации другим типом появляются понятия ковариантность и контрвариантность:

|                   | Тип параметр <br> | Тип параметр <br> | Производный тип | Производный тип |
| ----------------- | ----------------- | ----------------- | --------------- | --------------- |
|                   | T1                | T2                | `A<T1>`         | `A<T2>`         |
| Ковариантность    | Тип               | Подтип            | Тип             | Подтип          |
| Контрвариантность | Тип               | Подтип            | Подтип          | Тип             |
|                   |                   |                   |                 |                 |

В случае функциональных объектов они всегда котравариантны относительно типов параметров.
```
Например,
пусть есть типы, образованные одноименными классами Animal <- Dog
есть функции fn_dog(d: Dog) и fn_animal(a: Animal).
И есть переменная которая ожидает в качестве значения функцию fn_dog(d: Dog) и мы можем ей присвоить функцию fn_animal(a: Animal) и использовать. На основании этого можем говорить, что  fn_animal(a: Animal) - это подтип функционального объекта fn_dog(d: Dog).
```


**Ковариантность и полиморфизм.**

**Пример полиморфного вызова** метода есть в задании [OOAP2\task1.ts](OOAP2\task1.ts) 
Есть класс Shape от которого наследуются Circle и Trianle и есть метод вычисления площади фигур, который вызывает area() полиморфно.

```ts
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
        
function area(shapes: Shape[]): number {
    let result = 0;
    for(const shape of shapes) {
        result += shape.area(); //Полиморфизм. Вызывается запрос area() для конкретного подкласса.
    }
    return result;
}
```

**Пример ковариантного вызова** метода сделаю по мотивам задания  [OOAP2\task14.py](OOAP2\task14.py) 

[OOAP2\task16_1_reflection.py](OOAP2\task16_1_reflection.py) 
```python


from copy import copy, deepcopy
import json
from typing import Generic, Self, Sequence, TypeVar, Union
from inspect import isfunction
from typing import final


class String:
    def __init__(self, value:str):
        self._value = value

    def __str__(self):
        return self._value

string = TypeVar("string", bound=String, covariant=True)

class Vector(Generic[string]):
    def __init__(self, values:Sequence[string]): 
        self._values = values

    def __len__(self):
        return len(self._values)

    def print(self):
        values = [str(value) for value in self._values]
        print(f"[{', '.join(values)}]")

class CapitalizedString(String):
    def __init__(self, value:str):
          self._value = value.capitalize()

    def __str__(self):
        return self._value.capitalize()    


# Проверка типов:
# uv run --with mypy  mypy "OOAP2\task16_1_reflection.py"
# Запуск:
# uv run OOAP2\task16_1_reflection.py
if __name__ == "__main__":
    a: Vector[String] = Vector[CapitalizedString]([CapitalizedString("один"), CapitalizedString("два")])

    a.print() #["Один", "Два"]
		
```

Решение корректно как во время исполнения, так и проходит проверку типов.

