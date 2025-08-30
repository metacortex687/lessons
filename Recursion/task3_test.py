import unittest
from task3 import len_list


class TestTask3(unittest.TestCase):
    def test_len_list(self):

        self.assertEqual(len_list([]),0)

        self.assertEqual(len_list(['a']),1)
        
        self.assertEqual(len_list(['a', 1, 5, 6, 7, "b"]),6)



        
        
if __name__ == '__main__':
    unittest.main()
   
   