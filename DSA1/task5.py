# 1. Implemented using a doubly linked list
# 2. The algorithmic complexity of "enqueue" is O(1), which is the same as adding to the head of a doubly linked list
# 3. The algorithmic complexity of "dequeue" is O(1), which matches the complexity of retrieving and removing the tail of a doubly linked list
# If a singly linked list had been used instead, the complexity of "dequeue" would have been O(n),
# because removing the tail requires traversal from the head to the penultimate node.



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
         
        
        

          
        
