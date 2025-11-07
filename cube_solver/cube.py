from datetime import date
import random


class Face:
    def __init__(self, data: list | str):
        self.data = list(data)

    def __eq__(self, value: False):
        return self.data == value.data

    def eq_f(self) -> "Face":
        return Face(self.data.copy())

    def eq_r(self) -> "Face":
        return Face([self.data[3], self.data[0], self.data[1], self.data[2]])

    def eq_rt(self) -> "Face":
        return Face([self.data[3], self.data[0], self.data[1], self.data[2]])

    def __str__(self):
        return f"[{self.data[0]},{self.data[1]},{self.data[2]},{self.data[3]}]"

    def copy(self):
        return Face(self.data)


class Cube:

    def __init__(self, t: Face, b: Face, d: Face, f: Face, l: Face, r: Face):
        self.t = t
        self.b = b
        self.d = d
        self.f = f
        self.l = l
        self.r = r

    def __eq__(self, v: "Cube"):
        return (
            self.t == v.t
            and self.b == v.b
            and self.d == v.d
            and self.f == v.f
            and self.l == v.l
            and self.r == v.r
        )

    def __hash__(self):
        return self.__str__().__hash__()

    def __str__(self):
        return f"top{str(self.t)}back{str(self.b)}down{str(self.d)}front{str(self.f)}left{str(self.l)}right{str(self.r)}"

    @staticmethod
    def init_empty() -> "Cube":
        return Cube(
            Face("xxxx"),
            Face("xxxx"),
            Face("xxxx"),
            Face("xxxx"),
            Face("xxxx"),
            Face("xxxx"),
        )

    @staticmethod
    def init_random() -> "Cube":
        lst = list(range(24))
        random.shuffle(lst)
        return Cube(
            Face(lst[0:4]),
            Face(lst[4:8]),
            Face(lst[8:12]),
            Face(lst[12:16]),
            Face(lst[16:20]),
            Face(lst[20:24]),
        )

    @staticmethod
    def init_standart() -> "Cube":
        return Cube(
            Face("1111"),
            Face("2222"),
            Face("3333"),
            Face("4444"),
            Face("5555"),
            Face("6666"),
        )

    def copy(self) -> "Cube":
        return Cube(
            t=self.t.copy(),
            b=self.b.copy(),
            d=self.d.copy(),
            f=self.f.copy(),
            l=self.l.copy(),
            r=self.r.copy(),
        )

    def rotate_z(self) -> "Cube":
        return Cube(
            f=self.f.copy(),
            b=self.b.copy(),
            r=self.t.copy(),
            d=self.r.copy(),
            l=self.d.copy(),
            t=self.l.copy(),
        )

    def rotate_y(self) -> "Cube":
        return Cube(
            t=self.t.copy(),
            d=self.d.copy(),
            f=self.r.copy(),
            l=self.f.copy(),
            b=self.l.copy(),
            r=self.b.copy(),
        )

    def rotate_x(self) -> "Cube":
        return Cube(
            t=self.f.copy(),
            b=self.t.copy(),
            d=self.b.copy(),
            f=self.d.copy(),
            l=self.l.copy(),
            r=self.r.copy(),
        )
