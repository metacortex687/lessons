import unittest


# run tests:
# python ./DSA2/task9-3.py


class TestTask9(unittest.TestCase):
    from task9 import SimpleTree, SimpleTreeNode

    def test_AddChild_Count_LeafCount_GetAllNodes(self):
        st = self.SimpleTree(None)
        self.assertEqual(st.Count(), 0)
        self.assertEqual(st.LeafCount(), 0)
        self.assertEqual(st.GetAllNodes(), [])

        root = self.SimpleTreeNode(100, None)
        st = self.SimpleTree(root)
        self.assertEqual(st.Count(), 1)
        self.assertEqual(st.LeafCount(), 1)
        self.assertCountEqual(st.GetAllNodes(), [root])

        stn10 = self.SimpleTreeNode(10, None)
        st.AddChild(root, stn10)
        self.assertEqual(st.Count(), 2)
        self.assertEqual(st.LeafCount(), 1)
        self.assertCountEqual(st.GetAllNodes(), [root, stn10])

        stn20 = self.SimpleTreeNode(20, None)
        st.AddChild(stn10, stn20)
        self.assertEqual(st.Count(), 3)
        self.assertEqual(st.LeafCount(), 1)
        self.assertCountEqual(st.GetAllNodes(), [root, stn10, stn20])

        stn30 = self.SimpleTreeNode(30, None)
        st.AddChild(stn10, stn30)
        self.assertEqual(st.Count(), 4)
        self.assertEqual(st.LeafCount(), 2)
        self.assertCountEqual(st.GetAllNodes(), [root, stn10, stn20, stn30])

    def test_MoveNode(self):
        root = self.SimpleTreeNode(100)
        st = self.SimpleTree(root)

        stn10 = self.SimpleTreeNode(10)
        st.AddChild(root, stn10)

        stn20 = self.SimpleTreeNode(20, None)
        st.AddChild(stn10, stn20)

        stn30 = self.SimpleTreeNode(30, None)
        st.AddChild(stn10, stn30)

        self.assertEqual(st.Count(), 4)
        self.assertEqual(st.LeafCount(), 2)
        self.assertCountEqual(st.GetAllNodes(), [root, stn10, stn20, stn30])

        st.MoveNode(stn20, root)
        st.MoveNode(stn30, root)
        self.assertEqual(st.Count(), 4)
        self.assertEqual(st.LeafCount(), 3)
        self.assertCountEqual(st.GetAllNodes(), [root, stn10, stn20, stn30])

    def test_DeleteNode(self):
        root = self.SimpleTreeNode(100)
        st = self.SimpleTree(root)
        self.assertEqual(st.Count(), 1)
        st.DeleteNode(root)
        self.assertEqual(st.Count(), 0)

        st = self.SimpleTree(root)
        stn10 = self.SimpleTreeNode(10)
        stn20 = self.SimpleTreeNode(20)
        stn30 = self.SimpleTreeNode(30)

        st.AddChild(root, stn10)
        st.AddChild(stn10, stn20)
        st.AddChild(stn20, stn30)

        self.assertEqual(st.Count(), 4)
        self.assertEqual(st.LeafCount(), 1)

        st.DeleteNode(stn20)
        self.assertEqual(st.Count(), 2)
        self.assertEqual(st.LeafCount(), 1)

    def test_FindNodesByValue(self):
        st = self.SimpleTree(None)
        self.assertEqual(st.FindNodesByValue(20), [])

        root = self.SimpleTreeNode(20)
        st = self.SimpleTree(root)
        stn10 = self.SimpleTreeNode(10)
        stn20 = self.SimpleTreeNode(20)
        stn20_2 = self.SimpleTreeNode(20)
        stn30 = self.SimpleTreeNode(30)

        st.AddChild(root, stn10)
        st.AddChild(root, stn20)
        st.AddChild(stn10, stn20_2)
        st.AddChild(stn20, stn30)

        self.assertEqual(st.FindNodesByValue(10), [stn10])
        self.assertEqual(st.FindNodesByValue(30), [stn30])
        self.assertCountEqual(st.FindNodesByValue(20), [root, stn20, stn20_2])

    def test_EvenTrees(self):
        st = self.SimpleTree(None)
        self.assertEqual([], st.EvenTrees())

        n1 = self.SimpleTreeNode(1)
        st = self.SimpleTree(n1)
        self.assertEqual([], st.EvenTrees())

        n2 = self.SimpleTreeNode(2)
        st.AddChild(n1, n2)
        self.assertEqual([], st.EvenTrees())

        n3 = self.SimpleTreeNode(3)
        n4 = self.SimpleTreeNode(4)
        st.AddChild(n2, n3)
        self.assertEqual([], st.EvenTrees())

        st.AddChild(n3, n4)
        self.assertEqual([n2, n3], st.EvenTrees())

        n1 = self.SimpleTreeNode(1)
        st = self.SimpleTree(n1)
        n2 = self.SimpleTreeNode(2)
        n3 = self.SimpleTreeNode(3)
        n4 = self.SimpleTreeNode(4)
        n5 = self.SimpleTreeNode(5)
        n6 = self.SimpleTreeNode(6)
        n7 = self.SimpleTreeNode(7)
        n8 = self.SimpleTreeNode(8)
        n9 = self.SimpleTreeNode(9)
        n10 = self.SimpleTreeNode(10)

        st.AddChild(n1, n2)
        st.AddChild(n2, n5)
        st.AddChild(n2, n7)

        st.AddChild(n1, n3)
        st.AddChild(n3, n4)

        st.AddChild(n1, n6)
        st.AddChild(n6, n8)
        st.AddChild(n8, n9)
        st.AddChild(n8, n10)

        self.assertEqual([n1, n3, n1, n6], st.EvenTrees())


class TestTask9_2(unittest.TestCase):
    from task9_2 import SimpleTree, SimpleTreeNode

    def test_Rebalance(self):
        st = self.SimpleTree(None)
        st.Rebalance()
        self.assertEqual(0, st.Count())
        self.assertEqual(-1, st.MinPath())
        self.assertEqual(-1, st.MaxPath())
        self.assertEqual(None, st.Root)

        n10 = self.SimpleTreeNode(10)
        st = self.SimpleTree(n10)

        st.Rebalance()

        self.assertEqual(1, st.Count())
        self.assertEqual(0, st.MinPath())
        self.assertEqual(0, st.MaxPath())
        self.assertEqual(n10, st.Root)

        n9 = self.SimpleTreeNode(9)
        st.AddChild(n10, n9)
        self.assertEqual(n9, n10.Children[0])

        st.Rebalance()
        self.assertEqual(2, st.Count())
        self.assertEqual(0, st.MinPath())
        self.assertEqual(1, st.MaxPath())
        self.assertEqual(n10, st.Root)
        self.assertEqual(n9, n10.Children[0])

        n2 = self.SimpleTreeNode(2)
        st.AddChild(n9, n2)
        self.assertEqual(0, st.MinPath())
        self.assertEqual(2, st.MaxPath())

        st.Rebalance()
        self.assertEqual(n10, st.Root)
        self.assertEqual(n2, n10.Children[0])
        self.assertEqual(n9, n10.Children[1])
        self.assertEqual(3, st.Count())
        self.assertEqual(1, st.MinPath())
        self.assertEqual(1, st.MaxPath())

        n3 = self.SimpleTreeNode(3)
        n8 = self.SimpleTreeNode(8)
        n9.AddChild(n8)
        n8.AddChild(n3)
        st.Rebalance()
        self.assertEqual(n10, st.Root)
        self.assertEqual(n3, n10.Children[0])
        self.assertEqual(n2, n3.Children[0])
        self.assertEqual(n9, n10.Children[1])
        self.assertEqual(n8, n9.Children[0])
        self.assertEqual(5, st.Count())
        self.assertEqual(1, st.MinPath())
        self.assertEqual(2, st.MaxPath())

        n11 = self.SimpleTreeNode(11)
        n8.AddChild(n11)
        st.Rebalance()
        self.assertEqual(n11, st.Root)


    def test_CountEvenSubtrees(self):
        n1 = self.SimpleTreeNode(1)
        st = self.SimpleTree(n1)
        n2 = self.SimpleTreeNode(2)
        n3 = self.SimpleTreeNode(3)
        n4 = self.SimpleTreeNode(4)
        n5 = self.SimpleTreeNode(5)
        n6 = self.SimpleTreeNode(6)
        n7 = self.SimpleTreeNode(7)
        n8 = self.SimpleTreeNode(8)
        n9 = self.SimpleTreeNode(9)
        n10 = self.SimpleTreeNode(10)

        st.AddChild(n1, n2)
        st.AddChild(n2, n5)
        st.AddChild(n2, n7)

        st.AddChild(n1, n3)
        st.AddChild(n3, n4)

        st.AddChild(n1, n6)
        st.AddChild(n6, n8)
        st.AddChild(n8, n9)
        st.AddChild(n8, n10)

        self.assertEqual(3, st.CountEvenSubtrees())



if __name__ == "__main__":
    unittest.main()
