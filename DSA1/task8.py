class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        index = 0
        for c in value:
             index += ord(c)
             index %= self.size
             
        return index

    def seek_slot(self, value):
        start_index = self.hash_fun(value)
        index = start_index
        while self.slots[index]  is not None and self.slots[index] != value:
            index += self.step
            index %= self.size
            
            if index == start_index:
                return None       
               
        return index

    def put(self, value):
        index = self.seek_slot(value)
        
        if index is None:
            return None
        
        self.slots[index] = value
        
        return index

    def find(self, value):
        index = self.seek_slot(value)
        
        if index == None:
            return None
        
        if self.slots[index] == value:
            return index
        
        return None
