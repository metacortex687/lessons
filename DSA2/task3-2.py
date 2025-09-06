# Раздел: 3. Способы обхода дерева

# Задача 3 
# Реализуйте алгоритм инвертирования дерева: 
# надо сделать так, чтобы слева от главного узла были значения больше него, а справа — меньше.
# Класс: BST 
# Метод: Invert(self) -> None
# Вычислительная сложность:  O(n) - где n колличество узлов в дереве

# Решение: рекурсивно меняю местами узлы. Таким образом значения ключей слева будут больше, а справа меньше.


# Задача 4 
# Добавьте метод, который находит уровень в текущем дереве, сумма значений узлов на котором максимальна.
# Класс: BST 
# Метод: MaxSumLevel(self) -> int | None
# Вычислительная сложность: O(n) - где n колличество узлов в дереве

# Решение: Если в дереве нет узлов возвращает None. Оптимизация заключается в том, каждый узел должен посещатся только один раз.
# При проходе уровня из дочерних узлов формирую список для прохождения в следующей итерации.   



# Задача 5 
# Учитывая результаты обхода дерева в префиксном и инфиксном порядке, разработайте функцию для восстановления оригинального дерева.
# Класс: BST 
# Метод:  @staticmethod Restore(pre_order_list : list,in_order_list : list) -> 'BST'
# Вычислительная сложность: O(n * log n) - где n колличество узлов в дереве

# Решение: Массив pre-order задает порядок увеличения ключей слева направо.
# Массив in-order задает порядок добавления значений узлов с ключами полученными из pre-order

# Почему обязательно нужны оба обхода для однозначного построения дерева? 
# Если будет только список pre-order, то он может быть получен из дерева состоящим только из левых элементов.
# Так и из более сложной структуры. Значит не подходит.
# Если будет только список in-order, его также можно получить из дерева состоящим только из левых элементов. 
# Так и из более сложной структуры. Значит не подходит. 
# 
# Дерево однозначно задается значением ключа для значения элемента и порядком добавления этого узла.
# Эти два списка задают как порядок добавления значения элемента, так и значение ключа для этого элемента.






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

    def IsEqual(self, node: 'BSTNode'):
        if self.NodeValue != node.NodeValue:
            return False
        
        if self.IsLeaf() and node.IsLeaf():
            return self.NodeValue == node.NodeValue
        
        
        if (self.LeftChild is None) != (node.LeftChild is None):
            return False
        
        if (self.RightChild is None) != (node.RightChild is None):
            return False  

        return  self.RightChild.IsEqual(node.RightChild) and  self.LeftChild.IsEqual(node.LeftChild) 


    def WideAllNodes(self) -> list['BSTNode']:
        nodes = [self]
        start_position = 0
        count = 1

        while count>0:
            end_position = start_position + count - 1
            count = 0
            for i in range(start_position,end_position+1):
                if nodes[i].LeftChild is not None:
                    nodes.append(nodes[i].LeftChild)
                    count += 1
                if nodes[i].RightChild is not None:
                    nodes.append(nodes[i].RightChild) 
                    count += 1
                start_position += 1
            
        return nodes  
    
    def DeepAllNodes(self,visit_order) -> list['BSTNode']:
        ''' visit_order
        0 - in-order
        1 - post-order
        2 - pre-order
        '''
        left = []
        if self.LeftChild is not None:
            left = self.LeftChild.DeepAllNodes(visit_order)
        right = []
        if self.RightChild is not None:
            right = self.RightChild.DeepAllNodes(visit_order)

        result = []
        if visit_order == 0:   
            result.extend(left)
            result.append(self)
            result.extend(right)

        if visit_order == 1:   
            result.extend(left)
            result.extend(right)  
            result.append(self)

        if visit_order == 2:   
            result.append(self)
            result.extend(left)
            result.extend(right)  
        
        return result
    
    
    def Invert(self) -> None:
        self.LeftChild, self.RightChild = self.RightChild, self.LeftChild

        if self.LeftChild is not None:
            self.LeftChild.Invert()

        if self.RightChild is not None:
            self.RightChild.Invert()

    def MaxSumLevel(self):
 
        max_sum_level = 0
        max_sum_values = self.NodeValue
        nodes = [self]
        
        level = 0
        while len(nodes) > 0:
            sum_values = 0
            next_nodes = []
            for node in nodes:
                sum_values += node.NodeValue
                if node.LeftChild is not None:
                    next_nodes.append(node.LeftChild)
                if node.RightChild is not None:
                    next_nodes.append(node.RightChild)
            if sum_values > max_sum_values:
                max_sum_level = level
                max_sum_values = sum_values
            level += 1
            nodes = next_nodes

        return max_sum_level


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
    
    def WideAllNodes(self) -> list[BSTNode]:
        if self.Root is None:
            return []
        
        return self.Root.WideAllNodes()
    
    def DeepAllNodes(self,visit_order) -> list[BSTNode]:
        ''' visit_order:
        0 - in-order
        1 - post-order
        2 - pre-order
        '''
        if self.Root is None:
            return []
        
        return self.Root.DeepAllNodes(visit_order)
    
    def InvertTree(self):
        if self.Root is None:
            return
        
        self.Root.Invert()

    def MaxSumLevel(self) -> int | None:
        if self.Root is None:
            return
        
        return self.Root.MaxSumLevel()
    
    @staticmethod
    def Restore(pre_order_list : list,in_order_list : list) -> 'BST':
        if len(pre_order_list) == 0:
            return BST(None)
        
        value_key = {}
        for i, value in enumerate(in_order_list):
            value_key[value] = i


        bst = BST(None)
        for value in pre_order_list:
            bst.AddKeyValue(value_key[value],value)

        return bst 

    def IsEqual(self,bst : 'BST') -> bool:
        if self.Root is None and bst.Root is None:
            return True
        
        if (self.Root is None) != (bst.Root is None):
            return False
        
        return self.Root.IsEqual(bst.Root)   
    
