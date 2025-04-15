#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>

int calculate (int x, int a, char y[4]) {
    
    int z;

    if (strcmp(y, "+") == 0) {
        z = x + a;
        printf("Results : %d", z);
    } else if (strcmp(y, "-") == 0){
        z = x - a;
        printf("Results : %d", z);
    } else if (strcmp(y, "*") == 0){
        z = x * a;
        printf("Results : %d", z);
    } else if (strcmp(y, "/") == 0){
        z =  x / a;
        printf("Results : %d", z);
    } else if (strcmp(y, "/^2") == 0) {
        z = sqrt(x);
        printf("Results : %d", z);
    } else if (strcmp(y, "$sin") == 0) {
        float z = sin(x);
        printf("Results : %f", z);
    } else if (strcmp(y, "$cos") == 0) {
        float z = cos(x);
        printf("Results : %f", z);
    } else if (strcmp(y, "$tan") == 0) {
        float z = tan(x);
        printf("Results : %f", z);
    } else if (strcmp(y, "^2") == 0) {
        z = pow(x, a);
        printf("Results : %d", z);
    }
    return 0;
}  

int main () {

    int x, a;
    char y[4];

    printf("== Input The Number ==");
    printf("\nOperation (+, -, *, /, /^2, ^2)");
    printf("\nOperation ($sin, $cos, $tan)");
    printf("\nOperation : ");
    scanf("%s", y);

    if (strcmp(y, "/^2") == 0) {
        printf("Input Num 1: ");
        scanf("%d", &x);
    } else if (strcmp(y, "$sin") == 0) {
        printf("Input Num 1: ");
        scanf("%d", &x);
    } else if (strcmp(y, "$cos") == 0) {
        printf("Input Num 1: ");
        scanf("%d", &x);
    } else if (strcmp(y, "$tan") == 0) {
        printf("Input Num 1: ");
        scanf("%d", &x);
    } else if (strcmp(y, "^2") == 0) {
        printf("Input Num 1: ");
        scanf("%d", &x);
        printf("Raise : ");
        scanf("%d", &a);
    } else {
        printf("Input Num 1: ");
        scanf("%d", &x);
        printf("Input Num 2: ");
        scanf("%d", &a);
        }
    calculate(x, a, y);
    return 0;
}