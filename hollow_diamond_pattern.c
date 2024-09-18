#include <stdio.h>

int main()
{
	int rows;
    printf("Rows : ");
    scanf("%d", &rows);
    
	for (int i = 1;i <= rows ; i++) {

		for (int j = i; j < rows; j++) 
        {
			printf(" ");
		}

		for (int k = 1; k < 2 * i; k++) 
        {
            if (k == 1 || k == 2 * i - 1)
            {
                printf("%d", i);
            } else {
                printf(" ");
            }
		}
		printf("\n");
	}

    for (int z = rows - 1; z >= 1; z--)
    {
        for (int f = rows; f > z; f--)
        {
            printf(" ");
        }

        for (int a = 1; a <= 2 * z - 1; a++)
        {
            if (a == 1 || a == 2 * z - 1)
            {
                printf("%d", z);
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
	return 0;
}
