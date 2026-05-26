#include <stdio.h>
int main(){
    int num1, num2;
    
    printf("\nCalculadora 1.0");
    printf("\nDigite dois numeros para serem processados: ");
    scanf("%i%i", &num1, &num2);

    int soma = num1 + num2;
    int subtracao = num1 - num2;
    int multiplicacao = num1 * num2;
    int divisao = num1 / num2;
    int resto = num1% num2;

    printf("A soma e: ", soma);
    printf("A substracao e: ", subtracao);
    printf("A multiplicacao e: ", multiplicacao);
    printf("A divisao e: ", divisao);
    printf("O resto e: ", resto);

    return 0;
}