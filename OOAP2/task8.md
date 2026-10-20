Разделил бы понятие "декларация типа" и "используемый тип". В ООП такое отличие возможно в случае наследования. Для переменной, задекларированной с типом родителя, можем использовать значения с типом потомков.

Ковариантность и контрвариантность возникает, если тип параметризован другим типом. Проще всего нарисовать в таблице.

|                   | Тип параметр <br> | Тип параметр <br> | Производный тип | Производный тип |
| ----------------- | ----------------- | ----------------- | --------------- | --------------- |
|                   | T1                | T2                | `A<T1>`         | `A<T2>`         |
| Ковариантность    | Родитель          | Потомок           | Родитель        | Потомок         |
| Контрвариантность | Родитель          | Потомок           | Потомок         | Родитель        |

Рассмотрел вариант, когда тип A не наследуется. В случае наследование и при этом параметризации типами, рассуждения схожи.

В качестве решения выбрал два похожих случая печати документа.

Пример ковариантной типизации:


```python
from typing import Generic, TypeVar

class Document:
	def __init__(self, title: str, body: str) -> None:
		self._title = title
		self._body = body
		
	def __str__(self) -> str:
		return self._title

class PdfDocument(Document):
	pass	
	
DocumentT = TypeVar(
    "DocumentT",
    bound=Document,
    covariant=True, #декларируем допустимость ковариантности
)

class Printer(Generic[DocumentT]): #ковариантная параметризация типом
    def print(self, document: Document) -> None:
        print(f"Печатаю: {document}")	
		
printer: Printer[Document] = Printer[PdfDocument]() #здесь проявляется ковариантность используем специалированный тип, а декларируем общий

printer.print(PdfDocument("Новый документ", ""))
	
```



Пример контравариантной типизации:

```python
from typing import Generic, TypeVar

class Document:
	def __init__(self, title: str, body: str) -> None:
		self._title = title
		self._body = body
		
	def __str__(self) -> str:
		return self._title

class PdfDocument(Document):
	pass	
	
DocumentT = TypeVar(
    "DocumentT",
    bound=Document,
    contravariant=True, #декларируем допустимость контрвариантности
)

class Printer(Generic[DocumentT]): #контрвариантная параметризация типом
    def print(self, document: DocumentT) -> None:
        print(f"Печатаю: {document}")	
		
pdf_printer: Printer[PdfDocument] = Printer[Document]() #здесь проявляется контрвариантность, используем более общий тип, а делкарируем более специализированный

pdf_printer.print(PdfDocument("Новый документ", ""))	
```


---

Код выше выполнится в python даже при ошибках типизации. Для проверки типизации запускаются команды
```Bash
uv run --with mypy  mypy "OOAP2\task8_covariant.py"
uv run --with mypy  mypy "OOAP2\task8_contravariant.py"
```
