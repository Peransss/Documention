#include <iostream>
using namespace std;

void print();

int main()
{
    int i, fact = 1, num;
    cout << "Enter any Number: ";
    cin >> num;
    for (i = 1; i <= num; i++) {
        fact = fact * i;
    }
    cout << "Factorial of " << num << " is: " << fact << endl;
    return 0;
}

