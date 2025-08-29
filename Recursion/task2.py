#2. вычисление суммы цифр числа;
#алгоритмическая сложность O(n), где n - колличество цифр в числе
# тесты → ./task2_test.py: https://github.com/metacortex687/lessons/blob/main/Recursion/task2_test.py


def sum_digits(n):
    if n < 0:
        raise ValueError("Число должно быть >= 0")

    if n == 0:
        return 0

    return n%10 + sum_digits(n//10)

    