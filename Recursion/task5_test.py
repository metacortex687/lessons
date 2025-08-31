import unittest
from task5 import print_even_numbers

from unittest.mock import patch, call, MagicMock

class TestTask4(unittest.TestCase):

    def _assert_has_calls(self,data, mock_fun : MagicMock, any_order: bool):
        self.assertEqual(mock_fun.call_count,len(data))

        mock_fun.assert_has_calls([call(v) for v in data], any_order)


    def test_print_even_numbers(self):

        data = []
        with patch('builtins.print') as mock_print:
            print_even_numbers(data)
        self._assert_has_calls([],mock_print,any_order=False)

        data = [1]
        with patch('builtins.print') as mock_print:
            print_even_numbers(data)
        self._assert_has_calls([],mock_print,any_order=False)        

        data = [1,3,5,7]
        with patch('builtins.print') as mock_print:
            print_even_numbers(data)
        self._assert_has_calls([],mock_print,any_order=False)    

        data = [4,8,4,12]
        with patch('builtins.print') as mock_print:
            print_even_numbers(data)
        self._assert_has_calls([4,8,4,12],mock_print,any_order=False)   
        
        data = [1, 2, 3, 4]
        with patch('builtins.print') as mock_print:
            print_even_numbers(data)
        self._assert_has_calls([2,4],mock_print,any_order=False)


        














        
        
if __name__ == '__main__':
    unittest.main()
   
   