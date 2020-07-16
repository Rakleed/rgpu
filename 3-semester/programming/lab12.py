"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ЛР 12. Задание: написать программу для вычисления факториала.

"""


def main():
    number = -1
    input_number = input("Введите число: ")
    try:
        number = int(input_number)
    except:
        print("Вы ввели неверное значение.")
    result = factorial(number)
    print("Факториал {} = {}.".format(input_number, result))


def factorial(number):
    if type(number) is int and number >= 0:
        fl = 1
        i = number
        if number == 0:
            return 1
        else:
            while i > 1:
                fl = fl * i
                i -= 1
        return fl
    else:
        raise ValueError("Вы ввели неверное число.")


main()
