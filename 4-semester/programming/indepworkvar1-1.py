"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ВСР 1.1. Задание: разработать фрагмент программы, который будет
    сохранять вводимые пользователем данные, по выбору в json, или csv-
    файле (использовать модули csv, json) с использованием протокола
    менеджеров контекста, а также расширенного синтаксиса исключений.

"""

import json


def input_in_file(*data):
    try:
        with open("file.json", "w") as f:
            try:
                json.dump(data, f, sort_keys=True, indent=2)
                print("Данные записаны.")
            except json.Error as e:
                print("Что-то пошло не так.", e)
                return None
    except FileNotFoundError as e:
        print("Такого файла не существует — ", e)
        return None


def main():
    con = "y"
    names_and_surnames = []
    while con == "y":
        first_name = input("Введите своё имя: ")
        surname = input("Введите свою фамилию: ")
        data_of_user = {"first_name": first_name, "surname": surname}
        names_and_surnames.append(data_of_user)
        con = input("Хотели бы вы продолжить вводить данные? (Y/N) ")
    dict_for_data = {"members": names_and_surnames}
    input_in_file(dict_for_data)


main()
