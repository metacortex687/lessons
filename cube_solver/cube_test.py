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

    def test_copy(self):
        f = Face([0, 1, 2, 3])
        copy = f.copy()

        self.assertFalse(f is copy)
        self.assertTrue(f == copy)
        self.assertFalse(f.data is copy.data)


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

    def test_copy(self):
        random.seed(42)
        cube = Cube.init_random()
        copy = cube.copy()

        self.assertFalse(cube is copy)
        self.assertTrue(cube == copy)

    def test_eq_rotate_empty(self):
        empty = Cube.init_empty()

        self.assertTrue(empty == empty.rotate_x())
        self.assertTrue(empty == empty.rotate_y())
        self.assertTrue(empty == empty.rotate_z())

    def test_add_cube_in_set(self):
        cube1 = Cube.init_empty()
        cube1.t = Face("bbbb")

        s = set()
        s.add(cube1)

        self.assertTrue(cube1 in s)

        cube2 = Cube.init_empty()
        self.assertFalse(cube2 in s)

        cube2.t = Face("bbbb") 
        self.assertTrue(cube2 in s) 

        self.assertEqual(1,len(s))

        s.add(cube2)
        self.assertEqual(1,len(s))

        s.add(Cube.init_empty())
        self.assertEqual(2,len(s))

    def test_rotate_x_standart(self):
        cube = Cube.init_standart()
        self.assertFalse(cube == cube.rotate_x())
        self.assertFalse(cube == cube.rotate_x().rotate_x())
        self.assertFalse(cube == cube.rotate_x().rotate_x().rotate_x())
        self.assertTrue(cube == cube.rotate_x().rotate_x().rotate_x().rotate_x())

    def test_rotate_y_standart(self):
        cube = Cube.init_standart()
        self.assertFalse(cube == cube.rotate_y())
        self.assertFalse(cube == cube.rotate_y().rotate_y())
        self.assertFalse(cube == cube.rotate_y().rotate_y().rotate_y())
        self.assertTrue(cube == cube.rotate_y().rotate_y().rotate_y().rotate_y())

    def test_rotate_z_standart(self):
        cube = Cube.init_standart()
        self.assertFalse(cube == cube.rotate_z())
        self.assertFalse(cube == cube.rotate_z().rotate_z())
        self.assertFalse(cube == cube.rotate_z().rotate_z().rotate_z())
        self.assertTrue(cube == cube.rotate_z().rotate_z().rotate_z().rotate_z())

if __name__ == "__main__":
    unittest.main()
