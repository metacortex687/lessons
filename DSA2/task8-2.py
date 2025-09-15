# Раздел: 8. Графы

# Задача 2
# Реализуйте направленный граф, представленный матрицей смежности, и добавьте метод проверки, будет ли он циклическим.

# Класс: DirectedGraph
# Метод: IsCyclic(self) -> bool:
# Вычислительная сложность: O(n^2) где n - колличество ребер
# Предпологаю, наихудшим графом с точки зрения вычислительной сложности является граф вытянутый в цепочку.
# Если одно из ребер этого графа уберем с этой цепочки, то колличество повторных проходов по нему уменьшится.
# И он будет лучше вытянутого в цепочку. 

# Решение:
# Последовательно перебираю все узлы как стартовые.
# При этом запоминаю уже посещенные узлы, и исключаю их, чтобы не зациклиться.
# В случае если при обходе графа возвращаюсь на стартовый узел, то в этом случае считаю граф циклическим.
# Когда больше некуда двигаться, то перехожу к следующему узлу.
# Если граф не оказался циклическим по алгоритму выше, то значит он ациклический.   


class Vertex:

    def __init__(self, val):
        self.Value = val


class DirectedGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: list[Vertex] = [None] * size

    def AddVertex(self, v):
        for i, _v in enumerate(self.vertex):
            if _v is None:
                self.vertex[i] = Vertex(v)
                return

    def RemoveVertex(self, v):
        i = self._find_vertex(v)
        if i is None:
            return
        self.vertex[i] = None

        for j in range(self.max_vertex):
            self.m_adjacency[i][j] = 0
            self.m_adjacency[j][i] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        i1 = self._find_vertex(v1)
        if i1 is None:
            return False

        i2 = self._find_vertex(v2)
        if i2 is None:
            return False

        return self.m_adjacency[i1][i2] == 1

    def AddEdge(self, v1: int, v2: int):
        i1 = self._find_vertex(v1)
        if i1 is None:
            return

        i2 = self._find_vertex(v2)
        if i2 is None:
            return

        self.m_adjacency[i1][i2] = 1
        self.m_adjacency[i2][i1] = -1

    def RemoveEdge(self, v1, v2):
        i1 = self._find_vertex(v1)
        if i1 is None:
            return

        i2 = self._find_vertex(v2)
        if i2 is None:
            return

        self.m_adjacency[i1][i2] = 0
        self.m_adjacency[i2][i1] = 0

    def _find_vertex(self, v: int) -> int | None:
        for i, _v in enumerate(self.vertex):
            if _v is None:
                continue
            if _v.Value == v:
                return i

        return None

    def IsCyclic(self) -> bool:
        for idx_start, vertex in enumerate(self.vertex):
            if vertex is None:
                continue
            idx_visited_nodes = {idx_start}
            idx_curent_nodes = [idx_start]

            while len(idx_curent_nodes) > 0:
                idx_next_nodes = []

                for idx_curent_node in idx_curent_nodes:
                    for j in range(self.max_vertex):
                        if self.m_adjacency[idx_curent_node][j] != 1:
                            continue

                        if j == idx_start:
                            return True

                        if j in idx_visited_nodes:
                            continue

                        idx_visited_nodes.add(j)
                        idx_next_nodes.append(j)

                idx_curent_nodes = idx_next_nodes

        return False
