#include <iostream>
#include <stdlib.h>
using namespace std;

int main() {
    float num, num2;
    char op;
    cout << "----------------CALCULADORA----------------" << endl;
    cout << "Digite o primeiro numero: ";
    cin >> num;
    cout << "Digite o segundo numero: ";
    cin >> num2;
    cout << "Digite a operacaoo (+ - / *): ";
    cin >> op;
    switch (op)
    {
    case '+':
        cout << "Soma: " << num + num2 << endl;
        break;
    
    case '-':
        cout << "Subtracao: " << num - num2 << endl;
        break;
    
    case '*':
        cout << "Multiplicacao: " << num * num2 << endl;
        break;
    
    case '/':
        cout << "Divisao: " << num / num2 << endl;
        break;

    default:
        cout << "Operação inválida! Selecione uma das operações disponíveis: + - / *";
        break;
    }
    system("pause");
    return 0;
}