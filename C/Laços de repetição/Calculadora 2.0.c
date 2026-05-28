#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int main() {
    char operacao = '0'; 
    
    do {
        printf("\n----------------CALCULADORA 2.0----------------");
        printf("\n\nSelecione uma das operacoes: \n(0)Encerrar programa\n(1)Adicao\n(2)Subtracao\n(3)Multiplicao\n(4)Divisao\n\n>>> ");
        operacao = getche();

        if(operacao != '0' && (operacao == '1' || operacao == '2' || operacao == '3' || operacao == '4')) {
            float num1, num2, resultado;
            printf("\n\nDigite o primeiro numero: ");
            scanf("%f", &num1);
            printf("\nDigite o segundo numero: ");
            scanf("%f", &num2);

            if(operacao == '1') {
                resultado = num1 + num2;
            } else if(operacao == '2') {
                resultado = num1 - num2;
            } else if(operacao == '3') {
                resultado = num1 * num2;
            } else {
                resultado = num1 / num2;
            }
            printf("\nRESULTADO: %f\n\n", resultado);

        } else if(operacao != '0') {
            printf("\nOpcao invalida!\n\n");
        } else {
            printf("\n\n");
        }
        system("pause");
        system("cls");
    } while (operacao != '0');

    return 0;
}