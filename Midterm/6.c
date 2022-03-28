#include <stdio.h>

int main(void){
    float A[100];
    int i;
    for (i = 0; i <= 100; i=i+1){
        A[i]= i*i*i;
    }
    printf("%f", A);
    return 0;
}