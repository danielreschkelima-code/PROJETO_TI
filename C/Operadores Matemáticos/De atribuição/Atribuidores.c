#include <stdio.h>
#include <stdlib.h>

int main() {
    int i = 50;

    /*
        1) += SOMA
        2) -= SUBTRAÇÃO
        3) *= MULTIPLICAÇÃO (útil para fatorial)
        4) /= DIVISÃO
        5) %= RESTO 
    */

    printf("\n");
    printf("Soma: %i\n", i+=100);
    printf("Subtracao: %i\n", i-=50);
    printf("Multiplicacao: %i\n", i*=3);
    printf("Divisao: %i\n", i/=3);
    printf("Resto: %i\n", i%=3);

    return 0;
}