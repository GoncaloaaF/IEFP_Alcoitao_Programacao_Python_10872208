#include <stdio.h>

/*
 *
 *   1 2 3 4
 *
 */

/*
 *
 *   1   2   3   4
 *   5   6   7   8
 *   9  10  11  12
 */


#define linhas 5
#define col 5

int main(void) {
    int num[linhas][col] = {
            {1,2,3,4,5},
            {6,7,8,9,10},
            {11,12,13,14,15}
    };


    printf("%i\n", num[1][2]);
    printf("%i\n", num[0][3]);

    printf("-----\n");
    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < col; j++){
            printf("%i\t", num[i][j]);
        }
        printf("\n");

    }

    return 0;
}
