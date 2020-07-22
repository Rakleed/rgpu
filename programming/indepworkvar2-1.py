"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ВСР 2. Задание: разработать функцию-декоратор, вычисляющую время
    выполнения декорируемой функции.

"""

from datetime import datetime


def lead_time(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper


@lead_time
def number():
    list_of_numbers = []
    for i in range(10000):
        list_of_numbers.append(i)
    return list_of_numbers


print(number())
