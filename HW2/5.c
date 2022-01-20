#include <stdlib.h>
#include <stdio.h>
#include <time.h>


//Declare a function of coinflip
int flip(){
    //Generate random number, and find the remainder of it
    //If the number is odd, remainder = 1, which is tail
    //If the number is even, remainder = 0, which is head

    int i = rand() % 2; 

    if (i == 0)
        return 0;
    else
        return 1;
}

//Main function to run code
int main(void){
    int m; //number of experiments
    int n; //number of tosses
    int heads = 0; //initial heads =  0
    srand(time(NULL));
    
    for(m = 0; m < 1000; m++){
        for(n = 0; n < 100; n++){
            if(flip()==0){
                heads++; //If flip = 0, add 1 to heads
            }
        }

        if((heads > 0)){
            printf("%i, ", heads);
        }

        heads = 0; //Assign heads = 0, and run the experiment from the beginning again
    }
    
    return 0;
}

