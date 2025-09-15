import unittest
import random

# run tests:
# python ./DSA2/task8-3.py


class TestTask8(unittest.TestCase):
    from task8 import SimpleGraph

    def test_AddVertex(self):
        s = self.SimpleGraph(5)
        s.AddVertex(1)
        s.AddVertex(5)
        self.assertFalse(s.IsEdge(1, 5))
        s.AddEdge(1, 5)
        self.assertTrue(s.IsEdge(1, 5))
        self.assertTrue(s.IsEdge(5, 1))

        s = self.SimpleGraph(5)
        s.AddVertex(1)
        s.AddVertex(5)
        s.AddEdge(1, 5)
        self.assertTrue(s.IsEdge(1, 5))
        s.RemoveEdge(1, 5)
        self.assertFalse(s.IsEdge(1, 5))
        self.assertFalse(s.IsEdge(5, 1))

        s = self.SimpleGraph(5)
        s.AddVertex(1)
        s.AddVertex(5)
        s.AddEdge(1, 5)
        self.assertTrue(s.IsEdge(1, 5))
        s.RemoveVertex(1)
        self.assertFalse(s.IsEdge(1, 5))
        self.assertFalse(s.IsEdge(5, 1))

        s.AddVertex(7)
        self.assertFalse(s.IsEdge(5, 5))
        self.assertFalse(s.IsEdge(5, 7))


class TestTask8_2(unittest.TestCase):
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("task8-2", "./DSA2/task8-2.py")
    task8_2 = importlib.util.module_from_spec(spec)
    sys.modules["task8-2"] = task8_2
    spec.loader.exec_module(task8_2)
    DirectedGraph = task8_2.DirectedGraph

    def test_AddVertex(self):
        dg = self.DirectedGraph(5)
        dg.AddVertex(1)
        dg.AddVertex(5)
        self.assertFalse(dg.IsEdge(1, 5))
        dg.AddEdge(1, 5)
        self.assertTrue(dg.IsEdge(1, 5))
        self.assertFalse(dg.IsEdge(5, 1))

        dg = self.DirectedGraph(5)
        dg.AddVertex(1)
        dg.AddVertex(5)
        dg.AddEdge(1, 5)
        self.assertTrue(dg.IsEdge(1, 5))
        dg.RemoveEdge(1, 5)
        self.assertFalse(dg.IsEdge(1, 5))
        self.assertFalse(dg.IsEdge(5, 1))

        dg = self.DirectedGraph(5)
        dg.AddVertex(1)
        dg.AddVertex(5)
        dg.AddEdge(1, 5)
        self.assertTrue(dg.IsEdge(1, 5))
        dg.RemoveVertex(1)
        self.assertFalse(dg.IsEdge(1, 5))
        self.assertFalse(dg.IsEdge(5, 1))

    def test_is_cyclic(self):
        dg = self.DirectedGraph(10)
        dg.AddVertex(1)
        dg.AddVertex(2)
        self.assertFalse(dg.IsCyclic())
        dg.AddEdge(1, 2)
        self.assertFalse(dg.IsCyclic())
        dg.AddEdge(2, 1)
        self.assertFalse(dg.IsCyclic())

        dg.AddVertex(3)
        dg.AddEdge(1, 3)
        dg.AddEdge(3, 2)
        self.assertTrue(dg.IsCyclic())

        dg.AddEdge(3, 1)
        self.assertFalse(dg.IsCyclic())

        dg = self.DirectedGraph(10)
        dg.AddVertex(1)
        dg.AddVertex(2)
        dg.AddVertex(3)
        dg.AddVertex(4)
        dg.AddVertex(4)
        self.assertFalse(dg.IsCyclic())
        dg.AddEdge(1, 2)
        dg.AddEdge(2, 3)
        dg.AddEdge(3, 4)
        dg.AddEdge(4, 5)
        self.assertFalse(dg.IsCyclic())
        dg.AddEdge(4, 2)
        self.assertTrue(dg.IsCyclic())


if __name__ == "__main__":
    unittest.main()
