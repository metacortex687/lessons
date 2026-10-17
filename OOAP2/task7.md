**Приведите пример кода с комментариями, где применяется динамическое связывание.**

```python
class Animal():
	def sound(self):
		raise NotImplementedError #сделал вызвающим исключение, что бы подчеркнуть частичную реализацию базового класса
		
class Dog(Animal):
	def sound(self): #переопредяемый метод
		print("гав!!!")
		
class Cat(Animal):
	def sound(self): #переопредяемый метод
		print("мяу!!!")		
	
class Zoo():
	def __init__(self, animals: list[Animal]):
		self._animals = animals
		
	def sound(self): 
		for animal in self._animals:
			animal.sound() #при вызове использует динамическое связывание
			

zoo = Zoo([Dog(), Cat(), Cat()])
zoo.sound()

#вывод
# гав!!!
# мяу!!!
# мяу!!!

# через динамическое связывание был вызван метод сответствующего потомка. Класс Zoo ничего не знает о потомках, работает исключительно с базовым классом родителем. 		
	

```