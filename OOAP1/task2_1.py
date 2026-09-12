from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, TypeVar

# Статусы команд и запросов:

class StatusHead(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusTail(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusRight(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2
    ERR_CURSOR_ON_TAIL = 3

class StatusPutRight(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusPutLeft(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusRemove(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusAddToEmpty(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_NOT_EMPTY = 2

class StatusAddTail(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusReplace(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusFind(Enum):
    NIL = 0
    OK = 1
    NOT_FIND = 2
    ERR_LIST_EMPTY = 3
    FIND_ERR_CURSOR_ON_TAIL = 4

class StatusGet(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusIsHead(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2

class StatusIsTail(Enum):
    NIL = 0
    OK = 1
    ERR_LIST_EMPTY = 2


# Интерфейс

T = TypeVar('T')

class LinkedList(ABC, Generic[T]):

    @abstractmethod
    def __init__(self):
        """
        конструктор;
        постусловие: создан новый пустой связный список.
        """
        ...

    # Команды:

    @abstractmethod
    def head() -> None:
        """
        предусловие: список не пустой;
        постусловие: курсор на первом узле в списке.     
        """
        ...

    
    @abstractmethod
    def tail() -> None:
        """
        предусловие: список не пустой;
        постусловие: курсор на последнем узле в списке.     
        """
        ...

    @abstractmethod
    def right() -> None:
        """
        предусловие: 
        	список не пустой;
        	курсор не в конце списка;
        постусловие: курсор сдвинут вправо;
        """
        ...

    @abstractmethod
    def put_right(value: T) -> None:
        """
        предусловие: список не пустой;
        постусловие: 
            значение вставлено справа от курсора
            курсор на этом вставленном значении	
        """
        ...   

    
    @abstractmethod
    def put_left(value: T) -> None:
        """
        предусловие: список не пустой;
        постусловие: 
            значение вставлено слева от курсора
            курсор на этом вставленном значении
        """
        ...         

     
    @abstractmethod
    def remove() -> None:
        """
        предусловие: список не пустой;
        постусловие: 
            удален элемент на котором курсор;
            если курсор не на последнем элементе то курсор на элементе что был справа, иначе на элементе, что был слева;
        """
        ...   


    @abstractmethod
    def clear() -> None:
        """
        постусловие: список пуст
        """
        ...   


    @abstractmethod
    def add_to_empty(value: T) -> None:
        """
        предусловие: список пуст;
        постусловие: в списке один элемент; курсор на этом элементе; курсор одновременно и на начале и в конце списка;          
        """
        ...   


    
    @abstractmethod
    def add_tail(value: T) -> None:
        """
        предусловие: список не пустой;
        постусловие: новый элемент в конце списка, курсор на новом элементе;          
        """
        ...     

    
    @abstractmethod
    def replace(value: T) -> None:
        """
        предусловие: список не пустой;
        постусловие: новый элемент вместо того на котором был курсор; курсор на новом элементе;          
        """
        ...     

    
    @abstractmethod
    def find(value: T) -> None:
        """
        предусловие: 
            список не пустой;
            курсор не на последнем элементе;
        постусловие: если элемент найден, курсор на первом вхождении элемента за исходной позицией курсора иначе элементе в конце списка;          
        """
        ...     


    @abstractmethod
    def remove_all(value: T) -> None:
        """
        постусловие: в списке нет ни одного элемента равного удаляемому;          
        """
        ...    


    # Запросы:

    @abstractmethod
    def get() -> T:
        """
        предусловие: список не пустой; 
        """
        ...   


    @abstractmethod
    def size() -> int:
        """
        """
        ...   


    @abstractmethod
    def is_head() -> bool:
        """
        предусловие: список не пустой; 
        """
        ...   


    @abstractmethod
    def is_tail() -> bool:
        """
        предусловие: список не пустой; 
        """
        ...   


    @abstractmethod
    def is_value() -> bool:
        """
        """
        ...   


    # Дополнительные запросы:   
    @abstractmethod
    def get_head_status() -> StatusHead:
        ...

    @abstractmethod
    def get_tail_status() -> StatusTail:
        ...

    @abstractmethod
    def get_right_status() -> StatusRight:
        ...        

    @abstractmethod
    def get_put_right_status() -> StatusPutRight:
        ...

    @abstractmethod
    def get_put_left_status() -> StatusPutLeft:
        ...

    @abstractmethod
    def get_remove_status() -> StatusRemove:
        ...

    @abstractmethod
    def get_add_to_empty_status() -> StatusAddToEmpty:
        ...

    @abstractmethod
    def get_add_tail_status() -> StatusAddTail:
        ...

    @abstractmethod
    def get_replace_status() -> StatusReplace:
        ...

    @abstractmethod
    def get_find_status() -> StatusFind:
        ...

    @abstractmethod
    def get_get_status() -> StatusGet:
        ...

    @abstractmethod
    def get_is_head_status() -> StatusIsHead:
        ...

    @abstractmethod
    def get_is_tail_status() -> StatusIsTail:
        ...

