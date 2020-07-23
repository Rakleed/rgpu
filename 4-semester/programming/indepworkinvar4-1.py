"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 4.1. Задание: создать программу по заполнению массива
    случайными значениями. Сортировка значений в списке методом
    вставки, плавной сортировки, с помощью встроенных функций языка.

"""

import numpy as np
import numpy.random


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i - 1
        key = nums[i]
        while nums[j] > key and j >= 0:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def smooth_sort(nums):
    def down_heap(nums, k, n):
        new_element = nums[k]
        while 2 * k + 1 < n:
            child = 2 * k + 1
            if child + 1 < n and nums[child] < nums[child + 1]:
                child += 1
            if new_element >= nums[child]:
                break
            nums[k] = nums[child]
            k = child
        nums[k] = new_element
    size = len(nums)
    for i in range(size // 2 - 1, -1, -1):
        down_heap(nums, i, size)
    for i in range(size - 1, 0, -1):
        temp = nums[i]
        nums[i] = nums[0]
        nums[0] = temp
        down_heap(nums, 0, i)
    return nums


array = np.random.randint(0, 20, 10)
sort_array = sorted(array)
reverse_array = sorted(array, reverse=True)
rand_array = np.random.choice(array, 20, replace=True)
per_array = np.random.permutation(array)
print("Массив со случайными целыми числами:", array)
print("\n*Сортировка с помощью встроенных функций*")
print("Сортировка массива по возрастанию:", sort_array)
print("Сортировка массива по убыванию:", reverse_array)
print("Перемешанный массив:", per_array)
print("Случайна выборка из массива:", rand_array)
print("\nСортировка вставками:", insertion_sort(array))
print("Плавная сортировка:", smooth_sort(array))
