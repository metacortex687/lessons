#1. возведение числа N в степень M;
# алгоритмическая сложность O(M)
# файл тестов 
# https://github.com/metacortex687/lessons/blob/HEAD/Recursion/task1_test.py


def pow_rec(n,m):
    if m == 0:
        return 1
    return pow_rec(n,m-1)*n


    