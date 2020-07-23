"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ВСР 4. Задание: создать программу с реализацией вручную одного
    из алгоритмов сортировки (вставки, плавной сортировки).

"""

from random import randint


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i - 1
        key = nums[i]
        while nums[j] > key and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


array = []
for i in range(10):
    array.append(randint(0, 20))
print("Массив со случайными целыми числами:", array)
print("Сортировка вставками:", insertion_sort(array))
