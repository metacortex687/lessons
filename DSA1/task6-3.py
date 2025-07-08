from task6 import Deque

import unittest
#python ./DSA1/task6-3.py

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task6-2", "./DSA1/task6-2.py")
task6_2 = importlib.util.module_from_spec(spec)
sys.modules["task6-2"] = task6_2
spec.loader.exec_module(task6_2)

is_polindrom = task6_2.is_polindrom
TwoStackDequeue = task6_2.TwoStackDequeue
DynArrayDequeue = task6_2.DynArrayDequeue
bracket_control = task6_2.bracket_control

class TestDeque(unittest.TestCase):
    
    def test_deque(self):
        dq = Deque()
        
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())
        
        dq.addFront(5)
        self.assertEqual(dq.size(),1)
        self.assertEqual(dq.removeFront(),5)
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())
        
        dq.addTail(15)
        self.assertEqual(dq.size(),1)
        self.assertEqual(dq.removeTail(),15)
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())        
        
        dq.addTail(12)
        self.assertEqual(dq.removeFront(),12)
        
        dq.addFront(12)
        self.assertEqual(dq.removeTail(),12) 
        
        dq.addFront(1)
        dq.addFront(2) 
        dq.addFront(3)
        dq.addFront(4)
        
        self.assertEqual(dq.size(),4)
        self.assertEqual(dq.removeTail(),1)
        self.assertEqual(dq.removeTail(),2)
        self.assertEqual(dq.removeFront(),4)  
        self.assertEqual(dq.removeFront(),3)      
 
 
class TestTwoStackDequeue(unittest.TestCase):
    
    def test_deque(self):
        dq = TwoStackDequeue()
        
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())
        
        dq.addFront(5)
        self.assertEqual(dq.size(),1)
        self.assertEqual(dq.removeFront(),5)
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())
        
        dq.addTail(15)
        self.assertEqual(dq.size(),1)
        self.assertEqual(dq.removeTail(),15)
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())        
        
        dq.addTail(12)
        self.assertEqual(dq.removeFront(),12)
        
        dq.addFront(12)
        self.assertEqual(dq.removeTail(),12) 
        
        dq.addFront(1)
        dq.addFront(2) 
        dq.addFront(3)
        dq.addFront(4)
        
        self.assertEqual(dq.size(),4)
        self.assertEqual(dq.removeTail(),1)
        self.assertEqual(dq.removeTail(),2)
        self.assertEqual(dq.removeFront(),4)  
        self.assertEqual(dq.removeFront(),3)    
    
    def test_min(self):
        dq = TwoStackDequeue()
        
        self.assertIsNone(dq.min())
        
        dq.addFront(5)
        
        self.assertEqual(dq.min(),5) 
        
        dq.addTail(1)
        
        self.assertEqual(dq.min(),1)  
        
        dq.addTail(2)
        dq.addTail(7)
        
        self.assertEqual(dq.removeFront(),5) 
        self.assertEqual(dq.removeFront(),1)       

        self.assertEqual(dq.min(),2) 
 
     
class TestDynArrayDeque(unittest.TestCase):
    
    def test_deque(self):
        dq = DynArrayDequeue()
        
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())
        
        dq.addFront(5)
        self.assertEqual(dq.size(),1)
        self.assertEqual(dq.removeFront(),5)
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())
        
        dq.addTail(15)
        self.assertEqual(dq.size(),1)
        self.assertEqual(dq.removeTail(),15)
        self.assertEqual(dq.size(),0)
        self.assertIsNone(dq.removeFront())
        self.assertIsNone(dq.removeTail())        
        
        dq.addTail(12)
        self.assertEqual(dq.removeFront(),12)
        
        dq.addFront(12)
        self.assertEqual(dq.removeTail(),12) 
        
        dq.addFront(1)
        dq.addFront(2) 
        dq.addFront(3)
        dq.addFront(4)
        
        self.assertEqual(dq.size(),4)
        self.assertEqual(dq.removeTail(),1)
        self.assertEqual(dq.removeTail(),2)
        self.assertEqual(dq.removeFront(),4)  
        self.assertEqual(dq.removeFront(),3)        
 
    def test_capacity(self):
        dq = DynArrayDequeue(2)
        self.assertEqual(dq.capacity(),2)
        dq.addFront(1)
        dq.addFront(2)
        self.assertEqual(dq.capacity(),2)
        
        dq.addFront(3)
        self.assertEqual(dq.capacity(),4)
        
        self.assertEqual(dq.removeFront(),3)
        self.assertEqual(dq.removeFront(),2)
        self.assertEqual(dq.removeTail(),1)
    
        
        
        dq = DynArrayDequeue(2)
        self.assertEqual(dq.capacity(),2)
        dq.addFront(1)
        dq.addFront(2)
        self.assertEqual(dq.capacity(),2)
        
        dq.addTail(3)
        self.assertEqual(dq.capacity(),4)  
        
        self.assertEqual(dq.removeFront(),2)
        self.assertEqual(dq.removeFront(),1)
        self.assertEqual(dq.removeTail(),3)
        
        
        dq = DynArrayDequeue(2)
        self.assertEqual(dq.capacity(),2)
        dq.addFront(1)
        dq.addFront(2)
        self.assertEqual(dq.capacity(),2)
        
        dq.addTail(3)
        dq.addTail(4)
        self.assertEqual(dq.capacity(),4)  
        
        dq.addTail(5)
        self.assertEqual(dq.capacity(),8) 
        
        self.assertEqual(dq.removeFront(),2)
        self.assertEqual(dq.size(),4)
        self.assertEqual(dq.capacity(),8)
        
        self.assertEqual(dq.removeFront(),1)
        self.assertEqual(dq.size(),3)
        self.assertEqual(dq.capacity(),5)       
        
        self.assertEqual(dq.removeFront(),3)
        self.assertEqual(dq.size(),2)
        self.assertEqual(dq.capacity(),3)
        
        self.assertEqual(dq.removeFront(),4)
        self.assertEqual(dq.size(),1)
        self.assertEqual(dq.capacity(),2)
        
        self.assertEqual(dq.removeFront(),5)
        self.assertEqual(dq.size(),0)
        self.assertEqual(dq.capacity(),2)
  
        


        

         
             
class TestFunctions(unittest.TestCase):
    
    def test_is_polindrom(self):
        s = ""
        
        self.assertFalse(is_polindrom(s,deque_constractor=Deque))
        
        s = 'a'
       
        self.assertTrue(is_polindrom(s,deque_constractor=Deque))
        
        s = "aa"
        self.assertTrue(is_polindrom(s,deque_constractor=Deque))
        
        s = "qsarasq"
        self.assertTrue(is_polindrom(s,deque_constractor=Deque))
        
        s = "qskasq"
        self.assertFalse(is_polindrom(s,deque_constractor=Deque))
        
    def test_bracket_control(self):
        s = ""
        self.assertTrue(bracket_control(s,deque_constractor=Deque))  
        
        s = "{}"
        self.assertTrue(bracket_control(s,deque_constractor=Deque))         

        s = "()"
        self.assertTrue(bracket_control(s,deque_constractor=Deque))    
        
        s = "[]"
        self.assertTrue(bracket_control(s,deque_constractor=Deque))    
         
        s = "[]({})" 
        self.assertTrue(bracket_control(s,deque_constractor=Deque))   
        
        s = "(())}{(" 
        self.assertFalse(bracket_control(s,deque_constractor=Deque))     
        
if __name__ == '__main__':
    unittest.main()

