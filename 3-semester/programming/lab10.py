"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ЛР 11. Задание: доработать программу для поиска подстроки в тексте.

"""


def main():
    searchable_str = input("Введите строку, по которой мы ищем: ")
    input_str = input("Введите строку для поиска: ")
    choice = None
    while choice != '4':
        print('1 — поиск первого вхождения подстроки.')
        print('2 — замена первой подстроки.')
        print('3 — найти все вхождения подстроки.')
        print('4 — для выхода.')
        choice = input("Сделайте  выбор (1..4): ")
        if choice == '1':
            search_str(searchable_str, input_str)
        if choice == '2':
            rep_str = input('Введите строку для замены: ')
            search_n_replace_str(searchable_str, input_str, rep_str)
        if choice == '3':
            search_all_str(searchable_str, input_str)


def search_str(str_searchable, str_input):
    entry = str_searchable.find(str_input)
    if entry != -1:
        print('Первое вхождение подстроки: ', entry, "\n")
    else:
        print('Нет вхождений подстроки.\n')


def search_n_replace_str(str_searchable, str_input, str_rep):
    print('Получившаяся строка: ', str_searchable.replace(str_input, str_rep, 1), "\n")


def search_all_str(str_searchable, str_input):
    entry = str_searchable.find(str_input)
    if entry != -1:
        print('Первое вхождение подстроки: ', entry)
    else:
        print('Нет вхождений подстроки.\n')
    line = len(str_searchable)
    length = len(str_input)
    while entry != -1:
        entry = str_searchable.find(str_input, entry + length, line)
        if entry != -1:
            print('Вхождение подстроки: ', entry)
        else:
            print('Больше вхождений нет.\n')


main()
