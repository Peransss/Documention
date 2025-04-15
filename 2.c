#include <stdio.h>

void swap (int* xp, int* yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

int main() {
    int a[5] = {50, 12, 90, 4, 1};
    int n = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(&a[j], &a[j + 1]);
            }
        }
    }

    for (int b = 0; b < n; b++) {
        printf("%d ", a[b]);
    }
    
    return 0;
}