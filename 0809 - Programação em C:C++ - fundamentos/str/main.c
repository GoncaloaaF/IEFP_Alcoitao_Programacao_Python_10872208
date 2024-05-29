#include <stdio.h>

int main(void) {

    /*
     * int
     * float
     * double
     * char     ->  ' '
     * char[]   ->  " " <- String
     */

    char nome[3] = "Rui";
    char nome2[4] = {'R','u','i', '\0'};
    printf("%s\n", nome);
    printf("%s\n", nome2);



    printf("nome: ");
    scanf("%s", &nome);

    printf("o nome é %s\n", nome);
    nome[0] = 'r';

    printf("o nome é %s\n", nome);


    return 0;
}
