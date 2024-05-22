
#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    //comentario em uma linha
    printf("msg a mostrar\n");
    
    
    /*
     
     comentario
     em
     varias
     linhas
     
     */
    
    printf("linha 1\nlnha 2\n");
    
    
    int idade = 10; // cria uma var inteira
    
    int idade2;
    
    idade2 = 14;
    
    float altura = 1.78;
    
    char letra = 't';
    
    
    
    printf("a idade é %d\n", idade);
    printf("altura: %f\n", altura);
    printf("altura: %.2f\n", altura); //num decimal com 2 casas deciamis (.2f), se fosse .4f teria 4 casas decimais
    
    printf("letra: %c\n", letra);
    
    printf("O carlos tem %d anos e mede %.2fm\n", idade, altura);
    printf("O carlos mede %.2fm e tem %d anos\n", altura, idade);
    
    printf("\n");
    
    
    
    return 0;
}
