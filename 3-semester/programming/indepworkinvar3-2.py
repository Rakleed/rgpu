"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 3.2. Задание: разработайте сценарий с реализацией операции
    поиска подстроки в тексте.

"""


def all_occurrences(search_string, what_to_find):
    occurrence = search_string.find(what_to_find)
    if occurrence != -1:
        print('Первое вхождение подстроки:', occurrence)
    else:
        print('Нет вхождений подстроки.')

    length_search_string = len(search_string)
    length_what_to_find = len(what_to_find)
    while occurrence != -1:
        occurrence = search_string.find(what_to_find, occurrence +
                                        length_what_to_find,
                                        length_search_string)
        if occurrence != -1:
            print('Вхождение подстроки:', occurrence)
        else:
            print('Больше вхождений нет.')


def main():
    search_string = input("Введите строку. ")
    what_to_find = input("Что бы вы хотели найти? ")
    all_occurrences(search_string, what_to_find)


main()
