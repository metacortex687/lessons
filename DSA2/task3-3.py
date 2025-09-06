import unittest
import random

#run tests: 
# python ./DSA2/task3-3.py


class TestTask3(unittest.TestCase):
    
    from task3 import BST, BSTNode, BSTFind

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


    def test_WideAllNodes(self):
        bst = self.BST(None)
        self.assertEqual([],[node.NodeKey for node in bst.WideAllNodes()]) 

        bst = self.BST(self.BSTNode(10,"10",None))
        self.assertEqual([10],[node.NodeKey for node in bst.WideAllNodes()])  

        bst.AddKeyValue(8,"8")
        bst.AddKeyValue(12, "12")
        self.assertEqual([10,8,12],[node.NodeKey for node in bst.WideAllNodes()])  

        bst = self._create_test_bst()
        expected_keys = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        self.assertEqual(expected_keys,[node.NodeKey for node in bst.WideAllNodes()]) 


    def test_DeepAllNodes(self):
        ''' visit_order
        0 - in-order
        1 - post-order
        2 - pre-order
        '''
                
        bst = self.BST(None)
        self.assertEqual([],[node.NodeKey for node in bst.DeepAllNodes(0)]) 
        self.assertEqual([],[node.NodeKey for node in bst.DeepAllNodes(1)]) 
        self.assertEqual([],[node.NodeKey for node in bst.DeepAllNodes(2)]) 

        bst.AddKeyValue(10,"10")
        self.assertEqual([10],[node.NodeKey for node in bst.DeepAllNodes(0)]) 
        self.assertEqual([10],[node.NodeKey for node in bst.DeepAllNodes(1)]) 
        self.assertEqual([10],[node.NodeKey for node in bst.DeepAllNodes(2)]) 

        bst.AddKeyValue(8,"10")
        bst.AddKeyValue(11,"11")
        self.assertEqual([8,10,11],[node.NodeKey for node in bst.DeepAllNodes(0)]) 
        self.assertEqual([8,11,10],[node.NodeKey for node in bst.DeepAllNodes(1)]) 
        self.assertEqual([10,8,11],[node.NodeKey for node in bst.DeepAllNodes(2)]) 

        bst = self._create_test_bst()
        self.assertEqual([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[node.NodeKey for node in bst.DeepAllNodes(0)]) 
        self.assertEqual([1,3,2,5,7,6,4,9,11,10,13,15,14,12,8],[node.NodeKey for node in bst.DeepAllNodes(1)]) 
        self.assertEqual([8,4,2,1,3,6,5,7,12,10,9,11,14,13,15],[node.NodeKey for node in bst.DeepAllNodes(2)]) 


class TestTask3_2(TestTask3):
    import importlib.util
    import sys
    spec = importlib.util.spec_from_file_location("task3-2", "./DSA2/task3-2.py")
    task3_2 = importlib.util.module_from_spec(spec)
    sys.modules["task3-2"] = task3_2
    spec.loader.exec_module(task3_2)
    BST = task3_2.BST
    BSTNode = task3_2.BSTNode
    BSTFind = task3_2.BSTFind


    def _create_test_bst(self) -> BST:
        bst = self.BST(None)
        values = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            bst.AddKeyValue(v,f"{v}")
        return bst

    def _create_test_int(self) -> BST:
        bst = self.BST(None)
        values = [8,4,12,2,6,10,14,1,3,5,7,9,11,13,15]
        for v in values:
            bst.AddKeyValue(v,v)
        return bst

    def test_InvertTree(self):
        bst = self.BST(None)
        self.assertIsNone(bst.Root)

        root = self.BSTNode(10,'10',None)
        bst = self.BST(root)
        bst.InvertTree()
        self.assertEqual(root,bst.Root)

        root = self.BSTNode(10,'10',None)
        bst = self.BST(root)
        bst.AddKeyValue(8,'8')
        bst.AddKeyValue(11,'11')
        left = bst.Root.LeftChild
        right = bst.Root.RightChild
        bst.InvertTree()
        self.assertEqual(left,bst.Root.RightChild)
        self.assertEqual(right,bst.Root.LeftChild)


        bst = self._create_test_bst()
        bst.InvertTree()
        self.assertEqual([8,12,4,14,10,6,2,15,13,11,9,7,5,3,1],[node.NodeKey for node in bst.WideAllNodes()]) 

    def test_MaxSumLevel(self):
        bst = self.BST(None)
        self.assertIsNone(bst.MaxSumLevel())

        root = self.BSTNode(10,10,None)
        bst = self.BST(root)
        self.assertEqual(0,bst.MaxSumLevel())

        bst.AddKeyValue(8,8)
        self.assertEqual(0,bst.MaxSumLevel())

        bst.AddKeyValue(11,11)
        self.assertEqual(1,bst.MaxSumLevel())

        bst = self._create_test_int()
        bst.Root.NodeValue = 1000
        self.assertEqual(0,bst.MaxSumLevel())


        bst = self._create_test_int()
        bst.Root.LeftChild.NodeValue = 1000
        self.assertEqual(1,bst.MaxSumLevel())


        bst = self._create_test_int()
        bst.Root.LeftChild.RightChild.NodeValue = 1000
        self.assertEqual(2,bst.MaxSumLevel())


        bst = self._create_test_int()
        bst.Root.LeftChild.RightChild.RightChild.NodeValue = 1000
        self.assertEqual(3,bst.MaxSumLevel())

    def test_Restore(self):
        bst = self.BST.Restore([],[])
        self.assertEqual(0,bst.Count())
        self.assertIsNone(bst.Root)

        bst = self.BST.Restore([1],[1])
        self.assertEqual(1,bst.Count())
        self.assertEqual(1, bst.Root.NodeValue)

        bst = self.BST.Restore([1,2],[2,1])
        self.assertEqual(2,bst.Count())
        self.assertEqual(1, bst.Root.NodeValue)
        self.assertEqual(2, bst.Root.LeftChild.NodeValue)



        bst = self.BST.Restore([1,2],[1,2])
        self.assertEqual(2,bst.Count())
        self.assertEqual(1, bst.Root.NodeValue)
        self.assertEqual(2, bst.Root.RightChild.NodeValue)

        bst = self.BST.Restore([1,2,3],[2,1,3])
        self.assertEqual(3,bst.Count())
        self.assertEqual(1, bst.Root.NodeValue)
        self.assertEqual(2, bst.Root.LeftChild.NodeValue)
        self.assertEqual(3, bst.Root.RightChild.NodeValue)

        bst = self.BST.Restore([1,2,4,5,3,6,7],[4,2,5,1,6,3,7]) 
        self.assertEqual(7,bst.Count())
        self.assertEqual(1, bst.Root.NodeValue)
        self.assertEqual(2, bst.Root.LeftChild.NodeValue)
        self.assertEqual(3, bst.Root.RightChild.NodeValue)
        self.assertEqual(4, bst.Root.LeftChild.LeftChild.NodeValue)
        self.assertEqual(5, bst.Root.LeftChild.RightChild.NodeValue)
        self.assertEqual(6, bst.Root.RightChild.LeftChild.NodeValue)
        self.assertEqual(7, bst.Root.RightChild.RightChild.NodeValue)


        bst = self._create_test_bst()
        pre_order_list = [node.NodeValue for node in bst.DeepAllNodes(2)]
        in_order_list =  [node.NodeValue for node in bst.DeepAllNodes(0)]
        self.assertEqual([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],[int(v) for v in in_order_list]) 
        self.assertEqual([8,4,2,1,3,6,5,7,12,10,9,11,14,13,15],[int(v) for v in pre_order_list]) 
        bst_restored = self.BST.Restore(pre_order_list,in_order_list)
        self.assertTrue(bst.IsEqual(bst_restored))


if __name__ == '__main__':
    unittest.main()

