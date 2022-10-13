import re


def get_product(sheet) -> dict:

    dict_names = {'Product': []}

    for row in range(1, sheet.max_row):
        for column in range(0, sheet.max_column):
            if sheet[row][column].value != None:
                if re.search(r'PRODUCTO', str(sheet[row][column].value)) != None:
                    while row != sheet.max_row - 1:
                        dict_names['Product'].append(
                            sheet[row + 1][column].value)
                        row += 1

                    return dict_names
    return None
