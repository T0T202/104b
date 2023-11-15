#include <stdio.h>
#include <math.h>

int main() {
    float n, sum;
    sum = 0;
    printf("Please enter a number: ");
    scanf("%f", &n);
    for(int i = 0; i<=n; i++) {
        sum = sum + i;
    }
    printf("sum: %12.0f", sum);
    return 0;
}