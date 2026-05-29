#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("\nREPETICOES\n\n0 AO 10 COM WHILE:");

    //WHILE
    int i = 0;
    while(i <= 10) {
        printf("\n");
        printf("\t%i", i);
        i++;
    }

    //DO
    i = 0;
    printf("\n\n0 AO 10 COM DO WHILE (do sempre faz no comeco): ");
        do {
        printf("\n");
        printf("\t%i", i);
        i++;
    } while(i <= 10); 

    //FOR
    printf("\n\n0 AO 10 COM FOR:");

    for(int i = 0; i <= 10; i++) {
        printf("\n");
        printf("\t%i", i);
    }

    printf("\n\n");
    system("pause");
    return 0;
}