#include <stdio.h>

int main () {
    int angka[5] = {13, 4, 20, 9, 12};
    int n = sizeof(angka) / sizeof(angka[0]);

    for (int i = 0; i < n; i++) {
        int maxAR = i;
        for (int a = i + 1; a < n; a++) {
            if (angka[a] < angka[maxAR]) {
                maxAR = a;
            }
        }
            int temp = angka[i];
            angka[i] = angka[maxAR];
            angka[maxAR] = temp;
    }

    for (int b = 0; b < n; b++) {
        printf("%d ", angka[b]);
    }

    return 0;
}