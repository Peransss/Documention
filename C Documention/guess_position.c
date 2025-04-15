#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int Post_chair[5] = {15, 31, 22, 59, 41};

int post_chair(int incash, int chance_get){

    srand(time(NULL));
    int x, y, temp;

    int n = sizeof(Post_chair) / sizeof(Post_chair[0]);
    for (int i = 0; i < n; i++){
        printf("%d ", Post_chair[i]);
    }

    for (int i = 0; i < 6; i++) {
        x = rand() % 5;
        y = rand() % 5;
        temp =  Post_chair[x];
        Post_chair[x] =  Post_chair[y];
        Post_chair[y] = temp;
    }

    int guessChair, t;
    t = rand() % 5;

    do {

        if (incash ==  0) {
            puts("Must insert your cash!");
            break;
        }
        
        printf("\nYour chance are : %d", chance_get);
        chance_get--;
        printf("\nGuess the position chair %d (Start From 0 to 5): ", t);
        scanf("%d", &guessChair);
        
        if (chance_get == 0) {
            puts("Over! Chance are 0");
            break;
        }

        if (guessChair == Post_chair[t]) {
            puts("You may success guess the position!");
            break;
        }
    } while (chance_get != 0);
    return Post_chair[guessChair];
}

int main() {

    int incash, chance_get; 

    printf("Input you cash to convert to be chance : ");
    
    scanf("%d", &incash);

    chance_get = 2 * incash;

    post_chair(incash, chance_get);
    
    return 0;
}