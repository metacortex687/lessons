# DSA 1
# Section: 1. Linked List
# Problem 1.8
# Add the values of two linked lists into corresponding positions of a resulting linked list
# Solution complexity: O(n)

# Solution:
# I will check the lengths. If the lengths are not equal, return None.
# Comparing lengths does not affect the overall O(n) complexity.
# Then, in a single loop, I will simultaneously traverse both lists and append the sum to the tail of the resulting linked list.
# All these operations have O(n) complexity, so the final algorithm remains O(n).

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
    
    
    
    