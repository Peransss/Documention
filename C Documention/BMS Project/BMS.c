#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

struct Account{
    char name[50];
    int PIN, PIN1;
    char dd_mm_yyyy[11];
    int balance;
};

void createAccount(){
    struct Account Acc;

    FILE *acc;

    acc = fopen("list_acc.dat", "wb");

    printf("\n-----===-----\n");
    printf("Full Name : ");
    scanf(" %[^\n]", Acc.name);
    printf("DD/MM/YYYY : ");
    scanf(" %10s", Acc.dd_mm_yyyy);

    while (true) {
        printf("PIN : ");
        scanf("%d", &Acc.PIN);
        printf("Confirm PIN : ");
        scanf("%d", &Acc.PIN1);

        if (Acc.PIN == Acc.PIN1) {
            printf("Account has been create!");
            Acc.balance = 50000;
            break;
        }
    }

    fwrite(&Acc, sizeof(struct Account), 1, acc);
    fclose(acc);
}   

void loginAccount() {
    struct Account Acc;
    int PIN, n;
    FILE *acc;

    acc = fopen("list_acc.dat", "rb");
    fread(&Acc, sizeof(struct Account), 1, acc);

    if (acc == NULL) {
        printf("Account hasn't been created!");
    } else {
        printf("\n-----Login Account-----\n");
        while (true) {
            printf("PIN : ");
            scanf("%d", &PIN);
            n += 1;
            if (PIN == Acc.PIN && n <= 3) {
                printf("Login succesfully!");
                break;
            }
        }
    }
}

void transferMoney() {
    struct Account Acc;
    FILE *acc;
    int tf, rek;

    acc = fopen("list_acc.dat", "rb");
    fread(&Acc, sizeof(struct Account), 1, acc);

    if (Acc.balance == 0) {
        printf("Your balance insufficient for transfer");
    } else {
        printf("Transfer to [Number]: ");
        scanf("%d", &rek);
        printf("Amount to transfer : ");
        scanf("%d", &tf);
    }
    Acc.balance -= tf;
}

void checkBalance() {
    struct Account Acc;
    FILE *acc;

    acc = fopen("list_acc.dat", "rb");
    fread(&Acc, sizeof(struct Account), 1, acc);

    printf("Balance : %d", Acc.balance);
}

int main() {
    int a;

    while (true) {
        printf("\n--- Bank Account ---\n");
        printf("Main Menu : ");
        printf("\n1. Create Account");
        printf("\n2. Login Account");
        printf("\n3. Transfer");
        printf("\n4. Check Balance");
    
        printf("\nMenu : ");
        scanf("%d", &a);
        switch (a) {
            case 1:
                createAccount();
                break;
            case 2: 
                loginAccount();
                break;
            case 3:
                transferMoney();
                break;
            case 4:
                checkBalance();
                break;
            default:
                printf("Must select!");
                break;
        }
    }
    return 0;
}