import unittest
import random

#run tests: 
# python ./DSA2/task4-3.py


class TestTask4(unittest.TestCase):
    from task4 import aBST

    def _create_test_abst(self) -> aBST:
        abst = self.aBST(3)
        values = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            abst.AddKey(v)
        return abst

    def test_init(self):
        abst = self.aBST(0)
        self.assertEqual(1,len(abst.Tree))
        self.assertIsNone(abst.Tree[0])

        abst = self.aBST(3)
        self.assertEqual(15,len(abst.Tree))
        self.assertIsNone(abst.Tree[12])


    def test_AddKeyValue(self):
        abst = self.aBST(0)
        self.assertEqual(0,abst.AddKey(50))
        self.assertEqual(0,abst.AddKey(50))
        self.assertEqual(-1,abst.AddKey(25))


        abst = self.aBST(3)
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
        added_elements = [(0,50),(1,25),(2,75),(4,37),(5,62),(6,84),(11,55),(14,92)]

        abst = self.aBST(3)
        for _, key in added_elements: 
            abst.AddKey(key)

        for expected_index, key in added_elements:
            finded_index = abst.FindKeyIndex(key)
            self.assertEqual(expected_index,finded_index)

        self.assertIsNone(abst.FindKeyIndex(3))
        self.assertIsNone(abst.FindKeyIndex(7))
        self.assertIsNone(abst.FindKeyIndex(8))
        self.assertIsNone(abst.FindKeyIndex(12))
        self.assertIsNone(abst.FindKeyIndex(13))


    def test_WideAllKeys(self):
        abst = self.aBST(3)
        self.assertEqual([],abst.WideAllNodes()) 

        abst.AddKey(10)
        self.assertEqual([10],abst.WideAllNodes())  

        abst.AddKey(8)
        abst.AddKey(12)
        self.assertEqual([10,8,12],abst.WideAllNodes())  

        abst = self._create_test_abst()
        expected_keys = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        self.assertEqual(expected_keys,abst.WideAllNodes()) 



class TestTask4_2(TestTask4):
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("task4-2", "./DSA2/task4-2.py")
    task4_2 = importlib.util.module_from_spec(spec)
    sys.modules["task4-2"] = task4_2
    spec.loader.exec_module(task4_2)
    aBST = task4_2.aBST

    def _create_test_abst(self) -> aBST:
        abst = self.aBST(3)
        values = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            abst.AddKey(v)
        return abst

    def test_FindLowestCommonAncestor(self):
        abst = self._create_test_abst()

        self.assertEqual(8,abst.FindLowestCommonAncestor(8,8))
        self.assertEqual(8,abst.FindLowestCommonAncestor(4,12))
        self.assertEqual(8,abst.FindLowestCommonAncestor(6,9))

        self.assertEqual(4,abst.FindLowestCommonAncestor(5,2))
        self.assertEqual(4,abst.FindLowestCommonAncestor(2,5))

        self.assertEqual(10,abst.FindLowestCommonAncestor(10,11))
        self.assertEqual(10,abst.FindLowestCommonAncestor(11,10))

        self.assertEqual(12,abst.FindLowestCommonAncestor(10,15))
        self.assertEqual(12,abst.FindLowestCommonAncestor(15,10))


if __name__ == '__main__':
    unittest.main()

    

        




