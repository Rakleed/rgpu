"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    Задание: разработайте скрипт с функцией, которая строит таблицу ис-
    тинности для логического выражения (по вариантам) для двух и трех
    аргументов (используются различные наборы значений аргументов).

"""

values_2 = ((0, 0), (0, 1), (1, 0), (1, 1))
values_3 = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1),
            (1, 1, 0), (1, 1, 1))


def head_2():
    header = "| A | B | F |"
    under_header = "+ " + "-" * (len(header) - 4) + " +"
    print(under_header)
    print(header)
    print(under_header)


def head_3():
    header = "| A | B | C | F |"
    under_header = "+ " + "-" * (len(header) - 4) + " +"
    print(under_header)
    print(header)
    print(under_header)


def truth_table_2(val):
    result = (not val[0]) or val[0]  # ((A→B)∧A)↔A∧B = ¬A∨A
    result = int(result)
    line = "| " + str(val[0]) + " | " + str(val[1]) + " | " + str(result) + \
           " |"
    print(line)
    print('+', '-' * (len(line) - 4), '+')


def truth_table_3(val):
    result = (val[0] or val[1]) and (not val[2])
    result = int(result)
    line = "| " + str(val[0]) + " | " + str(val[1]) + " | " + str(val[2]) + \
           " | " + str(result) + " |"
    print(line)
    print('+', '-' * (len(line) - 4), '+')


def main_2():
    print("F = ((A→B)∧A)↔A∧B\n")
    head_2()
    for i in range(len(values_2)):
        truth_table_2(values_2[i])


def main_3():
    print("\n\nF = (A∨B)∧¬C\n")
    head_3()
    for i in range(len(values_3)):
        truth_table_3(values_3[i])


main_2()
main_3()
