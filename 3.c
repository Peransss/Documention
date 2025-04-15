#include <stdio.h>
#include <stdlib.h>

int main () {
    int n;
    int *arrScore;
    int *avrg;
    float avrg1;

    printf("People : ");
    scanf("%d", &n);

    arrScore = (int*)malloc(sizeof(int)*n);

    for (int i = 0; i < n; i++) {
        printf("Score %d : ", i + 1);
        scanf("%d", &arrScore[i]);
    }

    for (int j = 0; j < n; j++) {
        printf("%d ", arrScore[j]);
    }

    for (int a = 0; a < n; a++) {
        for (int b = 1; b < n; b++) {
            arrScore[a] += arrScore[b];
            avrg = arrScore;
            avrg1 = *avrg;
            avrg1 = avrg1 / n;
        }
    }
    printf("\nAverage : %.1f", avrg1);

    return 0;
}