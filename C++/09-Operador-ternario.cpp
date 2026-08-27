#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
    cout << "-----------------CALCULADOR 2 MEDIA-----------------\n" << endl;

    float nota, nota1;
    cout << "Digite valor da primeira nota: ";
    cin >> nota;
    cout << "Digite valor da segunda nota: ";
    cin >> nota1;

    float media = (nota + nota1) / 2;

    string textoMedia = (media>=7) ? "Aprovado!\n" : "Reprovado!\n";
    cout << textoMedia;

    cout << endl;
    system("pause");
    return 0;
}