#include <stdio.h>

int main(void) {

    // while
    printf("------while-----");
    int num = 12;

    while (num > 0){
        printf("num: %d\n", num);

        if (num == 50){
            printf("O while vai terminar mais cedo");
            break;
        }

        num -= 1;
    }
    printf("fim do loop\n\n");

    // do while

    printf("------do - while-----\n\n");


    int num2 = 12;

    do{
        printf("num: %d\n", num2);

        if (num2 == 50){
            printf("O while vai terminar mais cedo");
            break;
        }

        num2 -= 1;

    } while (num2 > 888);

    // for
    printf("------ for ----\n");

    int i = 5;
    for (int i = 0; i < 10; i++ ){

        printf("%d\n", i);

    }
    printf("Pos for\n");
    printf("%d\n", i);

    
    return 0;
}
