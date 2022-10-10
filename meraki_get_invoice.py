import re


def get_invoice(sheet) -> str:

    for row in range(1, sheet.max_row):

        for column in range(0, sheet.max_column):

            if sheet[row][column].value != None:
                if re.search(r'\d+-\d{,6}$', str(sheet[row][column].value)) != None:
                    invoice = re.sub(r'Invoice\D+', '',
                                     sheet[row][column].value)
                    return invoice
    return None
