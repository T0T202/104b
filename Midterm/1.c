#include <stdio.h>

int main() {
    int square;
    for(int i = 1; i <= 20; i++){
        if(i % 2 == 0){
            printf("%i\t", i);
            square = i * i;
            printf("%i\n", square);
        }
    }
    return 0;
}