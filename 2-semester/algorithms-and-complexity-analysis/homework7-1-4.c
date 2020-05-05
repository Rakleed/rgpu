#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define size 11 // Количество элементов в массиве

int main() {
    int array[size], i;
    srand(time(NULL));
    // Заполнение массива случайными числами
    printf("Неотсортированный массив:   ");
    for (i = 0; i < size; i++) {
        array[i] = rand() % 100 - 50;
        printf("%d ", array[i]);
    }
    for (int i = 0; i < size - 1; i++) {
        int min = i; // Устанавливаем начальное значение минимального индекса
        // Находение индекса минимального элемента
        for (int j = i + 1; j < size; j++)
        {
            if (array[j] < array[min])
            {
                min = j;
            }
        }
        // Меняем значения местами
        int temp = array[i];
        array[i] = array[min];
        array[min] = temp;
    }
    printf("\n\nОтсортированный массив:   ");
    for (i = 0; i < size; i++)
        printf("%d ", array[i]);
    printf("\n\nМедиана массива: %d.", array[size / 2]);
    return 0;
}
