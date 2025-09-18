# Раздел: 8. Чётные деревья и леса

# Задача 2
# Добавьте метод, который сбалансирует чётное двоичное дерево.

# Класс: SimpleTreeNode
# Метод: Rebalance(self):
# Вычислительная сложность: в лучшем случае O(m * log n) где n - количество элементов, а m - количество элементов
# которые требуется переместить для восстановления баланса. В худшем O(n^2) в случае если элементы вытянуты в цепочку.

# Решение:
# Определяю максимальный путь от вершины, до узлов у которых нет потомков.
# И минимальный путь от вершины, до узла у которого не хватает хотя бы одного потомка.
# В случае если разница между ними больше 1, значит дерево несбалансированно.
# И буду выполнять балансировку, пока дерево не станет сбалансированным.
#
# Вставляю узел до которого максимальный путь,в виде потомка к элементу до которого минимальный путь.
# И далее он "всплывает" вверх ("BubbleUp()"), пока не упрется в родителя у которого значение больше или равно чем у него.
# При всплывании отслеживаю, чтобы сохранялся корректный порядок дочерних узлов.
#
# Получение минимального и максимального пути кэширую храня значение в узлах.
# Пространственная сложность (по памяти) при кэшировании сохраняется неизменной O(n).
# При первом вызове "Rebalance" получение максимального и минимального пути занимает О(n) времени.
# Поскольку очищаю путь вверх до корня при изменениях потомков у узлов, последующие вызовы занимают в лучшем случае O(log n).
# В худшем O(n)


# Задача 3
# Добавьте метод, который для любого заданного подузла текущего дерева определит общее количество чётных поддеревьев.

# Класс: SimpleTreeNode
# Метод: CountEvenSubtrees(self) -> int:
# Вычислительная сложность: O(n) где n - чисол элементов в дереве

# Решение: рекурсивно считаю колличество узлов.
# Количество узлов кэшируется, что позволяет исключить квадратичную алогоритмическую сложность.


class SimpleTreeNode:

    def __init__(self, val, parent: "SimpleTreeNode" = None):
        self.NodeValue = val
        self.Parent: SimpleTreeNode = parent
        self.Children: list[SimpleTreeNode] = []
        self._cache_count = None
        self._cache_max_path = None
        self._cache_min_path = None

    def _get_all_nodes(self):
        result = [self]
        for child in self.Children:
            result.extend(child._get_all_nodes())
        return result

    def _ClearCache(self):
        self._cache_count = None
        self._cache_max_path = None
        self._cache_min_path = None
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

    def Rebalance(self):

        if self.MaxPath() - self.MinPath() < 2:
            return None

        node_moved = self._NodeAtMaxPath()
        node_start_parent = self._NodeAtMinPath()

        node_moved._ClearCacheUp()
        node_start_parent._ClearCacheUp()

        node_start_parent.AddChild(node_moved)
        upper_bound_parent = node_moved.BubbleUp()
        node_moved._ClearCacheUp()

        # if upper_bound_parent is not None:
        #     upper_bound_parent._ClearCacheUp()

        new_root = None
        if upper_bound_parent is None:
            new_root = node_moved

        next_new_root = None

        if new_root is None:
            next_new_root = self.Rebalance()

        if new_root is not None:
            next_new_root = new_root.Rebalance()

        if next_new_root is not None:
            return next_new_root

        return new_root

    def BubbleUp(self) -> "SimpleTreeNode":
        if self.Parent is None:
            return None

        if self.Parent.NodeValue >= self.NodeValue:
            return self.Parent

        self.Parent.Children, self.Children = self.Children, self.Parent.Children

        if self.Parent is not None:
            for child in self.Parent.Children:
                child.Parent = self.Parent

        self.Children.remove(self)
        self.Children.append(self.Parent)
        self.SortChildren()
        self.Parent.SortChildren()

        if self.Parent.Parent is not None:
            self.Parent.Parent.Children.remove(self.Parent)
            self.Parent.Parent.Children.append(self)
            self.Parent.Parent.SortChildren()

        self.Parent.Parent, self.Parent = self, self.Parent.Parent

        for child in self.Children:
            child.Parent = self

        return self.BubbleUp()

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

    def Rebalance(self):
        if self.Root is None:
            return

        self.Root._ClearCache()
        new_root = self.Root.Rebalance()
        if new_root is not None:
            self.Root = new_root

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
