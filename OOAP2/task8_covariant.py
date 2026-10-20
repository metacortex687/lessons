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
    covariant=True,
)

class Printer(Generic[DocumentT]): #ковариантная параметризация типом
    def print(self, document: Document) -> None:
        print(f"Печатаю: {document}")	
		
printer: Printer[Document] = Printer[PdfDocument]() #здесь проявляется ковариантность используем специалированный тип, а декларируем общий

printer.print(PdfDocument("Новый документ", ""))