#include <stdio.h>
int main(){
    int num1, num2;
    
    printf("\nCalculadora 1.0");
    printf("\nDigite dois numeros para serem processados:\n");
    scanf("%i%i", &num1, &num2);

    int soma = num1 + num2;
    int subtracao = num1 - num2;
    int multiplicacao = num1 * num2;
    int divisao = num1 / num2;
    int resto = num1% num2;

    printf("\nA soma e: %i", soma);
    printf("\nA substracao e: %i", subtracao);
    printf("\nA multiplicacao e: %i", multiplicacao);
    printf("\nA divisao e: %i", divisao);
    printf("\nO resto e: %i", resto);
    return 0;
}