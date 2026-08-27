#include <iostream>
#include <stdlib.h>
using namespace std;

struct Pessoa {
    string nome;
    string sobrenome;
    int idade;
    string cpf;
};

int main() {

    Pessoa p1, p2;
    p1.nome = "Fulano";
    p1.sobrenome = "De tal";
    p1.idade = 25;
    p1.cpf = "86190314034";

    p2.nome = "Daniel";
    p2.sobrenome = "Reschke";
    p2.idade = 18;
    p2.cpf = "86190814034";


    system("pause");
    return 0;
}