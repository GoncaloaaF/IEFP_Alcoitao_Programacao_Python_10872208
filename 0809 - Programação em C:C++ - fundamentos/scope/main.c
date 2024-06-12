#include <stdio.h>


// socpe



void fun();
void foo(char nome[]);

int main(void) {

    int x = 10;
    //fun();

    if (x == 10){
        printf("%d\n", x);

        int x = 14;
        printf("%d\n", x);

        if (1){
            int x = 15;

        }

        x = 331;
    }
    printf("%d\n", x);


    printf("----------------------\n");

    char teste[20] = "Gonçalo";
    printf("%s\n",teste);

    foo(teste);

    printf("%s\n",teste);
    return 0;
}


void fun(){
    int x = 10;
    printf("%d", x);
}


void foo(char nome[]){

    nome = "Outro nome";
    printf("%s\n",nome);

}