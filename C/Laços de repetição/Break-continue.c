#include <stdio.h>
#include <stdlib.h>

int main() {
    
    printf("\n\n------------------BREAK E CONTINUE------------------");
    
    for(int i = 0; i <= 10; i++) {
        printf("\n");
        if(i == 2) {
            continue; // interrompe o laço: só o 2 não vai ser impresso.
        }
        if(i == 8) {
            break; // interrompe todo o laço de repetição: nada depois do 8 vai ser impresso.
        }
        printf("\t%i", i);
    }

    printf("\n\n");
    system("pause");
    return 0;
}