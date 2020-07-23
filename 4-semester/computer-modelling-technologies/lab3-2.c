#include <stdio.h>
#define n 4

int main() {
    int i, j, k;
    float c, s;
    float a[n][n+1] = {-1, 0, 0, -1, -9.8, 1, -1, 0, -1, 0.098, 0, 1, -1, -1, 0.098, 0, 0, 1, -1, 0.098};
    float x[n];

    printf("\nИсходная матрица:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n + 1; j++)
            printf("%.3f\t", a[i][j]);
        printf("\n");
    }

    for (i = 0; i < n - 1; i++)
    {
        for (k = i + 1; k < n; k++)
            if (a[k][i] != 0)
            {
                {
                    c = a[k][i] / a[i][i];
                    for (j = i; j < n + 1; j++)
                        a[k][j] = a[k][j] - c * a[i][j];
                }
            }
    }

    printf("\nПреобразованная матрица:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n+1; j++)
            printf("%f\t", a[i][j]);
        printf("\n");
    }

    x[n-1] = a[n-1][n] / a[n-1][n-1];
    for (i = 2; i >= 0; i--)
    {
        s = 0;
        for (j = i + 1; j < n; j++)
            s += a[i][j] * x[j];
        x[i] = (a[i][n] - s) / a[i][i];
    }

    printf("\nX:\n");
    for (i = 0; i < n - 1; i++)
        printf("F%d = %.4f\n", i + 1, x[i]);
    printf("a  = %.5f\n", x[3]);
    return 0;
}
