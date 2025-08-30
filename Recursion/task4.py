# 4. проверка, является ли строка палиндромом;
# Алгоритмическая сложность O(n), где n - длина строки
# тесты → ./task4_test.py: https://github.com/metacortex687/lessons/blob/main/Recursion/task4_test.py

# Описание решения:
# Первоначальный вариант использования срезов вида world[1:-1], не подошел так как для стандартного массива python делается поверхностная копия.
# Срез без копирования делается, например при работе с массивами библиотеки NumPy.
#
# Буду использовать индексы. И две функции.
# Пустую строку считаю палиндромом, так как она соответствует условию "s == reverse(s)""


def is_polindrom(s: str):
    return _is_polindrom_rec(s,0,len(s)-1)   

def _is_polindrom_rec(s,left_index,rigth_index):
    if left_index >= rigth_index: 
        return True
    
    if s[left_index] != s[rigth_index]:
        return False
    
    return _is_polindrom_rec(s,left_index+1,rigth_index-1)
    

    

