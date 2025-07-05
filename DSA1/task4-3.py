import unittest
from task4 import Stack

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task4_2", "./DSA1/task4-2.py")
task4_2 = importlib.util.module_from_spec(spec)
sys.modules["task4_2"] = task4_2
spec.loader.exec_module(task4_2)
bracket_control = task4_2.bracket_control
NumberStack = task4_2.NumberStack
stack_calculate = task4_2.stack_calculate
string_expr_to_stack = task4_2.string_expr_to_stack


class TestStack(unittest.TestCase):
    def test_stack(self):
        
        s = Stack()
        
        self.assertEqual(s.peek(), None)
        self.assertEqual(s.pop(), None)
        self.assertEqual(s.size(),0)
        
        s.push(1)
        s.push('a')
        self.assertEqual(s.size(),2)
        
        self.assertEqual(s.peek(), 'a')
        self.assertEqual(s.pop(), 'a')
        self.assertEqual(s.size(), 1)
        
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.size(), 0)   
        
        self.assertEqual(s.peek(), None)
        self.assertEqual(s.pop(), None)
        self.assertEqual(s.size(),0)
             
  

 
class TestFunctions(unittest.TestCase):
    
    def test_bracket_control(self):
        brackets = ""
        self.assertEqual(bracket_control(brackets),True)
        
        brackets = "()"
        self.assertEqual(bracket_control(brackets),True)
        
        brackets = "("
        self.assertEqual(bracket_control(brackets),False)
        
        brackets = ")"
        self.assertEqual(bracket_control(brackets),False)
        
        brackets = ")("
        self.assertEqual(bracket_control(brackets),False)
        
        brackets = "(()())"
        self.assertEqual(bracket_control(brackets),True)
        
        brackets = "(()))("
        self.assertEqual(bracket_control(brackets),False)
        
        brackets = "((()))))(()"
        self.assertEqual(bracket_control(brackets),False)
     
     
    def test_multy_bracket_control(self):
        brackets = ""
        self.assertEqual(bracket_control(brackets),True)
        
        brackets = "({}[])"
        self.assertEqual(bracket_control(brackets),True)
        
        brackets = "({[}])"
        self.assertEqual(bracket_control(brackets),False)
      
      
    def test_stack_calculate(self):
         
        s = string_expr_to_stack("4 5 + =")
        self.assertEqual(stack_calculate(s),9)
        
        s = string_expr_to_stack("42 5 * = ")
        self.assertEqual(stack_calculate(s),210)  
        
        s = string_expr_to_stack("8 2 + 5 * 9 + =")
        self.assertEqual(stack_calculate(s),59)  
        
        
        s = string_expr_to_stack("4 5 + ")
        self.assertIsNone(stack_calculate(s)) 
    
 
class TestNumberStack(unittest.TestCase):
    def test_average(self):
        s = NumberStack()
        
        self.assertIsNone(s.average())
        
        s.push(5)
        
        self.assertEqual(s.average(),5.)
        
        s.push(2)
        
        self.assertEqual(s.average(),3.5)
        
        s.push(2)
        
        self.assertEqual(s.average(),3)
        
        s.peek()
        self.assertEqual(s.average(),3)
        
        
        s.pop()
        self.assertEqual(s.average(),3.5)
        
    def test_min(self):
        s = NumberStack()
        self.assertIsNone(s.min())
        
        s.push(5)
        self.assertEqual(s.min(),5)
        self.assertEqual(s.peek(),5)
        
        s.push(7)
        self.assertEqual(s.min(),5)
        self.assertEqual(s.peek(),7)
        
        s.push(1)
        self.assertEqual(s.min(),1)
        self.assertEqual(s.peek(),1)
        
        s.pop()
        self.assertEqual(s.min(),5)
        self.assertEqual(s.peek(),7)
        
        s.pop()
        self.assertEqual(s.min(),5)
        self.assertEqual(s.peek(),5)
        
        s.pop()
        self.assertIsNone(s.min())
        self.assertIsNone(s.peek()) 
        

               
        
if __name__ == '__main__':
    unittest.main()
   
   
     
        