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
    int n; //Number of tosses
    int heads = 0; //initial heads =  0
    int tails = 0; //initial tails = 0
    srand(time(NULL));

    for(n = 1; n <= 1000; n++){
        printf("%d\n", flip());

        if(flip()==0){
            heads++; //If flip = 0, add 1 to heads
        }
        else{
            tails++; //If flip = 1, add 1 to tails
        }
    }
    
    printf("Heads: %d\n", heads);
    printf("Tails: %d", tails);
}

