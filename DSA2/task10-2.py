# Раздел: 8. Чётные деревья и леса

# Задача 1
# Добавьте метод, проверяющий, будет ли текущий неориентированный граф связным.

# Класс: SimpleGraph
# Метод: IsConnected(self):
# Вычислительная сложность: O(n) - где n колличество ребер в графе

# Решение: выбираю первый узел и для всех связных узлов рекурсивно проставляю признак посещения.
# После чего перебираю все узлы и если хоть у одного узла, не стоит этот признак то значит граф несвязный.
# Иначе связный.


# Задача 2
# В ориентированном графе найдите длину самого длинного простого пути (пути без повторяющихся вершин).

# Класс: DirectedGraph
# Метод: MaxPath(self):
# Вычислительная сложность: O(n) - где n колличество ребер в графе

# Решение: Храню в узле признак посещения и длину максимального  пути из этого узла.
# Выбираю первый узел и рекурсивно проставляю максиамльный путь и признак посещения для узлов графа.
# Беру следующие все точки, и так же рекурсивно проставляю максиамльный путь и признак посещения для узлов графа.
# В случае если в узле уже есть признак посещения и стоит длинна максимального пути, то использую это значение.
#
# Исключаю циклы при подсчете, за счет того, что у узла есть два признака признак посещения и длинна максимального  пути.
# Вначале поиска максимального  пути сразу ставлю признак посещения узла.
# Но длинну максимального пути оставляю 0, а заполняю уже после того как найден максимальный путь для дочерних элементов.
# При этом подходе узел, который уже был посещен во время поиска максимального пути,
# не участвует в поиске и не искажает итоговый результат.


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.MaxPath = 0

    def __repr__(self):
        return f"v{self.Value}"


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: list[Vertex] = [None] * size

    def AddVertex(self, value) -> Vertex:
        for i, _v in enumerate(self.vertex):
            if _v is None:
                self.vertex[i] = Vertex(value)
                return self.vertex[i]

    def RemoveVertex(self, v):
        self.vertex[v] = None

        for j in range(self.max_vertex):
            self.m_adjacency[v][j] = 0
            self.m_adjacency[j][v] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        if self.vertex[v1] is None:
            return False

        if self.vertex[v2] is None:
            return False

        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch_WhithWhile(self, VFrom: int, VTo: int):

        for v in self.vertex:
            if v is None:
                continue
            v.Hit = False

        stack = Stack()
        stack_index = Stack()

        curent_index = VFrom
        curent_vertex = self.vertex[VFrom]
        curent_vertex.Hit = True
        stack.Push(curent_vertex)
        stack_index.Push(VFrom)

        while not stack.IsEmpty():

            curent_vertex = stack.Pop()
            curent_index = stack_index.Pop()
            stack.Push(curent_vertex)
            stack_index.Push(curent_index)

            if self.IsEdge(curent_index, VTo):
                stack.Push(self.vertex[VTo])
                return stack.ToList()

            next_vertex = None
            next_index = None
            for i in range(self.max_vertex):
                if not self.IsEdge(curent_index, i):
                    continue

                vertex = self.vertex[i]

                if vertex.Hit:
                    continue

                next_vertex = vertex
                next_index = i
                break

            if next_vertex is not None:
                stack.Push(next_vertex)
                stack_index.Push(next_index)

            if next_vertex is None:
                stack.Pop()
                stack_index.Pop()

        return []

    def DepthFirstSearch(self, VFrom: int, VTo: int):
        for v in self.vertex:
            if v is None:
                continue
            v.Hit = False

        return self._DepthFirstSearch(VFrom, VTo)

    def _DepthFirstSearch(self, VFrom: int, VTo: int):
        if self.IsEdge(VFrom, VTo):
            return [self.vertex[VFrom], self.vertex[VTo]]

        self.vertex[VFrom].Hit = True

        for i, vertex in enumerate(self.vertex):

            if vertex is None:
                continue

            if vertex.Hit:
                continue

            if not self.IsEdge(VFrom, i):
                continue

            vertex.Hit = True

            path = self._DepthFirstSearch(i, VTo)

            if len(path) > 0:
                return [self.vertex[VFrom]] + path

        return []

    def IsConnected(self):

        for v in self.vertex:
            if v is None:
                continue
            v.Hit = False

        is_empty = True
        for v in self.vertex:
            if v is None:
                continue
            is_empty = False
            break

        if is_empty:
            return False

        VFrom = None
        for i, _ in enumerate(self.vertex):
            if v is None:
                continue
            VFrom = i
            break

        self._SetHitInField(VFrom)

        for v in self.vertex:
            if v is None:
                continue
            if not v.Hit:
                return False

        return True

    def _SetHitInField(self, VFrom: int):
        self.vertex[VFrom].Hit = True

        for i, v in enumerate(self.vertex):
            if v is None:
                continue

            if v.Hit:
                continue

            if self.IsEdge(VFrom, i):
                self._SetHitInField(i)


class DirectedGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: list[Vertex] = [None] * size

    def AddVertex(self, value):
        for i, _v in enumerate(self.vertex):
            if _v is None:
                self.vertex[i] = Vertex(value)
                return

    def RemoveVertex(self, v):
        self.vertex[v] = None

        for j in range(self.max_vertex):
            self.m_adjacency[v][j] = 0
            self.m_adjacency[j][v] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = -1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def MaxPath(self) -> int:
        is_empty = True
        for v in self.vertex:
            if v is None:
                continue
            v.MaxPath = 0
            v.Hit = False
            is_empty = False

        if is_empty:
            return 0

        max_path = 0
        for i, v in enumerate(self.vertex):
            if v is None:
                continue
            if v.Hit:
                continue

            max_path = max(max_path, self._MaxPath(i))

        return max_path

    def _MaxPath(self, VFrom: int):
        if self.vertex[VFrom].Hit:
            return self.vertex[VFrom].MaxPath

        self.vertex[VFrom].Hit = True

        max_child_path = 0
        for i, vertex in enumerate(self.vertex):
            if vertex is None:
                continue
            if i == VFrom:
                continue

            if not self.IsEdge(VFrom, i):
                continue

            max_child_path = max(max_child_path, self._MaxPath(i))

        self.vertex[VFrom].MaxPath = 1 + max_child_path

        return self.vertex[VFrom].MaxPath


class Stack:

    def __init__(self):
        self.elements = []

    def Push(self, val):
        self.elements.append(val)

    def Pop(self):
        if self.IsEmpty():
            return None

        return self.elements.pop()

    def IsEmpty(self):
        return len(self.elements) == 0

    def ToList(self):
        return self.elements.copy()
