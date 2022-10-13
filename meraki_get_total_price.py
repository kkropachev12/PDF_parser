import re


def get_total_price(sheet) -> dict:

    dict_total_prices = {'Total': []}

    for row in range(1, sheet.max_row):
        for column in range(0, sheet.max_column):
            if sheet[row][column].value != None:
                if re.fullmatch(r'TOTAL$', str(sheet[row][column].value)) != None:
                    while row != sheet.max_row - 1:
                        dict_total_prices['Total'].append(float(str(
                            sheet[row + 1][column].value).replace(',', '.')))
                        row += 1

                    return dict_total_prices
    return None
