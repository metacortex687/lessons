import unittest

from task1 import BoundedStack

# run tests:
# python ./OOAP1/task1_tests.py



class TestBoundedStack(unittest.TestCase):

    # push

    def test_unused_push_operation_has_nil_status(self):
        stack = BoundedStack[str]()

        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_NIL)

    # постуловие:
    # на верх стека добавлен элемент  
    def test_push_add_element(self):
        stack = BoundedStack[str]()
        stack.push('qwert')
        stack.push('asdfg')
        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_OK)
        self.assertEqual(stack.peek(), 'asdfg')
        self.assertEqual(stack.size(), 2)

    # предусловие:
    # 2~. Тип значения совпадает с типом который указан при инициализации
    def test_push_sets_error_status_for_value_not_mathing_declared_type(self):
        stack = BoundedStack[str]()

        stack.push(1)
        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_ERR_TYPE)

    # предусловие:
    # 1. В стеке уже находится элементов меньше чем максимальное колличество
    def test_push_sets_error_status_when_stack_is_full(self):
        stack = BoundedStack[str](max_size=3)

        stack.push('qwert')
        stack.push('qwert')
        stack.push('qwert')

        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_OK)

        stack.push('qwert')
        self.assertEqual(stack.get_push_status(), BoundedStack.PUSH_ERR_FULL)

    # постуловие:
    # 2~. Если добавление элемента заврешилось ошибкой, то размер стека не меняется 
    def test_push_does_not_change_size_when_stack_is_full(self):
        stack = BoundedStack[str](max_size=3)

        stack.push('qwert')
        stack.push('qwert')
        stack.push('qwert')

        self.assertEqual(stack.size(), 3)

        stack.push('qwert')
        self.assertEqual(stack.size(), 3)


    # pop

    def test_unused_pop_operation_has_nil_status(self):
        stack = BoundedStack[str]()

        self.assertEqual(stack.get_pop_status(), BoundedStack.POP_NIL)

    # постусловие: из стека удалён верхний элемент
    def test_pop_remove_last_pushed_element(self):
        stack = BoundedStack[str]()

        stack.push('a')
        stack.push('b')
        stack.push('c')

        stack.pop()

        self.assertEqual(stack.peek(), 'b')

    # предусловие: стек не пустой;
    def test_pop_sets_error_status_when_stack_is_empty(self):
        stack = BoundedStack[str]()

        stack.pop()
        self.assertEqual(stack.get_pop_status(), BoundedStack.POP_ERR)


    # peek

    def test_unused_peek_operation_has_nil_status(self):
        stack = BoundedStack[str]()

        self.assertEqual(stack.get_peek_status(), BoundedStack.PEEK_NIL)

    # предусловие:
    # стек не пустой      
    def test_peek_sets_error_status_when_stack_is_empty(self):
        stack = BoundedStack[str]()
        stack.peek()

        self.assertEqual(stack.get_peek_status(), BoundedStack.PEEK_ERR)


if __name__ == '__main__':
    unittest.main()
