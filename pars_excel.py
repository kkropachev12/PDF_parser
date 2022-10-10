import openpyxl


def pars_excel(file_name:str):
    '''Ф-ция принимает файл excel и
    парсит его с помощью openpyxl, возвращает первую страницу -> sheet'''

    book = openpyxl.open(file_name)

    sheet = book.active
    return sheet
