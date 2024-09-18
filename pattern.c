#include <stdio.h>

int main(){

    int rows;
    printf("Rows Are : ");
    scanf("%d", &rows);

    int i, j, k, l;

    for (k = 1; k <= rows; k++){
        for (l = 1; l <= k; l++){
            printf("* ");
        }
        printf("\n");
    }

    for (i = rows; i >= 0; i--){
        for (j = i; j >= 0; j--){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}