#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//Declare original function
double func(double x){
    return x*exp(x) - 8;
}
//Derivative function
double derivFunc(double x){
    return exp(x) + exp(x)*x;
}
//Implement Newton's method
void newtonMethod(double x){
    double h = func(x) / derivFunc(x);
    while (fabs(h) >= 0.001)
    {
        h = func(x)/derivFunc(x);
        x = x-h;
    }
    printf("The solution is: %f", x);
}

int main(){
    //Initial guess
    double x0 = 5;
    newtonMethod(x0);
    return 0;
}