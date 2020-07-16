"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 3.3. Задание: реализовать программу-игру «Угадай число», в
    которой для вывода на экран информации использовать метод format.

"""


def guess_number(a, b):
    import random
    random_number = random.randint(a, b)
    user_number = -0.5
    while random_number != user_number:
        user_number = int(input('Введите число: '))
        if user_number < random_number:
            print('Вы не угадали, введите число больше.')
        elif user_number > random_number:
            print('Вы не угадали, введите число меньше.')
    print('Вы угадали число {} из диапазона [{}, {}]!'.format(random_number,
                                                             a, b))


def main():
    print('Введите диапазон для игры.')
    a = int(input('Нижний предел: '))
    b = int(input('Верхний предел: '))
    guess_number(a, b)


main()
