import unittest
import random

#run tests: 
# python ./DSA2/task4-3.py

class TestTask5(unittest.TestCase):
    from task5 import GenerateBBSTArray
    GenerateBBSTArray = staticmethod(GenerateBBSTArray)
    from task4 import aBST

    def _depth(self, count_elements):
        depth = 0
        while True:
            if pow(2,depth+1)-1 >= count_elements:
                return depth
            depth += 1


    def test_depth(self):
        self.assertEqual(0,self._depth(1))
        self.assertEqual(1,self._depth(2))
        self.assertEqual(3,self._depth(15))
        self.assertEqual(3,self._depth(13))



    def test_GenerateBBSTArray(self):
        self.assertEqual([],self.GenerateBBSTArray([]))

        self.assertEqual([1],self.GenerateBBSTArray([1]))

        keys = [1,2]
        self.assertEqual([2,1,None],self.GenerateBBSTArray(keys))

        keys = [1,3,2]
        self.assertEqual([2,1,3],self.GenerateBBSTArray(keys))

        keys = [8,4,12]
        self.assertEqual([8,4,12],self.GenerateBBSTArray(keys))

        keys = [2, 4, 6, 8, 10, 12, 14]
        self.assertEqual([8,4,12,2,6,10,14],self.GenerateBBSTArray(keys))

        keys = [1,2,3,4]
        result = self.GenerateBBSTArray(keys)
        self.assertEqual([3,2,4,1,None,None,None],result)

        keys = [2, 4, 6, 8, 10, 12]
        result = self.GenerateBBSTArray(keys)
        self.assertEqual([8,4,12,2,6,10,None],result)

        keys = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        self.assertEqual(keys,self.GenerateBBSTArray(keys))


    def test_random_GenerateBBSTArray(self):
        

        arr= list(range(1,101))
        random.seed(42)
        random.shuffle(arr)
        result = self.GenerateBBSTArray(arr)
        self.assertEqual(sorted(arr),sorted([key for key in result if key is not None]))
        










