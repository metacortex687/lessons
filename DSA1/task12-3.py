import unittest
from task12 import NativeCache
#python ./DSA1/task12-3.py

class TestNativeCache(unittest.TestCase):
    def test_put_get_hit(self):
        nc = NativeCache(2)
        
        _str1 = "abc" 
        self.assertIsNone(nc.get(_str1))
        nc.put(_str1, 15)
        self.assertEqual(nc.get(_str1), 15)
        
        _str2 = "cba" 
        self.assertIsNone(nc.get(_str2))
        nc.put(_str2, 25)
        self.assertEqual(nc.get(_str2), 25)    
        self.assertEqual(nc.get(_str2), 25) 
        
        self.assertIsNone(nc.count_hit("test"))
        self.assertEqual(nc.count_hit(_str1), 1)
        self.assertEqual(nc.count_hit(_str2), 2) 
        
        _str3 = "over"
        nc.put(_str3, 50)
        nc.get(_str3)
         
        self.assertEqual(nc.count_hit(_str2), 2)
        self.assertEqual(nc.count_hit(_str3), 1) 
        self.assertIsNone(nc.count_hit(_str1))        
   
    def test_put_get_hit_many(self):   
        nc = NativeCache(10)   
        
        for i in range(100):
            _str = f"test{i}" 
            nc.put(_str,i) 
            if i >= 90:
                nc.get(_str) 
            
        for i in range(90,100):
            _str = f"test{i}" 
            self.assertEqual(nc.get(_str), i)
            
        for i in range(90,100):
            _str = f"test{i}" 
            self.assertEqual(nc.count_hit(_str), 2)        
           
        


        
        
if __name__ == '__main__':
    unittest.main()
   