"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 1.3. Задание: дополнить программу для считывания данных с
    использованием менеджера контекстов и реализацией расширенного
    синтаксиса для обработки исключений.

"""

import json

try:
    with open("file.json") as f:
        data_dict = json.load(f)
except FileNotFoundError as e:
    print(e)

try:
    with open("file.json") as f:
        data_dict = json.load(r)
except NameError as e:
    print(e)

try:
    for el in range(len(data_dict)):
        temp = data_dit[el]
        res = string.format(**temp)
        table.append(res)
except NameError as e:
    print(e)
else:
    print("Congratulations! Your program work right.")
finally:
    print("It is impossible to learn anything without mistakes.")


def json_table(fl):
    with open(fl) as f:
        data_dict = json.load(f)

    table = []
    string = '| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |'
    t_caption = '| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |'.format('id', 'first_name', 'last_name', 'email',
                                                                               'gender', 'ip_address')
    header = '-' * len(t_caption)

    table.append(header)
    table.append(t_caption)
    table.append(header)

    for element in range(len(data_dict)):
        temp = data_dict[element]
        res = string.format(**temp)
        table.append(res)
    table.append(header)

    return table


def main():
    a = json_table('file.json')
    for element in a:
        print(element)


main()
