import unittest
import random

# run tests:
# python ./DSA2/task11-3.py


class TestTask11(unittest.TestCase):
    from task11 import SimpleGraph

    def test_AddVertex(self):
        s = self.SimpleGraph(5)
        s.AddVertex(1)
        s.AddVertex(5)
        self.assertFalse(s.IsEdge(0, 1))
        s.AddEdge(0, 1)
        self.assertTrue(s.IsEdge(0, 1))
        self.assertTrue(s.IsEdge(1, 0))

        s = self.SimpleGraph(5)
        s.AddVertex(1)
        s.AddVertex(5)
        s.AddEdge(0, 1)
        self.assertTrue(s.IsEdge(0, 1))
        s.RemoveEdge(0, 1)
        self.assertFalse(s.IsEdge(0, 1))
        self.assertFalse(s.IsEdge(1, 0))

        s = self.SimpleGraph(5)
        s.AddVertex(1)
        s.AddVertex(5)
        s.AddEdge(0, 1)
        self.assertTrue(s.IsEdge(0, 1))
        s.RemoveVertex(1)
        self.assertFalse(s.IsEdge(0, 1))
        self.assertFalse(s.IsEdge(1, 0))

        s = self.SimpleGraph(5)
        s.AddVertex(7)
        self.assertFalse(s.IsEdge(0, 0))
        s.AddEdge(0, 0)
        self.assertTrue(s.IsEdge(0, 0))

    def test_DepthFirstSearch(self):
        s = self.SimpleGraph(5)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        self.assertEqual([], s.DepthFirstSearch(0, 1))
        self.assertEqual([], s.DepthFirstSearch(1, 0))

        s.AddEdge(0, 1)
        self.assertEqual([v0, v1], s.DepthFirstSearch(0, 1))
        self.assertEqual([v1, v0], s.DepthFirstSearch(1, 0))

        v2 = s.AddVertex(2)
        s.AddEdge(0, 2)
        self.assertEqual([v0, v1], s.DepthFirstSearch(0, 1))
        self.assertEqual([v1, v0], s.DepthFirstSearch(1, 0))

        v3 = s.AddVertex(3)
        self.assertEqual([], s.DepthFirstSearch(3, 2))
        s.AddEdge(0, 3)
        self.assertEqual([v3, v0, v2], s.DepthFirstSearch(3, 2))

    def test_DepthFirstSearch_WhithWhile(self):
        s = self.SimpleGraph(5)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        self.assertEqual([], s.DepthFirstSearch_WhithWhile(0, 1))
        self.assertEqual([], s.DepthFirstSearch_WhithWhile(1, 0))

        s.AddEdge(0, 1)
        self.assertEqual([v0, v1], s.DepthFirstSearch_WhithWhile(0, 1))
        self.assertEqual([v1, v0], s.DepthFirstSearch_WhithWhile(1, 0))

        v2 = s.AddVertex(2)
        s.AddEdge(0, 2)
        self.assertEqual([v0, v1], s.DepthFirstSearch_WhithWhile(0, 1))
        self.assertEqual([v1, v0], s.DepthFirstSearch_WhithWhile(1, 0))

        v3 = s.AddVertex(3)
        self.assertEqual([], s.DepthFirstSearch_WhithWhile(3, 2))
        s.AddEdge(0, 3)
        self.assertEqual([v3, v0, v2], s.DepthFirstSearch_WhithWhile(3, 2))

    def test_BreadthFirstSearch(self):
        s = self.SimpleGraph(5)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        self.assertEqual([], s.BreadthFirstSearch(0, 1))
        self.assertEqual([], s.BreadthFirstSearch(1, 0))

        s.AddEdge(0, 1)
        self.assertEqual([v0, v1], s.BreadthFirstSearch(0, 1))
        self.assertEqual([v1, v0], s.BreadthFirstSearch(1, 0))

        v2 = s.AddVertex(2)
        s.AddEdge(0, 2)
        self.assertEqual([v0, v1], s.BreadthFirstSearch(0, 1))
        self.assertEqual([v1, v0], s.BreadthFirstSearch(1, 0))

        v3 = s.AddVertex(3)
        self.assertEqual([], s.BreadthFirstSearch(3, 2))
        s.AddEdge(0, 3)
        self.assertEqual([v3, v0, v2], s.BreadthFirstSearch(3, 2))

        s.AddEdge(2, 3)
        self.assertEqual([v3, v2], s.BreadthFirstSearch(3, 2))


class TestTask11_2(unittest.TestCase):

    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("task11-2", "./DSA2/task11-2.py")
    task11_2 = importlib.util.module_from_spec(spec)
    sys.modules["task11-2"] = task11_2
    spec.loader.exec_module(task11_2)
    SimpleGraph = task11_2.SimpleGraph
    SimpleTree = task11_2.SimpleTree
    SimpleTreeNode = task11_2.SimpleTreeNode

    def test_FindAllCicles(self):

        s = self.SimpleGraph(10)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        v2 = s.AddVertex(2)

        self.assertEqual([], s.FindAllCicles())

        s.AddEdge(0, 1)
        self.assertEqual([], s.FindAllCicles())

        s.AddEdge(1, 2)
        self.assertEqual([], s.FindAllCicles())

        s.AddEdge(2, 0)
        self.assertEqual([[0, 1, 2]], s.FindAllCicles())

        v3 = s.AddVertex(3)
        s.AddEdge(1, 3)
        self.assertCountEqual([[0, 1, 2]], s.FindAllCicles())

        v4 = s.AddVertex(4)
        s.AddEdge(3, 2)
        result = s.FindAllCicles()
        self.assertCountEqual([[0, 1, 2], [1, 2, 3], [0, 1, 3, 2]], result)

        v5 = s.AddVertex(5)
        v6 = s.AddVertex(6)
        v7 = s.AddVertex(7)
        s.AddEdge(5, 6)
        s.AddEdge(6, 7)
        s.AddEdge(7, 5)
        self.assertCountEqual(
            [[0, 1, 2], [1, 2, 3], [0, 1, 3, 2], [5, 6, 7]], s.FindAllCicles()
        )

        s.AddEdge(6, 0)
        result = s.FindAllCicles()
        self.assertCountEqual([[0, 1, 2], [1, 2, 3], [0, 1, 3, 2], [5, 6, 7]], result)


    def test_FindTreeDiameter(self):
        st = self.SimpleTree(None)
        #self.assertEqual(0,st.FindTreeDiameter())

        root = self.SimpleTreeNode("_root",None)
        st = self.SimpleTree(root)
        #self.assertEqual(0,st.FindTreeDiameter())

        l1 = self.SimpleTreeNode(0,None)
        st.AddChild(root,l1)

        self.assertEqual(1,st.FindTreeDiameter())

        r1 = self.SimpleTreeNode(0,None) 
        st.AddChild(root,r1)
        self.assertEqual(2,st.FindTreeDiameter())

        

if __name__ == "__main__":
    unittest.main()





