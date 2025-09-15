class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

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
        self.m_adjacency[i2][i1] = 1

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
