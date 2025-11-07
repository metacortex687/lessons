import unittest
from cube import Face, Cube
import random

# python ./DSA1/task3-3.py


class TestFace(unittest.TestCase):
    def test_eq(self):
        f1 = Face([0, 1, 2, 3])
        f2 = Face([0, 1, 2, 3])
        f3 = Face([1, 0, 2, 3])

        self.assertTrue(f1 == f2)
        self.assertFalse(f1 == f3)
        self.assertTrue(f1 == f1)

    def test_in(self):

        f1 = Face([0, 1, 2, 3])
        f2 = Face([0, 1, 2, 3])
        f3 = Face([1, 0, 2, 3])

        lst = [f3]

        self.assertFalse(f1 in lst)

        lst.append(f2)
        self.assertTrue(f1 in lst)

    def test_eq_f(self):
        f1 = Face([0, 1, 2, 3])
        f2 = Face([0, 1, 2, 3])
        self.assertTrue(f1.eq_f() == f2)

    def test_eq_r(self):
        f1 = Face([0, 1, 2, 3])
        f2 = Face([3, 0, 1, 2])
        self.assertTrue(f1.eq_r() == f2)

    def test_eq_rt(self):
        f1 = Face([0, 1, 2, 3])
        f2 = Face([3, 0, 1, 2])
        self.assertTrue(f1.eq_rt() == f2)


class TestCube(unittest.TestCase):
    def test_eq(self):
        c1 = Cube(
            Face([0, 1, 2, 3]),
            Face([4, 5, 6, 7]),
            Face([8, 9, 10, 11]),
            Face([12, 13, 14, 15]),
            Face([16, 17, 18, 19]),
            Face([20, 21, 22, 23]),
        )
        c2 = Cube(
            Face([0, 1, 2, 3]),
            Face([4, 5, 6, 7]),
            Face([8, 9, 10, 11]),
            Face([12, 13, 14, 15]),
            Face([16, 17, 18, 19]),
            Face([20, 21, 22, 23]),
        )
        self.assertTrue(c1 == c2)

    def test_init_empty(self):
        c1 = Cube.init_empty()
        c2 = Cube.init_empty()
        self.assertEqual(c1, c2)

    def test_str(self):
        empty = Cube.init_empty()
        empty.l = Face([1, 2, 3, 4])
        self.assertEqual(
            "top[x,x,x,x]back[x,x,x,x]down[x,x,x,x]front[x,x,x,x]left[1,2,3,4]right[x,x,x,x]",
            str(empty),
        )

    def test_init_random(self):
        random.seed(42)
        random1 = Cube.init_random()
        empty = Cube.init_empty()
        self.assertTrue(empty != random1)

        random2 = Cube.init_random()
        self.assertTrue(random1 != random2)

        random.seed(42)
        random3 = Cube.init_random()
        self.assertTrue(random1 == random3)

    def test_eq_rotate_empty(self):
        empty = Cube.init_empty()

        rotate_f = empty.rotate_z()
        rotate_f = empty.rotate_y()
        rotate_f = empty.rotate_x()


if __name__ == "__main__":
    unittest.main()
