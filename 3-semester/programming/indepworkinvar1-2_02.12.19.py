"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 1.2. Задание: разработать скрипт, вычисляющий сумму первых
    n-членов арифметической прогрессии (использовать функции, условные операторы).

    Прогрессия от 1 с шагом 1.

"""


def summa(s):
    return sum(list(range(s + 1)))


def main():
    numbers = int(input())
    if numbers >= 2:
        print("Сумма = " + str(summa(numbers)) + ".")
    else:
        print("Введите целое число больше 1.")
        main()


print("Программа считает сумму n-членов арифметической прогрессии c шагом 1.\n"
      "Скольких членов вы хотите узнать сумму?")

main()
