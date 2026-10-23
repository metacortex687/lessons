from copy import copy, deepcopy
import json
from typing import Self

class General(object):
    def copy(self)  -> Self:
        return copy(self)

    def deep_copy(self)  -> Self:
        return deepcopy(self)

    def eq(self, other):
        return self == other


    def serialize(self) -> str:
        return json.dump(self)

    @classmethod
    def deserialize(cls: type[Self], data: str) -> Self:
        fields = json.load(data)
        return cls(**fields)


    def print(self):
        print(self.__str__())

    def is_type(self, check_type: type) -> bool:
        return type(self) is check_type 

    def type(self) -> type:
        return type(self)



class Any(General):
    pass



    
