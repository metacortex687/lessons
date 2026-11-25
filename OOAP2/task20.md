Примеры кода.

Наследования вариаций.

```python
class Human:
    def max_weight(self):
        return 100
		
class Male(Human):
    def max_weight(self):
        return super().max_weight()*1.2:
	
class Female(Human):
    def max_weight(self):
        return super().max_weight()*0.95:
```


Наследование с конкретизацией.

```python
class Transport:
    def move(self):
    raise NotImplementedError()
		
class Ship(Transport):
    def move(self):
    print("Корабль движется")
		

class Car(Transport):
    def move(self):
    print("Атомобиль движется")
	
```


Структурное наследование.



```python
from abc import ABC, abstractmethod

class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass
		
		
class Ship(Movable):
    def move(self):
        print("Корабль движется")
		

class Car(Movable):
    def move(self):
        print("Атомобиль движется")
	
```

