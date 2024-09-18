#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    int iSecret, iGuess, i = 4;

    srand(time(NULL));

    iSecret = rand() % 30 + 100;

    do {
        i--;
        printf("Have Chance %d", i);
        printf("\nGuess The Number : ");
        scanf("%d", &iGuess);
        if (i == 1) break;
        else if (iSecret > iGuess) puts("Secret Number is Higher");
        else if (iSecret < iGuess) puts("Secret Number is Lower");
    } while (iSecret != iGuess);

    if (i == 1) puts("Over! Chance are 0");
    else if (iSecret == iGuess) puts("Congratulations");
    
    return 0;
}