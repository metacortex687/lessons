#8. поиск всех файлов в заданном каталоге, включая файлы, расположенные в подкаталогах произвольной вложенности.
# Алгоритмическая сложность: O(n) - где n - колличество файлов если файлов очень много, или n может быть колличеством каталогов 
# если запрос на список файлов делается долго.  

#Описание решения: Убрал вариант с копированием возвращаемого результата в итоговый массив, что бы исключить лишине операции, а массив передаю 
# как ссылку для заполнения.

import os

def find_files(path):
    result = []
    _find_files(path,result)
    return result


def _find_files(path,result):
    _scandir = os.scandir(path)
    for entry in _scandir:
        if entry.is_dir():
            _find_files(entry.path,result)
            continue
        result.append(entry.name)


