#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n = 10, k = 0;
    int M[n], i, j;
    srand(time(NULL));
    printf("Неотсортированный массив:   ");
    for (i = 0; i < n; i++) {
        M[i] = rand() % 20;
        printf("%d ", M[i]);
    }
    int max = M[0]; // Найти максимальный элемент для определения количества элементов массива C
    for (i = 1; i < n; i++) {
        if (M[i] > max) max = M[i];
    }
    int C[max + 1];
    for (i = 0; i < max + 1; i++)
        C[i] = 0;
    for (i = 0; i < n; i++)
        C[M[i]] = C[M[i]] + 1; // Определяю сколько раз содержится каждый элемент массива в массиве
        printf("\n\n");
    for (i = 0; i < max; i++)
        printf("%d ", C[i]);
    for (i = 0; i < max + 1; i++) {
        for (j = 0; j < C[i]; j++) {
            M[k] = i;
            k = k + 1;
        }
    }
    printf("\n\nОтсортированный массив:   ");
    for (i = 0; i < n; i++)
        printf("%d ", M[i]);
    return 0;
}
