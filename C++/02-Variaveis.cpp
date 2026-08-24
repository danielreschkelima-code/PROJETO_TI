#include <iostream>
#include <stdlib.h>

using namespace std;

int main() {
    int num;
    num = 10;
    int num2 = 20;

    cout << num + num2 << endl;

    // TODOS OS TIPOS:

    bool logico = true;
    char caractere = 'A';
    int inteiro = 10;
    float ponto_flutuante = 10.1;
    double ponto_flutuante64bit = 10.222222222222222222;
    // void vazio
    wchar_t string = 'Tex';

    // MANIPULANDO ELAS

    cout << "O valor da variavel carctere e: " << caractere << endl;
    cout << "A memoria que ela gasta e: " << sizeof(caractere) << " bytes" << endl;

    system("pause");
    return 0;
}