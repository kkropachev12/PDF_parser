import re


def get_box(sheet, len_column: int) -> dict:

    dict_boxies = {'Half-box': []}

    for row in range(1, sheet.max_row):
        for column in range(0, sheet.max_column):
            if sheet[row][column].value != None:
                if re.fullmatch(r'N$', str(sheet[row][column].value)) != None:
                    for i in range(1, len_column + 1):
                        if sheet[row + i][column].value == None:
                            dict_boxies['Half-box'].append('')
                        else:
                            box = re.search(
                                r'\d+', str(sheet[row + i][column].value))
                            dict_boxies['Half-box'].append(box.group())

                    return dict_boxies
    return None
