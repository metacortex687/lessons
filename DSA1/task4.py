# 1. Использую связный список
# 2. Реализовал на основе упрощенного связного списка, в котором есть есть добавление в head, удаление элемента из head, и 
# получение элеента из head
# 3. Если четное значение  в стеке, то выведет все значения. Если не четное, то выведет все значения, и еще None
# 4. Solution complexity операции push, равна  solution complexity добавленя в head, O(1)
# 4. Solution complexity операции pop, равна  solution complexity чтения значения из головы связного спсика 
# и у даления этого элемента из головы списка, то-есть O(1)

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
            
    

    

