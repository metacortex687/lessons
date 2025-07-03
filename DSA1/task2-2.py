# DSA 1
# Section: 2. Двунаправленный связный (связанный) список

# Problem 2.10 
# Метод который перворачивает пордок элементов в связном списке
# Имя метода: self.reverse()
# Solution complexity: O(n). Проход цикла.
# Solution:
# Зеркально меняю prev и next у всех узлов. Результирующий спсисок так и должен выглядеть

# Problem 2.11 
# Метод который определяет есть ли замкнутые списки
# Имя метода: bool self.is_loop()
# Solution complexity: O(n). Два прохода цикла.
# Solution:
# Использую объект set() для запоминания пройденных узлов.
# Если при движении в выбранном направлении повторно встречаю узел, значит список замкнут.
# Проверяю на циклы как при движении от головы к хвосту, так и от хвоста к голове.

# Problem 2.12 
# Метод который сортирует элементы в связном списке
# Имя метода: self.sort()
# Solution complexity: O(n^2). Использую пузырьковую сортировку. Циклы вложены друг в друга.
# Solution:
# Если при движении от головы к хвосту обнаруюиваю элемент меньше предыдущего, то начинаю его двигать к голове, пока он не уткнется в меньший или равный

# Problem 2.13 
# Метод который объединит два произвольных связных списка в итоговый третий отсортированный. Использовать предварительно отсортированные списки. Итоговый список не сортировать после слияния.
# Имя метода: LinkedList2.merge_into_new_sorted(s_list1 : 'LinkedList2', s_list2 : 'LinkedList2')
# Solution complexity: O(n^2). Сортировка  O(n1^2) + O(n2^2) для списков 1 и 2. Слияние O(n),так как сделано за один проход цикла
#
# Solution:
# Делаю копии списков для последующей сортировки, что бы не менять входящие объекты. 
# При добавлении значений в итоговый список создаю новые экземпляры узлов.
# Двигаюсь одновременно под двум спискам, добавляя вначале меньший в хвост итогового списка.
# После для списка откуда было добавлено значение двигаюсь на следующий элемент.
# Двигаюсь пока оба списка не дойдут до хвоста.
# Если один из списков дошел до хвоста раньше, добавляю значения из оставшегося.
# Слияние сделано за один проход цикла.


# Problem 2.14
# Использовать в двунаправленном связном списоке dummy узел
# Имя метода: все методы в LinkedList2
# Solution complexity: не поменялась
#
# Solution:
# В Node добавлен признак is_dummy, по этому признаку определяю в зависимости от нпаравления голову или хвост
# Добавил один dummy узел в LinkedList2
# Операциия дла узла в середине или скарю списка стали одинаковыми
# Стало меньше условий "if"  


class Node:
    def __init__(self, v, is_dummy = False):
        self.value = v
        self.prev : Node = None
        self.next : Node = None
        self.is_dummy : bool = is_dummy
        
    def __repr__(self):
        if self.is_dummy:
            return "dummy"
        else:
            return str(self.value)

class LinkedList2:  
    def __init__(self):
        self._dummy = Node(None, is_dummy=True)
        self._dummy.next, self._dummy.prev = self._dummy, self._dummy
        
        
    @property
    def head(self):
        return None if self._dummy.next.is_dummy else self._dummy.next
   
    @property
    def tail(self):
        return None if self._dummy.prev.is_dummy else self._dummy.prev
       

  
    def sort(self):
        
        node = self._dummy.next
        
        while not node.is_dummy:
            next_node = node.next
            while not node.prev.is_dummy:
                if node.prev.value > node.value:
                    node.prev.prev.next = node
                    node.next.prev = node.prev
                    node.prev.next = node.next
                    node.prev.prev, node.next, node.prev = node, node.prev, node.prev.prev
                else:
                    break
            node = next_node

    
    def reverse(self):
          
        node = self._dummy.next
        
        self._dummy.next, self._dummy.prev = self._dummy.prev, self._dummy.next
        
        while not node.is_dummy:
            next_node = node.next
            
            node.next, node.prev = node.prev, node.next
            
            node = next_node
       
    def is_loop(self):
        
        s = set()
        node = self._dummy.next
        while not node.is_dummy:     
            s.add(node) 
            node = node.next
            
            if node in s:
                return True
            
        s = set()
        node = self._dummy.prev
        while not node.is_dummy:     
            s.add(node) 
            node = node.prev
            
            if node in s:
                return True
        
        return False        
     
    def __repr__(self):
        
        right = []
        s = set()
        right.append(str(self._dummy))
        node = self._dummy.next
        while not node.is_dummy:     
            if node in s:
                 right.append("loop")
            else:
                right.append(str(node)) 
            node = node.next   
        right.append(str(self._dummy))
        
        left = []
        s = set()
        left.insert(0,str(self._dummy))
        node = self._dummy.prev
        while not node.is_dummy:     
            if node in s:
                 left.insert(0,"loop")
            else:
                left.insert(0,str(node)) 
            node = node.prev  
             
        left.insert(0,str(self._dummy))
        
        return f"{str(right)} = {str(left)}"
  
        
    def copy(self):
        result = LinkedList2()
         
        node = self._dummy.next
        while not node.is_dummy:
            result.add_in_tail(Node(node.value))
            node = node.next
            
        return result
        
          
    @staticmethod              
    def merge_into_new_sorted(s_list1 : 'LinkedList2', s_list2 : 'LinkedList2'):
        result = LinkedList2()
        
        _s_list1 = s_list1.copy()
        _s_list2 = s_list2.copy()
        _s_list1.sort()
        _s_list2.sort()
        
        node1 = _s_list1._dummy.next
        node2 = _s_list2._dummy.next
        
        while (not node1.is_dummy) or (not node2.is_dummy):
            
            if node1.is_dummy and not node2.is_dummy:
                result.add_in_tail(Node(node2.value))  
                node2 = node2.next
            elif node2.is_dummy and not node1.is_dummy:
                result.add_in_tail(Node(node1.value))
                node1 = node1.next
            elif node1.value < node2.value:
                result.add_in_tail(Node(node1.value)) 
                node1 = node1.next
            else:
                result.add_in_tail(Node(node2.value))
                node2 = node2.next
                
        
        return result
        
        
  
    def add_in_tail(self, item : Node):
        self._dummy.prev.next, self._dummy.prev, item.prev, item.next = item, item, self._dummy.prev, self._dummy


    def find(self, val):
        node = self._dummy.next
        while not node.is_dummy:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        
        node = self._dummy.next
        while not node.is_dummy:
            if node.value == val:
                result.append(node)
            node = node.next
            
        return result

    def delete(self, val, all=False):
        node = self._dummy.next
        while not node.is_dummy:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                
                if not all:
                    return

            node = node.next
            
    def to_list_values(self, dir_forward = True):
        result = []  
            
        if dir_forward:
            
            node = self._dummy.next
            while not node.is_dummy:
                result.append(node.value)
                node = node.next
                
        else:
            
            node = self._dummy.prev
            while not node.is_dummy:
                result.append(node.value)
                node = node.prev    

        return result       

    def clean(self):
        self._dummy.next, self._dummy.prev = self._dummy, self._dummy

    def len(self):
        result = 0
        node = self._dummy.next
        while not node.is_dummy:
            result += 1
            node = node.next

        return result

    def insert(self, afterNode : Node, newNode : Node):
        if afterNode is None:
            afterNode = self._dummy
        
        afterNode.next.prev = newNode
        newNode.next = afterNode.next
        
        afterNode.next = newNode
        newNode.prev = afterNode
  

    def add_in_head(self, newNode):
        self.insert(None,newNode)
 
 