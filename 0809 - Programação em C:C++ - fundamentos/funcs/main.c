#include <stdio.h>



/*
 *
 * void - não retorna nada
 *  int
 *  char
 *  float
 *  double
 *  []
 *
 */


void olaMundo(){
    printf("Ola Mundo\n");
    printf("Hello, World!\n");
}


void olaMundo2(int ano){
    printf("Ola Mundo, %d\n", ano);
}


void olaMundo3(char nome[], int ano){
    printf("Ola Mundo, %s, em %d\n", nome, ano);
}


int soma(int v1, int v2){
    int res = v1 + v2;
    return res;
}


int main(void) {

    olaMundo();
    printf("----\n");
    olaMundo();
    printf("----\n");
    olaMundo();
    printf("----\n");
    printf("----\n");

    int ano1 = 2007;
    olaMundo2(ano1); //  olaMundo2(ano1);
    olaMundo2(2009);
    olaMundo2(2012);
    olaMundo2(2024);

    printf("----\n");
    printf("----\n");

    char nome[10] = "Gonçalo";
    olaMundo3(nome, 2004);
    olaMundo3("Rita", 2012);


    printf("----\n");
    printf("----\n");

    int val1 = 10;
    int num2 = 30;

    int res = soma(val1, num2);

    printf("res = %d\n", res);
    printf("res = %d\n", soma(val1, num2));


    return 0;
}
