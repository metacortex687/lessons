import unittest
from task7 import second_max


class TestTask7(unittest.TestCase):
    def test_second_max(self):

        with self.assertRaises(ValueError):
            second_max([])

        with self.assertRaises(ValueError):
            second_max([1])

        self.assertEqual(second_max([1,2]),1)

        self.assertEqual(second_max([2,2]),2)

        self.assertEqual(second_max([2,2,2]),2)

        self.assertEqual(second_max([2,5,4,3,5]),5)

        self.assertEqual(second_max([5,5,4,3,2]),5)

        self.assertEqual(second_max([2,3,5,4]),4)

        
        
if __name__ == '__main__':
    unittest.main()
   
   