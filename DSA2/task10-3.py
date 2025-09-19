import unittest
import random

# run tests:
# python ./DSA2/task10-3.py


class TestTask10(unittest.TestCase):
    from task10 import SimpleGraph

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


class TestTask10_2(TestTask10):
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("task10-2", "./DSA2/task10-2.py")
    task10_2 = importlib.util.module_from_spec(spec)
    sys.modules["task10-2"] = task10_2
    spec.loader.exec_module(task10_2)
    SimpleGraph = task10_2.SimpleGraph
    DirectedGraph = task10_2.DirectedGraph

    def test_IsConnected(self):
        s = self.SimpleGraph(5)
        self.assertFalse(s.IsConnected())

        v0 = s.AddVertex(0)
        self.assertTrue(s.IsConnected())

        v1 = s.AddVertex(1)
        self.assertFalse(s.IsConnected())

        s.AddEdge(0, 1)
        self.assertTrue(s.IsConnected())

        v2 = s.AddVertex(2)
        self.assertFalse(s.IsConnected())
        s.AddEdge(0, 2)
        self.assertTrue(s.IsConnected())

        v3 = s.AddVertex(3)
        self.assertFalse(s.IsConnected())
        s.AddEdge(0, 3)
        self.assertTrue(s.IsConnected())

    def test_LenMaxPath(self):
        dg = self.DirectedGraph(15)
        self.assertEqual(0, dg.MaxPath())

        dg.AddVertex(0)
        self.assertEqual(1, dg.MaxPath())

        dg.AddVertex(1)
        self.assertEqual(1, dg.MaxPath())

        dg.AddEdge(0, 1)
        self.assertEqual(2, dg.MaxPath())

        dg.AddVertex(2)
        dg.AddEdge(0, 2)
        self.assertEqual(2, dg.MaxPath())

        dg.AddEdge(2, 0)
        self.assertEqual(3, dg.MaxPath())

        dg.AddVertex(3)
        dg.AddVertex(4)
        dg.AddVertex(5)
        dg.AddVertex(6)
        dg.AddVertex(7)
        dg.AddVertex(8)

        dg.AddEdge(3, 4)
        self.assertEqual(3, dg.MaxPath())
        dg.AddEdge(4, 5)
        self.assertEqual(3, dg.MaxPath())
        dg.AddEdge(5, 6)
        self.assertEqual(4, dg.MaxPath())

        dg.AddEdge(6, 4)
        self.assertEqual(4, dg.MaxPath())

        dg.AddEdge(6, 7)
        dg.AddEdge(7, 8)
        self.assertEqual(6, dg.MaxPath())

        dg.AddEdge(1, 3)
        self.assertEqual(9, dg.MaxPath())

        dg.AddEdge(3, 1)
        self.assertEqual(6, dg.MaxPath())


if __name__ == "__main__":
    unittest.main()
