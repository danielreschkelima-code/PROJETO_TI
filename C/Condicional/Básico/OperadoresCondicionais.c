#include <stdio.h>
#include <stdlib.h>

int main() {
    //&& E lógico
    //! NÃO lógico
    //||OU lógico

    int i = 40;
    
    int condicao = (i>20)&&(i<100);

    printf("\n%i", condicao); //printa 1
    printf("\n%i", !condicao);//printa 0

    system("cls"); //limpa a tela

    int x = 10;
    int cond = (x==10)||(x<1);

    printf("\n%i", cond);
    printf("\n%i", !cond);

    return 0;
}