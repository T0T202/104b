#include <stdio.h>
#include <math.h>
int main(){
    float num;
    printf("Please enter a number: ");
    scanf("%f", &num);
    do{
        num = sqrt(num); 
        printf("%.6f\n", num);
    } while(num > 1.2);

    return 0;
}