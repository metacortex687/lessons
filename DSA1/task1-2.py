# АСД 1 
# Раздел: 1. Связанный (связный) список
# Задача 1.8
# Сложить значения двух связанных списков в соответсвующие значения итогового связанного списка
# Сложность решения O(n)

# Решение:
# Проверю длины. Если длинны не равны верну None. 
# Действие по сравнению длинн сложность решения так и оставит O(n)
# Далее в одном цикле, сделаю одновременный обход по двум спискам и добавление в итоговый связный список в хвост
# все эти операции имет сложность алгоритма O(n), значит и итоговый алгоритм имеет сложность O(n)

from task1 import Node, LinkedList

def sum_linked_list(linked_lest_1 : LinkedList, linked_lest_2 : LinkedList):
    if linked_lest_1.len() != linked_lest_2.len():
        return None
    
    result = LinkedList()
    
    node1 = linked_lest_1.head
    node2 = linked_lest_2.head
    
    while node1 is not None:
        
        result.add_in_tail(Node(node1.value + node2.value))
 
        node1 = node1.next
        node2 = node2.next
    
    return result
    
    
    
    