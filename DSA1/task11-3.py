import unittest
from task11 import BloomFilter

#python ./DSA1/task11-3.py

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task11-2", "./DSA1/task11-2.py")
task11_2 = importlib.util.module_from_spec(spec)
sys.modules["task11-2"] = task11_2
spec.loader.exec_module(task11_2)
BloomFilter2 = task11_2.BloomFilter2

class TestBloomFilter(unittest.TestCase):
    def test_simply(self):
        bf = BloomFilter(32)
        self.assertFalse(bf.is_value("0123456789"))
        bf.add("0123456789")
        self.assertTrue(bf.is_value("0123456789"))
        
        bf.add("12345")
        self.assertTrue(bf.is_value("0123456789"))    
        self.assertTrue(bf.is_value("12345")) 
        
        _str = "11122111111111111111" 
        self.assertFalse(bf.is_value("111111111111111"))     
        
    def test_many(self):
        bf = BloomFilter(32)
        
        _str = "0123456789"
        for _ in range(10):
            bf.add(_str)
            _str = _str[1:] + _str[0]
            
        _str = "0123456789"
        for _ in range(10):
            self.assertTrue(bf.is_value(_str))  
            _str = _str[1:] + _str[0]    
            
        _str = "12345" 
        self.assertFalse(bf.is_value(_str))             
 
        
class TestBloomFilter2(unittest.TestCase):
    def test_simply(self):
        bf = BloomFilter2(32)
        self.assertFalse(bf.is_value("0123456789"))
        bf.add("0123456789")
        self.assertTrue(bf.is_value("0123456789"))
        
        bf.add("12345")
        self.assertTrue(bf.is_value("0123456789"))    
        self.assertTrue(bf.is_value("12345")) 
        
        _str = "11122111111111111111" 
        self.assertFalse(bf.is_value("111111111111111"))     
        
    def test_many(self):
        bf = BloomFilter2(32)
        
        _str = "0123456789"
        for _ in range(10):
            bf.add(_str)
            _str = _str[1:] + _str[0]
            
        _str = "0123456789"
        for _ in range(10):
            self.assertTrue(bf.is_value(_str))  
            _str = _str[1:] + _str[0]    
            
        _str = "12345" 
        self.assertFalse(bf.is_value(_str))                


    def test_add_filter(self):
        bf1 = BloomFilter2(32)
        bf2 = BloomFilter2(32)
        _val = "0123456789"
        self.assertFalse(bf1.is_value(_val))
        self.assertFalse(bf2.is_value(_val))
        bf2.add("0123456789")
        bf1.add_filter(bf2)
        self.assertTrue(bf1.is_value(_val))
        
        bf1 = BloomFilter2(32)
        bf2 = BloomFilter2(32)   
        
        _str = "0123456789"
        for _ in range(5):
            bf1.add(_str)
            _str = _str[1:] + _str[0]
            
        for _ in range(5,10):
            bf2.add(_str)
            _str = _str[1:] + _str[0]           
        
        bf2.add_filter(bf1) 
            
        _str = "0123456789"
        for _ in range(10):
            self.assertTrue(bf2.is_value(_str))  
            _str = _str[1:] + _str[0]   
            
            
        _str = "11122111111111111111" 
        self.assertFalse(bf2.is_value("111111111111111"))       

        
        
if __name__ == '__main__':
    unittest.main()
   
   
     
        