# 1. I use a linked list
# 2. Implemented based on a simplified linked list that supports adding to the head,
# removing an element from the head, and retrieving an element from the head
# 3. If the top value in the stack is even, it returns all values. If it’s odd, it returns all values plus None
# 4. The solution complexity of the push operation is equal to the complexity of adding to the head of the linked list — O(1)
# 4. The solution complexity of the pop operation is equal to the complexity of reading the value from the head of the linked list
# and removing this element from the head — that is, O(1)


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
            
    

    

