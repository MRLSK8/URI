/*
Functions

In the last math class, Rafael, Beto and Carlos learned some new math functions. Each one of them liked one particular function,
and they decided to compete to see which function had the higher outcome.

The function that Rafael chose is r(x, y) = (3x)² + y².

Beto chose the function b(x, y) = 2(x²) + (5y)².

Carlos, however, chose the function c(x, y) = -100x + y³.

Given the values of x and y, say who chose the function with higher outcome.

Input
The first line of input contains an integer N that determines the number of test cases. Each test case consists of two 
integers x and y (1 ≤ x, y ≤ 100), indicating the variables to input in the function.

Output
For each test case print one line, containing one sentence, indicating who won the contest. For example, if Rafael wins the contest, 
print “Rafael ganhou”. Assume that there will be no ties.
*/

#include <stdio.h>
int main(void){
    int times, x, y, result1, result2, result3;

    scanf("%d", &times);

    while(times > 0){
        scanf("%d %d", &x, &y);
        result1 =  ((3*x)  * (3*x)) + (y*y);        // (3x)² + y².
        result2 =  (2 * (x*x)) + ((5*y) * (5*y));   //2(x²) + (5y)²
        result3 =  (-100 * x) + (y*y*y);            //-100x + y³.

        printf(result1 > result2 ? (result1 > result3 ? "Rafael ganhou\n" : "Carlos ganhou\n") : (result2 > result3 ? "Beto ganhou\n" : "Carlos ganhou\n"));
        
        times--;
    }

    return 0;
}