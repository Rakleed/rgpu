#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define n 10 // Количество элементов в массиве

int main() {
    int array[n], i;
    srand(time(NULL));
    /* Заполнение массива случайными числами */
    printf("Массив А:   ");
    for (i = 0; i < n; i++) {
        array[i] = rand() % 50;
        printf("%d ", array[i]);
    }
    /* Первоначальное значение максимального и минимального
    элемента — первый элемент массива */
    int min = array[0], max = array[0];
    // Проходим по массиву, сравнивая max и min c элементами массива
    for (i = 1; i < n; i++) {
        if (array[i] > max)
            max = array[i];
        if (array[i] < min)
            min = array[i];
    }
    printf("\n\n%d — минимальный элемент, %d — максимальный элемент.", min, max);
    return 0;
}
