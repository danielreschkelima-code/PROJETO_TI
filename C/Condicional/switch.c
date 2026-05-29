#include <stdio.h>
#include <stdlib.h>

int main() {

    printf("\n-----------------SWITCH-----------------\n");
    
    int i;
    printf("\nDigite um valor de 0 a 3: "); 
    scanf("%i", &i);

    switch(i) {
        case 0:
            printf("\nA opcao digitada foi 0\n");
            break;
        case 1:
            printf("\nA opcao digitada foi 1\n");
            break;
        case 2:
            printf("\nA opcao digitada foi 2\n");
            break;
        case 3:
            printf("\nA opcao digitada foi 3\n");
            break;
        default:
            printf("\nA opcao digitada nao e valida!\n");
    }

    printf("\n");
    system("pause");
    return 0;
}