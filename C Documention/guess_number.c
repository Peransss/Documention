#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){

    int iSecret, iGuess, i, cash;

    printf("Convert your cash to be chance : ");
    scanf("%d", &cash);

    i = 2 * cash;

    srand(time(NULL));

    iSecret = rand() % 100 + 1;

    do {
        printf("Have Chance %d", i);
        i--;
        printf("\nGuess The Number (1 to 100) : ");
        scanf("%d", &iGuess);
        if (i == 0) break;
        else if (iSecret > iGuess) puts("Secret Number is Higher");
        else if (iSecret < iGuess) puts("Secret Number is Lower");
    } while (iSecret != iGuess);

    if (i == 0) puts("Over! Chance are 0");
    else if (iSecret == iGuess) {
        puts("Congratulations!");
        cash += 2;
        printf("Your cash now %d", cash);
    }
    return 0;
}