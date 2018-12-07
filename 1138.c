/*
Digits Count
Diana is going to write a list of all positive integers between A and B, inclusive, in base 10 and 
without any leading zeros. She wants to know how many times each digit is going to be used.

Input
Each test case is given in a single line that contains two integers A and B (1 ≤ A ≤ B ≤ 108).
The last test case is followed by a line containing two zeros.

Output
For each test case print a single line with 10 integers representing the number of times each digit
is used when writing all integers between A and B, inclusive, in base 10 and without leading zeros.
Write the counter for each digit in increasing order from 0 to 9.

example:
    1 9
    0 1 1 1 1 1 1 1 1 1
    12 321
    61 169 163 83 61 61 61 61 61 61
    5987 6123
    134 58 28 24 23 36 147 24 27 47
    0 0
*/
#include <stdio.h>
#include <stdlib.h>

int main(){
    long long int a , b , i, c, r;

    while(scanf("%lld %lld", &a, &b) && a!=0 && b!=0){
        int *vet = (int *)calloc(10,sizeof(int));

        for(i = a; i <= b; i++){
            c = i;

            while(1){
                r = c % 10;
                (*(vet+r))++;
                c = c / 10;
                if(c == 0)break;
            }
        }

        for(i = 0; i < 10; i++){
            printf(" %d", *(vet+i));
        }
        printf("\n");
    }
    return 0;
}



   