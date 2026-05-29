#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("\n--------------OPERADOR TERNARIO--------------");

    int num, num2, maior;

    printf("\n\nInforme um numero: ");
    scanf("%i", &num);

    printf("\nInforme outro numero: ");
    scanf("%i", &num2);

    maior = (num > num2) ? num : num2;
    printf("\n\nO maior numero e: %i\n\n", maior);

    system("pause");
    return 0;
}