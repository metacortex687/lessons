from copy import copy, deepcopy
import json
from typing import Self
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
    def __eq__(self, other: Self):
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


#надо отслеживать листья
@final
class CNone(A, B):
    def __init__(self):
        self.__dict__ = {}

        def return_none(self, *args, **kwargs):
            return None

        cls = type(self)

        for base in cls.__mro__[1:]:
            for name, value in vars(base).items():
                if isfunction(value) and not name.startswith("__"):
                    setattr(cls, name, return_none)
        
    def value1(self):
        return None


# запуск тестов: uv run OOAP2\task11.py
if __name__ == '__main__':

    a = A({})
    b = B()
    none = CNone()

    assert issubclass(type(none), A)
    assert issubclass(type(none), B)
    assert issubclass(type(none), General)
    assert issubclass(type(none), Any)

    assert a.value1() == "value1 of A"

    assert b.value1() == "value1 of B"
    assert b.value2() == "value2 of B"

    assert none.value1() is None
    assert none.value2() is None




