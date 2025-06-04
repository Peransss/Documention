#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define MAX 100

int game(char you, char comp) {
    if (you == comp) {
        return -1;
    }

    // Rock
    if (you == 'r' && comp == 'p') {
        return 0;
    } else if (you == 'p' && comp == 'r') {
        return 1;
    }

    // Scissors
    if (you == 's' && comp == 'r') {
        return 0;
    } else if (you == 'r' && comp == 's') {
        return 1;
    }

    // Paper
    if (you == 'p' && comp == 's') {
        return 0;
    } else if (you == 's' && comp == 'p') {
        return 1;
    }
    return 2;
}

char rand_rps() {
    srand(time(NULL));

    int x = rand () % MAX;

    if (x < 33) {
        return 'r';
    } else if (x > 33 && x < 66) {
        return 'p';
    } else {
        return 's';
    }
}

int main () {
    char you, comp, result;

    comp = rand_rps();

    printf("Welcome to RPS Game!");
    printf("Choose your choice (r/p/s) : ");
    scanf("%c", &you);

    result = game(you, comp);

    printf("You : %c Computer : %c\n", you, comp);

    if (result == 1) {
        printf("You are the winners!");
    } else if (result == 0) {
        printf("Computer capture the winners!");
    } else {
        printf("No one else win this game!");
    }
}