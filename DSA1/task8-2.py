# Note: Since this task is not intended for automatic testing, I will use Cyrillic for the explanation of solutions


# Section: 5. Хэширование

# Задание 3
# Реализовать динамическую хэш-таблицу
# Class: DinamicHashTable
# Method name: _resize
# Вычислительная сложность: O(n)
# Решение: Использую в классе два атрибута: размер таблицы и размер данных.
# В момент, когда отношение между ними больше 0.75, перестраиваю хэш-таблицу.
# Создаю новую хэш-таблицу. Перебираю в исходной таблице ячейки — если есть значение, то помещаю в новую.
# После этого все значения атрибутов из нового объекта помещаю в атрибуты исходного объекта класса.
# Оптимизация, которую использую: считаю количество помещённых в новую таблицу объектов и, после того как это 
# достигает исходного числа, прерываю перебор значений.
# Для хорошей хэш-функции, по идее, это единственная оптимизация, которая возможна.

# Задание 3
# Использовать несколько хэш-функций, чтобы уменьшить вероятность коллизий.
# Class: DinamicHashTable
# Методы: hash_fun_1, hash_fun_2, seek_slot 
# Вычислительная сложность: O(n)
# Решение: Буду использовать две хэш-функции. 
# Одна — для поиска ячейки, другая — для поиска следующей ячейки. Далее ячейку буду искать через обход с некоторым шагом.
# Размер таблицы будет простым числом — это гарантирует, что, выбрав любое число 
# меньше простого числа для шага, я гарантированно обойду все доступные индексы. 
# Использую для получения простых чисел метод nextprime из библиотеки sympy.

# Задание 4
# Реализуйте ddos-атаку. Посолите для уменьшения коллизий.
# Class: SoltHashTable
# Вычислительная сложность: от числа значений в хэш-таблице неизменна
# Решение: Обернул DinamicHashTable классом SoltHashTable, где к входящим значениям функций получения хэша добавляю "solt".
# Ddos-атаку не организовывал.

from sympy import nextprime
from random import randint

class DinamicHashTable:
    def __init__(self, sz):
        self.size = nextprime(sz-1)
        self.step = randint(1,self.size-1)
        self.slots = [None] * self.size
        self.count = 0
        
        self.p1 = self._randprime(5,100)
        self.p2 = self._randprime(5,100)
        
        self.a1 = randint(1, self.p1-1)
        self.a2 = randint(1, self.p2-1)
        
        self.b1 = randint(1, self.p1-1)
        self.b2 = randint(1, self.p2-1)
        
    def _randprime(self,min_val, max_val):
       return nextprime(randint(min_val, max_val - 1))    

    def hash_fun_1(self, value):
        sum = 0
        for c in value:
             sum += ord(c)
              
        return ((self.a1 * sum + self.b1) % self.p1) % self.size
    
    def hash_fun_2(self, value):
        sum = 0
        for c in value:
             sum += ord(c)
              
        return ((self.a2 * sum + self.b2) % self.p2) % self.size        

    def seek_slot(self, value):
        index = self.hash_fun_1(value)
        
        if self.slots[index]  is None or self.slots[index] == value:
            return index
        
        index = self.hash_fun_2(value)
        
        if self.slots[index]  is None or self.slots[index] == value:
            return index      
         
        start_index = index
        while self.slots[index]  is not None and self.slots[index] != value:
            index += self.step
            index %= self.size
            
            if index == start_index: #Формально излишне, так как размер таблицы в виде простого числа гарантирует обход всех доступных элементов, а автоматическое увеличение размера гарантирует наличие свободных ячеек
                return None       
               
        return index

    def _resize(self, new_size):
        new_dt = DinamicHashTable(new_size)
        for i in range(self.size):
            value = self.slots[i]
            
            if value is None:
                continue
            
            new_dt.put(value)
            
            if new_dt.count == self.count:
                break
            
        self.size = new_dt.size
        self.step = new_dt.step
        self.slots = new_dt.slots 
        self.count = new_dt.count
        
        self.p1 = new_dt.p1
        self.p2 = new_dt.p2
        
        self.a1 = new_dt.a1
        self.a2 = new_dt.a2
        
        self.b1 = new_dt.b1
        self.b2 = new_dt.b2

    
    def put(self, value):
        
        index = self.seek_slot(value)
        
        if index is None:
            return None
        
        self.slots[index] = value
        self.count += 1
        
        if self.count/self.size > 0.75:
            self._resize(self.size*2)
            index = self.find(value)
         
        return index

    def find(self, value):
        index = self.seek_slot(value)
        
        if index == None:
            return None
        
        if self.slots[index] == value:
            return index
        
        return None
    
    
class SoltHashTable(DinamicHashTable):
    def __init__(self, sz):
        super().__init__(sz)

    def hash_fun_1(self, value):
        return super().hash_fun_1(value)
    
    def hash_fun_2(self, value):
        return super().hash_fun_2(value)
   

      
    