import unittest
import random

# run tests:
# python ./DSA2/task12-3.py


class TestTask12(unittest.TestCase):
    from task12 import SimpleGraph

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

    def test_WeakVertices(self):
        s = self.SimpleGraph(10)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        v2 = s.AddVertex(2)
        self.assertEqual([v0, v1, v2], s.WeakVertices())

        s.AddEdge(0, 1)
        s.AddEdge(0, 2)
        self.assertEqual([v0, v1, v2], s.WeakVertices())

        s.AddEdge(1, 2)
        self.assertEqual([], s.WeakVertices())

        s = self.SimpleGraph(10)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        v2 = s.AddVertex(2)
        v3 = s.AddVertex(3)
        v4 = s.AddVertex(4)
        v5 = s.AddVertex(5)
        v6 = s.AddVertex(6)
        v7 = s.AddVertex(7)
        v8 = s.AddVertex(8)

        s.AddEdge(0, 1)
        s.AddEdge(0, 2)
        s.AddEdge(0, 3)

        s.AddEdge(1, 2)
        s.AddEdge(1, 4)

        s.AddEdge(2, 3)
        s.AddEdge(2, 5)

        s.AddEdge(4, 5)

        s.AddEdge(5, 6)
        s.AddEdge(5, 7)

        s.AddEdge(6, 7)

        s.AddEdge(7, 8)

        self.assertEqual([v4, v8], s.WeakVertices())


class TestTask12_2(unittest.TestCase):

    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("task12-2", "./DSA2/task12-2.py")
    task12_2 = importlib.util.module_from_spec(spec)
    sys.modules["task12-2"] = task12_2
    spec.loader.exec_module(task12_2)
    SimpleGraph = task12_2.SimpleGraph


    def test_WeakVertices(self):
        s = self.SimpleGraph(10)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        v2 = s.AddVertex(2)
        self.assertEqual(0, s.CountTriangles())

        s.AddEdge(0, 1)
        s.AddEdge(0, 2)
        self.assertEqual(0, s.CountTriangles())

        s.AddEdge(1, 2)
        self.assertEqual(1, s.CountTriangles())

        s = self.SimpleGraph(15)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        v2 = s.AddVertex(2)
        v3 = s.AddVertex(3)
        v4 = s.AddVertex(4)
        v5 = s.AddVertex(5)
        v6 = s.AddVertex(6)
        v7 = s.AddVertex(7)
        v8 = s.AddVertex(8)

        s.AddEdge(0, 1)
        s.AddEdge(0, 2)
        s.AddEdge(0, 3)

        s.AddEdge(1, 2)
        s.AddEdge(1, 4)

        s.AddEdge(2, 3)
        s.AddEdge(2, 5)

        s.AddEdge(4, 5)

        s.AddEdge(5, 6)
        s.AddEdge(5, 7)

        s.AddEdge(6, 7)

        s.AddEdge(7, 8)

        self.assertEqual(3, s.CountTriangles())

        v9 = s.AddVertex(9)
        v10 = s.AddVertex(10)
        v11 = s.AddVertex(11)
        s.AddEdge(10, 9)
        s.AddEdge(10, 11)
        s.AddEdge(9, 11)
        self.assertEqual(4, s.CountTriangles())

    def test_FindWeakVertexIndices(self):
        s = self.SimpleGraph(10)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        v2 = s.AddVertex(2)
        self.assertCountEqual([0, 1, 2], s.FindWeakVertexIndices())

        s.AddEdge(0, 1)
        s.AddEdge(0, 2)
        self.assertEqual([0, 1, 2], s.FindWeakVertexIndices())

        s.AddEdge(1, 2)
        self.assertCountEqual([], s.FindWeakVertexIndices())

        s = self.SimpleGraph(10)
        v0 = s.AddVertex(0)
        v1 = s.AddVertex(1)
        v2 = s.AddVertex(2)
        v3 = s.AddVertex(3)
        v4 = s.AddVertex(4)
        v5 = s.AddVertex(5)
        v6 = s.AddVertex(6)
        v7 = s.AddVertex(7)
        v8 = s.AddVertex(8)

        s.AddEdge(0,1)
        s.AddEdge(0,2)
        s.AddEdge(0,3)

        s.AddEdge(1,2)
        s.AddEdge(1,4)

        s.AddEdge(2,3)
        s.AddEdge(2,5)

        s.AddEdge(4,5)

        s.AddEdge(5,6)
        s.AddEdge(5,7)

        s.AddEdge(6,7)

        s.AddEdge(7,8)

        self.assertCountEqual([4,8], s.FindWeakVertexIndices())


if __name__ == "__main__":
    unittest.main()
