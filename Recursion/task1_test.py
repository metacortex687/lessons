import unittest
from task1 import pow
#python ./DSA1/task3-3.py

class TestTask1(unittest.TestCase):
    def test_pow(self):
        self.assertEqual(pow(0,0),1)

        self.assertEqual(pow(1,10),1)

        self.assertEqual(pow(3,3),27)
        self.assertEqual(pow(2,4),16)
        
        
if __name__ == '__main__':
    unittest.main()
   