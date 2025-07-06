# DSA 1
# Section: 5. Queue

# Problem 3
# A function that вращает очередь по кругу
# Method name: rotate_queue
# Time complexity: определяется сложностью методов "dequeue" и "enqueue". 
# Если у них обоих O(1), то и вращение не будет зависеть от числа элементов в очереди
# Solution: беру значение из хвоста очереди методои "dequeue", и кладу в голову методом "enqueue"

# Problem 4
# Реализуйте очередь с помощью двух стэков
# Class name: TwoStackQueue
# Time complexity: метода "enqueue" O(1), а для метода "dequeue" o(1) и O(n)
# Solution: Использую два стека, один для того что бы ложить новые элементы, другой что бы получать элементы из хвоста.
# Если в стэке который для получения элементов, нет ничего, то перекладываю из стэка для входящих элеменов.
# После перкладывания элементы лежат в нужном порядке для получения.

# Problem 5
# Add a function что обращает эдементы в обратном порядке.
# Class name: TwoStackQueue
# Method name: self.reverse()
# Time complexity: O(1)
# Solution:
# Меняю местами стэк который был для входящих элементов и стэк что для получения элементов.


# Problem 6
# Сделать стэк на ститческом массиве.
# Class name: FixedArrayQueue
# Solution:
# Храню в переменных класса положения хвоста и размер очереди.
# Рассматривал и другой вариант, в котором храню положение гловы и хвоста а размер вычисляю, но там больше "if".


# Method name: self.enqueue(item)
# Time complexity: O(1)
# Solution:
# Вызываю исключение "OverflowError" если уже заполнена очередь
# Вычисляю положение головы, добавляя размер очереди к положению хвоста. 
# Если выходит за границы массива, то считаю что голова преходит на начало массива.


# Method name: self.dequeue()
# Time complexity: O(1)
# Solution:
# Получаю значения по указателю хвоста, после чего вигаю вперед.
# Если выходит за границы массива, то считаю что преходит на начало массива.


# Method name: self.is_full()
# Time complexity: O(1)
# Solution: Сравниваю _capacity с _size. Это все переменные класса. Сapacity задается при инициализации. А _size
# меняется на единицу в зависимости от "enqueue" или "dequeue"





import ctypes


class FixedArrayQueue:
    def __init__(self, capacity):
        self._queue =   (capacity * ctypes.py_object)()
        self._capacity = capacity
        self._size = 0
        self._tail = 0
        
    def enqueue(self, item):
        
        if self.is_full():
            raise OverflowError
        
        position = self._tail + self._size
        if position >= self._capacity:
            position -= self._capacity   
        self._queue[position] = item
        
        self._size += 1
        
 
    def is_full(self):
        return self._size == self._capacity
        


    def dequeue(self):
        if self._size == 0:
            return None
        
        result = self._queue[self._tail]
        
        self._tail += 1 
        if self._tail == self._capacity:
            self._tail -= self._capacity 
            
        self._size -= 1          
        
        return result

    def size(self):
        return self._size
        
    


class TwoStackQueue:
    def __init__(self):
        self._size = 0
        self._head = Stack()
        self._tail = Stack()
 
    def enqueue(self, item):
        self._head.push(item)

    def dequeue(self):
        if self._tail.size() == 0:
            while self._head.size() > 0:
                self._tail.push(self._head.pop())
         
        return self._tail.pop() 

    def size(self):
        return self._head.size() + self._tail.size() 

    def reverse(self):
        self._head, self._tail = self._tail , self._head

class Stack:
    def __init__(self):
        self.stack = SimplyLinkedList()
        self._size = 0

    def size(self):
        return self._size

    def pop(self):
        if self.stack.head is None:
            return None
        
        result = self.stack.head.value
        
        self.stack.delete_head()
        self._size -=1
        
        return result

    def push(self, value):
        self.stack.add_in_head(Node(value)) 
        self._size += 1


    def peek(self):
        if self.stack.head is None:
            return None
        else:
            return self.stack.head.value

    
    
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class SimplyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def add_in_head(self, newNode : Node):
        newNode.next = self.head 
        self.head = newNode
        
    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
   
            
def rotate_queue(queue, n):
    for _ in range(n):
        queue.enqueue(queue.dequeue())    
