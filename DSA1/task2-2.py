# DSA 1
# Section: 2. Doubly Linked List

# Problem 2.10
# Method that reverses the order of elements in the linked list
# Method name: self.reverse()
# Solution complexity: O(n), single loop pass
# Solution:
# I swap `prev` and `next` pointers for all nodes symmetrically.
# The resulting list should be fully reversed.

# Problem 2.11
# Method that detects whether the list contains a cycle
# Method name: bool self.is_loop()
# Solution complexity: O(n), two loop passes
# Solution:
# I use a `set()` to keep track of visited nodes.
# If I encounter the same node again while traversing in a given direction, the list is cyclic.
# I check for cycles in both directions: from head to tail and from tail to head.

# Problem 2.12
# Method that sorts the elements in the linked list
# Method name: self.sort()
# Solution complexity: O(n²), bubble sort via nested loops
# Solution:
# While traversing from head to tail, if I find an element smaller than its previous one,
# I start moving it towards the head until it meets a smaller or equal element.

# Problem 2.13
# Method that merges two arbitrary linked lists into a third sorted result list.
# Requires input lists to be sorted beforehand.
# The resulting list must not be sorted after merging.
# Method name: LinkedList2.merge_into_new_sorted(s_list1: 'LinkedList2', s_list2: 'LinkedList2')
# Solution complexity: O(n²) — sorting is O(n1²) + O(n2²) for the two inputs; merging is O(n) via a single pass
#
# Solution:
# I create copies of both input lists for sorting, so the originals remain unchanged.
# When adding nodes to the resulting list, I create new node instances.
# I traverse both lists simultaneously and always add the smaller current node to the result.
# Then I move forward in the list from which the node was taken.
# This continues until both lists are fully traversed.
# If one list reaches the end first, I add the remaining nodes from the other list.
# The merging process is completed in a single loop pass.


# Problem 2.14
# Use of a dummy node in a doubly linked list
# Method name: applies to all methods in LinkedList2
# Solution complexity: unchanged
#
# Solution:
# A flag `is_dummy` was added to the Node class to distinguish dummy nodes.
# Based on this flag and direction, I determine whether a node is the head or tail.
# A single dummy node is added to LinkedList2.
# Operations on the list became uniform regardless of whether they are at the head, tail, or middle.
# Reduced the number of conditionals like `if`.
# The @property decorators for head and tail are used to enable test code reuse.


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
 
 