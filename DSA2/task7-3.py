import unittest
import random

# run tests:
# python ./DSA2/task7-3.py


class TestTask7(unittest.TestCase):
    from task7 import Heap

    def test_MakeHeap_len_HeapArray(self):
        h = self.Heap()
        h.MakeHeap([], 0)
        self.assertEqual(1, len(h.HeapArray))
        h.MakeHeap([], 1)
        self.assertEqual(3, len(h.HeapArray))
        h.MakeHeap([], 2)
        self.assertEqual(7, len(h.HeapArray))
        h.MakeHeap([], 3)
        self.assertEqual(15, len(h.HeapArray))

    def test_MakeHeap(self):
        h = self.Heap()
        h.MakeHeap([5], 0)
        self.assertEqual([5], h.HeapArray)

        # with self.assertRaises(OverflowError):
        #     h.MakeHeap([5, 2], 0)

        h = self.Heap()
        # expected = [11, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, None, None, None]
        expected = [11, 9, 8, 7, 6, 5, 4, 3, 2, 1, None, None, None, None, None]
        array = [v for v in expected if v is not None]
        # random.shuffle(array)
        h.MakeHeap(array, 3)
        self.assertEqual(expected, h.HeapArray)

    def test_AddMax(self):
        h = self.Heap()
        h.MakeHeap([11, 9, 4], 3)
        h.Add(7)
        self.assertEqual([11, 9, 4, 7], [v for v in h.HeapArray if v is not None])

        h.Add(6)
        self.assertEqual([11, 9, 4, 7, 6], [v for v in h.HeapArray if v is not None])

        h.Add(3)
        h.Add(1)
        self.assertEqual(
            [11, 9, 4, 7, 6, 3, 1], [v for v in h.HeapArray if v is not None]
        )

        h.Add(2)
        h.Add(5)
        self.assertEqual(
            [11, 9, 4, 7, 6, 3, 1, 2, 5], [v for v in h.HeapArray if v is not None]
        )

        h.Add(8)
        self.assertEqual(
            [11, 9, 4, 7, 8, 3, 1, 2, 5, 6], [v for v in h.HeapArray if v is not None]
        )
        self.assertTrue(h.IsValid())

        h = self.Heap()
        h.MakeHeap([10, 9, 4], 1)
        self.assertFalse(h.Add(11))

        h = self.Heap()
        h.MakeHeap([10, 9, 4], 2)
        self.assertEqual([10, 9, 4], [v for v in h.HeapArray if v is not None])
        self.assertTrue(h.Add(11))
        self.assertEqual([11, 10, 4, 9], [v for v in h.HeapArray if v is not None])

    def test_GetMax(self):
        h = self.Heap()
        h.MakeHeap([11, 9, 4], 3)
        self.assertTrue(11, h.GetMax())
        self.assertEqual([9, 4], [v for v in h.HeapArray if v is not None])

        h = self.Heap()
        h.MakeHeap([11, 9, 4, 8, 7, 3], 2)
        self.assertTrue(h.IsValid())
        # self.assertEqual([11, 9, 8, 7, 4, 3], [v for v in h.HeapArray if v is not None])
        self.assertEqual([11, 9, 4, 8, 7, 3], [v for v in h.HeapArray if v is not None])
        self.assertTrue(11, h.GetMax())
        self.assertEqual([9, 8, 4, 3, 7], [v for v in h.HeapArray if v is not None])

        self.assertTrue(9, h.GetMax())
        self.assertEqual([8, 7, 4, 3], [v for v in h.HeapArray if v is not None])

        self.assertTrue(8, h.GetMax())
        self.assertEqual([7, 3, 4], [v for v in h.HeapArray if v is not None])

        self.assertTrue(7, h.GetMax())
        self.assertEqual([4, 3], [v for v in h.HeapArray if v is not None])

        self.assertTrue(4, h.GetMax())
        self.assertEqual([3], [v for v in h.HeapArray if v is not None])

        self.assertTrue(3, h.GetMax())
        self.assertEqual([], [v for v in h.HeapArray if v is not None])

        self.assertTrue(-1, h.GetMax())
        self.assertEqual([], [v for v in h.HeapArray if v is not None])

    def test_GetMax_many(self):
        array = [v for v in range(10)]
        h = self.Heap()
        h.MakeHeap([], 4)

        for e in array:
            h.Add(e)

        array.sort(reverse=True)
        for e in array:
            self.assertEqual(e, h.GetMax())

    def test_IsValid(self):
        h = self.Heap()
        h.MakeHeap([], 3)
        self.assertTrue(h.IsValid())

        h.Add(10)
        self.assertTrue(h.IsValid())

        h.Add(9)
        self.assertTrue(h.IsValid())

        h.HeapArray[0], h.HeapArray[1] = h.HeapArray[1], h.HeapArray[0]
        self.assertFalse(h.IsValid())

        h._rebuild_up(1)
        self.assertTrue(h.IsValid())


class TestTask7_2(TestTask7):
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("task7-2", "./DSA2/task7-2.py")
    task7_2 = importlib.util.module_from_spec(spec)
    sys.modules["task7-2"] = task7_2
    spec.loader.exec_module(task7_2)
    Heap = task7_2.Heap

    def test_FindMaxInRange(self):
        h = self.Heap()
        h.MakeHeap([], 3)
        self.assertIsNone(h.FindMaxInRange(5, 10))

        h.Add(7)
        self.assertEqual(7, h.FindMaxInRange(5, 10))

        h.Add(9)
        self.assertEqual(7, h.FindMaxInRange(5, 8))

        self.assertIsNone(h.FindMaxInRange(2, 6))
        self.assertIsNone(h.FindMaxInRange(10, 13))
        self.assertEqual(7, h.FindMaxInRange(7, 7))
        self.assertEqual(9, h.FindMaxInRange(9, 9))

        h = self.Heap()
        h.MakeHeap([11, 15, 17, 20, 40], 3)
        self.assertEqual(20, h.FindMaxInRange(15, 25))

    def test_FindMin(self):
        h = self.Heap()
        h.MakeHeap([], 3)
        self.assertIsNone(h.FindMin())

        h.Add(7)
        self.assertEqual(7, h.FindMin())

        h.Add(9)
        self.assertEqual(7, h.FindMin())

        h.Add(4)
        self.assertEqual(4, h.FindMin())
        h.Add(3)
        self.assertEqual(3, h.FindMin())
        h.Add(1)
        self.assertEqual(1, h.FindMin())

    def test_Merge(self):
        h1 = self.Heap()
        h1.MakeHeap([], 3)
        h2 = self.Heap()
        h2.MakeHeap([], 3)
        h1.Merge(h2)
        self.assertEqual([], [v for v in h1.HeapArray if v is not None])

        h1 = self.Heap()
        h1.MakeHeap([5, 10, 50], 3)
        h2 = self.Heap()
        h2.MakeHeap([3, 7, 200], 3)
        h1.Merge(h2)
        self.assertCountEqual(
            [200, 50, 10, 7, 5, 3], [v for v in h1.HeapArray if v is not None]
        )

        h1 = self.Heap()
        h1.MakeHeap([3, 7, 200], 3)
        h2 = self.Heap()
        h2.MakeHeap([5, 10, 50], 3)
        h1.Merge(h2)
        self.assertCountEqual(
            [200, 50, 10, 7, 5, 3], [v for v in h1.HeapArray if v is not None]
        )


if __name__ == "__main__":
    unittest.main()
