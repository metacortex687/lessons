# Раздел: 6. Пирамиды

# Задача 4
# Добавьте метод поиска максимального элемента в заданном диапазоне значений.

# Класс: Heap
# Метод: FindMaxInRange(self, min_key: int, max_key: int)-> int | None:
# Вычислительная сложность:  O(n) - где n количество элементов в куче
# Решение:
# Рекурсивно проверяю условие. Не проверяю для потомков если у текущего узла меньше нижней границы диапазона, потомки будут еще меньше.
# Таким образом использую свойство кучи, чтобы сократить вычисления.


# Задача 5
# Поиск наименьшего значения используя свойства кучи

# Класс: Heap
# Метод: FindMin(self) -> int | None:
# Вычислительная сложность:  O(n) - где n количество узлов в дереве

# Решение:
# Ищу минимальный элемент в листьях. Индексы листьев определяю по индексу последнего узла.
# Для последнего узла вычисляю родителя и добавляю к результату единицу. И с этого индекса и до индекса последнего узла,- это листья.


# Задача 6
# Добавьте метод объединения текущей кучи с кучей-параметром.

# Класс: Heap
# Метод: Merge(self, other_heap: "Heap") -> None:
# Вычислительная сложность:  в лучшем случае O(n2) - где n2 количество узлов в other_heap (куче источнике). Поскольку беру снизу кучи,
# то в лучшем случае эти элементы не надо будет подымать вверх.
# В худшем случае не хуже чем O(n2 * log(n1 + n2))
# n1 - колличество элементов в куче приемнике, а n2 количество узлов в куче источнике.

# Решение:
# Забираю последний элемент из кучи источника добавленным методом "GetLast" и добавляю в кучу приемник  с помощью метода "Add".


class Heap:

    def __init__(self):
        self.HeapArray = []
        self._last_index = -1

    def MakeHeap(self, a: list[int], depth: int):
        size = pow(2, depth + 1) - 1
        # if len(a) > size:
        #     raise OverflowError("Array size exceeds heap capacity")
        
        self.HeapArray = [None]*size

        for key in a:
            self.Add(key)

        # self.HeapArray = sorted(a.copy(), reverse=True)
        # self.HeapArray.extend([None] * (size - len(self.HeapArray)))

        # self._last_index = len(a) - 1

    def _allocate_slot(self) -> int:
        self._last_index += 1
        if self._last_index >= len(self.HeapArray):
            return None

        return self._last_index

    def _deallocate_last_slot(self):
        if self._last_index == -1:
            return

        self.HeapArray[self._last_index] = None
        self._last_index -= 1

    def _rebuild_up(self, idx_child: int):
        if idx_child == 0:
            return

        idx_parent = (idx_child - 1) // 2
        if self.HeapArray[idx_parent] < self.HeapArray[idx_child]:
            self.HeapArray[idx_parent], self.HeapArray[idx_child] = (
                self.HeapArray[idx_child],
                self.HeapArray[idx_parent],
            )
            self._rebuild_up(idx_parent)

    def _rebuild_down(self, idx_curent: int):
        idx_left_child = idx_curent * 2 + 1
        if idx_left_child > self._last_index:
            return

        idx_righ_child = idx_curent * 2 + 2

        idx_max_element = idx_left_child

        if (
            idx_righ_child <= self._last_index
            and self.HeapArray[idx_left_child] < self.HeapArray[idx_righ_child]
        ):
            idx_max_element = idx_righ_child

        if self.HeapArray[idx_max_element] <= self.HeapArray[idx_curent]:
            return

        self.HeapArray[idx_curent], self.HeapArray[idx_max_element] = (
            self.HeapArray[idx_max_element],
            self.HeapArray[idx_curent],
        )

        self._rebuild_down(idx_max_element)

    def GetMax(self):
        if len(self.HeapArray) == 0:
            return -1

        self.HeapArray[0] = self.HeapArray[self._last_index]
        self._deallocate_last_slot()
        self._rebuild_down(0)

    def Add(self, key):
        idx_last_slot = self._allocate_slot()

        if idx_last_slot is None:
            return False

        self.HeapArray[idx_last_slot] = key
        self._rebuild_up(idx_last_slot)

        return True

    def FindMaxInRange(self, min_key: int, max_key: int) -> int:
        if self._last_index == -1:
            return None

        return self._MaxInRange(min_key, max_key, 0)

    def _MaxInRange(self, min_key: int, max_key: int, idx: int):

        if self.HeapArray[idx] < min_key:
            return None

        result = None
        if self.HeapArray[idx] <= max_key:
            result = self.HeapArray[idx]

        if result == max_key:
            return result

        result_left_child = None
        idx_left_child = idx * 2 + 1
        if idx_left_child <= self._last_index:
            result_left_child = self._MaxInRange(min_key, max_key, idx_left_child)

        if result is None:
            result = result_left_child

        if result_left_child is not None:
            result = max(result, result_left_child)

        if result == max_key:
            return result

        result_righ_child = None
        idx_righ_child = idx * 2 + 2
        if idx_righ_child <= self._last_index:
            result_righ_child = self._MaxInRange(min_key, max_key, idx_righ_child)

        if result is None:
            result = result_righ_child

        if result_righ_child is not None:
            result = max(result, result_righ_child)

        return result

    def FindMin(self) -> int | None:
        if self._last_index == -1:
            return None

        if self._last_index == 0:
            return self.HeapArray[0]

        idx_parent_last_leaf = (self._last_index - 1) // 2

        result = self.HeapArray[self._last_index]
        for i in range(idx_parent_last_leaf + 1, self._last_index):
            result = min(result, self.HeapArray[i])

        return result

    def GetLast(self) -> int | None:
        if self._last_index == -1:
            return None

        result = self.HeapArray[self._last_index]
        self._deallocate_last_slot()
        return result

    def Merge(self, other_heap: "Heap") -> None:
        key = other_heap.GetLast()
        while key is not None:
            self.Add(key)
            key = other_heap.GetLast()

    def _IsValid(self, idx):
        result = True

        idx_left_child = idx * 2 + 1
        idx_righ_child = idx * 2 + 2

        if (
            idx_left_child <= self._last_index
            and self.HeapArray[idx_left_child] > self.HeapArray[idx]
        ):
            return False

        if (
            idx_righ_child <= self._last_index
            and self.HeapArray[idx_righ_child] > self.HeapArray[idx]
        ):
            return False

        if idx_left_child <= self._last_index:
            result = result and self._IsValid(idx_left_child)

        if idx_righ_child <= self._last_index:
            result = result and self._IsValid(idx_righ_child)

        return result

    def IsValid(self) -> bool:
        if self._last_index < 1:
            return True

        return self._IsValid(0)
