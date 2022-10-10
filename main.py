from pars_excel import pars_excel
from get_company_name import get_company_name
from meraki_get_box import get_box
from meraki_get_date import get_date
from meraki_get_invoice import get_invoice
from meraki_get_length import get_length
from meraki_get_price import get_price
from meraki_get_product import get_product
from meraki_get_quantity import get_quantity
from meraki_get_total_price import get_total_price
from meraki_dict_to_csv import dict_to_csv


if __name__ == '__main__':

    for i in range(5):

        file_name = f'Meraki{i}'
        sheet = pars_excel(f'{file_name}.xlsx')

        company_name = get_company_name(sheet)

        date = get_date(sheet)

        invoice = get_invoice(sheet)

        dict_lengths = get_length(sheet)

        dict_pricies = get_price(sheet)

        dict_products = get_product(sheet)

        dict_quantities = get_quantity(sheet)

        dict_total_prices = get_total_price(sheet)

        len_column = len(dict_products['Product'])

        dict_boxies = get_box(sheet, len_column)

        dict_to_csv(company_name, file_name, date, invoice, dict_lengths, dict_pricies, dict_products, dict_quantities, dict_total_prices, dict_boxies)
