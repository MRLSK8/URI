/*
Read an integer N. Print all numbers between 1 and 10000, which divided by N will give the rest = 2.

Input
The input is an integer N (N < 10000)

Output
Print all numbers between 1 and 10000, which divided by n will give the rest = 2, one per line.
*/

#include <stdio.h>

int main(void) {
  int n;
  long int i;

  scanf("%d", &n);

  for(i = 1; i < 10000; i++){
    if(i % n == 2){
      printf("%ld\n", i);
    }
  }

  return 0;
}