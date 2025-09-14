# Section: 6. Heaps
#
# Task 3
# Add a method to check that the array actually represents a valid heap.
#
# Class: Heap
# Method: IsValid(self) -> bool:
# Time complexity: O(n) - where n is the number of elements in the heap
# Solution:
# Recursively check the condition that the parent is greater than its children.

class Heap:

    def __init__(self):
        self.HeapArray = []
        self._last_index = -1

    def MakeHeap(self, a: list[int], depth: int):
        size = pow(2, depth + 1) - 1
        # if len(a) > size:
        #     raise OverflowError("Array size exceeds heap capacity")

        self.HeapArray = [None] * size

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
        
        result = self.HeapArray[0]
        self.HeapArray[0] = self.HeapArray[self._last_index]
        self._deallocate_last_slot()
        self._rebuild_down(0)
        return result

    def Add(self, key):
        idx_last_slot = self._allocate_slot()

        if idx_last_slot is None:
            return False

        self.HeapArray[idx_last_slot] = key
        self._rebuild_up(idx_last_slot)

        return True

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
    
