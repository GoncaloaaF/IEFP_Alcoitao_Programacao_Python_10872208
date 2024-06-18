#include <stdio.h>
#include <string.h>
/*
 *  nome - char[]
 *  telefone - int
 *
 */


typedef struct contacto{
    char nome[50];
    int telefone;
} Contacto;


int main(void) {

    Contacto lostaCts[10];


    Contacto ct;
    Contacto ct2 = {"Gonaçlo 2", 2134234};


    strcpy(ct.nome, "Gonaçlo");
    ct.telefone = 1231;

    printf("ct = %i\n", ct.telefone);
    printf("ct2 = %i\n", ct2.telefone);

    return 0;
}
