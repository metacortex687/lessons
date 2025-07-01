

import unittest
from task1 import Node, LinkedList

import importlib.util
import sys

spec = importlib.util.spec_from_file_location("task1_2", "./task1-2.py")
task1_2 = importlib.util.module_from_spec(spec)
sys.modules["task1_2"] = task1_2
spec.loader.exec_module(task1_2)


class TestLinkedList(unittest.TestCase):

    def test_len(self):

        s_list  = LinkedList()

        self.assertEqual(s_list.len(),0)

        s_list.add_in_tail(Node(34))
        s_list.add_in_tail(Node(15))

        self.assertEqual(s_list.len(),2)

    def test_find_all(self):
        s_list  = LinkedList()

        result = s_list.find_all(5)
        self.assertEqual(result, [])

        s_list.add_in_tail(Node(34))
        result = s_list.find_all(5)
        self.assertEqual(result, [])     

        
        s_list.add_in_tail(Node(5))
        result = s_list.find_all(5)
        self.assertEqual(len(result), 1) 
        self.assertEqual(result[0].value, 5) 

        s_list.add_in_tail(Node(4))
        s_list.add_in_tail(Node(5))
        result = s_list.find_all(5)
        self.assertEqual(len(result), 2) 
        self.assertEqual(result[0].value, 5) 
        self.assertEqual(result[1].value, 5) 

    def test_delete(self):
        s_list  = LinkedList()
        s_list.delete(5)
        self.assertEqual(s_list.len(), 0)

        s_list.add_in_tail(Node(5))
        self.assertEqual(s_list.len(), 1)
        s_list.delete(5)
        self.assertEqual(s_list.len(), 0)   

        s_list.add_in_tail(Node(34))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.delete(5)
        self.assertEqual(s_list.len(), 2)



    def test_delete_all(self):
        s_list  = LinkedList()
        s_list.delete(5,True)
        self.assertEqual(s_list.len(), 0)

        s_list.add_in_tail(Node(5))
        self.assertEqual(s_list.len(), 1)
        s_list.delete(5,True)
        self.assertEqual(s_list.len(), 0)       


        s_list.add_in_tail(Node(34))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.delete(5,True)

        self.assertEqual(s_list.len(), 1)


    def test_clean(self):
        s_list  = LinkedList()   
        s_list.add_in_tail(Node(34))
        s_list.add_in_tail(Node(5))
        s_list.add_in_tail(Node(5))
        s_list.clean()

        self.assertEqual(s_list.len(), 0)

    
    def test_to_list_values(self):
        s_list  = LinkedList()  
        self.assertEqual(s_list.to_list_values(), [])  


        s_list.add_in_tail(Node(34)) 
        s_list.add_in_tail(Node(3))

        self.assertEqual(s_list.to_list_values(), [34, 3])       


    def test_insert_after_none(self):
        s_list  = LinkedList()  
        s_list.add_in_tail(Node(34)) 
        s_list.insert(None, Node(3))

        self.assertEqual(s_list.len(), 2)
        self.assertEqual(s_list.to_list_values(), [3, 34])



    def test_insert(self):
        s_list  = LinkedList()  
        s_list.add_in_tail(Node(1)) 
        s_list.add_in_tail(Node(2)) 
        node_3 = Node(3)
        s_list.add_in_tail(node_3) 
        s_list.add_in_tail(Node(4)) 
        s_list.add_in_tail(Node(5)) 

        s_list.insert(node_3, Node(7))

        self.assertEqual(s_list.to_list_values(), [1, 2, 3, 7, 4, 5])
        
        
    def test_sum_linked_list_difrent_len(self):
            s_list_1  = LinkedList()  
            s_list_1.add_in_tail(Node(1)) 
            s_list_1.add_in_tail(Node(2))   
            
            s_list_2  = LinkedList()  
            s_list_2.add_in_tail(Node(3)) 
            
            
            
            result = task1_2.sum_linked_list(s_list_1,s_list_2)
            
            self.assertIsNone(result, None)
            
    def test_sum_linked_list_difrent_len(self):
        s_list_1  = LinkedList()  
        s_list_1.add_in_tail(Node(1)) 
        s_list_1.add_in_tail(Node(2))   
            
        s_list_2  = LinkedList()  
        s_list_2.add_in_tail(Node(3)) 
        s_list_2.add_in_tail(Node(5)) 
             
        result = task1_2.sum_linked_list(s_list_1,s_list_2)
         
        self.assertIsNotNone(result)    
        self.assertEqual(result.to_list_values(), [4,7])
            
            
            
            
 

if __name__ == '__main__':
    unittest.main()