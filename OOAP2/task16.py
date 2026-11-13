from collections.abc import Callable

class Doc:
    def print(self):
        print("Печать Doc")

class DocPdf(Doc):
    def print(self):
        print("Печать DocPdf")


def print_doc(doc: Doc):
    doc.print()

def print_doc_pdf(doc: DocPdf):
    doc.print()     

# Проверка типов:
# uv run --with mypy  mypy "OOAP2\task16.py"
# Запуск:
# uv run OOAP2\task16.py
if __name__ == "__main__":

# Полиморфное присваивание

    # doc: DocPdf = Doc() #Ошибка типов, контравариантное присваивание недоступно

    doc: Doc = DocPdf() #полиморфное присваивание 
    doc.print() #Печать DocPdf


# Контравариантное присваивание
#     
    # print_fn: Callable[[Doc], None] = print_doc_pdf #Ошибка так как доступно только контравариантное присваивание по типам Doc -> DocPdf

    print_fn: Callable[[DocPdf], None] = print_doc
    print_fn(Doc()) #Печать Doc
    print_fn(DocPdf()) #Печать DocPdf








