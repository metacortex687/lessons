# DSA 1
# Section: 4. Стек

# Problem 5
# Функция которая считает закрывающиеся и закрывающиеся скобки "()"
# Method name: bracket_control
# Алгоритмическая сложность: O(1)
# Solution: частный случай Problem 6

# Problem 6
# Функция которая считает баланс скобок в строке "(), {}, []."
# Method name: bracket_control
# Алгоритмическая сложность: O(1)
# Solution: Открывающуюся скобку ложу в стек, для закрывающей скобки получаю значение из стека, 
# и проверяю что скобка того же типа что и закрывающая

# Problem 7
# Добавить в стэк функцию который возвращает минимальное  число в стэке
# Class name: NumberStack
# Method name: self.min()
# Алгоритмическая сложность: O(1)
# Solution: 
# Использую внутри этого класса два стэка, один для хранения элементов, другой для хранения актуальных минимальных элементов.
# Из второго стэк в с помощью peek можно получить актуальный минимальный элемент.
# При добавлении нового числа стэк, в этот второй стэк кладу наименьшее число из добавляемого, и того что там на вершине там.
# При получении элемента из стэка, удаляю элемент как из основного стэка так и из стэка уктуальных минимальных значений.

# Problem 8
# Добавить в стэк функцию который возвращает среднее значение чисел в стэке
# Class name: NumberStack
# Method name: self.average()
# Алгоритмическая сложность: O(1)
# Solution: 
# Храню сумму элементов в отдельной переменной . При "push" увеличиваю эту переменную на добавляемое число, при "pop" соотвественно уменьшаю.
# Среднее значение получаю делением этой суммы на число элементов в стеке


# Problem 9
# Функция вычисляет постфиксные выражения вида "8 2 + 5 * 9 + ="
# Method name: stack_calculate
# Алгоритмическая сложность: O(n)
# Solution: 
# Если "+" или "-" беру два последних элемента из стэка, вычисляю и кладу обратно
# Если "=" возвращаю из стэка значение
# Иначе считаю числом икладу в стэк
#
# Реализована вспомогательная функция  "string_expr_to_stack" которая парсит строку слева направо и кладет разделенные пробелом элементы в стэк.
# После чего что бы поменять порядок элементов стэке, перекладывает в другой стэе. Алгоритмическая сложность O(n), есть проходы циклов, нет вложенных циклов.


 


class NumberStack():
    def __init__(self):
        self.stack = Stack()
        self._sum = 0
        self._min = Stack()
        
        

    def average(self):
        if self.size() == 0:
            return None
        else:
            return self._sum/self.size()
        
    def min(self):
        if self.size() == 0:
            return None
        else:
            return self._min.peek()


    def size(self):
        return self.stack.size()

    def pop(self):
       
        result = self.stack.pop()
        
        self._sum -= result
        
        self._min.pop()
        
        return result

    def push(self, value):
        self.stack.push(value)
        self._sum += value
        
        if self._min.size() == 0:
            self._min.push(value)
        else:
            self._min.push(min(self._min.peek(),value))


    def peek(self):
        return self.stack.peek()


class Stack:
    def __init__(self):
        self.stack = SimplyLinkedList()
        self._size = 0

    def size(self):
        return self._size

    def pop(self):
        if self.stack.head is None:
            return None
        
        result = self.stack.head.value
        
        self.stack.delete_head()
        self._size -=1
        
        return result

    def push(self, value):
        self.stack.add_in_head(Node(value)) 
        self._size += 1


    def peek(self):
        if self.stack.head is None:
            return None
        else:
            return self.stack.head.value
    
    
class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class SimplyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def add_in_head(self, newNode : Node):
        newNode.next = self.head 
        self.head = newNode
        
    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
            
            

def bracket_control(brackets : str):

    s = Stack()
    
    for b in brackets:
        if b in'({[':
            s.push(b)
        elif b == ')':
            t = s.pop()
            if t != '(':
                return False
        elif b == '}':
            t = s.pop()
            if t != '{':
                return False
        elif b == ']':
            t = s.pop()
            if t != '[':
                return False
            
    return s.size() == 0



def string_expr_to_stack(expr : str):
    stk_reversed_expr = Stack()
    
    symbol = None
    for e in expr:
        if e == ' ':
            if symbol is None:
                pass
            else:
                stk_reversed_expr.push(symbol)
                symbol = None
        elif symbol is None:
            symbol = e
        else:
            symbol += e
    
    if symbol is not None:
        stk_reversed_expr.push(symbol)
    
    stk_expr = Stack()        
    while stk_reversed_expr.size() > 0:
        stk_expr.push(stk_reversed_expr.pop())
        
    return stk_expr
    

def stack_calculate(expr : Stack):
    if expr.size() == 0:
        return None
    
    temp = Stack()
    
    while expr.size() > 0:
        v = expr.pop()
        
        if v == '+':
            temp.push(temp.pop() + temp.pop())
        elif v == '*':
            temp.push(temp.pop() * temp.pop())  
        elif v == '=':  
            if temp.size() == 1:
                return temp.pop()
            else:
                return None
        else:
            temp.push(int(v))
    
    return None   
        
    
