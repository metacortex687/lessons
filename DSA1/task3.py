#Solution complexity:"append" o(1) O(n)
#Solution complexity:"insert" o(n) O(n)
#Solution complexity:"delete" o(n) O(n)  

import ctypes

class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        
        if self.capacity == new_capacity:
            return
        
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
        
    def resize_and_insert(self, new_capacity, i , itm):
        
        if self.capacity == new_capacity:
            return
        
        new_array = self.make_array(new_capacity)
        for j in range(i):
            new_array[j] = self.array[j]
        
        new_array[i] = itm   
            
        for j in range(i,self.count):
            new_array[j+1] = self.array[j]
             
        self.array = new_array
        self.capacity = new_capacity
        self.count += 1
        
    def resize_and_delete(self, new_capacity, i):
        
        if self.capacity == new_capacity:
            return
        
        new_array = self.make_array(new_capacity)
        for j in range(i):
            new_array[j] = self.array[j]
            
        for j in range(i+1,self.count):
            new_array[j-1] = self.array[j]
             
        self.array = new_array
        self.capacity = new_capacity
        self.count -= 1
  
    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

  
        
    def insert(self, i, itm):
        if i == self.count:
            self.append(itm)
            return
            
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        
        if self.count == self.capacity:
            self.resize_and_insert(2*self.capacity,i,itm)
            return
           
        for j in range(self.count,i,-1): 
            self.array[j] = self.array[j-1]
            
        self.array[i] = itm
        
        self.count += 1 


    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
         
        if (self.count-1) < self.capacity//2:
            new_capacity = max(16,self.capacity*2//3)
            if new_capacity != self.capacity:
                self.resize_and_delete(new_capacity, i)
                return
            
        self.count -= 1 
        for i in range(i,self.count): 
            self.array[i] = self.array[i+1]
            
        

        
        
        