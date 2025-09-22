# Раздел: 11. Поиск пути в графе (обход в ширину)


# Задача 2
# Используя BFS, найдите два наиболее удалённых друг от друга узла в обычном дереве

# Класс: SimpleTree
# Метод: FindTreeDiameter(self):
# Вычислительная сложность: O(n) - где n колличество ребер в графе

# Решение: Нахожу наиболее удаленный от корня узел (до него максимальный путь).
# И далее методом BFS от него делаю обход узлов, самый последний является самым удаленным.
# Для вычисления, расстояний при распространении передаю, минимальный уровень который был посещен при распространении (уровень горки).
# Расстояние это уровень стартового узла минус минимальный уровень на пути, плюс уровень конечного узла минус минимальный уровень на пути.


# Задача 3
# Добавьте метод, который находит все циклы в текущем (неориентированном) графе с использованием BFS.

# Класс: SimpleGraph
# Метод: FindAllCicles(self) -> list[list[int]]:
# Вычислительная сложность: O(n*m) - где n - колличество связей в графе, а m - количество петель.

# Решение:
# Перебираю узлы графа алгоритмом BFS.
# Сохраняю в узле в "self.visited_from: set[int]"посещенные узлы.
# Непустой "visited_from" является признаком того что узел был посещен уже.
# В этом случае ищу пересечени множеств для этого узла и текущего.
# Так получаю индексы общих точек.

# Восстанавливаю методом BreadthFirstSearch пути до этих точек.
# В случае если эти пути содержат общие точки, значит фигура похожа на "эскимо", они имеют общий путь.
# Тогда убираю из дальнейшего распространения.

# Если нет общих точек, то соединяю эти пути как цикл и возвращаю массив.
# Для удобства тестирования, массив привожу к виду, что бы первый индекс был наименьшим во всем списке.
# И второй индекс, так как возможен обход в двух направлениях, был наименьшим из возможных.
#
# Допускаю, что граф может быть не полносвязным. Для этого повторяю эту операцию для всех узлов,
#  которые не участововали в этом алгоритме. Определяю по пустому множеству "visited_from"


class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False
        self.PrevNode: Vertex = None
        self.visited_from: set[int] = set()
        self.idx_in_node = None

    def __repr__(self):
        return f"v{self.Value}"

    def PathTo(self):
        if self.PrevNode is None:
            return [self]
        return self.PrevNode.PathTo() + [self]


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex: list[Vertex | None] = [None] * size

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

    def BreadthFirstSearch(self, VFrom, VTo):

        if VFrom == VTo:
            return [VFrom]
        
        for v in self.vertex:
            if v is None:
                continue
            v.Hit = False
            v.PrevNode = None

        queue = Queue()
        queue.enqueue(VFrom)

        curent_index = None
        curent_vertex = None

        while not queue.IsEmpty():
            curent_index = queue.dequeue()
            curent_vertex = self.vertex[curent_index]
            curent_vertex.Hit = True

            for i, vertex in enumerate(self.vertex):

                if vertex is None:
                    continue

                if not self.IsEdge(curent_index, i):
                    continue

                if vertex.Hit:
                    continue

                self.vertex[i].PrevNode = curent_vertex

                if i == VTo:
                    return self.vertex[i].PathTo()

                queue.enqueue(i)

        return []

    def FindAllCicles(self) -> list[list[int]]:
        for i, v in enumerate(self.vertex):
            if v is None:
                continue
            v.visited_from = set()
            v.idx_in_node = i

        result = []

        for i, v in enumerate(self.vertex):
            if v is None:
                continue
            if len(v.visited_from) > 0:
                continue

            result.extend(self.FindAllCiclesInField(i))

        return result

    def FindAllCiclesInField(self, VFrom: int):

        result = []

        queue = Queue()
        queue.enqueue(VFrom)
        self.vertex[VFrom].visited_from.add(VFrom)

        curent_index = None
        curent_vertex = None

        while not queue.IsEmpty():

            curent_index = queue.dequeue()
            curent_vertex = self.vertex[curent_index]

            for i, vertex in enumerate(self.vertex):
                if vertex is None:
                    continue

                if not self.IsEdge(curent_index, i):
                    continue

                if i in curent_vertex.visited_from:
                    continue

                intersection_visiteds = curent_vertex.visited_from.intersection(
                    vertex.visited_from
                )

                for idx_intersection in intersection_visiteds:
                    path = self._BreadthFirstSearchCicle(
                        idx_intersection, curent_index, i
                    )
                    if path is None:
                        curent_vertex.visited_from.remove(idx_intersection)
                        # vertex.visited_from.remove(idx_intersection)
                        continue
                    result.append(path)

                if len(self.vertex[i].visited_from) == 0:
                    self.vertex[i].visited_from = curent_vertex.visited_from.copy()
                    queue.enqueue(i)

                self.vertex[i].visited_from.add(curent_index)

        return result

    def _BreadthFirstSearchCicle(self, VFrom: int, VTo1: int, VTo2: int):

        path1 = self.BreadthFirstSearch(VFrom, VTo1)
        path2 = self.BreadthFirstSearch(VFrom, VTo2)
        path1 = [n.idx_in_node for n in path1]
        path2 = [n.idx_in_node for n in path2]

        set1 = set(path1)
        set1.remove(VFrom)
        set2 = set(path2)
        set2.remove(VFrom)

        if len(set1.intersection(set2)) != 0:
            return None

        result1 = path1[1:] + list(reversed(path2))
        result2 = path2[1:] + list(reversed(path1))

        result1 = self.rotate_list_from_min(result1)
        result2 = self.rotate_list_from_min(result2)

        if result1[1] < result2[1]:
            return result1

        return result2

    def rotate_list_from_min(self, lst: list[int]) -> list[int]:
        if len(lst) == 0:
            return []

        queue = Queue()

        min_value = lst[0]

        for v in lst:
            queue.enqueue(v)
            min_value = min(min_value, v)

        rotaded = []
        found_min = False

        while not queue.IsEmpty():
            v = queue.dequeue()
            if v == min_value:
                found_min = True

            if found_min:
                rotaded.append(v)
                continue

            queue.enqueue(v)

        return rotaded


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


class Queue:
    def __init__(self):
        self._size = 0
        self._queue = LinkedList2()

    def enqueue(self, item):
        self._size += 1
        self._queue.add_in_head(Node(item))

    def dequeue(self):
        if self._size > 0:
            self._size -= 1
        else:
            return None

        result = self._queue.tail().value

        self._queue.delete_tail()

        return result

    def IsEmpty(self):
        return self._size == 0

    def size(self):
        return self._size


class Node:
    def __init__(self, v, is_dummy=False):
        self.value = v
        self.prev: Node = None
        self.next: Node = None
        self.is_dummy: bool = is_dummy


class LinkedList2:
    def __init__(self):
        self._dummy = Node(None, is_dummy=True)
        self._dummy.next, self._dummy.prev = self._dummy, self._dummy

    def head(self) -> Node:
        return None if self._dummy.next.is_dummy else self._dummy.next

    def tail(self) -> Node:
        return None if self._dummy.prev.is_dummy else self._dummy.prev

    def add_in_head(self, newNode: Node):
        self._dummy.next.prev = newNode
        newNode.next = self._dummy.next
        newNode.prev = self._dummy
        self._dummy.next = newNode

    def delete_tail(self):
        self._dummy.prev.prev.next = self._dummy
        self._dummy.prev = self._dummy.prev.prev


class SimpleTreeNode:

    def __init__(self, val, parent: "SimpleTreeNode" = None):
        self.NodeValue = val
        self.Parent: SimpleTreeNode = parent
        self.Children: list[SimpleTreeNode] = []
        self.Level = 0
        self._cache_count = None
        self._cache_max_path = None
        self._cache_min_path = None
        self.Hit = False
        self.MinLevelInPath = None

    def _get_all_nodes(self):
        result = [self]
        for child in self.Children:
            result.extend(child._get_all_nodes())
        return result

    def _ClearCache(self):
        self._cache_count = None
        self._cache_max_path = None
        self._cache_min_path = None
        self.Hit = False
        self.MinLevelInPath = None
        for child in self.Children:
            child._ClearCache()

    def Count(self):
        if self._cache_count is not None:
            return self._cache_count

        self._cache_count = 1
        for child in self.Children:
            self._cache_count += child.Count()

        return self._cache_count

    def _find_nodes_by_value(self, val):
        result = []
        if self.NodeValue == val:
            result.append(self)

        for child in self.Children:
            result.extend(child._find_nodes_by_value(val))

        return result

    def EvenTrees(self):
        result = []
        for child in self.Children:
            if child.Count() % 2 == 0:
                result.append(self)
                result.append(child)

            result.extend(child.EvenTrees())

        return result

    def SortChildren(self):
        self.Children.sort(key=lambda node: node.NodeValue)

    def _ClearCacheUp(self):
        if (
            self._cache_count == None
            and self._cache_max_path == None
            and self._cache_min_path == None
        ):
            return

        self._cache_count = None
        self._cache_max_path = None
        self._cache_min_path = None

        if self.Parent is not None:
            self.Parent._ClearCacheUp()

    def _NodeAtMinPath(self) -> "SimpleTreeNode":
        if len(self.Children) < 2:
            return self

        if self.Children[0].MinPath() > self.Children[1].MinPath():
            return self.Children[1]._NodeAtMinPath()

        return self.Children[0]._NodeAtMinPath()

    def _NodeAtMaxPath(self) -> "SimpleTreeNode":
        if len(self.Children) == 0:
            return self

        if len(self.Children) == 1:
            return self.Children[0]._NodeAtMaxPath()

        if self.Children[0].MaxPath() > self.Children[1].MaxPath():
            return self.Children[0]._NodeAtMaxPath()

        return self.Children[1]._NodeAtMaxPath()

    def __repr__(self):
        return f"n{self.NodeValue}"

    def MaxPath(self) -> int:
        if self._cache_max_path is not None:
            return self._cache_max_path

        if len(self.Children) == 0:
            self._cache_max_path = 0
            return self._cache_max_path

        self._cache_max_path = 0
        for child in self.Children:
            self._cache_max_path = max(self._cache_max_path, child.MaxPath())

        self._cache_max_path += 1

        return self._cache_max_path

    def MinPath(self) -> int:
        if self._cache_min_path is not None:
            return self._cache_min_path

        if len(self.Children) < 2:
            self._cache_min_path = 0
            return self._cache_min_path

        self._cache_min_path = self.Children[0].MinPath()
        self._cache_min_path = min(self._cache_min_path, self.Children[1].MinPath())

        self._cache_min_path += 1

        return self._cache_min_path

    def AddChild(self, NewChild: "SimpleTreeNode"):
        if NewChild is None:
            return

        if NewChild.Parent is not None:
            NewChild.Parent.Children.remove(NewChild)
            NewChild.Parent.SortChildren()

        NewChild.Parent = self
        self.Children.append(NewChild)
        self.SortChildren()

    def CountEvenSubtrees(self):
        result = 0
        if self.Count() % 2 == 0:
            result = 1

        for child in self.Children:
            result += child.CountEvenSubtrees()

        return result

    def AddValue(self, val):
        if len(self.Children) < 2:
            self.AddChild(SimpleTreeNode(val, None))
            return

        if self.NodeValue <= val:
            self.Children[1].AddValue(val)

        self.Children[0].AddValue(val)

    def _SetLevel(self, level):
        self.Level = level

        for child in self.Children:
            child._SetLevel(level + 1)

    def Vertex(self) -> list["SimpleTreeNode"]:
        result = []
        if self.Parent is not None:
            result.append(self.Parent)

        result.extend(self.Children)

        return result


class SimpleTree:

    def __init__(self, root: SimpleTreeNode):
        self.Root: SimpleTreeNode = root
        if self.Root is not None:
            self.Root.Parent = None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        if NewChild is None:
            return

        if ParentNode is None:
            self.Root = NewChild
            NewChild.Parent = None
            return

        ParentNode.AddChild(NewChild)

    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        if NodeToDelete == self.Root:
            self.Root = None
            return

        NodeToDelete.Parent.Children.remove(NodeToDelete)
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None:
            return []

        return self.Root._get_all_nodes()

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []

        return self.Root._find_nodes_by_value(val)

    def MoveNode(self, OriginalNode: SimpleTreeNode, NewParent: SimpleTreeNode):
        OriginalNode.Parent.Children.remove(OriginalNode)
        NewParent.Children.append(OriginalNode)
        OriginalNode.Parent = NewParent

    def Count(self):
        if self.Root is None:
            return 0

        self.Root._ClearCache()
        return self.Root.Count()

    def EvenTrees(self):
        if self.Root is None:
            return []

        self.Root._ClearCache()

        if self.Root.Count() % 2 == 1:
            return []

        return self.Root.EvenTrees()

    def CountEvenSubtrees(self):
        if self.Root is None:
            return 0

        self.Root._ClearCache()

        return self.Root.CountEvenSubtrees()

    def MinPath(self):
        if self.Root is None:
            return -1

        self.Root._ClearCache()
        return self.Root.MinPath()

    def MaxPath(self):
        if self.Root is None:
            return -1

        self.Root._ClearCache()
        return self.Root.MaxPath()

    def AddValue(self, val):
        if self.Root is None:
            self.Root = SimpleTreeNode(val, None)
            return

        self.Root.AddValue(val)

    def FindTreeDiameter(self):
        if self.Root is None:
            return 0

        self.Root._ClearCache()
        self.Root._SetLevel(0)
        max_deep_node = self.Root._NodeAtMaxPath()
        max_deep_node.MinLevelInPath = max_deep_node.Level

        queue = Queue()
        queue.enqueue(max_deep_node)
        max_deep_node.Hit = True

        curent_vertex = None
        while not queue.IsEmpty():
            curent_vertex = queue.dequeue()

            for vertex in curent_vertex.Vertex():

                if vertex.Hit:
                    continue
                vertex.Hit = True

                vertex.MinLevelInPath = min(vertex.Level, curent_vertex.MinLevelInPath)

                queue.enqueue(vertex)

        return (max_deep_node.Level - curent_vertex.MinLevelInPath) + (
            curent_vertex.Level - curent_vertex.MinLevelInPath
        )
