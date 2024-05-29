#include <stdio.h>



// bissexto - 2000
// comum = 2001


int main() {
// ex17 - decisão

    int ano;

    printf("Indique o ano: ");
    scanf("%i", &ano);

    if((ano % 4 == 0 && ano % 100 != 0) || ano % 400 == 0) {
        printf("O ano é bissexto.");
    } else {
        printf("O ano não é bissexto.");
    }


    return 0;
}
