Вариант исходного кода взят из существующего проекта, в котором он несколько более сложен. В исходном используются предопределённые значения.

```python
from typing import Literal

class EDBase:
    pass

class EDObjectRef(EDBase):
    kind: Literal["Документ", "Справочник"]
    name_type: str

class ORMSaver():
    ...

    def _name_table(self, obj:EDObjectRef)
        prefix = ""
        if obj.name_type == "Документ":
            prefix = "d_"

        if obj.name_type == "Справочник":
            prefix = "c_"

        return prefix + obj.name_type
```


Этот же пример, когда вместо предопределённых значений применяется наследование.

```python
from typing import Literal

class EDBase:
    pass

class KindType:
    def prefix_table_db(self):
        return NotImplementedError

class KindTypeDocument(KindType):
    def prefix_table_db(self):
        return "d_"

class KindTypeCatalog(KindType):
    def prefix_table_db(self):
        return "c_"    

class EDObjectRef(EDBase):
    kind: KindType
    name_type: str

class ORMSaver():
    ...

    def _name_table(self, obj:EDObjectRef)
        return obj.kind.prefix_table_db() + obj.name_type
```

