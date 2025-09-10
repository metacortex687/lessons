# Раздел: 5. Строим сбалансированные двоичные деревья поиска

# Задача 3 
# Реализуйте метод удаления узла из двоичного дерева, заданного в виде массива. 

# Класс: BBST 
# Метод: def DeleteKey(a: list) -> list:
# Вычислительная сложность:  O(n) - где n количество узлов в дереве

# Решение: 
# Определяю есть ли этот ключ в дереве за O(log n)
# Восстанавливаю отсортированный массив за O(n) при этом исключаю удаляемый ключ оттуда
# Получаю массив упорядоченных позиций для построения в массиве структуры сбалансированного дерева за O(n). 
# Строю это дерево за O(n)
# 
# Примечание: для наследования тестов использую класс аBST из предыдущего задания. 
# Добавление ключа работает, но при этом не перeстраиваю структуру дерева в массиве. 
# При необходимости взяв за основу DeleteKey, можно сделать метод пересборки структуры дерева.
# После добавления ключа, удаленияе ключа работать не будет, так как
# восстановление исходного отсортированного массива работает исключительно для сбалансированного дерева.
# Для восстановления отсортированного массива из двоичного дерева, можно использовать двусвязный 
# список, рекурсивно заполняемый вставками. 


# Задача 3 
# Отсортировать двоичное дерево за O(1)
#
# Ответ:
# Операция сортировки применима для неупорядоченных массивов.
# Например если массив уже упорядочен, тогда достаточно передать ссылку на этот массив, то-есть
# сортировать не надо.
# В двоичном дереве значения уже хранятся в упорядоченном виде, таким образом за время O(1)
# можно передать ссылку на двоичное дерево.     

 

class BBST:

    def __init__(self, keys: list[int]):
        self.Tree = self._GenerateBBSTArrayFromSorted(sorted(keys))

	
    def FindKeyIndex(self, key):
        return self._FindKeyIndex(key,0)
    
    def _FindKeyIndex(self, key, index):
        if index >= len(self.Tree):
            return -index
        
        if self.Tree[index] is None:
            return -index
        
        if self.Tree[index] == key:
            return index
        
        return self._FindKeyIndex(key,self._NextIndex(key,index))

    def _NextIndex(self,key,index):
        if self.Tree[index] == key:
            return index

        if self.Tree[index] > key:
            return index*2+1
        
        return index*2+2
      
    def DeleteKey(self,key):
        if len(self.Tree) == 0:
            return False
        
        index_deleted_key = self.FindKeyIndex(key)

        if index_deleted_key < 0:
            return False
        
        if index_deleted_key == 0 and self.Tree[0] != key:
            return False
       
        ordered_array = self._build_sorted_array_excluding(index_deleted_key)

        self.Tree = self._GenerateBBSTArrayFromSorted(ordered_array)

        return True

    def _build_sorted_array_excluding(self, index_deleted_key):
        bbst_order = self._GenerateBBSTIndexOrder(self.Count())
        sorted_array = [None]*(self.Count()-1)

        removed_pos = bbst_order[index_deleted_key]
        
        for tree_index, sorted_index in enumerate(bbst_order):
            if sorted_index is None:
                continue

            if removed_pos == sorted_index:
                continue
            
            if removed_pos < sorted_index:
                sorted_index -= 1

            key = self.Tree[tree_index]
            
            # if key is None:
            #     continue

            sorted_array[sorted_index] = key

        return sorted_array

    def Count(self):
        return sum(1 for v in self.Tree if v is not None)

    def WideAllNodes(self) -> list[int]:
        return [key for key in self.Tree if key is not None]
        
    def AddKey(self, key):
        if len(self.Tree) == 0:
            self.Tree.append(key)
            return 0

        index = self.FindKeyIndex(key)

        if index >= 0:
            return index
        
        index = -index

        if index >= len(self.Tree):
            self.Tree.extend([None]*(index+1-len(self.Tree)))

        self.Tree[index] = key

        return index


    def _GenerateBBSTIndexOrder(self, count):
        if count == 0:
            return []
        
        index_order_result = [None] * count

        ranges = [(0,count-1,0)]
        while len(ranges) > 0:
            next_ranges = []
            for left_index, right_index, position in ranges:
                if position >= len(index_order_result):
                    index_order_result.extend([None] * (position+1-len(index_order_result)))


                if left_index == right_index:
                    index_order_result[position] = left_index
                    continue

                mid_index = (left_index + right_index +1)//2
                index_order_result[position] = mid_index

                next_ranges.append((left_index,mid_index-1,2*position+1))
                if right_index-left_index > 1:
                    next_ranges.append((mid_index+1,right_index,2*position+2))

            ranges = next_ranges
        
        return index_order_result

    def _GenerateBBSTArrayFromSorted(self, sorted_a: list) -> list:
        idxs = self._GenerateBBSTIndexOrder(len(sorted_a))
        result = []
        for idx in idxs:
            if idx is None:
                result.append(None)
                continue
            result.append(sorted_a[idx])
        return result
