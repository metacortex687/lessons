#1. Сложность addHead/removeHead и addTail/removeTail одинакова так как использую двусвязный списко
#2. Релаизовал

class Deque:
    def __init__(self):
        self._size = 0
        self._linked_list = LinkedList2()

    def addFront(self, item):
        self._size += 1
        self._linked_list.add_in_head(Node(item))

    def addTail(self, item):
        self._size += 1
        self._linked_list.add_in_tail(Node(item))

    def removeFront(self):
        if self._size > 0:
            self._size -= 1
        else:
            return None
            
        result = self._linked_list.head().value  
        self._linked_list.delete_head()   
                
        return result 

    def removeTail(self):
        if self._size > 0:
            self._size -= 1
        else:
            return None
            
        result = self._linked_list.tail().value  
        self._linked_list.delete_tail()              
            
        return result

    def size(self):
        return self._size 
   
    
class Node:
    def __init__(self, v, is_dummy = False):
        self.value = v
        self.prev : Node = None
        self.next : Node = None
        self.is_dummy : bool = is_dummy


class LinkedList2:  
    def __init__(self):
        self._dummy = Node(None, is_dummy=True)
        self._dummy.next, self._dummy.prev = self._dummy, self._dummy
  
    def head(self) -> Node:
        return None if self._dummy.next.is_dummy else self._dummy.next
 
    def tail(self) -> Node:
        return None if self._dummy.prev.is_dummy else self._dummy.prev
    
    def add_in_head(self,newNode : Node):
        self._dummy.next.prev = newNode
        newNode.next = self._dummy.next 
        newNode.prev = self._dummy
        self._dummy.next = newNode
        
    def add_in_tail(self, item : Node):
        self._dummy.prev.next, self._dummy.prev, item.prev, item.next = item, item, self._dummy.prev, self._dummy

    def delete_head(self):  
        self._dummy.next.next.prev = self._dummy
        self._dummy.next = self._dummy.next.next   
        
    def delete_tail(self): 
        self._dummy.prev.prev.next = self._dummy
        self._dummy.prev = self._dummy.prev.prev   
        
        
        