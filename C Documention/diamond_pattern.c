#include <stdio.h>

int main()
{
	int rows;
    printf("Rows : ");
    scanf("%d", &rows);
    
	for (int i = 1;i <= rows ; i++) {

		for (int j = 1; j <= 2 * (rows - i) ; j++) 
        {
			printf(" ");
		}

		for (int k = 1; k < 2 * i; k++) 
        {
            printf("%d ", i);
		}
		printf("\n");
	}

    for (int z = rows - 1; z >= 1; z--)
    {
        for (int f = 1; f <= 2 * (rows - z); f++)
        {
            printf(" ");
        }

        for (int a = 1; a <= 2 * z - 1; a++)
        {
            printf("%d ", z);
        }
        printf("\n");
    }
	return 0;
}
