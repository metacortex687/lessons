#1. Реализовал используя двунаправленного связный список
#2. Аллгоритмическа сложность "enqueue" O(1) равна сложности добавления в голову двунаправленного связного списока
#2. Аллгоритмическа сложность "dequeue" O(1) равна сложности получения и удаления хвоста двунаправленного связного списока 
# Если бы использовал однонаправленный связный список, то сложность была бы O(n), как у удаления хвоста.

class Queue:
    def __init__(self):
        self._size = 0
        self._queue = LinkedList2()

    def enqueue(self, item):
        self._size += 1
        self._queue.add_in_head(Node(item))

    def dequeue(self):
        if self._size > 0:
            self._size -=1
        else:
            return None
            
        result = self._queue.tail().value
        
        self._queue.delete_tail()
         
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


        
    def delete_tail(self): 
        self._dummy.prev.prev.next = self._dummy
        self._dummy.prev = self._dummy.prev.prev
         
        
        

          
        
