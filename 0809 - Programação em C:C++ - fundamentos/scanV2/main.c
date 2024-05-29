#include <stdio.h>

int main(void) {
   int dia;
   int mes;
   int ano;

    printf("data (dia/mes/ano) o mes tem de estar por extenso: ");
    scanf("%d/%d/%d", &dia, &mes, &ano);

    printf("data e:\n");
    printf("%d/%d/%d\n", dia, mes, ano);

    char foo[10];

    scanf("%s", foo);

    printf("%s", foo);



    return 0;
}
