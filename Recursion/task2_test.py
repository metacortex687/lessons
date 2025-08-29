import unittest
from task2 import sum_digits


class TestTask2(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(7), 7)

        self.assertEqual(sum_digits(245354), 23)

        with self.assertRaises(ValueError):
            sum_digits(-1)
        
        
if __name__ == '__main__':
    unittest.main()
   
   