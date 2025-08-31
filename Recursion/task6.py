#6. печать элементов списка с чётными индексами;
# Алгоритмическая сложность O(n), где n - колличество элементов
# тесты → ./task4_test.py: https://github.com/metacortex687/lessons/blob/main/Recursion/task6_test.py


def print_even_index_numbers(lst):

    _print_even_index_numbers_rec(lst,0)


def _print_even_index_numbers_rec(lst, index): 
    if index >= len(lst):
        return
    
    print(lst[index])

    _print_even_index_numbers_rec(lst, index+2)


