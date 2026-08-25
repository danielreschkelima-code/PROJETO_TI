#include <iostream>
#include <stdlib.h>
#include <iomanip>
using namespace std;

int main() {

    // << é inserção; >> extracao

    // obj cout
    cout << setw(1000) << "Estudando entrada e saida de dados" << endl; // campo de mil carcteres por causa do setw
    cout << "Viu so" << endl;
    cout << hex << 10 + 50 << endl; // vai sair em hexa por causa do hex

    // obj cin
    cout << "Informe um numero: " << endl;
    int num1 = 0;
    cin >> num1;

    cout << "\nO numero digitado e: " << dec << num1 << "." << endl;

    system("pause");
    return 0;
}