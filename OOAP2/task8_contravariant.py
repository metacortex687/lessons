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