# Раздел: 1. Деревья

# Задача 1: Метод, который перебирает всё дерево и прописывает каждому узлу его уровень.
# Класс: SimpleTree2
# Метод:  SetLevels
# Алгоритмическая сложность: O(n) — где n — количество узлов
# Решение: рекурсивно перебираю все узлы через метод в узле "_set_level". Уровень корня дерева считаю нулевым. 
# Значение устанавливаю в свойство узлов "Level"

# Задача 2: Поддержка уровня узлов без анализа всего дерева.
# Класс: SimpleTree2
# Метод:  GetLevelNode
# Алгоритмическая сложность: O(n) - где n максимальный уровень дерева
# Решение: через метод в узле "_get_level" рекурсивно получаю уровень родителя и добавляю единицу. 
# Уровень корня дерева считаю нулевым, определяю через отсутствие родителя.


class SimpleTreeNode2:
	
    def __init__(self, val, parent = None):
        self.NodeValue = val 
        self.Parent: SimpleTreeNode2 | None = parent 
        self.Children: list[SimpleTreeNode2] = [] 
        self.Level : int = 0 

    def _set_level(self, level):
        self.Level = level
        for child in self.Children:
            child._set_level(level+1)

    def _get_level(self):
        if self.Parent is None:
            return 0
        
        return self.Parent._get_level()+1

	
class SimpleTree2:

    def __init__(self, root: SimpleTreeNode2 ):
        self.Root: SimpleTreeNode2 = root 
        
        if self.Root is not None:
            self.Root.Parent = None
	
    def AddChild(self, ParentNode, NewChild):
        NewChild.Parent = ParentNode
        ParentNode.Children.append(NewChild)
  
    def SetLevels(self) -> None:
        if self.Root is None:
            return
        
        self.Root._set_level(0)

    def GetLevelNode(self,Node: SimpleTreeNode2) -> int:
        return Node._get_level()
    
