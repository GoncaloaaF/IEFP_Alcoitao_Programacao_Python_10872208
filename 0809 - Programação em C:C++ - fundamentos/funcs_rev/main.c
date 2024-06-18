#include <stdio.h>

void saudacao();
int soma(int val1, int val2);



int main(void) {

    saudacao();
    saudacao();
    saudacao();

    int soma_res = soma(10, 20);

    printf("soma = %i\n", soma_res);
    printf("soma = %d\n", soma_res);

    return 0;
}


void saudacao(){
    char nome[10];
    int ano;

    printf("nome: ");
    scanf("%s", nome);

    printf("ano: ");
    scanf("%d", &ano);

    printf("Hello, World!, %s\n", nome);
}



int soma(int val1, int val2){
    int res = val1 + val2;

    return res;
}
