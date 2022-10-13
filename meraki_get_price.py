import re


def get_price(sheet) -> dict:

    dict_prices = {'Price': []}

    for row in range(1, sheet.max_row):

        for column in range(0, sheet.max_column):

            if sheet[row][column].value != None:
                if re.search(r'\w+IT PRICE', str(sheet[row][column].value)) != None:
                    while row != sheet.max_row - 1:
                        dict_prices['Price'].append(
                            float(str(sheet[row + 1][column].value).replace(',', '.')))
                        row += 1

                    return dict_prices
    return None
