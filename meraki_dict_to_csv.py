import csv


def dict_to_csv(company_name: str, file_name: str, date: str, invoice: str, dict_lengths: dict, dict_pricies: dict, dict_products: dict, dict_quantities: dict, dict_total_prices: dict, dict_boxies: dict):
    # Создаем список с заголовками каждого столбца
    list_headers = [list(dict_boxies.keys())[0], list(dict_products.keys())[0], list(dict_lengths.keys())[
        0], list(dict_quantities.keys())[0], list(dict_pricies.keys())[0], list(dict_total_prices.keys())[0]]
    # Список значений каждой колонки
    list_data = [list(dict_boxies.values())[0], list(dict_products.values())[0], list(dict_lengths.values())[
        0], list(dict_quantities.values())[0], list(dict_pricies.values())[0], list(dict_total_prices.values())[0]]
    # Название компании, номер инвойса, дата инвойса
    main_info = [
        company_name, invoice, date
    ]

    with open(f"{file_name}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(
            main_info
        )
        writer.writerow(list_headers)
        for i in range(len(list_data[0])):
            list_d = []
            for data in list_data:
                list_d.append(data[i])
            writer.writerow(
                list_d
            )
