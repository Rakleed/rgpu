"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    Задание: разработать программу, которая для заданного количества
    значений возвращала бы список из уникальных элементов,
    содержащихся во входном наборе значений.

"""


def set_func(values):
    var = set(values)
    return list(var)


def main():
    numbers = int(input("Введите количество значений: "))
    print("Теперь вводите числа:")
    values = list()
    while numbers != 0:
        values.append(input())
        numbers -= 1
    print('Введённые значения: ', values)
    print('Уникальные значения: ', set_func(values))


main()
