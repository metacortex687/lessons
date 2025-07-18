class BloomFilter:

    def __init__(self, f_len):
        self.filter_len = f_len
        self.filter = 0

    def hash1(self, str1):
        _mask = (1 << self.filter_len) - 1
        _hash = 0
        # 17
        for c in str1:
            _hash = _hash*17 + ord(c)
            _hash &= _mask
        return _hash

    def hash2(self, str1):
        _mask = (1 << self.filter_len) - 1
        _hash = 0
        # 223
        for c in str1:
            _hash = _hash*223 + ord(c)
            _hash &= _mask
        return _hash

    def add(self, str1):
        self.filter |= self.hash1(str1)
        self.filter |= self.hash2(str1)


    def is_value(self, str1) -> bool:
        
        _hash1 = self.hash1(str1)
        _hash2 = self.hash2(str1)
        
        return (_hash1 & self.filter == _hash1) and  (_hash2 & self.filter == _hash2)
    
    
        