# BoundedStack

# За основу взят класс Stack реализации одноименного АТД из первого урока курса ООАП-1

# а) Убрал сброс статусов команд на *_NILL для команды clear. Иначе надо тогда объяснить, почему, например, статус для команды push или запроса peek не сбрасывается после команды pop, а в clear сбрасываем.
# Явно зафиксировал это в постусловиях.
# б) Поскольку Python — язык с динамической типизацией, также делаю проверку типов во время выполнения. Вспомогательный метод проверки типов сделан приватным, так как не является частью интерфейса. 
# Разделил типы ошибок на PUSH_ERR_TYPE и PUSH_ERR_FULL. Для ошибки типа и для случая когда стек на начало команды уже полон.

# в) В файле OOAP1\task1_tests.py добавлены тесты. Постарался сделать тесты атомарными, один тест проверяет одно постусловие или предусловие.
# В первоначальном варианте был, например, тест для запроса peek, в котором проверял, что возвращается элемент с вершины стека.
# Но по факту этот тест совпал с тестом постусловия для pop — «из стека удалён верхний элемент», как следствие убрал лишний тест запроса peek.
# Можно считать, что подобно тому, как класс является реализацией АТД, тесты является имплементацией проверки предусловий или постусловий.

# г) Дополнительные предусловия и постусловия, которые формально можно не считать основными для АТД Стек, обозначены `~`. Тестируются выборочно.

# д) Максимальную вместимость стека считаю опцией команд. При этом установка значения этой опции может вызывать ошибку. Ошибку обрабатываю через получение статуса.

from typing import TypeVar, Generic, List, get_args

T = TypeVar('T')


class BoundedStack(Generic[T]):
    PUSH_NIL = 0  # push() ещё не вызывалась
    PUSH_OK = 1  # последняя push() отработала нормально
    PUSH_ERR_TYPE = 2  # тип помещаемого значения, не соотвествует указаному при инициализации стека
    PUSH_ERR_FULL = 2  # стек уже заполнен до предела
    POP_NIL = 0  # pop() ещё не вызывалась
    POP_OK = 1  # последняя pop() нормально отработала
    POP_ERR = 2  # стек пуст
    PEEK_NIL = 0  # peek() ещё не вызывалась
    PEEK_OK = 1  # последняя peek() вернула корректное значение
    PEEK_ERR = 2  # стек пуст
    SET_MAX_SIZE_OK = 1 # максимальный размер стека установлен
    SET_MAX_SIZE_ERR = 2 # максимальный размер статуса меньше числа элементов в стеке


    # oбъявление приватных переменных класса
    _max_size: int
    _stack: List[T]

    _push_status: int
    _peek_status: int
    _pop_status: int
    _set_max_size_status: int

    # конструктор
    def __init__(self, max_size: int = 32): # Постусловие создан новый пустой стек
        self._max_size = max_size

        self._stack = []

        self._push_status = BoundedStack.PUSH_NIL
        self._peek_status = BoundedStack.PEEK_NIL
        self._pop_status = BoundedStack.POP_NIL
        self._set_max_size_status = BoundedStack.SET_MAX_SIZE_OK

    # Команды:

    # предусловие:
    # 1. В стеке уже находится элементов меньше чем максимальное колличество
    # 2~. Тип значения совпадает с типом который указан при инициализации
    # постуловие:
    # 1. на верх стека добавлен элемент
    # 2~. Если добавление элемента заврешилось ошибкой, то размер стека не меняется
    # 3~. не меняет статусы команды pop и запроса peek 
    def push(self, value: T) -> None:
        if not self._check_type_value(value):
            self._push_status = BoundedStack.PUSH_ERR_TYPE
        elif self.size() < self.get_max_size():
            self._stack.append(value)
            self._push_status = BoundedStack.PUSH_OK
        else:
            self._push_status = BoundedStack.PUSH_ERR_FULL

    # предусловие: стек не пустой;
    # постусловие: 
    # 1. из стека удалён верхний элемент
    # 2~. не меняет статусы команды push и запроса peek 
    def pop(self) -> T:
        if self.size() > 0:
            del self._stack[-1]
            self._pop_status = BoundedStack.POP_OK
        else:
            self._pop_status = BoundedStack.POP_ERR

    # постуловие: 
    # 1. из стека удалены все элементы
    # 2~. не меняет статусы команд pop, push и запроса peek 
    def clear(self) -> None:
        self.reset_operation_statuses()

        self._stack = []

    # Запросы:

    # предусловие:
    # стек не пустой
    def peek(self) -> T:
        if self.size() > 0:
            result = self._stack[-1]
            self._peek_status = BoundedStack.PEEK_OK
        else:
            result = None
            self._peek_status = BoundedStack.PEEK_ERR
        return result

    def size(self) -> int:
        return len(self._stack)


    # установка и чтение опций
    # предусловие: число элементов меньше или равно допустимой максимальной вместимости стека 
    # постусловие: установлена опция - новая вместимость стека
    def set_max_size(self, max_size: int) -> None:
        if max_size < self.size():
            self._set_max_size_status = BoundedStack.SET_MAX_SIZE_ERR
        else:
            self._max_size = max_size
            self._set_max_size_status = BoundedStack.SET_MAX_SIZE_OK


    def get_max_size(self) -> int:
        return self._max_size  


    # дополнительные запросы:
    def get_push_status(self) -> int:
        return self._push_status

    def get_pop_status(self) -> int:
        return self._pop_status

    def get_peek_status(self) -> int:
        return self._peek_status

    def get_set_max_size_status(self) -> int:
        return self._set_max_size_status

    # приватные методы класса
    def _check_type_value(self, value) -> bool:
        return isinstance(value, get_args(self.__orig_class__)[0])
