import unittest
from task9 import NativeDictionary

#python ./DSA1/task9-3.py

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task9-2", "./DSA1/task9-2.py")
task9_2 = importlib.util.module_from_spec(spec)
sys.modules["task9-2"] = task9_2
spec.loader.exec_module(task9_2)
BitNativeDictionary = task9_2.BitNativeDictionary
OrderedListDictionary = task9_2.OrderedListDictionary



class TestBitNativeDictionary(unittest.TestCase):
    def test_put_get(self):
        nd = BitNativeDictionary(1)
        key = 0b0
        self.assertFalse(nd.is_key(key))
        self.assertIsNone(nd.get(key))
        
        nd.put(key,10)
        self.assertTrue(nd.is_key(key))
        self.assertEqual(nd.get(key),10)   
        
        nd.put(key,15)
        self.assertTrue(nd.is_key(key))
        self.assertEqual(nd.get(key),15)    
        
        nd = BitNativeDictionary(2)
        key = 0b10
        self.assertFalse(nd.is_key(key))
        self.assertIsNone(nd.get(key))
        
        nd.put(key,10)
        self.assertTrue(nd.is_key(key))
        self.assertEqual(nd.get(key),10)   
        
        nd.put(key,15)
        self.assertTrue(nd.is_key(key))
        self.assertEqual(nd.get(key),15)  
        
        
        nd = BitNativeDictionary(1)
        key = 0b10
        
        with self.assertRaises(ValueError):
            nd.is_key(key)
            
        with self.assertRaises(ValueError):
            nd.get(key)            
            
        with self.assertRaises(ValueError):
            nd.put(key,15) 
            
            
        nd = BitNativeDictionary(12)
        key = 0b101011111111
        self.assertFalse(nd.is_key(key))
        self.assertIsNone(nd.get(key))
        
        nd.put(key,10)
        self.assertTrue(nd.is_key(key))
        self.assertEqual(nd.get(key),10)   
        
        nd.put(key,15)
        self.assertTrue(nd.is_key(key))
        self.assertEqual(nd.get(key),15) 
        
        self.assertFalse(nd.is_key(0b101011011111))
        self.assertIsNone(nd.get(0b101010111111))        
            
            

class TestNativeDictionary(unittest.TestCase):
    def test_put_get(self):
        nd = NativeDictionary(2)
        _str = "test"
        self.assertFalse(nd.is_key(_str))
        self.assertIsNone(nd.get(_str))
        
        nd.put(_str,10)
        self.assertTrue(nd.is_key(_str))
        self.assertEqual(nd.get(_str),10)   
        
        nd.put(_str,15)
        self.assertTrue(nd.is_key(_str))
        self.assertEqual(nd.get(_str),15)   
        
        
        _str = "test2"
        self.assertFalse(nd.is_key(_str))
        self.assertIsNone(nd.get(_str))
        nd.put(_str,27)
        self.assertEqual(nd.get(_str),27)   
        
        
        nd.put("resize",27)
            
            
class TestOrderedListDictionary(unittest.TestCase):
    def test_put_get(self):
        nd = OrderedListDictionary()
        _str = "test"
        self.assertFalse(nd.is_key(_str))
        self.assertIsNone(nd.get(_str))
        
        nd.put(_str,10)
        self.assertTrue(nd.is_key(_str))
        self.assertEqual(nd.get(_str),10)   
        
        nd.put(_str,15)
        self.assertTrue(nd.is_key(_str))
        self.assertEqual(nd.get(_str),15)   
        
        
        _str = "test2"
        self.assertFalse(nd.is_key(_str))
        self.assertIsNone(nd.get(_str))
        nd.put(_str,27)
        self.assertEqual(nd.get(_str),27)   
        
        
        nd.put("resize",35)
        self.assertEqual(nd.get("test"),15)  
        self.assertEqual(nd.get("test2"),27)  
        self.assertEqual(nd.get("resize"),35)                  
        
        
        
if __name__ == '__main__':
    unittest.main()
   