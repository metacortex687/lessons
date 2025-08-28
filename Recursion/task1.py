#1. возведение числа N в степень M;
# алгоритмическая сложность O(M)
# тесты → task1_test.py: https://github.com/metacortex687/lessons/blob/main/Recursion/task1_test.py


def pow_rec(n,m):
    if m == 0:
        return 1
    return pow_rec(n,m-1)*n


    