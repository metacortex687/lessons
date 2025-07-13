import unittest
from task8 import HashTable
# from task8_2 import DinamicHashTable, SoltHashTable
#python ./DSA1/task8-3.py

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task8-2", "./DSA1/task8-2.py")
task8_2 = importlib.util.module_from_spec(spec)
sys.modules["task8-2"] = task8_2
spec.loader.exec_module(task8_2)
DinamicHashTable = task8_2.DinamicHashTable
SoltHashTable = task8_2.SoltHashTable



class TestHashTable(unittest.TestCase):
    def test_put(self):
        ht = HashTable(2,1)
        
        _i_fun = ht.hash_fun('a')
        _i_seek = ht.seek_slot("a")
        self.assertIsNotNone(_i_seek)
        self.assertEqual(_i_fun,_i_seek)
         
        i_put = ht.put("a")
        self.assertIsNotNone(i_put)
        self.assertEqual(i_put,_i_seek)
        
        i_find = ht.find("a")
        self.assertIsNotNone(i_find)
        self.assertEqual(i_put,i_find)       
        
        _i_fun_b = ht.hash_fun('b')
        _i_seek_b = ht.seek_slot("b")
        self.assertIsNotNone(_i_seek_b)
        self.assertEqual(_i_fun_b,_i_seek_b)
         
        i_put_b = ht.put("b")
        self.assertIsNotNone(i_put_b)
        self.assertEqual(i_put_b,_i_seek_b)
        
        i_find_b = ht.find("b")
        self.assertIsNotNone(i_find_b)
        self.assertEqual(i_put_b,i_find_b)   
        
        self.assertCountEqual(ht.slots,["a","b"])    
        
        
        _i_seek = ht.seek_slot("c")
        self.assertIsNone(_i_seek)
        i_put = ht.put("c")
        self.assertIsNone(i_put)
        
        self.assertIsNone(ht.find("c"))

         
class TestDinamicHashTable(unittest.TestCase):
    def test_put(self):
        ht = DinamicHashTable(2)
        
        _i_fun = ht.hash_fun_1('a')
        _i_seek = ht.seek_slot("a")
        self.assertIsNotNone(_i_seek)
        self.assertEqual(_i_fun,_i_seek)
         
        i_put = ht.put("a")
        self.assertIsNotNone(i_put)
        self.assertEqual(i_put,_i_seek)
        
        i_find = ht.find("a")
        self.assertIsNotNone(i_find)
        self.assertEqual(i_put,i_find)       
        
        # _i_fun_b = ht.hash_fun_1('b')
        # _i_seek_b = ht.seek_slot("b")
        # self.assertIsNotNone(_i_seek_b)
        # self.assertEqual(_i_fun_b,_i_seek_b)
        
        _i_seek_b = ht.seek_slot("b")
        self.assertIsNotNone(_i_seek_b)        
        i_put_b = ht.put("b")
        self.assertIsNotNone(i_put_b)
        # self.assertNotEqual(i_put_b,_i_seek_b)
        self.assertEqual(ht.size,5)
        self.assertEqual(ht.count,2)
        self.assertEqual(i_put_b,ht.find("b"))
        
        i_find_b = ht.find("b")
        self.assertIsNotNone(i_find_b)
        self.assertEqual(i_put_b,i_find_b)   
        
        self.assertCountEqual(ht.slots,["a","b",None, None, None])    
        
        
        _i_seek = ht.seek_slot("c")
        # self.assertIsNotNone(_i_seek)
        i_put = ht.put("c")
        self.assertIsNotNone(i_put)
        self.assertIsNotNone(ht.find("c"))
     
     
    def test_many_insert(self): 
        ht = DinamicHashTable(2)
        
        for i in range (50,100):
            ht.put(f"test_{i}")
            
        for i in range (50,100):
            self.assertIsNotNone(ht.find(f"test_{i}"))
            
        for i in range (1,50):
            self.assertIsNone(ht.find(f"test_{i}"))
          
         
class TestSoltashTable(unittest.TestCase):
    def test_put(self):
        ht = SoltHashTable(2)
        
        _i_fun = ht.hash_fun_1('a')
        _i_seek = ht.seek_slot("a")
        self.assertIsNotNone(_i_seek)
        self.assertEqual(_i_fun,_i_seek)
         
        i_put = ht.put("a")
        self.assertIsNotNone(i_put)
        self.assertEqual(i_put,_i_seek)
        
        i_find = ht.find("a")
        self.assertIsNotNone(i_find)
        self.assertEqual(i_put,i_find)       
 
        
        _i_seek_b = ht.seek_slot("b")
        self.assertIsNotNone(_i_seek_b)        
        i_put_b = ht.put("b")
        self.assertIsNotNone(i_put_b)
    
        self.assertEqual(ht.size,5)
        self.assertEqual(ht.count,2)
        self.assertEqual(i_put_b,ht.find("b"))
        
        i_find_b = ht.find("b")
        self.assertIsNotNone(i_find_b)
        self.assertEqual(i_put_b,i_find_b)   
        
        self.assertCountEqual(ht.slots,["a","b",None, None, None])    
        
        
        _i_seek = ht.seek_slot("c")
        # self.assertIsNotNone(_i_seek)
        i_put = ht.put("c")
        self.assertIsNotNone(i_put)
        self.assertIsNotNone(ht.find("c"))
     
     
    def test_many_insert(self): 
        ht = SoltHashTable(2)
        
        for i in range (50,100):
            ht.put(f"test_{i}")
            
        for i in range (50,100):
            self.assertIsNotNone(ht.find(f"test_{i}"))
            
        for i in range (1,50):
            self.assertIsNone(ht.find(f"test_{i}"))
          
           
        
if __name__ == '__main__':
    unittest.main()