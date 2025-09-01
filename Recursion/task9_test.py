import unittest
from task9 import generate_balanced_parentheses


class TestTask9(unittest.TestCase):

    def test_second_max(self):
        self.assertCountEqual(generate_balanced_parentheses(1),["()"])


        self.assertCountEqual(generate_balanced_parentheses(2),["()()","(())"])

        self.assertCountEqual(generate_balanced_parentheses(3),["(()())", "((()))", "()(())", "(())()", "()()()"])

        result = generate_balanced_parentheses(4)
        expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())",
          "(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
        #self._print_dif(result,expected)
        self.assertCountEqual(result,expected)


    def _print_dif(self,a,b):
        sa, sb = set(a), set(b)
        only_in_a = sa - sb
        only_in_b = sb - sa

        print("------")
        if only_in_a:
            print("1:", sorted(only_in_a))
        if only_in_b:
            print("2:", sorted(only_in_b))
        if not only_in_a and not only_in_b:
            print("=======")

        print("------")

    
        






   

        
        
if __name__ == '__main__':
    unittest.main()
   
   