# Раздел: 9. Ассоциативный массив

# Задача 5 
# Реализовать словарь с использованием упорядоченного поиска.
# Класс: OrderedListDictionary 
# Вычислительная сложность: O(n), o(n/2) для операций вставки, получения значения 
# и проверки наличия ключа. Где n это количество значений в ассоциативном массиве.
# Решение:
# Использую для хранения ключей упорядоченный связный список, а для хранения значений обычный связный список.
# Упорядоченный список при вставке возвращает индекс, куда была вставка.
# А связный список поддерживает добавление элемента по индексу.
# В упорядоченном списке реализован поиск индекса элемента.
# А в связном списке — обновление значения по индексу.

# Задача 6
# Реализовать словарь, в котором ключ — это битовый словарь фиксированной строки.
# Класс: BitNativeDictionary 
# Вычислительная сложность: O(n), где n — длина битовой строки.
# Решение:
# Для хранения использую древовидную структуру. По значению бита определяю, следующий узел — правый или левый. 
# Если длина битовой строки превышает фиксированную длину, указанную при инициализации — вызываю исключение.
# Значение бита получаю через битовую операцию "& 1".
# Переход к следующему биту осуществляю через битовую операцию ">> 1".



class Node:
    def __init__(self, v):
        self.value = v
        self.left : Node = None
        self.right : Node = None

class BitNativeDictionary:
    def __init__(self, bit_length):
        self.bit_length = bit_length
        self._node : Node = Node(None)

    def is_key(self, key):
        
        self.control_bitstring_length(key)
        
        _node = self._node
        for _ in range(self.bit_length):
            _bit = key & 1
            key = key >> 1
            
            if _bit == 0:
                _node = _node.left
                
            if _bit == 1:
                _node = _node.right
                
            if _node is None:
                return False

        return _node.value is not None 

    def control_bitstring_length(self, key):
        if key >> self.bit_length > 0:
            raise ValueError("Invalid bitstring length")
         

    def put(self, key, value):
        
        self.control_bitstring_length(key)
        
        _node = self._node
        for _ in range(self.bit_length):
            _bit = key & 1
            key = key >> 1
            
            if _bit == 0:
                if _node.left is None:
                    _node.left = Node(None)
                    
                _node = _node.left
                
            if _bit == 1:
                if _node.right is None:
                    _node.right = Node(None)
                    
                _node = _node.right
                
        _node.value = value
            
            

    def get(self, key):
        
        self.control_bitstring_length(key)
        
        _node = self._node
        for _ in range(self.bit_length):
            _bit = key & 1
            key = key >> 1
            
            if _bit == 0:
                _node = _node.left
                
            if _bit == 1:
                _node = _node.right
                
            if _node is None:
                return None

        return _node.value

class OrderedListDictionary:
    def __init__(self):
        self.slots = OrderedList(True)
        self.values = LinkedList(True)

    def is_key(self, key):
        return self.slots.find(key) is not None

    def put(self, key, value):
        
        i = self.slots.find(key)
        
        if i is not None:
            self.values.update(i,value)
            return
        
        i = self.slots.add(key)
        self.values.insert(i,value)

    def get(self, key):
        i = self.slots.find(key)
        
        if i is None:
            return None
        
        return self.values.get(i)

class OrderedList:
    def __init__(self, asc):
        self.head : Node = None
        self.tail : Node = None
        self.__ascending = asc
        self._len = 0

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif  v1 == v2:
            return 0
        else:
            return 1

    def _insert_after(self,after_node : Node, value):
        new_node = Node(value)
 
        if after_node is None:
            if self.head is None :
                self.head = new_node
                self.tail = self.head
                return
            self.head.left = new_node
            new_node.right = self.head
            self.head = new_node
            return
        
        if after_node.right is None:
            self.tail = new_node
        else:
            after_node.right.left = new_node  
              
        new_node.right  = after_node.right         
        after_node.right = new_node
        new_node.left = after_node



    def add(self, value):
        self._len  += 1
        
        _asc = 1 if self.__ascending else -1
        
        if self.head is None and self.tail is None :
            self._insert_after(None,value)
            return 0
        
        if self.compare(value,self.head.value)*_asc <= 0:
            self._insert_after(None,value)
            return 0
        
        if self.compare(value,self.tail.value)*_asc >= 0:
            self._insert_after(self.tail,value)
            return self._len-1
        
        index = 0
        node = self.head
        while self.compare(node.value,value)*_asc < 0:
            node = node.right
            index += 1
        
        self._insert_after(node.left,value)    


    def find(self, val):
        if self._len == 0:
            return None
       
        if self.compare(self.head.value ,val) == 0:
            return 0   
            
        if self.compare(self.tail.value ,val) == 0:
            return self._len-1     
         
        _asc = 1 if self.__ascending else -1
        
        if self.compare(val,self.head.value)*_asc < 0:
            return None
        
        if self.compare(val,self.tail.value)*_asc > 0:
            return None

        i = 0
        node = self.head
        while self.compare(node.value,val)*_asc < 0:
            node = node.right
            i += 1
            
        if self.compare(node.value,val) == 0:
            return i
         
        return None 
    
    def get_all_val(self): 
        r = []
        node = self.head
        while node != None:
            r.append(node.value) 
            node = node.right
        return r
    
    def __repr__(self):
        return str(self.get_all_val())

class LinkedList:
    def __init__(self, asc):
        self.head : Node = None
        self.tail : Node = None
        self.__ascending = asc
        self._len = 0


    def _insert_after(self,after_node : Node, value):
        new_node = Node(value)
 
        if after_node is None:
            if self.head is None :
                self.head = new_node
                self.tail = self.head
                return
            self.head.left = new_node
            new_node.right = self.head
            self.head = new_node
            return
        
        if after_node.right is None:
            self.tail = new_node
        else:
            after_node.right.left = new_node  
              
        new_node.right  = after_node.right         
        after_node.right = new_node
        new_node.left = after_node

    def insert(self,index : int , value):
        if index == 0:
            self._insert_after(None,value)
            return
        
        node = self.head
        for _ in range(index-1):
            node = node.right
        
        self._insert_after(node,value)
    
    def update(self,index : int , value):
        node = self.head
        for _ in range(index):
            node = node.right
            
        node.value = value
    
    def get(self,index : int) -> any:
        node = self.head
        for _ in range(index):
            node = node.right
            
        return node.value
    
    def get_all_val(self): 
        r = []
        node = self.head
        while node != None:
            r.append(node.value) 
            node = node.right
        return r
    
    def __repr__(self):
        return str(self.get_all_val())
               