class Node:
    def __init__(self, v):
        self.value = v
        self.prev : Node = None
        self.next : Node = None

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
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            return
        
        if after_node.next is None:
            self.tail = new_node
        else:
            after_node.next.prev = new_node  
              
        new_node.next  = after_node.next         
        after_node.next = new_node
        new_node.prev = after_node



    def add(self, value):
        self._len  += 1
        
        _asc = 1 if self.__ascending else -1
        
        if self.head is None and self.tail is None :
            self._insert_after(None,value)
            return
        
        if self.compare(value,self.head.value)*_asc <= 0:
            self._insert_after(None,value)
        elif self.compare(value,self.tail.value)*_asc >= 0:
            self._insert_after(self.tail,value)
        else:
            node = self.head
            while self.compare(node.value,value)*_asc < 0:
                node = node.next
            
            self._insert_after(node.prev,value)    


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
            
        
        _asc = 1 if self.__ascending else -1
        if self.compare(val,self.head.value)*_asc < 0:
            return
        elif self.compare(val,self.tail.value)*_asc > 0:
            return
        
        node = self.head.next
        while node.next is not None:
            if self.compare(node.value,val) == 0:
                node.prev.next = node.next
                node.next.prev = node
                self._len -= 1
                return
            
            node = node.next
        



            

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
            
           

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1 :str, v2 : str):
        v1  = v1.strip()
        v2 = v2.strip()
        return super().compare(v1,v2)