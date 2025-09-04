import unittest
import random

#run tests: 
# python ./DSA2/task2-3.py

class TestTask2(unittest.TestCase):
    from task2 import BST, BSTNode, BSTFind

    def _create_test_bst(self) -> BST:
        bst = self.BST(None)
        values = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            bst.AddKeyValue(v,f"{v}")
        return bst
    
    def _count():
        pass

    def test_AddKeyValue(self):
        bst = self.BST(None)

        is_ok = bst.AddKeyValue(8,"8")
        self.assertTrue(is_ok)
        self.assertEqual(bst.Root.NodeKey, 8)

        is_ok = bst.AddKeyValue(4,"4")
        self.assertTrue(is_ok)
        _node = bst.Root.LeftChild
        self.assertEqual(_node.NodeKey, 4)

        is_ok = bst.AddKeyValue(12,"12")
        self.assertTrue(is_ok)
        _node = bst.Root.RightChild
        self.assertEqual(_node.NodeKey, 12)


        values = [2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            self.assertFalse(bst.FindNodeByKey(v).NodeHasKey)
            is_ok = bst.AddKeyValue(v,f"{v}")
            self.assertTrue(bst.FindNodeByKey(v).NodeHasKey)
            self.assertTrue(is_ok)

        _node = bst.Root.RightChild.LeftChild.RightChild
        self.assertEqual(_node.NodeKey, 11)

        _node = bst.Root.LeftChild.RightChild.RightChild
        self.assertEqual(_node.NodeKey, 7)

        self.assertFalse(bst.AddKeyValue(14,"14"))
        self.assertFalse(bst.AddKeyValue(7,"7"))

    def test_FindNodeByKey(self):
        bst = self.BST(None)
        bst_f = bst.FindNodeByKey(10)
        self.assertIsNone(bst_f.Node)
        self.assertFalse(bst_f.NodeHasKey)

        bst = self._create_test_bst()
        bst_f = bst.FindNodeByKey(8)
        self.assertEqual(bst.Root,bst_f.Node)
        self.assertTrue(bst_f.NodeHasKey)        

        bst_f = bst.FindNodeByKey(11)
        expected_node = bst.Root.RightChild.LeftChild.RightChild
        self.assertEqual(expected_node,bst_f.Node)
        self.assertTrue(bst_f.NodeHasKey)

        bst_f = bst.FindNodeByKey(16)
        expected_node = bst.Root.RightChild.RightChild.RightChild
        self.assertEqual(expected_node,bst_f.Node)
        self.assertFalse(bst_f.NodeHasKey)
        self.assertFalse(bst_f.ToLeft)

    def test_FindMinMax(self):
        bst = self.BST(None)
        self.assertIsNone(bst.FinMinMax(bst.Root,FindMax=False))
        self.assertIsNone(bst.FinMinMax(bst.Root,FindMax=True))


        bst = self._create_test_bst()
        self.assertEqual(1,bst.FinMinMax(bst.Root,FindMax=False).NodeKey)
        self.assertEqual(15,bst.FinMinMax(bst.Root,FindMax=True).NodeKey)

        node = bst.FindNodeByKey(6).Node
        self.assertEqual(5,bst.FinMinMax(node,FindMax=False).NodeKey)
        self.assertEqual(7,bst.FinMinMax(node,FindMax=True).NodeKey)

    def test_DeleteNodeByKey(self):
        bst = self.BST(None)
        result = bst.DeleteNodeByKey(1)
        self.assertFalse(result)
        self.assertEqual(0,bst.Count())

        bst = self.BST(self.BSTNode(10,"100",None))
        result = bst.DeleteNodeByKey(10)
        self.assertTrue(result)
        self.assertEqual(0,bst.Count())        

        bst = self._create_test_bst()
        self.assertEqual(15,bst.Count())
        bst.DeleteNodeByKey(1)
        self.assertEqual(14,bst.Count())
        bst.DeleteNodeByKey(3)
        self.assertEqual(13,bst.Count())
        bst.DeleteNodeByKey(15)
        self.assertEqual(12,bst.Count())
        bst.DeleteNodeByKey(14)
        self.assertEqual(11,bst.Count())
        bst.DeleteNodeByKey(9)
        self.assertEqual(10,bst.Count())

        bst = self._create_test_bst()
        self.assertEqual(15,bst.Count())

        find_result = bst.FindNodeByKey(10)
        self.assertTrue(find_result.NodeHasKey)

        result = bst.DeleteNodeByKey(100)
        self.assertFalse(result)
        self.assertEqual(15,bst.Count())

        result = bst.DeleteNodeByKey(10)
        self.assertTrue(result)
        self.assertEqual(14,bst.Count())
        
        find_result = bst.FindNodeByKey(10)
        self.assertFalse(find_result.NodeHasKey) 
        self.assertEqual(14,bst.Count()) 

        find_result = bst.FindNodeByKey(9)
        self.assertTrue(find_result.NodeHasKey)
        self.assertEqual(14,bst.Count())

        find_result = bst.FindNodeByKey(11)
        self.assertTrue(find_result.NodeHasKey)
        self.assertEqual(14,bst.Count())

        result = bst.DeleteNodeByKey(8)
        self.assertTrue(find_result.NodeHasKey)
        self.assertEqual(13,bst.Count())


    def test_many_DeleteNodeByKey(self):
        bst = self.BST(None)

        #random.seed(42)
        
        count = 0
        arr= list(range(1,101))
        random.shuffle(arr)
        for v in arr:
            bst.AddKeyValue(v,f"{v}")
            count += 1
            self.assertEqual(count,bst.Count())

        random.shuffle(arr)
        for v in arr:
            bst.DeleteNodeByKey(v)
            count -= 1
            self.assertEqual(count,bst.Count())        




class TestTask2_2(unittest.TestCase):
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("task1-2", "./DSA2/task2-2.py")
    task2_2 = importlib.util.module_from_spec(spec)
    sys.modules["task2-2"] = task2_2
    spec.loader.exec_module(task2_2)
    BST = task2_2.BST
    BSTNode = task2_2.BSTNode
    BSTFind = task2_2.BSTFind


    def _create_test_bst(self) -> BST:
        bst = self.BST(None)
        values = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            bst.AddKeyValue(v,f"{v}")
        return bst

    def test_AddKeyValue(self):
        bst = self.BST(None)

        is_ok = bst.AddKeyValue(8,"8")
        self.assertTrue(is_ok)
        self.assertEqual(bst.Root.NodeKey, 8)

        is_ok = bst.AddKeyValue(4,"4")
        self.assertTrue(is_ok)
        _node = bst.Root.LeftChild
        self.assertEqual(_node.NodeKey, 4)

        is_ok = bst.AddKeyValue(12,"12")
        self.assertTrue(is_ok)
        _node = bst.Root.RightChild
        self.assertEqual(_node.NodeKey, 12)


        values = [2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            self.assertFalse(bst.FindNodeByKey(v).NodeHasKey)
            is_ok = bst.AddKeyValue(v,f"{v}")
            self.assertTrue(bst.FindNodeByKey(v).NodeHasKey)
            self.assertTrue(is_ok)

        _node = bst.Root.RightChild.LeftChild.RightChild
        self.assertEqual(_node.NodeKey, 11)

        _node = bst.Root.LeftChild.RightChild.RightChild
        self.assertEqual(_node.NodeKey, 7)

        self.assertFalse(bst.AddKeyValue(14,"14"))
        self.assertFalse(bst.AddKeyValue(7,"7"))

    def test_FindNodeByKey(self):
        bst = self.BST(None)
        bst_f = bst.FindNodeByKey(10)
        self.assertIsNone(bst_f.Node)
        self.assertFalse(bst_f.NodeHasKey)

        bst = self._create_test_bst()
        bst_f = bst.FindNodeByKey(8)
        self.assertEqual(bst.Root,bst_f.Node)
        self.assertTrue(bst_f.NodeHasKey)        

        bst_f = bst.FindNodeByKey(11)
        expected_node = bst.Root.RightChild.LeftChild.RightChild
        self.assertEqual(expected_node,bst_f.Node)
        self.assertTrue(bst_f.NodeHasKey)

        bst_f = bst.FindNodeByKey(16)
        expected_node = bst.Root.RightChild.RightChild.RightChild
        self.assertEqual(expected_node,bst_f.Node)
        self.assertFalse(bst_f.NodeHasKey)
        self.assertFalse(bst_f.ToLeft)

    def test_FindMinMax(self):
        bst = self.BST(None)
        self.assertIsNone(bst.FinMinMax(bst.Root,FindMax=False))
        self.assertIsNone(bst.FinMinMax(bst.Root,FindMax=True))


        bst = self._create_test_bst()
        self.assertEqual(1,bst.FinMinMax(bst.Root,FindMax=False).NodeKey)
        self.assertEqual(15,bst.FinMinMax(bst.Root,FindMax=True).NodeKey)

        node = bst.FindNodeByKey(6).Node
        self.assertEqual(5,bst.FinMinMax(node,FindMax=False).NodeKey)
        self.assertEqual(7,bst.FinMinMax(node,FindMax=True).NodeKey)

    def test_DeleteNodeByKey(self):
        bst = self.BST(None)
        result = bst.DeleteNodeByKey(1)
        self.assertFalse(result)
        self.assertEqual(0,bst.Count())

        bst = self.BST(self.BSTNode(10,"100",None))
        result = bst.DeleteNodeByKey(10)
        self.assertTrue(result)
        self.assertEqual(0,bst.Count())        

        bst = self._create_test_bst()
        self.assertEqual(15,bst.Count())
        bst.DeleteNodeByKey(1)
        self.assertEqual(14,bst.Count())
        bst.DeleteNodeByKey(3)
        self.assertEqual(13,bst.Count())
        bst.DeleteNodeByKey(15)
        self.assertEqual(12,bst.Count())
        bst.DeleteNodeByKey(14)
        self.assertEqual(11,bst.Count())
        bst.DeleteNodeByKey(9)
        self.assertEqual(10,bst.Count())

        bst = self._create_test_bst()
        self.assertEqual(15,bst.Count())

        find_result = bst.FindNodeByKey(10)
        self.assertTrue(find_result.NodeHasKey)

        result = bst.DeleteNodeByKey(100)
        self.assertFalse(result)
        self.assertEqual(15,bst.Count())

        result = bst.DeleteNodeByKey(10)
        self.assertTrue(result)
        self.assertEqual(14,bst.Count())
        
        find_result = bst.FindNodeByKey(10)
        self.assertFalse(find_result.NodeHasKey) 
        self.assertEqual(14,bst.Count()) 

        find_result = bst.FindNodeByKey(9)
        self.assertTrue(find_result.NodeHasKey)
        self.assertEqual(14,bst.Count())

        find_result = bst.FindNodeByKey(11)
        self.assertTrue(find_result.NodeHasKey)
        self.assertEqual(14,bst.Count())

        result = bst.DeleteNodeByKey(8)
        self.assertTrue(find_result.NodeHasKey)
        self.assertEqual(13,bst.Count())


    def test_many_DeleteNodeByKey(self):
        bst = self.BST(None)

        #random.seed(42)
        
        count = 0
        arr= list(range(1,101))
        random.shuffle(arr)
        for v in arr:
            bst.AddKeyValue(v,f"{v}")
            count += 1
            self.assertEqual(count,bst.Count())

        random.shuffle(arr)
        for v in arr:
            bst.DeleteNodeByKey(v)
            count -= 1
            self.assertEqual(count,bst.Count())   

    def test_IsEqual(self):
        bst1 = self.BST(None)
        bst2 = self.BST(None)

        self.assertTrue(bst1.IsEqual(bst2))
        self.assertTrue(bst2.IsEqual(bst1))

        bst1 = self._create_test_bst()
        self.assertFalse(bst1.IsEqual(bst2))
        self.assertFalse(bst2.IsEqual(bst1))       

        bst2 = self._create_test_bst()
        self.assertTrue(bst1.IsEqual(bst2))
        self.assertTrue(bst2.IsEqual(bst1))    

        find_result = bst1.FindNodeByKey(10)
        find_result.Node.NodeValue = "10+"
        self.assertFalse(bst1.IsEqual(bst2))
        self.assertFalse(bst2.IsEqual(bst1))   
        find_result.Node.NodeValue = "10"
        self.assertTrue(bst1.IsEqual(bst2))
        self.assertTrue(bst2.IsEqual(bst1)) 

        bst1.DeleteNodeByKey(30)
        self.assertTrue(bst1.IsEqual(bst2))
        self.assertTrue(bst2.IsEqual(bst1)) 

        bst1.DeleteNodeByKey(6)
        self.assertFalse(bst1.IsEqual(bst2))
        self.assertFalse(bst2.IsEqual(bst1)) 

    def test_PathsToLeafs(self):
        bst = self.BST(None)
        self.assertEqual(bst.PathsToLeaves(0),[])
        self.assertEqual(bst.PathsToLeaves(100),[])

        root_node = self.BSTNode(10, "10", None) 
        bst = self.BST(root_node)
        self.assertEqual(bst.PathsToLeaves(0),[root_node.PathFromRoot()])
        self.assertEqual(bst.PathsToLeaves(1),[])

        bst.AddKeyValue(5,"5") 
        next_node = bst.Root.LeftChild
        self.assertEqual(bst.PathsToLeaves(0),[])
        self.assertEqual(bst.PathsToLeaves(2),[])
        self.assertEqual(bst.PathsToLeaves(1),[[root_node, next_node]])

        bst = self._create_test_bst()
        self.assertEqual(len(bst.PathsToLeaves(3)),8)
        self.assertEqual(len(bst.PathsToLeaves(4)),0) 
        self.assertEqual(len(bst.PathsToLeaves(2)),0) 

        bst.AddKeyValue(20,"20")
        self.assertEqual(len(bst.PathsToLeaves(4)),1) 

        self.assertEqual(len(bst.PathsToLeaves(2)),0)
        bst.DeleteNodeByKey(9)
        self.assertEqual(len(bst.PathsToLeaves(2)),0)
        bst.DeleteNodeByKey(11)
        self.assertEqual(len(bst.PathsToLeaves(2)),1)

    def test_MaxValueSumPaths(self):
        bst = self.BST(None)
        self.assertEqual(bst.MaxValueSumPaths(),[])

        root = self.BSTNode(10,10,None)
        bst = self.BST(root)
        self.assertEqual(bst.MaxValueSumPaths(),[[root]])

        bst.AddKeyValue(7,7)
        result = bst.MaxValueSumPaths()
        self.assertEqual(17,sum([node.NodeValue for node in result[0]]))

        bst.AddKeyValue(15,15)
        result = bst.MaxValueSumPaths()
        self.assertEqual(25,sum([node.NodeValue for node in result[0]]))

        bst.AddKeyValue(1,8)
        result = bst.MaxValueSumPaths()
        self.assertEqual(25,sum([node.NodeValue for node in result[0]]))
        self.assertEqual(25,sum([node.NodeValue for node in result[1]]))
        self.assertEqual(5,len(result[0])+len(result[1]))                

    def test_IsSymmetricTree(self):
        bst = self.BST(None)
        self.assertTrue(bst.IsSymmetricTree())

        bst.AddKeyValue(8,"8")
        self.assertTrue(bst.IsSymmetricTree())

        bst.AddKeyValue(4,"4")
        self.assertFalse(bst.IsSymmetricTree())

        bst.AddKeyValue(12,"12")
        self.assertTrue(bst.IsSymmetricTree())

        bst.AddKeyValue(2,"2")
        self.assertFalse(bst.IsSymmetricTree())

        bst.AddKeyValue(10,"10")
        self.assertTrue(bst.IsSymmetricTree())

        bst = self._create_test_bst()
        self.assertTrue(bst.IsSymmetricTree())

        bst.DeleteNodeByKey(6)
        self.assertFalse(bst.IsSymmetricTree())

        bst.DeleteNodeByKey(14)
        self.assertTrue(bst.IsSymmetricTree())

        
if __name__ == '__main__':
    unittest.main()
   

