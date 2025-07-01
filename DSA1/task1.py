class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []

        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result
    

    def delete(self, val, all=False):
        node = self.head
        befor = None
        while node is not None:
            if node.value == val:
                if befor is not None:
                    befor.next = node.next
                else:
                    self.head = node.next

                if not all:
                    return
                else:
                    node = node.next
                    continue

                
            befor = node    
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        result = 0

        node = self.head
        while node is not None:
            result += 1
            node = node.next

        return result


    def to_list_values(self):
        result = []
        node = self.head
        while node != None:
            result.append(node.value)
            node = node.next

        return result

    def insert(self, afterNode, newNode):
        if afterNode is None:
            old_head = self.head
            self.head = newNode
            self.head.next = old_head
        else:
            node = self.head
            while node is not None:
                if node == afterNode:
                    old_next = node.next
                    node.next = newNode
                    newNode.next = old_next
                    return
                
                node = node.next   



