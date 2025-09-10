import unittest
import random

#run tests: 
# python ./DSA2/task5-3.py

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
        self.assertEqual([2,1],self.GenerateBBSTArray(keys))

        keys = [1,3,2]
        self.assertEqual([2,1,3],self.GenerateBBSTArray(keys))

        keys = [8,4,12]
        self.assertEqual([8,4,12],self.GenerateBBSTArray(keys))

        keys = [2, 4, 6, 8, 10, 12, 14]
        self.assertEqual([8,4,12,2,6,10,14],self.GenerateBBSTArray(keys))

        keys = [1,2,3,4]
        result = self.GenerateBBSTArray(keys)
        self.assertEqual([3,2,4,1],result)

        keys = [2, 4, 6, 8, 10, 12]
        result = self.GenerateBBSTArray(keys)
        self.assertEqual([8,4,12,2,6,10],result)

        keys = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        self.assertEqual(keys,self.GenerateBBSTArray(keys))

        keys = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual([8, 5, 11, 4, 7, 10, 13, 2, 6,  9, 12],[v for v in self.GenerateBBSTArray(keys) if v is not None])

    def test_random_GenerateBBSTArray(self):
        

        arr= list(range(1,101))
        random.seed(42)
        random.shuffle(arr)
        result = self.GenerateBBSTArray(arr)
        self.assertEqual(sorted(arr),sorted([key for key in result if key is not None]))
        

class TestTask5_2(unittest.TestCase):
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("task5-2", "./DSA2/task5-2.py")
    task5_2 = importlib.util.module_from_spec(spec)
    sys.modules["task5-2"] = task5_2
    spec.loader.exec_module(task5_2)
    BBST = task5_2.BBST

    def _create_test_abst(self) -> BBST:
        return self.BBST([8,4,12,2,6,10,14,1,3,5,7,9,11,13,15])

    def test_init(self):
        abst = self.BBST([])
        self.assertEqual(0,len(abst.Tree))

        abst = self.BBST([1,2,3])
        self.assertEqual(3,len(abst.Tree))
        self.assertEqual([2,1,3],abst.Tree)

    def test_AddKeyValue(self):

        abst = self.BBST([])
        self.assertEqual(0,abst.AddKey(50))
        self.assertEqual(0,abst.AddKey(50))
        self.assertEqual(1,abst.AddKey(25))


        abst = self.BBST([])
        self.assertEqual(0,abst.AddKey(50))
        self.assertEqual(50,abst.Tree[0])

        self.assertEqual(0,abst.AddKey(50))

        self.assertEqual(1,abst.AddKey(25))
        self.assertEqual(25,abst.Tree[1])
       

        added_elements = [(2,75),(4,37),(5,62),(6,84),(11,55),(14,92)]
        for expected_index, key in added_elements:
            index = abst.AddKey(key)
            self.assertEqual(expected_index,index)

        self.assertIsNotNone(abst.Tree[11])

        self.assertIsNone(abst.Tree[3])
        self.assertIsNone(abst.Tree[7])
        self.assertIsNone(abst.Tree[8])
        self.assertIsNone(abst.Tree[12])
        self.assertIsNone(abst.Tree[13])

    def test_FindKeyIndex(self):
        abst = self.BBST([])
        self.assertEqual(0,abst.FindKeyIndex(10))
        self.assertEqual(0,abst.FindKeyIndex(15))

        abst = self.BBST([])
        abst.AddKey(10)
        self.assertEqual(0,abst.FindKeyIndex(10))
        self.assertEqual(-1,abst.FindKeyIndex(8))
        self.assertEqual(-2,abst.FindKeyIndex(15))

        added_elements = [(0,50),(1,25),(2,75),(4,37),(5,62),(6,84),(11,55),(14,92)]

        abst = self.BBST([])
        for i, key in added_elements: 
            self.assertEqual(-i,abst.FindKeyIndex(key))
            self.assertEqual(i,abst.AddKey(key))

        for expected_index, key in added_elements:
            finded_index = abst.FindKeyIndex(key)
            self.assertEqual(expected_index,finded_index)

        self.assertTrue(abst.FindKeyIndex(3) < 0)
        self.assertTrue(abst.FindKeyIndex(7) < 0)
        self.assertTrue(abst.FindKeyIndex(8) < 0)
        self.assertTrue(abst.FindKeyIndex(12) < 0)
        self.assertTrue(abst.FindKeyIndex(13) < 0)

    def test_WideAllKeys(self):
        abst = self.BBST([])
        self.assertEqual([],abst.WideAllNodes()) 

        abst.AddKey(10)
        self.assertEqual([10],abst.WideAllNodes())  

        abst.AddKey(8)
        abst.AddKey(12)
        self.assertEqual([10,8,12],abst.WideAllNodes())  

        abst = self._create_test_abst()
        expected_keys = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        self.assertEqual(expected_keys,abst.WideAllNodes()) 

    def test_DeleteKey(self):
        bst = self.BBST([])
        result = bst.DeleteKey(1)
        self.assertFalse(result)
        self.assertEqual(0,bst.Count())

        bst = self.BBST([10])
        result = bst.DeleteKey(10)
        self.assertTrue(result)
        self.assertEqual(0,bst.Count())        

        bst = self._create_test_abst()
        self.assertEqual(15,bst.Count())
        bst.DeleteKey(1)
        self.assertEqual(14,bst.Count())
        bst.DeleteKey(3)
        self.assertEqual(13,bst.Count())
        bst.DeleteKey(15)
        self.assertEqual(12,bst.Count())
        bst.DeleteKey(14)
        self.assertEqual(11,bst.Count())
        bst.DeleteKey(9)
        self.assertEqual(10,bst.Count())

        bst = self._create_test_abst()
        self.assertEqual(15,bst.Count())

        # find_result = bst.Fi(10)
        # self.assertTrue(find_result.NodeHasKey)

        # result = bst.DeleteKey(100)
        # self.assertFalse(result)
        # self.assertEqual(15,bst.Count())

        # result = bst.DeleteKey(10)
        # self.assertTrue(result)
        # self.assertEqual(14,bst.Count())
        
        # find_result = bst.FindNodeByKey(10)
        # self.assertFalse(find_result.NodeHasKey) 
        # self.assertEqual(14,bst.Count()) 

        # find_result = bst.FindNodeByKey(9)
        # self.assertTrue(find_result.NodeHasKey)
        # self.assertEqual(14,bst.Count())

        # find_result = bst.FindNodeByKey(11)
        # self.assertTrue(find_result.NodeHasKey)
        # self.assertEqual(14,bst.Count())

        # result = bst.DeleteKey(8)
        # self.assertTrue(find_result.NodeHasKey)
        # self.assertEqual(13,bst.Count())


    def test_many_DeleteKey(self):
        bst = self.BBST([])

        #random.seed(42)
        
        count = 0
        arr= list(range(1,101))
        random.shuffle(arr)
        for v in arr:
            bst.AddKey(v)
            count += 1
            self.assertEqual(count,bst.Count())

        # random.shuffle(arr)
        # for v in arr:
        #     bst.DeleteKey(v)
        #     count -= 1
        #     self.assertEqual(count,bst.Count())  




if __name__ == '__main__':
    unittest.main()









