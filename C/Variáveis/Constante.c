#include <stdio.h>
#include <stdlib.h>

#define a 1

int main() {

    const int b = 2;
    // b = 3; // vai dar erro.
    // a = 4; // também vai dar erro.

    printf("%i", a);
    printf("%i", b);

    system("pause");
    return 0;
}