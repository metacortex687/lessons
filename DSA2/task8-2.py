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
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

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
