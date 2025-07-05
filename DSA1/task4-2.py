# DSA 1
# Section: 4. Stack

# Problem 5
# A function that checks matching opening and closing parentheses "()"
# Method name: bracket_control
# Time complexity: O(1)
# Solution: a special case of Problem 6

# Problem 6
# A function that checks the balance of brackets in a string "(), {}, []."
# Method name: bracket_control
# Time complexity: O(1)
# Solution: I push each opening bracket onto a stack, for each closing bracket I pop a value from the stack
# and check whether the bracket type matches the closing one

# Problem 7
# Add a function to the stack that returns the minimum number in the stack
# Class name: NumberStack
# Method name: self.min()
# Time complexity: O(1)
# Solution:
# I use two stacks inside this class: one to store elements, and another to store the current minimums.
# From the second stack, the current minimum element can be obtained via peek.
# When pushing a new number, I push into the second stack the minimum of the new number and the current top.
# When popping from the stack, I remove the element from both the main stack and the stack of current minimums.

# Problem 8
# Add a function to the stack that returns the average value of the numbers in the stack
# Class name: NumberStack
# Method name: self.average()
# Time complexity: O(1)
# Solution:
# I store the sum of elements in a separate variable. On each "push", I increase this variable by the added number,
# and on "pop" I decrease it accordingly.
# The average value is calculated by dividing this sum by the number of elements in the stack.

# Problem 9
# A function that evaluates postfix expressions like "8 2 + 5 * 9 + ="
# Method name: stack_calculate
# Time complexity: O(n)
# Solution:
# If the token is "+" or "-", I take the last two elements from the stack, compute the result, and push it back
# If the token is "=", I return the value from the stack
# Otherwise, I treat it as a number and push it to the stack
#
# A helper function "string_expr_to_stack" is implemented, which parses the string from left to right,
# treating spaces as delimiters to separate tokens and push them into the stack.
# Then, to reverse the order of elements in the stack, it moves them to another stack.
# Time complexity: O(n), there are loop passes, no nested loops.

 


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
        
    
