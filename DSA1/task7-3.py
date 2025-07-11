import unittest

import task7
from task7 import OrderedStringList

#python ./DSA1/task7-3.py

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task7-2", "./DSA1/task7-2.py")
task7_2 = importlib.util.module_from_spec(spec)
sys.modules["task7-2"] = task7_2
spec.loader.exec_module(task7_2)


class TestOrderedList(unittest.TestCase):
    
    OrderedList = task7.OrderedList
    
    def test_add_asc(self):
        ol = self.OrderedList(True)
        ol.add(5)
        self.assertEqual(ol.len(),1)
        self.assertEqual(ol.head.value,5)
        self.assertEqual(ol.tail.value,5)
        
        ol.add(1)
        self.assertEqual(ol.len(),2)
        self.assertEqual(ol.head.value,1)
        self.assertEqual(ol.tail.value,5)    
        
        ol.add(7)
        self.assertEqual(ol.len(),3)
        self.assertEqual(ol.head.value,1)
        self.assertEqual(ol.tail.value,7)  
        self.assertEqual(ol.get_all_val(),[1,5,7])  
        
        ol.add(4)
        self.assertEqual(ol.len(),4)
        self.assertEqual(ol.head.value,1)
        self.assertEqual(ol.tail.value,7)    
        self.assertEqual(ol.get_all_val(),[1,4,5,7])
          
        ol.add(6)
        self.assertEqual(ol.len(),5)
        self.assertEqual(ol.head.value,1)
        self.assertEqual(ol.tail.value,7)    
        self.assertEqual(ol.get_all_val(),[1,4,5,6,7])    
        
    def test_add_desc(self):
        ol = self.OrderedList(False)
        ol.add(5)
        self.assertEqual(ol.len(),1)
        self.assertEqual(ol.head.value,5)
        self.assertEqual(ol.tail.value,5)
        
        ol.add(1)
        self.assertEqual(ol.len(),2)
        self.assertEqual(ol.tail.value,1)
        self.assertEqual(ol.head.value,5)    
        
        ol.add(7)
        self.assertEqual(ol.len(),3)
        self.assertEqual(ol.head.value,7)
        self.assertEqual(ol.tail.value,1)  
        self.assertEqual(ol.get_all_val(),[7,5,1])  
        
        ol.add(4)
        self.assertEqual(ol.len(),4)
        self.assertEqual(ol.head.value,7)
        self.assertEqual(ol.tail.value,1)    
        self.assertEqual(ol.get_all_val(),[7,5,4,1])
          
        ol.add(6)
        self.assertEqual(ol.len(),5)
        self.assertEqual(ol.head.value,7)
        self.assertEqual(ol.tail.value,1)    
        self.assertEqual(ol.get_all_val(),[7,6,5,4,1])        
        
    def test_delete_asc(self):
        ol = self.OrderedList.from_list([1,2,4], True)
        self.assertEqual(ol.get_all_val(),[1,2,4]) 
        
        ol.delete(1)
        self.assertEqual(ol.get_all_val(),[2,4]) 
        
        ol.delete(4)
        self.assertEqual(ol.get_all_val(),[2]) 
        
        ol.delete(2)
        self.assertEqual(ol.get_all_val(),[])       
        
        
        ol = self.OrderedList.from_list([1,2,3,3,4,5], True)
        ol.delete(3)
        self.assertEqual(ol.get_all_val(),[1,2,3,4,5]) 
        
        ol = self.OrderedList.from_list([1,2,3,3,4,5], False)
        self.assertEqual(ol.get_all_val(),[5,4,3,3,2,1])
        test_node = ol.head.next.next.next
        ol.delete(3)
        self.assertEqual(ol.head.next.next,test_node)    
        
    def test_delete_desc(self):
        ol = self.OrderedList.from_list([1,2,4], False)
        self.assertEqual(ol.get_all_val(),[4,2,1]) 
        
        ol.delete(1)
        self.assertEqual(ol.get_all_val(),[4,2]) 
        
        ol.delete(4)
        self.assertEqual(ol.get_all_val(),[2]) 
        
        ol = self.OrderedList.from_list([1,2,3,3,4,5], False)
        self.assertEqual(ol.get_all_val(),[5,4,3,3,2,1])
        ol.delete(3)
        self.assertEqual(ol.get_all_val(),[5,4,3,2,1])
        
        ol = self.OrderedList.from_list([1,2,3,3,4,5], False)
        self.assertEqual(ol.get_all_val(),[5,4,3,3,2,1])
        test_node = ol.head.next.next.next
        ol.delete(3)
        self.assertEqual(ol.head.next.next,test_node)    
        
  
     
    def test_find_asc(self):
        ol = self.OrderedList(True)
        self.assertEqual(ol.find(6),None)
        ol.add(5)
        self.assertEqual(ol.find(5),ol.head)
        
        ol.add(7)
        self.assertEqual(ol.find(7),ol.tail)
        
        ol.add(6)
        self.assertEqual(ol.find(6),ol.head.next)
        self.assertEqual(ol.find(6),ol.tail.prev) 
        
        ol.clean(True)
        for i in range(7):
            ol.add(i)
            
        self.assertEqual(ol.find(4),ol.head.next.next.next.next)     
            
    def test_find_desc(self):
        ol = self.OrderedList(False)
        self.assertEqual(ol.find(6),None)
        ol.add(5)
        self.assertEqual(ol.find(5),ol.head)
        
        ol.add(7)
        self.assertEqual(ol.find(7),ol.head)
        
        ol.add(6)
        self.assertEqual(ol.find(6),ol.tail.prev)
        self.assertEqual(ol.find(6),ol.head.next) 
        
        ol.clean(False)
        for i in range(7):
            ol.add(i)
            
        self.assertEqual(ol.find(2),ol.head.next.next.next.next)          
   
   

class TestOrderedList_2(TestOrderedList):
   
    OrderedList = task7_2.OrderedList
    
    def test_index_asc(self):
        ol = self.OrderedList(True)
        ol.add(1)
        self.assertEqual(ol.index(ol.head),0)
        
        ol.add(2)
        self.assertEqual(ol.index(ol.tail),1)  
        
        ol.add(3)
        
        self.assertEqual(ol._skip_list.head.down,ol.head)
        self.assertEqual(ol.index(ol.tail),2)     
        
        ol.add(4)
        self.assertEqual(ol.index(ol.tail.prev),2) 
        
        ol.add(4)
        self.assertEqual(ol.index(ol.tail),4)        
        
    
    def test_most_frequent_value(self):
        ol = self.OrderedList(True)
        self.assertIsNone(ol.most_frequent_value())
        
        ol.add(4)
        self.assertEqual(ol.most_frequent_value(),4)
        
        ol.add(5)
        ol.add(5)
        self.assertEqual(ol.most_frequent_value(),5)    
        
        ol.add(1)
        ol.add(1)
        ol.add(1)
        self.assertEqual(ol.most_frequent_value(),1)      
              
        
    
    def test_remove_duplicates(self):
        ol = self.OrderedList(True)
        ol.remove_duplicates()
        self.assertEqual(ol.get_all_val(),[])
        
        ol.add(5)
        ol.remove_duplicates()
        self.assertEqual(ol.get_all_val(),[5])
        
        ol.add(5)
        ol.remove_duplicates()
        self.assertEqual(ol.get_all_val(),[5])
        self.assertEqual(ol.len(),1)
        
        
        ol.add(1)
        ol.add(1)
        ol.add(3)
        ol.add(3)
        ol.add(7)
        ol.add(7)       
        ol.remove_duplicates()
        self.assertEqual(ol.get_all_val(),[1,3,5,7])
        self.assertEqual(ol.len(),4)

    def test_merge(self):
        ol1 = self.OrderedList(True)
        ol2 = self.OrderedList(False)
        
        res = self.OrderedList.merge(ol1,ol2,True)
        self.assertEqual(res.get_all_val(),[])
        
        ol1 = self.OrderedList(True)
        ol2 = self.OrderedList(False)
        ol2.add(4)
        
        res = self.OrderedList.merge(ol1,ol2,True)
        self.assertEqual(res.get_all_val(),[4])
        self.assertEqual(res.len(),1)
        
        ol1 = self.OrderedList(True)
        ol1.add(5)
        ol2 = self.OrderedList(False)
        
        res = self.OrderedList.merge(ol1,ol2,False)
        self.assertEqual(res.get_all_val(),[5])                
        self.assertEqual(res.len(),1)
        
    
        ol1 = self.OrderedList(True)
        ol2 = self.OrderedList(False)
        
        for i in range(5):
            ol1.add(i)
        for i in range(3,7):
            ol2.add(i)  
              
        res = self.OrderedList.merge(ol1,ol2,False)
        self.assertEqual(res.get_all_val(),[6,5,4,4,3,3,2,1,0])                
        self.assertEqual(res.len(),9)   
     
    def test_contains_subsequence(self):
        ol = self.OrderedList(True)
        subsequence = self.OrderedList(True) 
        
        self.assertTrue(ol.contains_subsequence(subsequence))
        
        subsequence.add(5)
        self.assertFalse(ol.contains_subsequence(subsequence))
        
        ol.add(5)
        self.assertTrue(ol.contains_subsequence(subsequence))
        
        subsequence.add(4)
        self.assertFalse(ol.contains_subsequence(subsequence))
        
        
        ol.add(1)
        ol.add(4)
        
        self.assertEqual(ol.get_all_val(),[1,4,5]) 
        self.assertEqual(subsequence.get_all_val(),[4,5]) 
        self.assertTrue(ol.contains_subsequence(subsequence))     
        
        ol.add(7)
        self.assertEqual(ol.get_all_val(),[1,4,5,7]) 
        self.assertEqual(subsequence.get_all_val(),[4,5]) 
        self.assertTrue(ol.contains_subsequence(subsequence))    
        
    def test_contains_subsequence_diffrent_asc(self):
        ol = self.OrderedList(False)
        subsequence = self.OrderedList(True) 
        
        self.assertTrue(ol.contains_subsequence(subsequence))
        
        subsequence.add(5)
        self.assertFalse(ol.contains_subsequence(subsequence))
        
        ol.add(5)
        self.assertTrue(ol.contains_subsequence(subsequence))
        
        subsequence.add(4)
        self.assertFalse(ol.contains_subsequence(subsequence))
        
        ol.add(1)
        ol.add(4)
        
        self.assertEqual(ol.get_all_val(),[5,4,1]) 
        self.assertEqual(subsequence.get_all_val(),[4,5]) 
        self.assertFalse(ol.contains_subsequence(subsequence))     
        
        ol.add(7)
        self.assertEqual(ol.get_all_val(),[7,5,4,1]) 
        self.assertEqual(subsequence.get_all_val(),[4,5]) 
        self.assertFalse(ol.contains_subsequence(subsequence))             
        
        
class TestOrderedStringList(unittest.TestCase):
    def test_add_asc(self):
        osl = OrderedStringList(True)
        self.assertEqual(osl.compare("as","bs"), -1)
        
        osl = OrderedStringList(True)
        self.assertEqual(osl.compare("as"," bs"), -1)
                   
              
        
            
if __name__ == '__main__':
    unittest.main()
   