#include<stdio.h>
#include<math.h>
int main(void)
{
   double a,b,c,x1,x2;
   printf("Enter a,b,c: ",a,b,c);
   scanf("%lf %lf %lf",&a,&b,&c);
   
   x1 = (-b+sqrt(pow(b,2)-4*a*c))/2*a;
   x2 = (-b-sqrt(pow(b,2)-4*a*c))/2*a;
   printf("first root %lf",x1);
   printf("\nsecond root %lf",x2);
return 0;
}