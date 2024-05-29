#include <stdio.h>

int main(int argc, const char * argv[]) {
   
    int idade;
    int idade2;
    
    printf("idade 1: ");
    scanf("%i", &idade);
    
    printf("idade 2: ");
    scanf("%i", &idade2);
    
    
    printf("idade = %i e idade 2 = %i\n", idade, idade2);
    
    
    /*
        bool v = true;
        bool v2 = false;
     
      10 == 10 -> t
     
     
     >  <- maior
     <  <- menor
     >=  <- maior ou igual
     <= <- menor ou igual
     
     == <- igual
     
     != <- nao igual (diferente)
     
*/
    

    //if....
    
    printf("------ Separador -------\n");
    
    printf("------ if  -------\n");
    
    if (idade == idade2){
        
        printf("idade = idade2 = %i\n", idade);
        
    }
    
    
    printf("------ if/else  -------\n");
    
    if (idade == idade2){
        
        printf("idade = idade2 = %i\n", idade);
        
    }else{
        
        printf("idade sao diferentes idade2 (%i, %i)\n", idade, idade2);
    }
    
    printf("------ if/else if /else -------\n");
    
    
    
    if (idade2 > idade){
        if(idade2 == 10){
            printf("idade2 == %i", idade2);
        }
        printf("idade2 é maior\n");
    }else if (idade > idade2){
        printf("idade é maior\n");
    }else{
        printf("idade e idade2 são iguais\n");
    }
    
    
    printf("------ if/else if /else - 2 -------\n");
    
    int i = 17;
    
    if (i < 14){
        printf("criança\n");
        
    }else if (i < 18){
        printf("teen\n");
        
    }else{
        printf("Adulto\n");
    }
    
    
    printf("pos if\n");
    
    
    printf("------ var scope -------\n");
    
    
    int val = 10;
    
    printf("val = %i\n", val);
    
    if (val == 10) {
        printf("val = %i\n", val);
        
        int val = 10;
        printf("val = %i\n", val);
        val = 15;
        printf("val = %i\n", val);
        printf("code..... \n");
        printf("val = %i\n", val);
    }
    
    printf("val = %i\n", val);
    

    printf("------ switch -------\n");
    
    int s_val = 5;
    
    switch (s_val) {
        case 5:
            printf("s_val = 5\n");
            // break;
        case 10:
            printf("s_val = 10\n");
            break;
            
        case 15:
            printf("s_val = 15\n");
            break;
            
        default:
            printf("s_val = Outro valor\n");
            break;
    }
    
    
/*
    if (s_val == 5){
        
        printf("s_val = 5\n");
        
    }else if (s_val == 10){
        
        printf("s_val = 10\n");
        
    }else if (s_val == 15){
        
        printf("s_val = 15\n");
        
    }else{
        
        printf("s_val = Outro valor\n");
    }
    */
    
    

    printf("pos switch\n");
    
    
    
    return 0;
}
