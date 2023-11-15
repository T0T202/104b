#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c, r1, r2;
    printf("Please enter the coefficients of quadratic formula: ");
    scanf("%lf%lf%lf", &a, &b, &c);
    r1 = (-b-sqrt(b*b - 4*a*c))/2*a;
    r2 = (-b+sqrt(b*b - 4*a*c))/2*a;
    printf("%.2lf\t%.2lf", r1, r2);
    return 0;
}