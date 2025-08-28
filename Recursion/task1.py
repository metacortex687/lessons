#1. возведение числа N в степень M;
# алгоритмическая сложность O(M)
# файл тестов [task1_test.py](./task1_test.py)

def pow(n,m):
    if m == 0:
        return 1
    return pow(n,m-1)*n


    