#include <stdio.h>

int main()
{
    int n;
    printf("Rows : ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = i; j < n; j++)
        {
            printf(" ");
        }

        for (int k = 1; k < 2 * i; k++)
        {
           printf("*");
        }
        printf("\n");
    }
        for (int a = 4; a <= n; a++)
    {
        for (int b = a; b < n; b++)
        {
            printf(" ");
        }

        for (int c = 1; c < 2 * a; c++)
        {
            printf("*");
        }
        printf("\n");
    }
    for (int d = 1; d <= 2; d++)
    {
        for (int t = 1; t <= 2; t++)
        {
            printf(" ");
        }
        for (int k = 1; k <= 5; k++)
        {
           printf("*");
        }
        printf("\n");
    }
    return 0;
}