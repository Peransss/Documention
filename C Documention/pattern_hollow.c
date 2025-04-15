#include <stdio.h>

int main()
{
    int n;
    printf("Rows : ");
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= i; j++)
        {
            if (j == 1 || j == i)
            {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }

    for (int k = n - 1; k >= 1; k--)
    {
        for (int z = 1; z <= k ; z++)
        {
            if (z == 1 || z == k)
            {
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
    return 0;
}