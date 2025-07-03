import unittest
import task2


import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task2_2", "./DSA1/task2-2.py")
task2_2 = importlib.util.module_from_spec(spec)
sys.modules["task2_2"] = task2_2
spec.loader.exec_module(task2_2)


    

class TestLinkedList2(unittest.TestCase):
    
    Node = task2.Node
    LinkedList2 = task2.LinkedList2
    
    def is_good_linked_list(self, s_list: LinkedList2):
        r_l = s_list.to_list_values(False)
        r_l.reverse()
        self.assertEqual(s_list.to_list_values(), r_l)
    
    def test_len(self):

        s_list  = self.LinkedList2()

        self.assertEqual(s_list.len(),0)

        s_list.add_in_tail(self.Node(34))
        self.assertEqual(s_list.len(),1)  
        
        self.is_good_linked_list(s_list)         
        
        s_list.add_in_tail(self.Node(15))

        self.assertEqual(s_list.len(),2)  
        self.is_good_linked_list(s_list)  
        
        
    def test_find_all(self):
        s_list  = self.LinkedList2()

        result = s_list.find_all(5)
        self.assertEqual(result, [])
        self.is_good_linked_list(s_list) 

        s_list.add_in_tail(self.Node(34))
        result = s_list.find_all(5)
        self.assertEqual(result, [])
        self.is_good_linked_list(s_list)      

        
        s_list.add_in_tail(self.Node(5))
        result = s_list.find_all(5)
        self.assertEqual(len(result), 1) 
        self.assertEqual(result[0].value, 5)
        self.is_good_linked_list(s_list)  

        s_list.add_in_tail(self.Node(4))
        s_list.add_in_tail(self.Node(5))
        result = s_list.find_all(5)
        self.assertEqual(len(result), 2) 
        self.assertEqual(result[0].value, 5) 
        self.assertEqual(result[1].value, 5)
        self.is_good_linked_list(s_list)  
        
    def test_to_list_values(self):
        s_list  = self.LinkedList2()  
        self.assertEqual(s_list.to_list_values(), [])  


        s_list.add_in_tail(self.Node(34)) 
        s_list.add_in_tail(self.Node(3))

        self.assertEqual(s_list.to_list_values(), [34, 3])   
        self.assertEqual(s_list.to_list_values(False), [3, 34]) 
        
           

    def test_delete(self):
        s_list  = self.LinkedList2()
        s_list.delete(5)
        self.assertEqual(s_list.len(), 0)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.is_good_linked_list(s_list) 

        s_list.add_in_tail(self.Node(5))
        self.assertEqual(s_list.len(), 1)
        s_list.delete(5)
        self.assertEqual(s_list.len(), 0)  
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.is_good_linked_list(s_list)  

        s_list.add_in_tail(self.Node(34))
        s_list.add_in_tail(self.Node(5))
        s_list.add_in_tail(self.Node(5))
        s_list.delete(5)
        self.assertEqual(s_list.len(), 2)
        self.assertEqual(s_list.head.value,34)
        self.assertEqual(s_list.tail.value,5)
        self.is_good_linked_list(s_list) 
        
    def test_delete_one_element(self):
        s_list  = self.LinkedList2()
        s_list.add_in_tail(self.Node(4))
        s_list.delete(4)
        self.assertEqual(s_list.len(), 0)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.is_good_linked_list(s_list) 
        
        
    def test_delete_from_4_3_4_delete_4(self):
        s_list  = self.LinkedList2()
        s_list.add_in_tail(self.Node(4))
        s_list.add_in_tail(self.Node(3))
        s_list.add_in_tail(self.Node(4))
        s_list.delete(4)
        self.assertEqual(s_list.to_list_values(), [3,4])
        self.assertEqual(s_list.head.value, 3)
        self.assertEqual(s_list.tail.value, 4)
        self.is_good_linked_list(s_list) 
        
    def test_delete_from_3_3_delete_4(self):
        s_list  = self.LinkedList2()
        s_list.add_in_tail(self.Node(3))
        s_list.add_in_tail(self.Node(4))
        s_list.delete(4)
        self.assertEqual(s_list.to_list_values(), [3])  
        self.assertEqual(s_list.head.value, 3)
        self.assertEqual(s_list.tail.value, 3)
        self.is_good_linked_list(s_list) 
        
    def test_delete_from_4_delete_4(self):
        s_list  = self.LinkedList2()
        s_list.add_in_tail(self.Node(4))
        s_list.delete(4)
        self.assertEqual(s_list.to_list_values(), [])   
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.is_good_linked_list(s_list) 
        

    def test_delete_from_4_delete_4(self):
        s_list  = self.LinkedList2()
        s_list.add_in_tail(self.Node(4))
        s_list.delete(4,True)
        self.assertEqual(s_list.to_list_values(), [])   
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.is_good_linked_list(s_list) 
        
    def test_delete_all(self):
        s_list  = self.LinkedList2()
        s_list.delete(5,True)
        self.assertEqual(s_list.len(), 0)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.is_good_linked_list(s_list) 

        s_list.add_in_tail(self.Node(5))
        self.assertEqual(s_list.len(), 1)
        s_list.delete(5,True)
        self.assertEqual(s_list.len(), 0)   
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail) 
        self.is_good_linked_list(s_list)    


        s_list.add_in_tail(self.Node(34))
        s_list.add_in_tail(self.Node(5))
        s_list.add_in_tail(self.Node(5))
        s_list.delete(5,True)
        self.is_good_linked_list(s_list) 

        self.assertEqual(s_list.len(), 1)
        self.assertEqual(s_list.head.value, 34)
        self.assertEqual(s_list.tail.value, 34)
        self.is_good_linked_list(s_list) 
        
    def test_clean(self):
        s_list  = self.LinkedList2()   
        s_list.add_in_tail(self.Node(34))
        s_list.add_in_tail(self.Node(5))
        s_list.add_in_tail(self.Node(5))
        s_list.clean()

        self.assertEqual(s_list.len(), 0)
        self.assertIsNone(s_list.head)
        self.assertIsNone(s_list.tail)
        self.is_good_linked_list(s_list)   
        
    def test_insert_in_empty_none(self):
        s_list  = self.LinkedList2()  
        s_list.insert(None, self.Node(3))

        self.assertEqual(s_list.len(), 1)
        self.assertEqual(s_list.to_list_values(), [3])
        self.assertIsNotNone(s_list.head)
        self.assertIsNotNone(s_list.tail)         
        self.assertEqual(s_list.head.value, 3)
        self.assertEqual(s_list.tail.value, 3) 
        self.is_good_linked_list(s_list)   
        
    def test_insert_in_tail(self):
        s_list  = self.LinkedList2()  
        s_list.add_in_tail(self.Node(12)) 
        n_34 = self.Node(34)
        s_list.add_in_tail(n_34) 
        s_list.insert(n_34, self.Node(3))
        

        self.assertEqual(s_list.len(), 3)
        self.assertEqual(s_list.to_list_values(), [12, 34, 3])   
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 3)   
        self.is_good_linked_list(s_list) 


    def test_insert_after_none(self):
        s_list  = self.LinkedList2()  
        s_list.add_in_tail(self.Node(34)) 
        s_list.insert(None, self.Node(3))

        self.assertEqual(s_list.len(), 2)
        self.assertEqual(s_list.to_list_values(), [34, 3])
        self.assertEqual(s_list.head.value, 34)
        self.assertEqual(s_list.tail.value, 3)
        self.is_good_linked_list(s_list)   
        
        s_list.insert(None, self.Node(7))
        self.assertEqual(s_list.len(), 3)
        self.assertEqual(s_list.to_list_values(), [34, 3, 7])
        self.assertEqual(s_list.head.value, 34)
        self.assertEqual(s_list.tail.value, 7)
        self.is_good_linked_list(s_list)  
    
    def test_insert(self):
        s_list  = self.LinkedList2()  
        s_list.add_in_tail(self.Node(1)) 
        s_list.add_in_tail(self.Node(2)) 
        node_3 = self.Node(3)
        s_list.add_in_tail(node_3) 
        s_list.add_in_tail(self.Node(4)) 
        s_list.add_in_tail(self.Node(5)) 

        s_list.insert(node_3, self.Node(7))

        self.assertEqual(s_list.to_list_values(), [1, 2, 3, 7, 4, 5])
        self.assertEqual(s_list.head.value, 1)
        self.assertEqual(s_list.tail.value, 5)
        self.is_good_linked_list(s_list)   
        
    def test_add_in_head(self):
        s_list  = self.LinkedList2()  
        s_list.add_in_tail(self.Node(34)) 
        s_list.add_in_head(self.Node(12))

        self.assertEqual(s_list.len(), 2)
        self.assertEqual(s_list.to_list_values(), [12, 34])
        self.assertEqual(s_list.head.value, 12)
        self.assertEqual(s_list.tail.value, 34)
        self.is_good_linked_list(s_list)  
        
    def test_find(self):
        s_list  = self.LinkedList2()  
        s_list.add_in_tail(self.Node(1)) 
        
        result = s_list.find(2)
        
        self.assertIsNone(result)
        
        node_2 = self.Node(2)
        s_list.add_in_tail(node_2)
        s_list.add_in_tail(self.Node(3))
        
        result = s_list.find(2)
        
        self.assertEqual(result,node_2)
        
        s_list.add_in_tail(self.Node(2))
        self.assertEqual(result,node_2)
        
    

class TestLinkedList2_dummy(TestLinkedList2):
    
    Node = task2_2.Node
    LinkedList2 = task2_2.LinkedList2
    
    def is_good_linked_list(self, s_list: LinkedList2):
        super().is_good_linked_list(s_list)
        self.assertFalse(s_list.is_loop())
   
    def test_sort(self):
        s_list  = self.LinkedList2()
        
        s_list.add_in_tail(self.Node(4))
        s_list.sort()
        self.assertEqual(s_list.to_list_values(),[4])
        self.is_good_linked_list(s_list)
        
        s_list.add_in_tail(self.Node(2))
        s_list.sort()
        self.assertEqual(s_list.to_list_values(),[2,4])
        self.is_good_linked_list(s_list)
        
        s_list.add_in_tail(self.Node(2))
        s_list.add_in_tail(self.Node(7))
        s_list.add_in_tail(self.Node(1))
        
        self.assertEqual(s_list.to_list_values(),[2,4,2,7,1])
        self.is_good_linked_list(s_list)
        
        s_list.sort()
        
        self.assertEqual(s_list.to_list_values(),[1,2,2,4,7])
        self.is_good_linked_list(s_list)
        
    
    def test_reverse(self):
        s_list  = self.LinkedList2()
        s_list.add_in_tail(self.Node(1))
        s_list.add_in_tail(self.Node(2))
        s_list.add_in_tail(self.Node(3))
        s_list.add_in_tail(self.Node(4))
        s_list.add_in_tail(self.Node(5))
        s_list.add_in_tail(self.Node(6))
        s_list.add_in_tail(self.Node(7))
        
        s_list.reverse()
        self.assertEqual(s_list.to_list_values(),[7,6,5,4,3,2,1])
      
    def test_copy(self):
        s_list  = self.LinkedList2()
        deep_copy = s_list.copy()
        self.assertNotEqual(s_list,deep_copy)
        self.assertIsNone(deep_copy.head)
        self.assertIsNone(deep_copy.tail)
        self.assertEqual(deep_copy.to_list_values(),[])
        
        s_list.add_in_tail(self.Node(1))
        
        deep_copy = s_list.copy()
        self.assertNotEqual(s_list,deep_copy)
        self.assertIsNotNone(deep_copy.head)
        self.assertIsNotNone(deep_copy.tail)
        self.assertEqual(deep_copy.to_list_values(),[1])    
         
        
        s_list.add_in_tail(self.Node(1))
        s_list.add_in_tail(self.Node(2))
        s_list.add_in_tail(self.Node(3))
        
        copy = s_list.copy()
        
        self.assertEqual(copy.to_list_values(),[1,1,2,3])
        self.assertNotEqual(s_list,copy)
        self.assertIsNotNone(copy.head)
        self.assertIsNotNone(copy.tail)
        self.assertNotEqual(s_list.head,copy.head)
        self.assertNotEqual(s_list.tail,copy.tail)
        
        
    def test_reverse_after_reverse(self):
        
        s_list  = self.LinkedList2()
        s_list.reverse()
        self.is_good_linked_list(s_list)
        
        s_list.add_in_tail(self.Node(1))
        s_list.reverse()
        self.assertEqual(s_list.to_list_values(),[1])
        self.is_good_linked_list(s_list)
        
        
        s_list.add_in_tail(self.Node(2))
        s_list.reverse()
        self.assertEqual(s_list.to_list_values(),[2,1])
        self.is_good_linked_list(s_list)
        
        
        s_list.add_in_tail(self.Node(7))
        s_list.add_in_tail(self.Node(8))
        s_list.reverse()
        self.assertEqual(s_list.to_list_values(),[8,7,1,2])
        self.is_good_linked_list(s_list)
        
    def test_is_loop_left(self):
        s_list  = self.LinkedList2()
        self.assertFalse(s_list.is_loop())
        
        node_1 = self.Node(1)
        node_2 = self.Node(2)
        node_3 = self.Node(3)
        s_list.add_in_tail(node_1)
        s_list.add_in_tail(node_2)
        s_list.add_in_tail(node_3)
        
        self.assertFalse(s_list.is_loop())
        
        node_2.next = node_1
        self.assertTrue(s_list.is_loop())
    
        
    def test_is_loop_right(self):
        s_list  = self.LinkedList2()
        self.assertFalse(s_list.is_loop())
        
        node_1 = self.Node(1)
        node_2 = self.Node(2)
        node_3 = self.Node(3)
        s_list.add_in_tail(node_1)
        s_list.add_in_tail(node_2)
        s_list.add_in_tail(node_3)
        
        self.assertFalse(s_list.is_loop())
        
        node_1.prev = node_1
        self.assertTrue(s_list.is_loop())
   
   
    def test_merge_into_new_sorted(self):
        s_list1  = self.LinkedList2()
        s_list2  = self.LinkedList2()
        
        s_list = self.LinkedList2.merge_into_new_sorted(s_list1, s_list2)
        self.assertEqual(s_list.to_list_values(),[])
        self.is_good_linked_list(s_list)
        
        s_list1.add_in_tail(self.Node(5))
        s_list2.add_in_tail(self.Node(1))
        
        s_list = self.LinkedList2.merge_into_new_sorted(s_list1, s_list2)
        self.assertEqual(s_list.to_list_values(),[1,5])
        self.is_good_linked_list(s_list)     
         

        s_list1.add_in_tail(self.Node(1))
        s_list1.add_in_tail(self.Node(2))
        s_list1.add_in_tail(self.Node(3))
        self.assertEqual(s_list1.to_list_values(),[5,1,2,3])
        
        s_list2.add_in_tail(self.Node(7))
        s_list2.add_in_tail(self.Node(8))
        self.assertEqual(s_list2.to_list_values(),[1,7,8])
        
        
        
        s_list = self.LinkedList2.merge_into_new_sorted(s_list1, s_list2)
        
        self.assertEqual(s_list.to_list_values(),[1,1,2,3,5,7,8])
        self.is_good_linked_list(s_list)         
     
   

if __name__ == '__main__':
    unittest.main()
    
    