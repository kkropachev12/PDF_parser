import re


def get_date(sheet) -> str:

    for row in range(1, sheet.max_row):

        for column in range(0, sheet.max_column):

            if sheet[row][column].value != None:
                if re.search(r'(^\d{1,2}\D\d{1,2}\D\d{2,4})|(^\d{2,4}\D\d{1,2}\D\d{1,2})', str(sheet[row][column].value)) != None:
                    date = re.search(r'(^\d{1,2}\D\d{1,2}\D\d{2,4})|(^\d{2,4}\D\d{1,2}\D\d{1,2})', str(
                        sheet[row][column].value))[0].replace('/', '-')
                    return date
    return None
