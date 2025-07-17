from __future__ import annotations
from typing import Any
        

class PowerSet:

    def __init__(self) -> None:
        self.hash_table = HashTable(10,1)

    def size(self) -> int:
        return self.hash_table.count

    def put(self, value: Any) -> None:
        self.hash_table.put(value)

    def get(self, value: Any) -> bool:
        return self.hash_table.find(value) is not None

    def remove(self, value: Any) -> bool:
        return self.hash_table.remove(value)

    def union(self, set2: PowerSet) -> PowerSet:
        ps = PowerSet()
        
        for v in self.hash_table:
            ps.put(v)
            
        for v in set2.hash_table:
            ps.put(v)            
        
        return ps

    def intersection(self, set2: PowerSet) -> PowerSet:
        ps = PowerSet()
        
        for v in self.hash_table:
            if set2.hash_table.find(v) is not None:
                ps.put(v)
        
        return ps

    def difference(self, set2: PowerSet) -> PowerSet:
        ps = PowerSet()
        
        for v in self.hash_table:
            if set2.hash_table.find(v) is None:
                ps.put(v)
        
        return ps    

    def issubset(self, set2: PowerSet) -> bool:
        if set2.size() == 0:
            return True
        
        if self.size() < set2.size():
            return False
        
        for v in set2.hash_table:
            if self.hash_table.find(v) is None:
                return False
            
        return True    

    def equals(self, set2: PowerSet) -> bool:
        if set2.size() == 0:
            return True
        
        if self.size() != set2.size():
            return False
                    
        return self.difference(set2).size() == 0    
    
    def values_to_list(self):
        return self.hash_table.values_to_list()    
    
    def __repr__(self):
        return str(self.values_to_list())
    


  
    
class HashTable:
    class RemovedValue:
        pass    
    REMOVED = RemovedValue()   
    
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size
        self.count = 0
        self._index = -1
        
        

    def hash_fun(self, value: Any):
        value = str(type(value)) + str(value)
        _hash = 0
        for e in value:
            _hash = (_hash*31+ord(e))%self.size
             
        return _hash

    def _resize(self,new_size):
        ht = HashTable(new_size,self.step)
        for i in range(self.size):
            if self.slots[i] is None:
                continue
            ht.put(self.slots[i])
        
        self.size = ht.size
        self.step = ht.step
        self.slots = ht.slots
        self.count = ht.count

    def seek_slot(self, value, find_value = False):
        start_index = self.hash_fun(value)
        index = start_index
        while self.slots[index]  is not None and self.slots[index] != value:
            if not find_value and self.slots[index]  is  HashTable.REMOVED:
                break

            index += self.step
            index %= self.size
            
            if index == start_index:
                return None       
               
        return index

    def put(self, value):
        if self.count >= self.size:
            self._resize(self.size*2)
        
        index = self.seek_slot(value)
        
        if index is None:
            return None
        
        if self.slots[index] == value:
            return
        
        
        self.slots[index] = value
        self.count += 1
        
        return index

    def remove(self, value):
        index = self.find(value)
        
        if index is None:
            return False
        
        self.slots[index] = HashTable.REMOVED
        self.count -= 1
        
        return True
    
    def __iter__(self):
        self._index = -1
        return self
    
    def __next__(self):
        if self.count == 0:
            raise StopIteration
         
        self._index += 1
        while True:
            if self._index >= self.size:
                raise StopIteration
            
            value = self.slots[self._index]
            
            if value is None or value is HashTable.REMOVED:
                self._index += 1
                continue
            
            return value
          
    def find(self, value):
        index = self.seek_slot(value, find_value = True)
        
        if index == None:
            return None
        
        if self.slots[index] == value:
            return index
        
        return None
    
    def values_to_list(self):
        res = []
        for v in self.slots:
            if v is None:
                continue
            if v is HashTable.REMOVED:
                continue
            res.append(v)
        return res
    
    def __repr__(self):
        return str(self.values_to_list())
    
    
    