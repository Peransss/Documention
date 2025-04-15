#include <iostream>
using namespace std;

int main () {
    int angka[0];
    int n;

    cout << "Batas : ";
    cin >> n;

    for (int i = 0; i <= n; i++) {
        for (int a = 1; a <= n; a++) {
            angka[i] = a;

            if (angka[i] % 2 == 0) {
                cout << angka[i] << " ";
            }
        }
        break;
    }
    return 0;
}