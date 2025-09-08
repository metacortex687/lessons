# Раздел: 3. Способы обхода дерева

# Задача 2 
# Поиск наименьшего общего предка (LCA)

# Класс: aBST 
# Метод: FindLowestCommonAncestor(self,key1: int, key2: int) -> int
# Вычислительная сложность:  O(log n) - где n количество узлов в дереве

# Решение: Вначале нахожу индексы ключей. 
# Далее, последовательно  применяя к наибольшему индексу формулу для поиска родителя  (I - 1) / 2
# продолжаю до тех пор пока индексы не совпадут.
# Для упрощения алгоритма элемент считаю сам себе предком.  


class aBST:

    def __init__(self, depth):
        tree_size = pow(2,depth+1)-1
        self.Tree = [None] * tree_size
	
    def FindKeyIndex(self, key):
        return self._FindKeyIndex(key,0)
    
    def _FindKeyIndex(self, key, index):
        if self.Tree[index] is None:
            return None
        
        if self.Tree[index] == key:
            return index
        
        return self._FindKeyIndex(key,self._NextIndex(key,index))


    def _NextIndex(self,key,index):
        if self.Tree[index] == key:
            return index

        if self.Tree[index] > key:
            return index*2+1
        
        return index*2+2
      
    def WideAllNodes(self) -> list[int]:
        return [key for key in self.Tree if key is not None]

    def _AddKey(self,key, index):
        if index >= len(self.Tree):
            return -1
        
        if self.Tree[index] is None:
            self.Tree[index] = key
            return index 
        
        if self.Tree[index] == key:
            return index
        
        return self._AddKey(key,self._NextIndex(key,index))

        
    def AddKey(self, key):
        return self._AddKey(key,0); 

    def FindLowestCommonAncestor(self,key1: int, key2: int) -> int:
        
        index1 = self.FindKeyIndex(key1)
        index2 = self.FindKeyIndex(key2)

        if index1 is None or index2 is None:
            return None
        
        if key1 == key2:
            return key1
        
        if index1 == 0:
            return key1
        
        if index2 == 0:
            return key2
        
        index = self._FindLCAByIndex(index1,index2)

        return self.Tree[index]
    
    def _IndexParent(self, index):
        return index
    
    def _FindLCAByIndex(self,index1,index2):
        if index1 == index2:
            return index1
        
        if index1 == 0 or index2 == 0:
            return 0
        
        if index1 > index2:
            return self._FindLCAByIndex((index1-1)//2,index2)
        
        return self._FindLCAByIndex(index1,(index2-1)//2)
    
