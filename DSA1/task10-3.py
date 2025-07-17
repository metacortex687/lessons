import unittest
import task10

#python ./DSA1/task10-3.py

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task10-2", "./DSA1/task10-2.py")
task10_2 = importlib.util.module_from_spec(spec)
sys.modules["task10-2"] = task10_2
spec.loader.exec_module(task10_2)


class TestPowerSet(unittest.TestCase):
    PowerSet = task10.PowerSet
    
    def test_init(self):
        ps = self.PowerSet()
        self.assertEqual(ps.size(),0)
        self.assertFalse(ps.get("hello"))
        
    def test_put_any_type(self):
        ps = self.PowerSet()
        ps.put("1")
        self.assertEqual(ps.size(),1)
        ps.put(1)    
        self.assertEqual(ps.size(),2)    
            
    def test_put_get_remove(self):
        ps = self.PowerSet()
        
        _str1 = "qwert"
        self.assertFalse(ps.get(_str1))
        ps.put(_str1)
        self.assertEqual(ps.size(),1)
        self.assertTrue(ps.get(_str1))
        
        _str2 = "12345"
        self.assertFalse(ps.get(_str2))
        ps.put(_str2)
        self.assertEqual(ps.size(),2)
        self.assertTrue(ps.get(_str2))
        
        _str3 = "54321"
        self.assertFalse(ps.get(_str3))
        ps.put(_str3)
        self.assertEqual(ps.size(),3)
        self.assertTrue(ps.get(_str3))
        
        self.assertFalse(ps.remove("test"))
        self.assertTrue(ps.remove(_str2))
        
        self.assertTrue(ps.get(_str1))
        self.assertFalse(ps.get(_str2))
        self.assertTrue(ps.get(_str3))
        
    def test_union(self):
        ps1 = self.PowerSet()
        ps2 = self.PowerSet()
        
        ps = ps1.union(ps2)
        
        self.assertEqual(ps.size(),0)
        
        ps1.put("a")
        ps = ps1.union(ps2)
        
        self.assertEqual(ps.size(),1) 
        self.assertEqual(ps.values_to_list(),["a"]) 
        
        ps2.put("b")
        ps2.put("a")
        ps = ps1.union(ps2)
        
        self.assertEqual(ps.size(),2) 
        self.assertCountEqual(ps.values_to_list(),["a","b"])         
        
    def test_intersection(self):
        ps1 = self.PowerSet()
        ps2 = self.PowerSet()   
        
        ps = ps1.intersection(ps2) 
        
        self.assertEqual(ps.size(),0) 
        self.assertCountEqual(ps.values_to_list(),[])   
        
        ps1.put("a")
        ps2.put("b")
        self.assertEqual(ps1.size(),1) 
        self.assertEqual(ps2.size(),1) 
        
        ps = ps1.intersection(ps2) 
        self.assertEqual(ps.size(),0) 
        self.assertCountEqual(ps.values_to_list(),[])           
           
        ps1.put("c")
        ps2.put("c") 
        ps = ps1.intersection(ps2) 
        self.assertEqual(ps.size(),1) 
        self.assertCountEqual(ps.values_to_list(),["c"])      
        
    def test_difference(self):
        ps1 = self.PowerSet()
        ps2 = self.PowerSet() 
          
        ps = ps1.difference(ps2)
        self.assertEqual(ps.size(),0) 
        self.assertCountEqual(ps.values_to_list(),[])   
        
        ps1.put("a")
        ps = ps1.difference(ps1)
        self.assertEqual(ps.size(),0) 
        self.assertCountEqual(ps.values_to_list(),[])     
        
        ps1.put("a")
        ps = ps1.difference(ps2)
        self.assertEqual(ps.size(),1) 
        self.assertCountEqual(ps.values_to_list(),["a"])     
                
        
        ps2.put("b")     
        ps = ps1.difference(ps2)
        self.assertEqual(ps.size(),1) 
        self.assertCountEqual(ps.values_to_list(),["a"])  
        
        ps1.put("c")     
        ps2.put("a")  
        ps = ps1.difference(ps2)
        self.assertEqual(ps.size(),1) 
        self.assertCountEqual(ps.values_to_list(),["c"])         
        
        
    def test_issubset(self):
        ps1 = self.PowerSet()
        ps2 = self.PowerSet() 
        
        self.assertTrue(ps1.issubset(ps2))
        
        ps2.put("a")
        self.assertFalse(ps1.issubset(ps2))
        
        ps1.put("a")
        self.assertTrue(ps1.issubset(ps2))    
        
        ps1.put("b")
        self.assertTrue(ps1.issubset(ps2))   
        
        self.assertTrue(ps1.issubset(ps1)) 
        
           
              
    def test_equals(self):
        ps1 = self.PowerSet()
        ps2 = self.PowerSet() 
        
        self.assertTrue(ps1.equals(ps2))
        
        ps2.put("a")
        self.assertFalse(ps1.equals(ps2))
        
        ps1.put("a")
        self.assertTrue(ps1.equals(ps1))      
             
    def test_put_get_many(self):   
        ps = self.PowerSet()
        for i in range(10000):
            ps.put(f"test{i}")
            
        self.assertEqual(ps.size(),10000)
        for i in range(10000):
            self.assertTrue(ps.get(f"test{i}"))     
      

class TestPowerSet_2(TestPowerSet):
    PowerSet = task10_2.PowerSet
    
    def test_prod(self):
        ps1 = self.PowerSet()
        ps2 = self.PowerSet()
        
        prod = ps1.prod(ps2)
        self.assertEqual(prod,[])
        
        ps1.put("a")
        prod = ps1.prod(ps2)
        self.assertEqual(prod,[])
        
        ps2.put("b")
        prod = ps1.prod(ps2)
        self.assertEqual(prod,[("a","b")])  
        
        ps1.put("c")     
        ps2.put("c") 
        prod = ps1.prod(ps2)
        self.assertCountEqual(prod,[("a","b"),("a","c"),("c","b"),("c","c")])  
        
    
    def test_many_intersection(self):
        ps1 = self.PowerSet()
        ps2 = self.PowerSet()   
        ps3 = self.PowerSet() 
        
        ps = ps1.intersection(ps2,ps3) 
        
        self.assertEqual(ps.size(),0) 
        self.assertCountEqual(ps.values_to_list(),[])   
        
        ps1.put("a")
        ps2.put("b")
        ps3.put("c")
        
        ps = ps1.intersection(ps2) 
        self.assertEqual(ps.size(),0) 
        self.assertCountEqual(ps.values_to_list(),[])           
           
        ps1.put("c")
        ps2.put("c") 
        ps = ps1.intersection(ps2) 
        self.assertEqual(ps.size(),1) 
        self.assertCountEqual(ps.values_to_list(),["c"])     
  

class TestBagSet(unittest.TestCase): 
    Bag = task10_2.Bag
     
    def test_put_delete_list(self):
        b = self.Bag()
        
        b.put("a")
        b.put("b")
        b.put("c")
        b.delete("c")
        b.delete("c")
        b.put("a")
        
        self.assertDictEqual(b.list(),{"a":2,"b":1})
      
        
if __name__ == '__main__':
    unittest.main()    
    