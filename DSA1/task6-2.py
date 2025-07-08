# Section: 5. Dequeue

# Problem 7.3
# A function that checks открытые закрыте скобки
# Method name: bracket_control
# Time complexity: O(1)
# Solution: используюу deque как стэк, с одной стороны ложу и с этой же стороны забираю

# Problem 7.3
# A function that возвращает инимыльный элемент в deque
# Class: TwoStackDequeue
# Method name: self.min()
# Time complexity: O(n) o(1)
# Solution: двусторонню очередь из двух стеков. Еще два стека в которых храню минимальные элементы. На вершине хранятся минимальные элементы.
# Удаляя из стэка хранения данных, удаляю и из стэка минимальных элементов.
# В момент когда, в одном из стеков заканчивюатся элементы, при перкладывании из другого стека, пересобираю и стэк минимальных элементов. 
# А тот другой стэк минимальных элементов очищаю.

# Problem 7.5
# Двустороннюю очередь сделанная с помощью динамического массива.
# Class: DynArrayDequeue
# Time complexity: O(n) o(1) для "addFront", "addTail", "removeFront", "removeTail". n - число элементов в очереди.
# Solution: Храню положение хвоста и длинну элементов в очереди. Положение головы вычисляю.
# Реализовано увеличение capacity в два раза, и уменьшение в полтора, аналогично как для динамических массивов
# Возможны два варианта, когда хвост позади головы. И другой вариант когда голова прошла, и вышла с другой стороны массива. 
# То-есть хвост впереди головы. Эти случаи при изменении вместимости очереди обрабатываю по разному.

# Problem 7.6
# Функция которая проверяет баланс кобок.
# Class: bracket_control
# Time complexity: O(n) n- число символов
# Solution: использу dequeue как стэк, кладу с одной стороны элементы, и с этой же стороны и забираю.
# Добавил использование словаря. В целом задача, сводится к ранее решаемой в теме про стэк.


import ctypes

def is_polindrom(s : str, deque_constractor) -> bool:
    dq = deque_constractor()
    
    if len(s) == 0:
        return False
    
    for e in s:
        dq.addFront(e)
        
    while dq.size() > 1:
        f = dq.removeFront()
        t = dq.removeTail()
        
        if f != t:
            return False
      
    return True

def bracket_control(brackets : str, deque_constractor) -> bool:
    dq = deque_constractor()
    
    if len(brackets) == 0:
        return True 
    
    dict= {'}':'{',')':'(',']':'['}  
         
    s = Stack()
    
    for b in brackets:
        if not  b in dict.keys():
            dq.addFront(b)
        else:
            t = dq.removeFront()
            if t != dict[b]:
                return False
            
    return s.size() == 0
      
    return True
      


class TwoStackDequeue:
    def __init__(self):
        self._size = 0
        self._head = Stack()
        self._tail = Stack()
        self._min_head = Stack()
        self._min_tail = Stack()
 
    def addFront(self, item):
        if self._min_head.size() > 0:
            self._min_head.push(min(self._min_head.peek(),item))
        else:
            self._min_head.push(item)
        
        self._head.push(item)
        
    def addTail(self, item):
        if self._min_tail.size() > 0:
            self._min_tail.push(min(self._min_tail.peek(),item))
        else:
            self._min_tail.push(item)
        
        self._tail.push(item)    

    def min(self):
        min_head = self._min_head.peek()
        min_tail = self._min_tail.peek()
        
        if min_head is None:
            return min_tail
        
        if min_tail is None:
            return min_head
        
        return min(min_head,min_tail)
         

    def removeFront(self):
        if self._head.size() == 0:
            if self._tail.size() == 0:
                return None
            
            while self._tail.size() > 0:
                value = self._tail.pop()
                self._min_tail.pop()
                
                if self._min_head.size() == 0:
                    self._min_head.push(value)
                else:
                    self._min_head.push(min(value,self._min_head.peek()))   
                     
                self._head.push(value)
        
        self._min_head.pop() 
        return self._head.pop() 

    def removeTail(self):
        if self._tail.size() == 0:
            if self._head.size() == 0:
                return None
            
            while self._head.size() > 0:
                value = self._head.pop()
                self._min_head.pop()
                
                if self._min_tail.size() == 0:
                    self._min_tail.push(value)
                else:
                    self._min_tail.push(min(value,self._min_tail.peek()))   
                     
                self._tail.push(value)
        
        self._min_tail.pop() 
        return self._tail.pop() 

    def size(self):
        return self._head.size() + self._tail.size() 



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
 

class DynArrayDequeue:
    def __init__(self, min_capacity = 16):
        self._size = 0
        self._min_capacity = min_capacity
        self._capacity = min_capacity
        self._array = self._make_array(self._capacity)
        
        self._index_tail = 0
  
    def _make_array(self, new_capacity):
        #return [None]*new_capacity
        return (new_capacity * ctypes.py_object)()
      
    def addFront(self, item):
        if self._size >= self._capacity:
            self._resize_array(self._capacity*2)
        
        self._size += 1 
        self._array[self._index_head()] = item
    


    def _index_head(self):
        _index_head = self._index_tail + self._size - 1

        if _index_head >= self._capacity:
            _index_head -= self._capacity
            
        return _index_head


    def _resize_array(self, new_capacity):
        
        if self._size == 0:
            return
        
        new_capacity = max(new_capacity, self._min_capacity)
        if new_capacity == self.capacity():
            return
        
        new_array = self._make_array(new_capacity)
        new_index_tail = None
        
        if self._index_head() >= self._index_tail:
            for i in range(self._index_tail,self._index_head()+1):
                new_array[i-self._index_tail] = self._array[i]
            new_index_tail = 0
        else:
            for i in range(0, self._index_head()+1):
                new_array[i] = self._array[i]
                
            for i in range(self._index_tail,self._capacity):
                new_array[i+new_capacity-self._capacity] = self._array[i]  
                
            new_index_tail = self._index_tail + new_capacity-self._capacity          
                
        self._capacity = new_capacity
        self._array = new_array  
        self._index_tail = new_index_tail        
          

        
        

    def addTail(self, item):
        if self._size >= self._capacity:
            self._resize_array(self._capacity*2)
        
        self._size += 1

        self._index_tail -= 1
        
        if self._index_tail < 0:
            self._index_tail += self._capacity
            
        self._array[self._index_tail] = item
         

    def removeFront(self):
        if self.size() == 0:
            return None
            
        value = self._array[self._index_head()]  
        self._array[self._index_head()] = None
        self._size -= 1
        
        if self._size < self._capacity/2:
            self._resize_array(self._capacity*2//3)
            
        if self._size == 0:
            self._index_tail = 0
        
        return value


    def removeTail(self):
        if self.size() == 0:
            return None
        
        self._size -= 1
        
        value = self._array[self._index_tail]
        self._array[self._index_tail] = None
        
        self._index_tail += 1
        
        if self._index_tail >= self._capacity:
            self._index_tail -= self._capacity
  
        if self._size < self._capacity/2:
            self._resize_array(self._capacity*2//3)
         
        if self._size == 0:
            self._index_tail = 0 
            
        return value
        

    def size(self):
        return self._size
    
    def capacity(self):
        return self._capacity
         
        
  
  


         
  
    
    