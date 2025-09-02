#8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
# Алгоритмическая сложность: O(n) - где n - колличество файлов если файлов очень много, или n может быть колличеством каталогов 
# если запрос на список файлов делается долго.  
# тесты → ./task4_test.py: https://github.com/metacortex687/lessons/blob/main/Recursion/task8_test.py

#Описание решения: Убрал вариант с копированием возвращаемого результата в итоговый массив, чтобы исключить лишние операции, а массив передаю 
# как ссылку для заполнения.

import os

def find_files(path: str, result: list) -> None:
    entries = os.scandir(path)
    for entry in entries:
        if entry.is_dir():
            find_files(entry.path,result)
            continue
        result.append(entry.name)


