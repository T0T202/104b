#include <stdio.h>
int main()
{   
    //Declare all the variables
    float a,b,c,d,e,f,x,y;

    //Input a, b, c, d, e, f
    printf("Enter the coefficients for the first line: " );
    scanf("%f %f %f", &a, &b, &c);
    printf("Enter the coefficients for the second line: ");
    scanf("%f %f %f", &d, &e, &f);

    //Find x and y
    x = (b*f - e*c)/(b*d - a*e);
    y = (d*c - a*f)/(b*d - a*e);

    // 3 cases, overlap, parallel and intersect
    if((a/b) == (d/e)){
        if((a == d) && (b == e) && (c == f)){
            printf("The two lines overlap. Infinite solutions");
        }
        else{
            printf("The two lines are parallel. No solution");
         }
    }
    else{
        printf("The two lines intersect. Unique solution\n");
        printf("The point of intersect: %f, %f", x, y);
    }
    return 0;
}