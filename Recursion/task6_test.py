import unittest
from task6 import print_even_index_numbers

from unittest.mock import patch, call, MagicMock

class TestTask6(unittest.TestCase):

    def _assert_has_calls(self,data, mock_fun : MagicMock, any_order: bool):
        self.assertEqual(mock_fun.call_count,len(data))
        mock_fun.assert_has_calls([call(v) for v in data], any_order)


    def test_is_polindrom(self):

        data = []
        with patch('builtins.print') as mock_print:
            print_even_index_numbers(data)
        self._assert_has_calls([],mock_print,any_order=False)

        data = [1]
        with patch('builtins.print') as mock_print:
            print_even_index_numbers(data)
        self._assert_has_calls([1],mock_print,any_order=False)

        data = [1,2,3,4,5]
        with patch('builtins.print') as mock_print:
            print_even_index_numbers(data)
        self._assert_has_calls([1,3,5],mock_print,any_order=False)
        














        
        
if __name__ == '__main__':
    unittest.main()
   
   