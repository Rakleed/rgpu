"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 3.3. Задание: создайте скрипт для считывания данных справочных
    логов из текстового файла и преобразования их в CSV-формат с после-
    дующей записью в новый файл.

"""


def json_function():
    import json
    help_logs = open('file.json')
    data_list = json.load(help_logs)
    return data_list


def csv_function(data_list):
    import csv
    with open('file.csv', 'w', newline='') as csv_file_handler:
        csv_writer = csv.writer(
            csv_file_handler,
            delimiter=';',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(list(data_list[0].keys()))
        for d_dict in data_list:
            csv_writer.writerow(list(d_dict.values()))


data = json_function()
csv_function(data)
