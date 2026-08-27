#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
    cout << "----------------IDADE----------------\n" << endl;
    cout << "Digite sua idade: ";
    int idade;
    cin >> idade;
    
    if(idade < 18) {
        cout << "\n" << idade << " : e menor de idade" << endl;
    } else if(idade < 60) {
        cout << "\n" << idade << " : e maior de idade" << endl;
    } else {
        cout << "\n" << idade << " : e da terceira idade" << endl;
    }
    cout << endl;
    system("pause");
    return 0;
}