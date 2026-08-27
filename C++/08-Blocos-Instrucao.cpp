#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {

    int num = 10;
    char c = 's';

    {
        cout << "Estamos dentro de um bloco de instrucao." << endl;
        double dinheiro = 4.99;
        cout << "O valor da var 'dinheiro' e: " << dinheiro << "." << endl;
    }

    cout << "Aqui, nos nao conseguimos acessar a variavel 'dinheiro' pois ela esta dentro daquele bloco." << endl;
    int dinheiro = 5; // precisamos redeclarar ela.

    system("pause");
    return 0;
}