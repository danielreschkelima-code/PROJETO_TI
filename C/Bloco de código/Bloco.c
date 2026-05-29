#include <stdio.h>
#include <stdlib.h>

int main() {

    printf("\n\n-------------BLOCOS-------------");

    {
        printf("\n\nBLOCO 1");
        int dinheiro = 1000;
        printf("\n%i", dinheiro);
    }
    // aqui dinheiro já está fora de escopo (não existe mais), é preciso redeclarar.

    int dinheiro = 2000;
    printf("\n\n%i\n\n", dinheiro);

    system("pause");
    return 0;
}