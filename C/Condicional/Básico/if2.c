#include <stdio.h>
#include <stdlib.h>

int main() {
    int i;
    printf("\nDigite um numero (vamos verificar se ele e maior que 10): ");
    scanf("%i", &i); // o & serve para representar o endereço da variável.

    if(i > 10) {
        printf("\n %i e maior que 10.\n", i);
    } else if (i < 10) {
        printf("\n %i e menor que 10.\n", &i); // repare que ele, por causa do & vai mostrar o endereço, mas não o número que i guarda.
    } else {
        printf("\n %i e igual a 10.\n", i);
    }
    printf("\n");
    return 0; // ele retorna -1 se dá erro
}