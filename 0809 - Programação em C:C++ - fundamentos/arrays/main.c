#include <stdio.h>

int main(void) {
    int idade = 10;

    int idades[] = {15, 30, 12, 23, 60};

   printf("%d\n", idades[0]);
    printf("%d\n", idades[1]);


    idades[0] = 1231;
    printf("%d\n", idades[0]);

    printf("----- array for  ---------\n");
    for (int i = 0; i < 5; i++) {

        printf("%d\n", idades[i]);
    };
    printf("------ sizeof -------\n");

    int nElm = sizeof(idades)/ sizeof(idades[0]);

    printf("%d\n", nElm);

    printf("------ end sizeof -------\n");

    printf("-----------------\n");
    printf("%d\n",  idades[5]);
    idades[5] = 121;
    printf("%d\n",  idades[5]);

    printf("------ sizeof2 -------\n");

    int nElm2 = sizeof(idades)/ sizeof(idades[0]);

    printf("%d\n", nElm2);

    printf("------ end sizeof2 -------\n");



    printf("----------------------------\n");

    int num[10]; //   int num[10]; <- o array tem 10 elementos 

    //num[20] = 10; // index may have a value of '20' which is out of bounds

    printf("------ sizeof3 -------\n");

    int nElm3 = sizeof(num) / sizeof(num[0]);

    printf("%d\n", nElm3);

    printf("------ end sizeof3 -------\n");


    return 0;
}
