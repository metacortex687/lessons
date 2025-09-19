# Section: 8. Even Trees and Forests
#
# Task
# Add a method that returns the path between vertices of an undirected graph
#
# Class: SimpleGraph
# Method: DepthFirstSearch(self):
# Time Complexity: O(n) - where n is the number of edges in the graph
#
# Solution: I considered two approaches — one uses an explicit stack and a while loop
# (method DepthFirstSearch_WithWhile).
# The other uses the call stack of recursion (method DepthFirstSearch).


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False

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

