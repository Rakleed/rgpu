"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 4.2. Задание: создать программу по распределению списка со
    случайными значениями на два списка по определенному критерию
    (четность/нечетность, положительные/отрицательные числа).

"""

import random

first_array = []
positive_numbers = []
negative_numbers = []
for i in range(10):
    first_array.append(int(random.random() * 15) - 8)
for i in first_array:
    if i < 0:
        negative_numbers.append(i)
    elif i > 0:
        positive_numbers.append(i)
print("Списики со случайными значениями (положительные/отрицательные):")
print(positive_numbers)
print(negative_numbers)

second_array = []
for i in range(10):
    second_array.append(int(random.random() * 20))
second_array.sort()
even_numbers = list(filter(lambda x: not x % 2, second_array))
odd_numbers = list(filter(lambda x: x % 2, second_array))
print("\nСписики со случайными значениями (чётные/нечётные):")
print(even_numbers)
print(odd_numbers)
