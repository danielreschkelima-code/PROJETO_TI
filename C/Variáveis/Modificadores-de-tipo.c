#include <stdio.h>
#include <stdlib.h>

int main() {
    /*
        1) char - carcter
        2) int - num inteiro
        3) float - decimais simples
        4) double - decimais grandes
        5) void - vazio

        1) signed -  + e -
        2) unsigned - +
        3) long - aumenta a capacidade de armazenamento da váriavel
        4) short - diminuir a capacidade de armazenamento da váriavel
    */

    unsigned short int i;
    double u;

    printf("\n%i -> variavel i\n", sizeof(i)); // printa em bytes
    printf("\n%i -> variavel i\n", sizeof(u));

    return 0;
}