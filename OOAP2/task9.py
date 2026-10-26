from copy import copy, deepcopy
import json
from typing import Self

class General(object):

    def copy(self)  -> Self:
        return copy(self)

    def deep_copy(self)  -> Self:
        return deepcopy(self)

    def __eq__(self, other: Self):
        return self.__dict__ == other.__dict__


    def serialize(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=True)

    @classmethod
    def deserialize(cls: type[Self], data: str) -> Self:
        fields = json.loads(data)
        return cls(**fields)


    def print(self):
        print(self.__str__())

    def is_type(self, check_type: type) -> bool:
        return type(self) is check_type 

    def type(self) -> type:
        return type(self)



class Any(General):
    pass



class A(Any):
    def __init__(self, nested_dict: dict):
        self.__dict__ = nested_dict.copy()



    
