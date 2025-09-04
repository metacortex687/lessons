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
            return True
        
        find_result.Node.RightChild = new_node

        return True
  
    def FinMinMax(self, FromNode: BSTNode, FindMax) -> BSTNode:
        if FromNode is None:
            return None
        
        return FromNode.FinMinMax(FindMax)

    def DeleteNodeByKey(self, key):
        if self.Root is None:
            return False
        
        find_result = self.FindNodeByKey(key)

        if not find_result.NodeHasKey:
            return False

        deleted_node = find_result.Node

        if deleted_node == self.Root:
            self.Root = None
            return True
        
        if deleted_node.Parent.LeftChild == deleted_node:
            deleted_node.Parent.LeftChild = None
            return True
        
        deleted_node.Parent.RightChild = None

        return True 

    def Count(self):
        if self.Root is None:
            return 0
        return self.Root.Count()
    
