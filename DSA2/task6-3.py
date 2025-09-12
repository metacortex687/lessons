import unittest
import random

# run tests:
# python ./DSA2/task6-3.py


class TestTask6(unittest.TestCase):
    from task6 import BalancedBST, BSTNode

    def test_GenerateTree(self):
        bbst = self.BalancedBST()
        bbst.GenerateTree([])
        self.assertIsNone(bbst.Root)

        bbst = self.BalancedBST()
        bbst.GenerateTree([10])
        self.assertEqual(bbst.Root.NodeKey, 10)

        bbst = self.BalancedBST()
        bbst.GenerateTree([10, 9])
        self.assertEqual(bbst.Root.NodeKey, 10)
        self.assertEqual(bbst.Root.LeftChild.NodeKey, 9)

        expected_keys = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
        bbst = self.BalancedBST()
        shuffle_expected_keys = expected_keys.copy()
        random.shuffle(shuffle_expected_keys)
        bbst.GenerateTree(shuffle_expected_keys)
        self.assertEqual(expected_keys, [node.NodeKey for node in bbst.WideAllNodes()])

        bbst.GenerateTree([])
        self.assertIsNone(bbst.Root)

    def test_IsBalanced(self):
        bbst = self.BalancedBST()
        bbst.GenerateTree([])
        self.assertTrue(bbst.IsBalanced(None))

        bbst = self.BalancedBST()
        bbst.Root = self.BSTNode(10, None)
        bbst.Root.Level = 0
        self.assertTrue(bbst.IsBalanced(bbst.Root))

        bbst.Root.RightChild = self.BSTNode(15, None)
        bbst.Root.RightChild.Level = 1
        self.assertTrue(bbst.IsBalanced(bbst.Root))

        bbst.Root.LeftChild = self.BSTNode(8, None)
        bbst.Root.LeftChild.Level = 1
        self.assertTrue(bbst.IsBalanced(bbst.Root))

        bbst.Root.LeftChild.LeftChild = self.BSTNode(6, None)
        bbst.Root.LeftChild.LeftChild.Level = 2
        self.assertTrue(bbst.IsBalanced(bbst.Root))

        bbst.Root.LeftChild.LeftChild.RightChild = self.BSTNode(7, None)
        bbst.Root.LeftChild.LeftChild.RightChild.Level = 3
        self.assertFalse(bbst.IsBalanced(bbst.Root))


class TestTask6_2(TestTask6):
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("task6-2", "./DSA2/task6-2.py")
    task6_2 = importlib.util.module_from_spec(spec)
    sys.modules["task6-2"] = task6_2
    spec.loader.exec_module(task6_2)
    BalancedBST = task6_2.BalancedBST
    BSTNode = task6_2.BSTNode

    def test_IsValidBST(self):
        bbst = self.BalancedBST()
        self.assertTrue(bbst.IsValidBST())

        bbst.Root = self.BSTNode(10, None)
        self.assertTrue(bbst.IsValidBST())

        bbst.Root.LeftChild = self.BSTNode(15, None)
        self.assertFalse(bbst.IsValidBST())

        bbst.Root.LeftChild, bbst.Root.RightChild = (
            bbst.Root.RightChild,
            bbst.Root.LeftChild,
        )

        bbst.Root.RightChild.RightChild = self.BSTNode(5, None)
        self.assertFalse(bbst.IsValidBST())


if __name__ == "__main__":
    unittest.main()
