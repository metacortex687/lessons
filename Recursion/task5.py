#5. печать только чётных значений из списка;
# Алгоритмическая сложность O(n), где n - колличество элементов
# тесты → ./task5_test.py: https://github.com/metacortex687/lessons/blob/main/Recursion/task5_test.py


def print_even_numbers(lst):
    _print_even_numbers_rec(lst,0)


def _print_even_numbers_rec(lst, index):
    if index >= len(lst):
        return

    if lst[index]%2 == 0:
        print(lst[index])

    _print_even_numbers_rec(lst,index+1)