class SimpleTreeNode:
	
    def __init__(self, val, parent: 'SimpleTreeNode' = None):
        self.NodeValue = val 
        self.Parent: SimpleTreeNode = parent 
        self.Children:list[SimpleTreeNode] = [] 

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
    
    def _count(self):
        result = 1
        for child in self.Children:
            result += child._count()
        return result
    
    def _find_nodes_by_value(self,val):
        result = []
        if self.NodeValue == val:
            result.append(self)

        for child in self.Children:
            result.extend(child._find_nodes_by_value(val))

        return result
        
	
class SimpleTree:

    def __init__(self, root: SimpleTreeNode ):
        self.Root: SimpleTreeNode = root
        if self.Root is not None:
            self.Root.Parent = None
        
        self._count = 0

        if self.Root is not None:
            self._count += 1

	
    def AddChild(self, ParentNode: SimpleTreeNode, NewChild: SimpleTreeNode):
        self._count += NewChild._count()
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)

  
    def DeleteNode(self, NodeToDelete: SimpleTreeNode):
        if NodeToDelete == self.Root:
            self.Root = None
            self._count = 0
            return
        
        self._count -= NodeToDelete._count()


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
        return self._count

    def LeafCount(self):
        if self.Root is None:
            return 0
        
        result = self.Root._leaf_count()

        if result == 0:
            return 1
        
        return result

