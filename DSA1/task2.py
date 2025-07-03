class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
            
        return result

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None:
                    self.head = node.next
                else:
                    node.prev.next = node.next
                    
                if node.next is None:
                    self.tail = node.prev
                else:
                    node.next.prev = node.prev
  
                if not all:
                    return
 
            node = node.next
            
    def to_list_values(self, dir_foraward = True):
        result = []  
            
        if dir_foraward:
            
            node = self.head
            while node != None:
                result.append(node.value)
                node = node.next
                
        else:
            
            node = self.tail
            while node != None:
                result.append(node.value)
                node = node.prev    


        return result       

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        result = 0
        node = self.head
        while node is not None:
            result += 1
            node = node.next

        return result

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head 
            
            if self.head is not None:
                self.head.prev = newNode 
                 
            self.head =  newNode
             
            if self.tail is None:
                self.tail = newNode
              
        else:
                
            node = self.head
            while node is not None:
                if node == afterNode:
                    newNode.next = afterNode.next
                    afterNode.next = newNode
                    newNode.prev = afterNode
                    
                    if newNode.next is None:
                        self.tail = newNode
                    else:
                        newNode.next.prev = newNode
 
                    return
                
                node = node.next   


    def add_in_head(self, newNode):
        self.insert(None,newNode)
 
