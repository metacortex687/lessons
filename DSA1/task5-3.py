import unittest
from task5 import Queue, LinkedList2, Node


import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task5_2", "./DSA1/task5-2.py")
task5_2 = importlib.util.module_from_spec(spec)
sys.modules["task5_2"] = task5_2
spec.loader.exec_module(task5_2)

TwoStackQueue = task5_2.TwoStackQueue
FixedArrayQueue = task5_2.FixedArrayQueue
rotate_queue = task5_2.rotate_queue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        
        self.assertEqual(q.size(),0)
        self.assertIsNone(q.dequeue())
        
        q.enqueue(7)
        self.assertEqual(q.size(),1)
        self.assertEqual(q.dequeue(),7)
        
        self.assertEqual(q.size(),0)
        self.assertIsNone(q.dequeue())   
        
        
        q.enqueue(1)   
        q.enqueue(2)  
        q.enqueue(3)  
        q.dequeue()
        q.enqueue(4) 
        
        self.assertEqual(q.size(),3)
        self.assertEqual(q.dequeue(),2)  
        self.assertEqual(q.dequeue(),3)  
        self.assertEqual(q.dequeue(),4)  
 
 
class TestTwoStacksQueue(unittest.TestCase):
    def test_queue(self):
        q = TwoStackQueue()
        
        self.assertEqual(q.size(),0)
        self.assertIsNone(q.dequeue())
        
        q.enqueue(7)
        self.assertEqual(q.size(),1)
        self.assertEqual(q.dequeue(),7)
        
        self.assertEqual(q.size(),0)
        self.assertIsNone(q.dequeue())   
        
        
        q.enqueue(1)   
        q.enqueue(2)  
        q.enqueue(3)  
        q.dequeue()
        q.enqueue(4) 
        
        self.assertEqual(q.size(),3)
        self.assertEqual(q.dequeue(),2)  
        self.assertEqual(q.dequeue(),3)  
        self.assertEqual(q.dequeue(),4)  
        
        
    def test_reverse(self):
        q = TwoStackQueue()
        q.enqueue(1)   
        q.enqueue(2)  
        q.enqueue(3)  
        
        q.reverse()
        
        self.assertEqual(q.dequeue(),3) 
        
        q.enqueue(4)  
        
        q.reverse()
        
        self.assertEqual(q.size(),3)
        
        self.assertEqual(q.dequeue(),4) 
        self.assertEqual(q.dequeue(),1) 
        self.assertEqual(q.dequeue(),2) 

        
 
class TestFixedArrayQueue(unittest.TestCase):
    def test_queue(self):
        q = FixedArrayQueue(3)
        
        self.assertEqual(q.size(),0)
        self.assertIsNone(q.dequeue())
        
        q.enqueue(7)
        self.assertEqual(q.size(),1)
        self.assertEqual(q.dequeue(),7)
        
        self.assertEqual(q.size(),0)
        self.assertIsNone(q.dequeue())   
        
        
        q.enqueue(1)   
        q.enqueue(2)  
        q.enqueue(3)  
        q.dequeue()
        q.enqueue(4) 
        
        self.assertEqual(q.size(),3)
        self.assertEqual(q.dequeue(),2)  
        self.assertEqual(q.dequeue(),3)  
        self.assertEqual(q.dequeue(),4) 
        
        
    def test_is_full_and_OverflowError(self): 
        
        q = FixedArrayQueue(3)
        
        q.enqueue(1)   
        q.enqueue(2)  
        
        self.assertFalse(q.is_full())
         
        q.enqueue(3)  
        q.dequeue()
        q.enqueue(4) 
        
        self.assertTrue(q.is_full())
        
        with self.assertRaises(OverflowError):
            q.enqueue(4) 
 
class TestFunctions(unittest.TestCase):   
    def test_rotate_queue(self): 
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        
        rotate_queue(q,3)
        
        self.assertEqual(q.dequeue(),4)  
        self.assertEqual(q.dequeue(),5)  
        self.assertEqual(q.dequeue(),1) 
        self.assertEqual(q.dequeue(),2)  
        self.assertEqual(q.dequeue(),3) 
  
 
        
class TestLinkedList2(unittest.TestCase):
    def test_linked_list(self):
        ll = LinkedList2()
        
        self.assertIsNone(ll.head())   
        self.assertIsNone(ll.tail()) 
        
        ll.add_in_head(Node(4))
        self.assertEqual(ll.head().value,4)  
        self.assertEqual(ll.tail().value,4)     
        
        ll.add_in_head(Node(5))
        self.assertEqual(ll.head().value,5)  
        self.assertEqual(ll.tail().value,4)            
        
        
        ll.delete_tail()
        self.assertEqual(ll.head().value,5)  
        self.assertEqual(ll.tail().value,5)  
        
        ll.add_in_head(Node(1))
        ll.add_in_head(Node(2))
        self.assertEqual(ll.head().value,2)  
        self.assertEqual(ll.tail().value,5)     
        
        ll.delete_tail()
        ll.delete_tail()
        self.assertEqual(ll.head().value,2)  
        self.assertEqual(ll.tail().value,2) 
        
        ll.delete_tail()         
        self.assertIsNone(ll.head())   
        self.assertIsNone(ll.tail())              
 
 
 
         
        
if __name__ == '__main__':
    unittest.main()