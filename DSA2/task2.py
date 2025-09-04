class BSTNode:
	
    def __init__(self, key, val, parent):
        self.NodeKey = key 
        self.NodeValue = val 
        self.Parent: BSTNode | None = parent 
        self.LeftChild: BSTNode | None = None 
        self.RightChild: BSTNode | None = None 

    def Count(self) -> int:
        result = 1

        if self.LeftChild is not None:
            result += self.LeftChild.Count()

        if self.RightChild is not None:
            result += self.RightChild.Count()

        return result            

    def FindNodeByKey(self,key) -> 'BSTFind':
        
        if self.NodeKey == key:
            result = BSTFind()
            result.Node = self
            result.NodeHasKey = True
            return result
        
        if key < self.NodeKey:
            if self.LeftChild is None:
                result = BSTFind()
                result.Node = self
                result.NodeHasKey = False
                result.ToLeft = True
                return result
            return self.LeftChild.FindNodeByKey(key)

        if key > self.NodeKey:
            if self.RightChild is None:
                result = BSTFind()
                result.Node = self
                result.NodeHasKey = False
                result.ToLeft = False
                return result
            return self.RightChild.FindNodeByKey(key)

    def FinMinMax(self, FindMax) -> 'BSTNode':
        if FindMax:
            if self.RightChild is None:
                return self
            return self.RightChild.FinMinMax(FindMax)
        
        if not FindMax:
            if self.LeftChild is None:
                return self
            return self.LeftChild.FinMinMax(FindMax)
        
    def IsLeaf(self) -> bool:
        return self.LeftChild is None and self.RightChild is None 
    
    def OneChild(self)->bool:
        if self.IsLeaf():
            return False
        
        return not ((self.LeftChild is not None) and ((self.RightChild is not None))) #todo проверить тесты когда убраны скобки


class BSTFind:

    def __init__(self):
        self.Node : BSTNode | None = None 

        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node):
        self.Root: BSTNode = node 

    def FindNodeByKey(self, key) -> BSTFind:
        if self.Root is None:
            result = BSTFind()
            result.Node = None
            result.NodeHasKey = False
            return result

        return self.Root.FindNodeByKey(key)

    def AddKeyValue(self, key, val):
        if self.Root is None:
            self.Root = BSTNode(key,val,None)
            return True
        
        find_result = self.FindNodeByKey(key)

        if find_result.NodeHasKey:
            return False
        
        new_node = BSTNode(key, val, find_result.Node)

        if find_result.ToLeft:
            find_result.Node.LeftChild = new_node
            new_node.Parent = find_result.Node
            return True
        
        find_result.Node.RightChild = new_node
        new_node.Parent = find_result.Node

        return True
  
    def FinMinMax(self, FromNode: BSTNode, FindMax) -> BSTNode:
        if FromNode is None:
            return None
        
        return FromNode.FinMinMax(FindMax)

    def _MoveSubtree(self,moved_node: BSTNode, parent: BSTNode) -> None:
        if moved_node is None:
            return

        if moved_node.Parent is not None:
            if moved_node.Parent.LeftChild == moved_node:
                moved_node.Parent.LeftChild = None

            if moved_node.Parent.RightChild == moved_node:
                moved_node.Parent.RightChild = None                

        moved_node.Parent = parent

        if parent is None:
            self.Root = moved_node
            return

        if moved_node.NodeKey > parent.NodeKey:
            parent.RightChild = moved_node
            return
        
        parent.LeftChild = moved_node
 

    def DeleteNodeByKey(self, key):
        if self.Root is None:
            return False
        
        find_result = self.FindNodeByKey(key)

        if not find_result.NodeHasKey:
            return False

        deleted_node = find_result.Node

        if deleted_node.IsLeaf():
            if deleted_node == self.Root:
                self.Root = None
                return True

            if deleted_node.Parent.LeftChild == deleted_node:
                deleted_node.Parent.LeftChild = None
                return True
            
            deleted_node.Parent.RightChild = None
            return True 
        
        if deleted_node.OneChild():
            child = deleted_node.LeftChild
            if child is None:
                child = deleted_node.RightChild
            self._MoveSubtree(child,deleted_node.Parent)
            return True 
        
        min_right_node = deleted_node.RightChild.FinMinMax(False)
        self._MoveSubtree(min_right_node.RightChild,min_right_node.Parent)
        self._MoveSubtree(min_right_node,deleted_node.Parent)
        self._MoveSubtree(deleted_node.RightChild,min_right_node)
        self._MoveSubtree(deleted_node.LeftChild,min_right_node)

        return True        
 
    def Count(self):
        if self.Root is None:
            return 0
        return self.Root.Count()
    
