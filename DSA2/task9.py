class SimpleTreeNode:

    def __init__(self, val, parent: "SimpleTreeNode" = None):
        self.NodeValue = val
        self.Parent: SimpleTreeNode = parent
        self.Children: list[SimpleTreeNode] = []
        self._count = None

    def _leaf_count(self) -> int:
        result = 0
        for child in self.Children:
            if len(child.Children) > 0:
                result += child._leaf_count()
                continue
            result += 1
        return result

    def _get_all_nodes(self):
        result = [self]
        for child in self.Children:
            result.extend(child._get_all_nodes())
        return result

    def _ClearCacheCount(self):
        self._count = None
        for child in self.Children:
            child._ClearCacheCount()

    def Count(self):
        if self._count is None:
            self._count = 1
            for child in self.Children:
                self._count += child.Count()

        return self._count

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

    def __repr__(self):
        return f"n{self.NodeValue}"


class SimpleTree:

    def __init__(self, root: SimpleTreeNode):
        self.Root: SimpleTreeNode = root
        if self.Root is not None:
            self.Root.Parent = None

    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

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

        self.Root._ClearCacheCount()

        return self.Root.Count()

    def LeafCount(self):
        if self.Root is None:
            return 0

        result = self.Root._leaf_count()

        if result == 0:
            return 1

        return result

    def EvenTrees(self):
        if self.Root is None:
            return []

        self.Root._ClearCacheCount()

        if self.Root.Count() % 2 == 1:
            return []

        return self.Root.EvenTrees()
