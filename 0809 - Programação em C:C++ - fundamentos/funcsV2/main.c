#include <stdio.h>

// declarar funcs
int soma(int val1, int val2);
int func2();


// main (ponto de entrada do programa)
int main(void) {

    int sum = soma(1,2);
    printf("sum = %d\n", sum);

    return 0;
}


// Funções
int func2(){
    printf("func 2\n");
}


int soma(int val1, int val2){
    func2();
    int aux =  val1 + val2;
    return  aux;
}