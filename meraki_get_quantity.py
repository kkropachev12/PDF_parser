import re


def get_quantity(sheet) -> dict:

    dict_quantities = {'Stems': []}

    for row in range(1, sheet.max_row):
        for column in range(0, sheet.max_column):
            if sheet[row][column].value != None:
                if re.search(r'TOTAL STEMS', str(sheet[row][column].value)) != None:
                    while sheet[row + 2][column].value != None:
                        dict_quantities['Stems'].append(
                            sheet[row + 1][column].value)
                        row += 1

                    return dict_quantities
    return None
