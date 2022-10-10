import re


def get_price(sheet) -> dict:

    dict_prices = {'Price': []}

    for row in range(1, sheet.max_row):

        for column in range(0, sheet.max_column):

            if sheet[row][column].value != None:
                if re.search(r'UNIT PRICE', str(sheet[row][column].value)) != None:
                    while sheet[row + 2][column].value != None:
                        dict_prices['Price'].append(
                            sheet[row + 1][column].value)
                        row += 1

                    return dict_prices
    return None
