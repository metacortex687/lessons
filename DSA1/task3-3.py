import unittest
from task3 import DynArray

import importlib.util
import sys
spec = importlib.util.spec_from_file_location("task3_2", "./DSA1/task3-2.py")
task3_2 = importlib.util.module_from_spec(spec)
sys.modules["task3_2"] = task3_2
spec.loader.exec_module(task3_2)
MultiArray = task3_2.MultiArray


class TestDynArray(unittest.TestCase):
    def test_init(self):
        d = DynArray()
        self.assertEqual(d.count,0)
        self.assertEqual(d.capacity,16)

        
    def test_insert(self):
        d = DynArray()
        
        d.insert(0,1)
        self.assertEqual(d.count,1)
        self.assertEqual(d.capacity,16)
        self.assertEqual(d[0],1)
        
        with self.assertRaises(IndexError):
            d.insert(5,4)
          
        with self.assertRaises(IndexError):
            d.insert(-1,4)  
            
            
        d.append(2)
        d.append(3)
        d.append(4)
        
        self.assertEqual(d[2],3)
        d.insert(2,30)
        self.assertEqual(d[2],30)
        self.assertEqual(d[3],3)
       
    def test_delete(self):
        d = DynArray()
        d.append(1)
        d.append(2)
        d.append(3)
        d.append(4)
        
        self.assertEqual(d[1],2)
        self.assertEqual(d.count,4)
        self.assertEqual(d.capacity,16)
        d.delete(1)
        self.assertEqual(d[1],3)
        self.assertEqual(d[2],4)
        self.assertEqual(d.count,3)
        self.assertEqual(d.capacity,16)
          
        with self.assertRaises(IndexError):
            d.delete(-1)
          
        with self.assertRaises(IndexError):
            d.delete(3)  
            
        d.delete(1) 
        self.assertEqual(d.count,2)
        self.assertEqual(d.capacity,16)
      
    def test_capacity(self):
        d = DynArray()
        self.assertEqual(d.count,0)
        self.assertEqual(d.capacity,16)
        
        for i in range(0,16):
            d.insert(i,i+1)
            
        self.assertEqual(d.count,16)
        self.assertEqual(d.capacity,16)      
        
        d.insert(16,17)
        self.assertEqual(d.count,17)
        self.assertEqual(d.capacity,32)  
        
        d.delete(0)
        self.assertEqual(d.count,16)
        self.assertEqual(d.capacity,32)  
        
        d.delete(0)      
        self.assertEqual(d.count,15)
        self.assertEqual(d.capacity,21)  
        
        for _ in range(8):
            d.delete(1)
            
        self.assertEqual(d.count,7)
        self.assertEqual(d.capacity,16)          
            

class  TestMultiArray(unittest.TestCase):
    def test_init(self):
        arr = MultiArray(1,1, default = 0)
        self.assertEqual(arr.shape,[1,1])
        self.assertEqual(arr[0,0],0)
 
         
    def test_set_get(self):
        
        arr = MultiArray(1,1, default = 0)
        arr[0,0] = 10
        self.assertEqual(arr[0,0],10)
        
        arr = MultiArray(3,4, 5, default = 0)   
        arr[2,1,3] = 7
              
        for i1 in range(arr.shape[0]):
            for i2 in range(arr.shape[1]):
                for i3 in range(arr.shape[2]):
                    if (i1, i2, i3) == (2, 1, 3):
                        self.assertEqual(arr[i1,i2,i3],7)
                    else:
                        self.assertEqual(arr[i1,i2,i3],0)
      
      
    def test_reshape(self):
        arr = MultiArray(1,1, default = 0) 
        arr[0,0] = 5
        arr.resize(2,2)
        self.assertEqual(arr[0,0],5)
        
        arr[1,0] = 5
        arr.resize(1,1)
        arr.resize(3,3)
        self.assertEqual(arr[0,0],5)
        self.assertEqual(arr[1,0],0)
        
        arr = MultiArray(3,4, 7, default = 0) 
        
        with self.assertRaises(IndexError):
            arr.resize(1,1,1, 1)
            
 
        arr[2,1,3] = 12
        arr.resize(4,2,40)
        
        with self.assertRaises(IndexError):
            t = arr[3,3,4]
            
        with self.assertRaises(IndexError):
            arr[3,3,4] = 7
        
        arr[3,1,3] = 15
        arr[3,1,39] = 71
        
        arr.resize(5,3,42)
         
        for i1 in range(arr.shape[0]):
            for i2 in range(arr.shape[1]):
                for i3 in range(arr.shape[2]):
                    if (i1, i2, i3) == (2, 1, 3):
                        self.assertEqual(arr[i1,i2,i3],12)
                    elif (i1, i2, i3) == (3, 1, 3):
                        self.assertEqual(arr[i1,i2,i3],15)
                    elif (i1, i2, i3) == (3, 1, 39):
                        self.assertEqual(arr[i1,i2,i3],71)
                    else:
                        self.assertEqual(arr[i1,i2,i3],0)
             
                        
    def test_assert_index(self):
        arr = MultiArray(1,1, default = 0)
        
        with self.assertRaises(IndexError):
            arr[1,0]
        
        with self.assertRaises(IndexError):
            arr[1,1]
        
        arr = MultiArray(3,4, 5, default = 0)
        
        with self.assertRaises(IndexError):
            arr[3,0,0]  
            
        with self.assertRaises(IndexError):
            arr[0,6,0] 
            
        with self.assertRaises(IndexError):
            arr[2,1,8]    
            
        with self.assertRaises(IndexError):
            arr[0,0,0,0]             
                 
        with self.assertRaises(IndexError):
            arr[0,0]  
                       
 
    
if __name__ == '__main__':
    unittest.main()
        
        