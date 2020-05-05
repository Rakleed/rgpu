"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    Задание: переписать лямбда-функцию, генерирующую квадраты чисел из
    переменной типа list, через генератор списка.

"""

import random


def random_generator(numbers, maximum):
    random_list = []
    for i in range(numbers):
        random_list.append(random.randint(0, maximum))
    return random_list


def main():
    print("Программа генерирует случайный список элементов, а потом создаёт "
          "новый список из этих же чисел, возведённых в квадрат.")
    maximum = int(input("Введите верхнюю границу диапазона случайных "
                        "чисел: "))
    numbers = int(input("Введите количество случайных элементов: "))
    random_items = random_generator(numbers, maximum)
    print("Список случайно сгенерированных элементов: ", random_items)
    print("Список этих же элементов, возведённых в квадрат: ",
          list(map(lambda x: x * x, random_items)))


main()
