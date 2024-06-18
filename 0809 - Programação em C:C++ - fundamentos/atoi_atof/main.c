#include <stdio.h>

int main(void) {
    char num[5] = "3122";
    char num2[5] = "12.39";

    //atoi  char[] -> int

    int numI = atoi(num);

    printf("num int = %i\n", numI);

    float numF = atof(num2);

    printf("num float = %.2f", numF);


    //atof char[] -> float


    return 0;
}
