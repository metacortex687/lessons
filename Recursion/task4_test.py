import unittest
from task4 import is_polindrom


class TestTask4(unittest.TestCase):
    def test_is_polindrom(self):

        self.assertTrue(is_polindrom(""))

        self.assertTrue(is_polindrom("a"))   

        self.assertFalse(is_polindrom("ab")) 

        self.assertTrue(is_polindrom("aba"))  

        self.assertTrue(is_polindrom("abfghhgfba")) 
        
        self.assertFalse(is_polindrom("ablghhgfba")) 








        
        
if __name__ == '__main__':
    unittest.main()
   
   