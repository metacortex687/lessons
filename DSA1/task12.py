from __future__ import annotations
from typing import Any


class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.count = 0
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size
    
    def count_hit(self, key: str):
        i = self._find_slot(key)
        if i is None:
            return None
        
        return self.hits[i]
         
    def put(self, key: str , value : Any):
        if self.size == self.count:
            self._remove_least_frequently_used()
        
        i = self._find_slot(key)
        
        if self.slots[i] != key:
            self.count += 1
            self.slots[i] = key
            self.hits[i] = 0
         
        self.values[i] = value
     
    def get(self, key: str):
        i = self._find_slot(key)
        
        if i is None:
            return None
        
        if self.slots[i] != key:
            return None
        
        self.hits[i] += 1
        
        return self.values[i]
         
    def _hash_fun(self, key: str):
        _hash = 0
        for e in key:
            _hash = (_hash*31+ord(e))%self.size
             
        return _hash
    
    def _find_slot(self, key: str):
        i = self._hash_fun(key)
        
        star_index = i
        while self.slots[i] is not None and self.slots[i] != key:
            i += 1
            i %= self.size
            if star_index == i:
                return None
            
        return i
    
    def _find_least_frequently_used_slot(self):
        min_val = self.hits[0]
        for i in range(1,self.size):
            if self.hits[i] == 0:
                return i
            
            if min_val > self.hits[i]:
                min_val = self.hits[i]
                
        for i in range(0,self.size):
           if self.hits[i] == min_val:
                return i
        
    def _remove_least_frequently_used(self):
        i = self._find_least_frequently_used_slot()
        
        self.count -= 1
        self.hits[i] = 0
        self.slots[i] = None      
        self.values[i] = None
     
    