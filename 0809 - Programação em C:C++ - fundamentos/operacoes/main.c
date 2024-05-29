
#include <stdio.h>

int main(int argc, const char * argv[]) {
   
    
    int n1 = 10, n2 = 13,  n3 = 10;
    float n4 = 3;
    int n7, n5, n6;
    
    
    
    int soma = n1 + n2;
    printf("%d+%d=%d\n", n1, n2, soma );
    
    
    float div = n3 / n4;
    printf("%d / %.0f = %f\n", n3, n4, div );
    
    
    
    
    int i;
    int idade;
    int idadeUserA;
    
    
 
    int nomeVar;
    int n1o1meV1ar1;
    
    int _n1o1meV1ar1;
    int _nomeVar;
    
    // int 12teste;
    int nome$;
    
    
    int myIdade;
    int nome = 10;
    char letraFavorita;
        
    printf("qual a sua idade: ");
    scanf("%d", &myIdade);
    
    printf("idade: %d", myIdade);
    
    float altura;
    printf("qual a sua Altura: ");
    scanf("%f", &altura);
    
    
    printf("Altura: %.2f\n\n", altura);
    
    
    
    /*
     
     pedir  temperatura em graus Fahrenheit -> scanf
     Converter em Celsius - > C = 5 * ((F-32) / 9). - > conta
     mostre a temperatura em graus Celsius -> printf
     
     */
    float temperaturaFahrenheit;
    float temperaturaCelsius;
    
    printf("temperatura em graus Fahrenheit: ");
    scanf("%f", &temperaturaFahrenheit);
    
    temperaturaCelsius = 5 * ( (temperaturaFahrenheit - 32) / 9);
    
    printf("%.0fºF  são %.2fºC", temperaturaFahrenheit, temperaturaCelsius);
    
    
    
    
    
    
    
    /*
     
  
     Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
     
     
     pedir Altura da pessoa
     calcular peso ideal -> (72.7*altura) - 58
     mostrar Resultado
     
     
     */
    
    printf("\n");
    return 0;
}
