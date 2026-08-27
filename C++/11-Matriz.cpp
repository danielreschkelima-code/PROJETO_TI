#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {

    int matriz[3][3] = {{1, 2, 3},{4, 5, 6},{7, 8, 9}};

     for (int i = 0; i < 3; i++) {
        cout << "Linha: " << i << endl;
        for (int j = 0; j < 3; j++) {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }

    system("pause");
    return 0;
}