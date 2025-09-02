# 7. нахождение второго максимального числа в списке 
# Алгоритмическая сложность O(n), где n - колличество элементов в массиве
# тесты → ./task4_test.py: https://github.com/metacortex687/lessons/blob/main/Recursion/task7_test.py

def second_max(lst: list[int]) -> int:
    if len(lst) < 2:
        raise ValueError("массив должен содержать минимум 2 элемента")

    return _second_max_rec(lst,2,len(lst)-1,max(lst[1],lst[0]),min(lst[1],lst[0]))


def _second_max_rec(lst: list[int],_index: int,max_index: int,max_val: int,second_max_val: int) -> int:
    if _index > max_index:
        return second_max_val

    if lst[_index] >= max_val:
        second_max_val = max_val
        max_val = lst[_index]
        return _second_max_rec(lst,_index+1,max_index,max_val,second_max_val)
    
    if lst[_index] >= second_max_val:
        second_max_val = lst[_index]

    return _second_max_rec(lst,_index+1,max_index,max_val,second_max_val)    



