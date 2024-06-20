#include<stdio.h>
#include<stdlib.h>
void waitAndClear();
void showMenu();
void ex1();
void ex2();
void ex3();
char myGetchar();

int main(){




    while (1) {
        showMenu();

        char opt = myGetchar();

        switch (opt) {
            case 'A':
            case 'a':

                ex1();

                waitAndClear();
                break;
            case 'B':
            case 'b':

                ex2();


                waitAndClear();
                break;
            case 'C':
            case 'c':
                ex3();

                waitAndClear();
                break;
            case 'q':
            case 'Q':
                printf("vai terminar o programa");
                waitAndClear();
                break;
            default:
                printf("seleção invalida\n");

                waitAndClear();
                break;
        }

        if(opt == 'q' || opt == 'Q'){

            break;
        }
    }

    printf("Final do porgrama");

    return 0;
}


void showMenu(){
    printf("--------Menu---------\n");
    printf("opt 1-------------- a\n");
    printf("opt 2-------------- b\n");
    printf("opt 3-------------- c\n");
    printf("sair--------------- q\n");
    printf("---------------------\n");
    printf("opt: ");
}



void showMenu2(){
    printf("--------Menu 2---------\n");
    printf("opt 1-------------- a\n");
    printf("opt 2-------------- b\n");
    printf("opt 3-------------- c\n");
    printf("sair--------------- q\n");
    printf("---------------------\n");
    printf("opt: ");
}


void waitAndClear(){
    printf("enter para continuar");
    getchar();
    system("clear");
}


void ex1(){
    showMenu2();
    char opt = myGetchar();
    printf("a opção secl foi %c\n", opt);

    printf("Ex 1\n");
}

void ex2(){
    printf("Ex 2\n");
}

void ex3(){
    printf("Ex 3\n");
}

char myGetchar(){
    char opt = getchar();
    fflush(stdin);
    system("clear");
    return opt;
}