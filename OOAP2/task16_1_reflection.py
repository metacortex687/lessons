
from copy import copy, deepcopy
import json
from typing import Generic, Self, Sequence, TypeVar, Union
from inspect import isfunction
from typing import final


class String:
    def __init__(self, value:str):
        self._value = value

    def __add__(self, other: 'String') -> 'String':
        return String(f"{self._value}{other._value}")

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
# uv run --with mypy  mypy "OOAP2\task17_1.py"
# Запуск:
# uv run OOAP2\task17_1.py
if __name__ == "__main__":
    a: Vector[String] = Vector[CapitalizedString]([CapitalizedString("один"), CapitalizedString("два")])

    a.print() #["Один", "Два"]


     
     
         
         



    