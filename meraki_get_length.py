import re
from traceback import print_tb
import time

def get_length(sheet) -> dict:

    dict_lengths = {'Length': []}

    for row in range(1, sheet.max_row):

        for column in range(0, sheet.max_column):

            if sheet[row][column].value != None:
                if re.search(r'CM', str(sheet[row][column].value)) != None:
                    while row != sheet.max_row - 1:
                        dict_lengths['Length'].append(
                            sheet[row + 1][column].value)
                        row += 1

                    return dict_lengths
    return None
