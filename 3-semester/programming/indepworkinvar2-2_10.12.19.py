"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    Задание: разработайте программу, которая выводит на экран
    с помощью ASCII-графики таблицу истинности на основе переданных ей
    на вход аргументов (логическое выражение, аргументы, результат
    вычисления выражения).

"""

values = ((0, 0), (0, 1), (1, 0), (1, 1))


def head():
    header = "| A | B | F |"
    under_header = "+ " + "-" * (len(header) - 4) + " +"
    print(under_header)
    print(header)
    print(under_header)


def truth_table(val):
    result = (not val[0] and val[1]) or (val[0] and not val[1])  # (A∨B)∧(¬A∨¬B) = (¬A∧B)∨(A∧¬B)
    result = int(result)
    line = "| " + str(val[0]) + " | " + str(val[1]) + " | " + str(result) + \
           " |"
    print(line)
    print('+', '-' * (len(line) - 4), '+')


def main():
    print("F = (A∨B)∧(¬A∨¬B)\n")
    head()
    for i in range(len(values)):
        truth_table(values[i])


main()
