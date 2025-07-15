class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.count = 0

    
    def _resize(self,new_size):
        nd = NativeDictionary(new_size)
        for i in range(self.size):
            if self.slots[i] is None:
                continue
            
            nd.put(self.slots[i], self.values[i])
        
        self.size = nd.size
        self.slots = nd.slots
        self.values = nd.values
        self.count = nd.count

    def hash_fun(self, key : str):
        _hash = 0
        for e in key:
            _hash = (_hash*31+ord(e))%self.size
        
        start_ondex = _hash
        while self.slots[_hash] is not None and self.slots[_hash] != key:
            _hash += 1
            _hash %= self.size
            
            if start_ondex == _hash:
                raise Exception("Не удалось определить индекс")

        return _hash

    def is_key(self, key):
        return self.slots[self.hash_fun(key)] == key

    def put(self, key, value):
        if self.count == self.size:
            self._resize(self.size*2)
        
        index = self.hash_fun(key)
        self.slots[index] = key
        self.values[index] = value
        self.count += 1


    def get(self, key):
        return self.values[self.hash_fun(key)]