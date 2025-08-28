import unittest
from task1 import pow_rec


class TestTask1(unittest.TestCase):
    def test_pow(self):
        self.assertEqual(pow_rec(0,0),1)

        self.assertEqual(pow_rec(1,10),1)

        self.assertEqual(pow_rec(3,3),27)
        self.assertEqual(pow_rec(2,4),16)
        
        
if __name__ == '__main__':
    unittest.main()
   
   