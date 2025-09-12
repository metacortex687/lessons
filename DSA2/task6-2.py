# Раздел: 6. Строим сбалансированные двоичные деревья поиска (2)

# Задача 2
# Добавьте метод проверки, действительно ли дерево получилось правильным

# Класс: BalancedBST
# Метод: IsValidBST(self) -> bool:
# Вычислительная сложность:  O(n) - где n количество узлов в дереве

# Решение:
# Рекурсивно проверяю условие на правильность ключа для всех непустых потомков

# Задача 4
# Добавьте метод проверки, действительно ли дерево получилось сбалансированным

# Класс: BalancedBST
# Метод: IsBalanced(self) -> bool:
# Вычислительная сложность:  O(n) - где n количество узлов в дереве

# Решение:
# Рассматривался вариант решения, полностью повторяющий условие задачи. 
# Но в этом случае, если не кэшировать определение глубины поддерева, то в этом случае алгоритмическая сложность O(n^2).
#     
# Использую вариант решения, когда определяю максимальный и минимальный путь до узлов, в которых хотя бы один потомок пустой.
# И если разница между этими путями больше 1, тогда дерево не сбалансировано. 
#  
# При определении максимального и минимального пути, использую поле "Level" в узле, предполагая, что оно заполнено верно.


class BSTNode:

    def __init__(self, key: int, parent: "BSTNode"):
        self.NodeKey: int = key  # ключ узла
        self.Parent: "BSTNode" = parent  # родитель или None для корня
        self.LeftChild: "BSTNode" = None  # левый потомок
        self.RightChild: "BSTNode" = None  # правый потомок
        self.Level: int = 0  # уровень узла

    def WideAllNodes(self) -> list["BSTNode"]:
        nodes = [self]
        start_position = 0
        count = 1

        while count > 0:
            end_position = start_position + count - 1
            count = 0
            for i in range(start_position, end_position + 1):
                if nodes[i].LeftChild is not None:
                    nodes.append(nodes[i].LeftChild)
                    count += 1
                if nodes[i].RightChild is not None:
                    nodes.append(nodes[i].RightChild)
                    count += 1
                start_position += 1

        return nodes

    def MaxPath(self):
        if self.LeftChild is None and self.RightChild is None:
            return self.Level

        if self.RightChild is None:
            return self.LeftChild.MaxPath()

        if self.LeftChild is None:
            return self.RightChild.MaxPath()

        return max(self.LeftChild.MaxPath(), self.RightChild.MaxPath())

    def MinPath(self):
        if self.LeftChild is None or self.RightChild is None:
            return self.Level

        return min(self.LeftChild.MinPath(), self.RightChild.MinPath())

    def IsBalanced(self):
        return self.MaxPath() - self.MinPath() <= 1

    def IsValidBST(self) -> bool:

        result = True

        if self.LeftChild is not None:
            result = (
                result
                and self.LeftChild.NodeKey < self.NodeKey
                and self.LeftChild.IsValidBST()
            )

        if self.RightChild is not None:
            result = (
                result
                and self.RightChild.NodeKey > self.NodeKey
                and self.RightChild.IsValidBST()
            )

        return result


class BalancedBST:

    def __init__(self):
        self.Root: BSTNode = None

    def GenerateTree(self, a: list) -> None:
        if len(a) == 0:
            self.Root = None
            return

        self._GenerateTree(sorted(a), 0, len(a) - 1, None, 0)

    def _GenerateTree(self, sorted_a, left_index, right_index, parent: BSTNode, level):
        mid_index = (left_index + right_index + 1) // 2
        node = BSTNode(sorted_a[mid_index], parent)
        node.Level = level

        if parent is None:
            self.Root = node

        if parent is not None and parent.NodeKey > node.NodeKey:
            parent.LeftChild = node

        if parent is not None and parent.NodeKey < node.NodeKey:
            parent.RightChild = node

        if left_index == right_index:
            return

        self._GenerateTree(sorted_a, left_index, mid_index - 1, node, level + 1)

        if right_index != mid_index:
            self._GenerateTree(sorted_a, mid_index + 1, right_index, node, level + 1)

    def WideAllNodes(self) -> list[BSTNode]:
        if self.Root is None:
            return []

        return self.Root.WideAllNodes()

    def IsBalanced(self, root_node: BSTNode) -> bool:
        if root_node is None:
            return True

        return root_node.IsBalanced()  # сбалансировано ли дерево с корнем root_node

    def IsValidBST(self) -> bool:
        if self.Root is None:
            return True

        return self.Root.IsValidBST()
