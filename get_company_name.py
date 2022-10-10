import re


def get_company_name(sheet) -> dict:

    for row in range(1, sheet.max_row):
        for column in range(0, sheet.max_column):
            if sheet[row][column].value != None:
                if re.search(r'MERAKI FLOWERS', str(sheet[row][column].value)) != None:

                    company_name = re.search(
                                r'MERAKI FLOWERS', str(sheet[row][column].value))
                    company_name = company_name.group()

                    return company_name
    return None
