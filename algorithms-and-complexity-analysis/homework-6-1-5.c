#include <stdlib.h>
#include <stdio.h>
#include <time.h>

#define n 10 // Количество элементов в массиве
#define l 50 // Граница интервала в котором берутся случайные числа

int main() {
    int array[n], i;
    srand(time(NULL));
    // Заполнение массива случайными числами
    printf("Массив А:   ");
    for (i = 0; i < n; i++) {
        array[i] = rand() % l;
        printf("%d ", array[i]);
    }
    // min — минимальный элемент, его первоначальное значение — первый элемент массива
    int min = array[0];
    for (i = 1; i < n; i++)
        if (array[i] < min)
            min = array[i];
    /* near_to_min — ближайший к минимальному элемент, его первоначальное значение
       должно быть больше минимального, поэтому присваиваем ему значение min+l */
    int near_to_min = min + l;
    for (i = 0; i < n; i++)
        if (array[i] < near_to_min && array[i] != min)
            near_to_min = array[i];
    printf("\n\n%d — минимальный элемент, %d — ближайший к минимальному элемент.",
           min, near_to_min);
    return 0;
}
