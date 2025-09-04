# Раздел: 2. Двоичные деревья поиска

# Задача 1 
# Добавьте метод, проверяющий, идентично ли текущее дерево дереву-параметру.
# Класс: BST 
# Метод: IsEqual(self,bst : 'BST') -> bool:
# Вычислительная сложность: O(min(n1,n2)) - где n1 и n2, колличество узлов в сравниваемых двоичных деревьях


# Задача 2 
# Добавьте метод, который нахождит все пути от корня к листьям, длина которых равна заданной величине.
# Класс: BST 
# Метод: PathsToLeaves(self, level: int) -> list[list[BSTNode]]
# Вычислительная сложность: O(n) - где n1 колличество узлов в дереве

# Решение: рекурсивно нахожу листья, которые на нужном расстоянии и возвращаю для этих этих листьев пути. 
# Так как путь до листа двоичного дерева от корня единственен.
# Расстояние до корня считаю 0, до его потомков уже 1.



# Задача 3 
# Добавьте метод, который находит все пути от корня к листьям, чтобы сумма значений узлов на этом пути была максимальной.
# Класс: BST 
# Метод: MaxValueSumPaths(self) -> list[list[BSTNode]]
# Вычислительная сложность: O(n) - где n колличество узлов в дереве


# Задача 4 
# Добавьте метод проверки, симметрично ли дерево относительно своего корня.
# Класс: BST 
# Метод: IsSymmetricTree(self)->bool
# Вычислительная сложность: O(min(n1,n2)) - где n1 и n2 колличество узлов в левом и правом потомке корневого элемента




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

    def IsLeaf(self):
        return self.LeftChild is None and self.RightChild is None 

    def IsEqual(self, node: 'BSTNode'):
        if self.NodeKey != node.NodeKey or self.NodeValue != node.NodeValue:
            return False
        
        if self.IsLeaf() and node.IsLeaf():
            return self.NodeKey == node.NodeKey and self.NodeValue == node.NodeValue
        
        
        if (self.LeftChild is None) != (node.LeftChild is None):
            return False
        
        if (self.RightChild is None) != (node.RightChild is None):
            return False  

        return  self.RightChild.IsEqual(node.RightChild) and  self.LeftChild.IsEqual(node.LeftChild)   

    def PathFromRoot(self) -> list['BSTNode']:
        result = []
        if self.Parent is not None:
            result = self.Parent.PathFromRoot()

        result.append(self)

        return result
    
    def PathsToLeaves(self, level: int) -> list[list['BSTNode']]:
        if level == 0:
            if self.LeftChild is not None or self.RightChild is not None:
                return []
            return [self.PathFromRoot()]
        
        result = []

        if self.LeftChild is not None:
            result.extend(self.LeftChild.PathsToLeaves(level-1))

        if self.RightChild is not None:
            result.extend(self.RightChild.PathsToLeaves(level-1))

        return result
    
    def MaxSumPathsLeaves(self) -> tuple[int, list['BSTNode']]:
        if self.IsLeaf():
            return self.NodeValue, [self]

        if self.LeftChild is None:
            value, path = self.RightChild.MaxSumPathsLeaves()
            return value + self.NodeValue, path
        
        if self.RightChild is None:
            value, path = self.LeftChild.MaxSumPathsLeaves()
            return value + self.NodeValue, path

        left_value, left_paths = self.LeftChild.MaxSumPathsLeaves()
        right_value, right_paths = self.RightChild.MaxSumPathsLeaves()

        max_value = max(left_value,right_value)

        result = []

        if max_value == left_value:
            result.extend(left_paths)

        if max_value == right_value:
            result.extend(right_paths)

        return max_value + self.NodeValue, result
    
    def IsSameShape(self,other: 'BSTNode'):
        if self.IsLeaf() != other.IsLeaf():
            return False

        if (self.LeftChild is None) != (other.LeftChild is None):
            return False
        
        if (self.RightChild is None) != (other.RightChild is None):
            return False        
        
        result = True

        if self.LeftChild is not None:
            result = result and self.LeftChild.IsSameShape(other.LeftChild)

        if self.RightChild is not None:
            result = result and self.RightChild.IsSameShape(other.RightChild)

        return result





class BSTFind:

    def __init__(self):
        self.Node : BSTNode | None = None 

        self.NodeHasKey = False
        self.ToLeft = False


class BST:

    def __init__(self, node: BSTNode):
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
            deleted_node.Parent = None
            return True
        
        deleted_node.Parent.RightChild = None
        deleted_node.Parent = None

        return True 

    def IsEqual(self,bst : 'BST') -> bool:
        if self.Root is None and bst.Root is None:
            return True
        
        if (self.Root is None) != (bst.Root is None):
            return False
        
        return self.Root.IsEqual(bst.Root)

    def Count(self):
        if self.Root is None:
            return 0
        return self.Root.Count()
    

    def PathsToLeaves(self, level: int) -> list[list[BSTNode]]:
        if self.Root is None:
            return []

        return self.Root.PathsToLeaves(level)
    
    def MaxValueSumPaths(self) -> list[list[BSTNode]]:
        if self.Root is None:
            return []
        
        _, leavs = self.Root.MaxSumPathsLeaves()
        
        return [leaf.PathFromRoot() for leaf in leavs]

    

    def IsSymmetricTree(self)->bool:
        if self.Root is None:
            return True
        
        if self.Root.IsLeaf():
            return True
        
        if (self.Root.LeftChild is None) or (self.Root.RightChild is None):
            return False
        
        return self.Root.LeftChild.IsSameShape(self.Root.RightChild)