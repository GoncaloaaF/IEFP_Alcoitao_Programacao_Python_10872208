#include <stdio.h>
#include <math.h>


int main(void) {
    printf("Hello, World!\n");

    double res = sqrt(16);
    printf("%.2f\n", res);

    int f = floor(10.99);
    printf("%d\n", f);

    int f2 = ceil(10.01);
    printf("%d\n", f2);

    double f3 = pow(2, 10);
    printf("%d\n", f2);


    int f4 = round(10.4);
    printf("%d\n", f4);

    int f5 = round(10.5);
    printf("%d\n", f5);


    float f6 = round(10.56);
    printf("%.2f\n", f6);



    return 0;
}
