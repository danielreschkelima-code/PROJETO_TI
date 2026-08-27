#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
    cout << "\nREPETICOES\n\n0 AO 10 COM WHILE:" << endl;

    //WHILE
    int i = 0;
    while(i <= 10) {
        cout << "\t" << i << endl;
        i++;
    }

    //DO
    i = 0;
    cout << "\n0 AO 10 COM DO WHILE (do sempre faz no comeco): " << endl;
        do {
        cout << "\t" << i << endl;
        i++;
    } while(i <= 10); 

    //FOR
    cout << "\n0 AO 10 COM FOR:" << endl;

    for(int i = 0; i <= 10; i++) {
        cout << "\t" << i << endl;
    }

    cout << endl;
    system("pause");
    return 0;
}