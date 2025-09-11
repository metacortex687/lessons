# Раздел: 6. Строим сбалансированные двоичные деревья поиска (2)

# Задача 2 
# Добавьте метод проверки, действительно ли дерево получилось правильным 

# Класс: BalancedBST 
# Метод: IsValidBST(self) -> bool:
# Вычислительная сложность:  O(n) - где n количество узлов в дереве

# Решение: 
# Рекурсивно проеряю условие на правильность ключа для всех непустых потомков

# Задача 4 
# Добавьте метод проверки, действительно ли дерево получилось сбалансированным 

# Класс: BalancedBST 
# Метод: IsBalanced(self) -> bool:
# Вычислительная сложность:  O(n^2) - где n количество узлов в дереве

# Решение: 
# O(n^2) получается так как приходится проверять для каждого узал максимаьлную глубину его потомков
# надо считать как мах Level и MinLevel
# использую заполненное поле левел  


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

    def MaxLevel(self):
        if self.LeftChild is None and self.RightChild is None:
            return self.Level

        if self.RightChild is None:
            return self.LeftChild.MaxLevel()

        if self.LeftChild is None:
            return self.RightChild.MaxLevel()

        return max(self.LeftChild.MaxLevel(), self.RightChild.MaxLevel())

    def IsBalanced(self):
        if self.LeftChild is None and self.RightChild is None:
            return True

        if self.RightChild is None:
            return self.LeftChild.IsBalanced() and (
                self.LeftChild.MaxLevel() - self.Level <= 1
            )

        if self.LeftChild is None:
            return self.RightChild.IsBalanced() and (
                self.RightChild.MaxLevel() - self.Level <= 1
            )

        left_max_level = self.LeftChild.MaxLevel()
        right_max_level = self.RightChild.MaxLevel()
        hight_difference = max(right_max_level, left_max_level) - min(
            right_max_level, left_max_level
        )

        return (
            self.LeftChild.IsBalanced()
            and self.RightChild.IsBalanced()
            and hight_difference <= 1
        )

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
        self.Root: BSTNode = None  # корень дерева

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
