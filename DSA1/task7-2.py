# Section: 5. Ordered List

# Problem 8
# Removing all duplicates
# Class: OrderedList
# Method name: self.remove_duplicates()
# Time complexity: O(n)
# Solution: Iterate through the list sequentially. If the current element is equal in value to the next one,
# remove the duplicate by skipping the current node and linking the previous node directly to the next one.


# Problem 9
# Merging two lists into one.
# Class: OrderedList
# Method name: self.merge()
# Time complexity: O(n), where n is the number of elements in the resulting list
# Solution: To ensure merging works in O(n), the elements should be inserted in increasing or decreasing order
# so they get appended at the beginning or end. That’s what I implemented, based on whether the two lists have
# matching or opposite ordering.


# Problem 10
# Checking if one list is a subsequence of another.
# Class: OrderedList
# Method name: self.contains_subsequence()
# Time complexity: O(n1 * (n2 - n1)), where n2 is the length of the list being searched
# Solution: First compare the lengths to see if the subsequence can fit. Then iterate through the list,
# comparing the start of the main list with the subsequence step by step.

# Problem 11
# A method that finds the most frequently occurring value.
# Class: OrderedList
# Method name: self.most_frequent_value()
# Time complexity: O(n)
# Solution: Use a dictionary to count the occurrences of each value.

# Problem 12
# Searching in O(log N)
# Class: OrderedList
# Method name: self.find()
# Time complexity: 
# Solution: Implemented only for a list of length 3.
# The idea is to use a sparse list as a class attribute, where each Node has 'down' and 'up' links
# for vertical navigation and updating.
# Also use a 'span' attribute to track distances between nodes in the sparse levels.
# Once the search reaches a node, it descends to the next level down, and so on.
# Sparse levels need to be updated when elements are inserted or deleted.
# Which I didn’t have time to implement, and I’m also unsure whether this approach is the right one.



class Node:
    def __init__(self, v):
        self.value = v
        self.prev : Node = None
        self.next : Node = None
 
        self.down : Node = None
        self.up : Node = None
        
        self.span = 1


class OrderedList:
    def __init__(self, asc, default_span = 1):
        self.head : Node = None
        self.tail : Node = None
        self.__ascending = asc
        self._len = 0
        self._skip_list : OrderedList = None 
        self._default_span = default_span

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif  v1 == v2:
            return 0
        else:
            return 1

    def nearest_first_node(self, value) -> tuple[int, Node]:
 
        if self._skip_list is None:
            _node = self.head
            index = 0
        else:
            index, _node = self._skip_list.nearest_first_node(value)    

        if _node.value == value:
            return _node.down
             
        while _node.next is not None and self.compare(value, _node.next.value) < 0:
            _node = _node.next
            index += _node.span
        
        return index, _node.down
             
        
    def index(self,node : Node) -> int:
        if self.head == node:
            return 0
        elif self.head.next == node:
            return 1
        else:
            index, start_node = self._skip_list.nearest_first_node(node.value)
            
            _node = start_node
            _index = index
            while _node is not None and _node != node and _node.value == node.value:
                _index -= 1
                _node = _node.prev
             
            if _node == node:
                 return _index   
            
            
            _node = start_node
            while _node != node:
                index += 1
                _node = _node.next  
            
            return index    
            


    def _insert_after(self,after_node : Node, value, down_node = None):
        self._len  += 1
        
        new_node = Node(value)
        new_node.down = down_node
 
        if after_node is None:
            if self.head is None :
                self.head = new_node
                self.tail = self.head
                return new_node
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return new_node
        
        if after_node.next is None:
            self.tail = new_node
        else:
            after_node.next.prev = new_node  
              
        new_node.next  = after_node.next         
        after_node.next = new_node
        new_node.prev = after_node
          
        if self.len() == 3:
            self._skip_list = OrderedList(self.__ascending)
            n = Node(self.head.value)
            n = self._skip_list._insert_after(None,self.head.value)
            n.down = self.head
            n.span = 0
 
            n = self._skip_list._insert_after(self._skip_list.head,self.tail.value)
            n.down = self.tail
            n.span = 2

        return new_node
            


    def add(self, value):
        _asc = 1 if self.__ascending else -1
        
        if self.head is None and self.tail is None :
            return self._insert_after(None,value)
            
        
        if self.compare(value,self.head.value)*_asc <= 0:
            self._insert_after(None,value)
        elif self.compare(value,self.tail.value)*_asc >= 0:
            self._insert_after(self.tail,value)
        else:
            node = self.head
            while self.compare(node.value,value)*_asc < 0:
                node = node.next
            
            self._insert_after(node.prev,value)    

    def most_frequent_value(self):
        if self._len == 0:
            return None
        
        _most_frequent_value = self.head.value
        node = self.head
        max_count = 1
        
        dict_frequen = {self.head: 1}
        
        while node is not None:
            if node.value in dict_frequen.keys():
                count = dict_frequen[node.value] + 1
                dict_frequen[node.value] = count
                
                if count > max_count:
                    max_count = count
                    _most_frequent_value = node.value
            else:
                dict_frequen[node.value] = 1
                    
                    
                     
                
            
            
            node = node.next
            
        
        return _most_frequent_value

    def find(self, val):
        if self._len == 0:
            return None
       
        if self.compare(self.head.value ,val) == 0:
            return self.head   
            
        if self.compare(self.tail.value ,val) == 0:
            return self.tail       
         
        _asc = 1 if self.__ascending else -1
        
        if self.compare(val,self.head.value)*_asc < 0:
            return None
        elif self.compare(val,self.tail.value)*_asc > 0:
            return None
        else:
            node = self.head
            while self.compare(node.value,val)*_asc < 0:
                node = node.next
                
            if self.compare(node.value,val) == 0:
                return node
         
        return None # здесь будет ваш код

    def _delete_node(self, node : Node):
        self._len -= 1
        
        if node == self.head:
            self.head.prev = None
            self.head = self.head.next
        else:
            node.prev.next = node.next
        
        if node == self.tail:
            self.tail.next = None
            self.tail = self.tail.prev
        else:
            node.next.prev = node.prev
            
       
         
    
    def delete(self, val):
        if self.head is None and self.tail is None:
            return
         
        if self.compare(self.head.value,val) == 0:
            self._delete_node(self.head)
            return
         
        _asc = 1 if self.__ascending else -1
        if self.compare(val,self.head.value)*_asc < 0:
            return
        elif self.compare(val,self.tail.value)*_asc > 0:
            return
        
        node = self.head.next
        while node is not None:
            if self.compare(node.value,val) == 0:
                self._delete_node(node)
                return
            
            node = node.next
        

    def remove_duplicates(self):
        if self._len <= 1:
            return
        
        node = self.head
        
        while node.next is not None:
            if node.value == node.next.value:
                self._len -= 1
                
                if node.prev is None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next
    
    def contains_subsequence(self, subsequence: 'OrderedList') -> bool:
        if subsequence.len() == 0:
            return True
        
        if self.len() == 0:
            return False
        
        if subsequence.len() > self.len():
            return False
        
        
        node = self.head

        count = 0
        
        
        while node is not None:
            if self.len() < subsequence.len() + count:
                return False
            
            if self.compare(node.value, subsequence.head.value) == 0:
                start_node = node
                start_sub_node = subsequence.head
                while self.compare(start_node.value, start_sub_node.value) == 0:
                    start_sub_node = start_sub_node.next
                    if start_sub_node is None:
                        return True
                    start_node = start_node.next
                
            node = node.next
            count += 1
          
        
        return False
        
        
        
    @staticmethod
    def merge(ol1 : 'OrderedList', ol2 : 'OrderedList', new_ask) -> 'OrderedList':
        result = OrderedList(new_ask)
        
        node1 = ol1.head
        if ol1.__ascending != ol2.__ascending:
            node2 = ol2.tail
        else:
            node2 = ol2.head
        
        _asc = 1 if ol1.__ascending else -1
        
        def next_node2(node2: Node) -> Node:
            if ol1.__ascending != ol2.__ascending:
                return node2.prev
            else:
                return node2.next
        
        while node1 is not None or node2 is not None:
            if node2 is None:
                result.add(node1.value)
                node1 = node1.next
            elif node1 is None:
                result.add(node2.value)
                node2 = next_node2(node2)
            elif result.compare(node1.value,node2.value)*_asc <= 0:
                result.add(node1.value)
                node1 = node1.next   
            else:
                result.add(node2.value)
                node2 = next_node2(node2)           
         
        return result
    

            

    def clean(self, asc):
        self._len = 0
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        return self._len 

    def get_all(self): #todo
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r
    
    def get_all_val(self): 
        r = []
        node = self.head
        while node != None:
            r.append(node.value) 
            node = node.next
        return r
    
    @staticmethod 
    def from_list(input_list : list, asc) -> 'OrderedList':
        lo = OrderedList(asc)
        
        for v in input_list:
            lo.add(v)
            
        return lo
            
           
