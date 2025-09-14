class Heap:

    def __init__(self):
        self.HeapArray = []
        self._last_index = -1

    def MakeHeap(self, a: list[int], depth: int):
        size = pow(2, depth + 1) - 1
        if len(a) > size:
            raise OverflowError("Array size exceeds heap capacity")

        self.HeapArray = sorted(a.copy(), reverse=True)
        self.HeapArray.extend([None] * (size - len(self.HeapArray)))

        self._last_index = len(a) - 1

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
    
