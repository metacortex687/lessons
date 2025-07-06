# Section: 5. Queue

# Problem 3
# A function that rotates the queue in a circular manner
# Method name: rotate_queue
# Time complexity: Depends on the complexity of the "dequeue" and "enqueue" methods.
# If both are O(1), then the rotation will not depend on the number of elements in the queue.
# Solution: Take the value from the tail of the queue using "dequeue", and place it at the head using "enqueue".

# Problem 4
# Implement a queue using two stacks
# Class name: TwoStackQueue
# Time complexity: The "enqueue" method is O(1), and the "dequeue" method is O(1) and O(n)
# Solution: Use two stacks — one to push new elements, and the other to retrieve elements from the tail.
# If the stack used for retrieving elements is empty, transfer elements from the input stack.
# After transferring, elements are in the correct order for retrieval.

# Problem 5
# Add a function that reverses the elements.
# Class name: TwoStackQueue
# Method name: self.reverse()
# Time complexity: O(1)
# Solution:
# Swap the input stack and the output stack.

# Problem 6
# Implement a queue using a static array.
# Class name: FixedArrayQueue
# Solution:
# Store the position of the tail and the size of the queue as class variables.
# Also considered another variant that stores both head and tail positions and computes the size,
# but that requires more "if" checks.

# Method name: self.enqueue(item)
# Time complexity: O(1)
# Solution:
# Raise an "OverflowError" if the queue is full.
# Compute the head position by adding the queue size to the tail position.
# If it goes beyond the array bounds, wrap around to the start of the array.

# Method name: self.dequeue()
# Time complexity: O(1)
# Solution:
# Retrieve the value at the tail pointer, then move it forward.
# If it goes beyond the array bounds, wrap around to the start.


# Method name: self.is_full()
# Time complexity: O(1)
# Solution: Compare _capacity with _size. These are class variables.
# _capacity is set during initialization, and _size changes by one after each "enqueue" or "dequeue".


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

