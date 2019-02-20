/*
Fast Fibonacci

Binet's formula is a way to calculate Fibonacci numbers.
    Fibonacci(n) = ( pow( ( (1 + sqrt(5)) / 2 ), n) ) - ( pow( ( (1 - sqrt(5)) / 2), n) ) ) / sqrt(5);
Your task is, given a natural number n, to compute the value of Fibonacci(n) using the formula above.

Input
The input is a natural number n (0 < n ≤ 50).

Output
The output is the value of Fibonacci(n) with 1 decimal place using the given Binet's formula.
*/
#include <stdio.h>
#include <math.h>

double fib(int n);

int main (void){
    int number;

    scanf("%d", &number);

    printf("%.1f\n", fib(number));

    return 0;
}
double fib(int n){
    return ( ( ( pow( ( (1 + sqrt(5)) / 2 ), n) ) - ( pow( ( (1 - sqrt(5)) / 2), n) ) ) / sqrt(5) );
}