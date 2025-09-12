class BSTNode:

    def __init__(self, key: int, parent: "BSTNode"):
        self.NodeKey: int = key
        self.Parent: "BSTNode" = parent
        self.LeftChild: "BSTNode" = None
        self.RightChild: "BSTNode" = None
        self.Level: int = 0

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

        return root_node.IsBalanced()
    
