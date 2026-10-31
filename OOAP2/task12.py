# добавлен метод 
# T = TypeVar("T")
# def assignment_attempt(target_type: type[T], source) -> T | CNone:
# ...

# И тессты через assert в __main__ блоке.

from copy import copy, deepcopy
import json
from typing import Self
from inspect import isfunction
from typing import final, TypeVar

class General(object):

    @final
    def copy(self)  -> Self:
        return copy(self)
    
    @final
    def deep_copy(self)  -> Self:
        return deepcopy(self)

    @final
    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__

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
        return str()
        
    @final
    def is_type(self, check_type: type) -> bool:
        return type(self) is check_type 

    @final
    def type(self) -> type:
        return type(self)



class Any(General):
    pass



class A(Any):
    def __init__(self, nested_dict: dict):
        self.__dict__ = nested_dict.copy()

    def value1(self):
        return "value1 of A"

class B(Any):
    def value1(self):
        return "value1 of B"

    def value2(self):
        return "value2 of B"

class C(B):
    pass



#надо отслеживать листья
@final
class CNone(A, C):
    def __init__(self):
        self.__dict__ = {}

        def return_none(self, *args, **kwargs):
            return None

        cls = type(self)

        for base in cls.__mro__[1:]:
            for name, value in vars(base).items():
                if isfunction(value) and not name.startswith("__"):
                    setattr(cls, name, return_none)
        
T = TypeVar("T")
def assignment_attempt(target_type: type[T], source) -> T | CNone:
    if not issubclass(type(source), target_type):
        return CNone()

    return source

       
                      


# запуск тестов: uv run OOAP2\task11.py
if __name__ == '__main__':
    # наследование
    # General <- Any
    # Any <- A
    # Any <- B <- C

    a = A({})
    b = B()
    c = C()


    t1:A = assignment_attempt(A, a)
    assert t1 is a

    t2:B = assignment_attempt(B, a)
    assert type(t2) is CNone   

    t3:B = assignment_attempt(B, c)
    assert isinstance(t3, B)   

    #t4:C = assignment_attempt(B, c) #будет ошибка при проверке типов uv run --with mypy  mypy "OOAP2\task12.py"
