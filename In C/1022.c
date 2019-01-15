
/*
TDA Rational

You were invited to do a little job for your Mathematic teacher. The job is to read a Mathematic 
expression in format of two rational numbers (numerator / denominator) 
and present the result of the operation. Each operand or operator is separated by a blank space. 
The input sequence (each line) must respect the following format: number, (‘/’ char), number,
operation char (‘/’, ‘*’, ‘+’, ‘-‘), number, (‘/’ char), number. The answer must be presented followed by ‘=’ 
operator and the simplified answer. If the answer can’t be simplified, it must be repeated after a ‘=’ operator.

Considering N1 and D1 as numerator and denominator of the first fraction, follow the orientation about how to do each one of these 4 operations:

Sum: (N1*D2 + N2*D1) / (D1*D2)
Subtraction: (N1*D2 - N2*D1) / (D1*D2)
Multiplication: (N1*N2) / (D1*D2)
Division: (N1/D1) / (N2/D2), that means (N1*D2)/(N2*D1)

Input
The input contains several cases of test. The first value is an integer N (1 ≤ N ≤ 1*104), indicating the amount of cases 
of test that must be read. Each case of test contains a rational value X (1 ≤ X ≤ 1000), an operation (-, +, * or /) 
and another rational value Y (1 ≤ Y ≤ 1000).
Output
The output must be a rational number, followed by a “=“ sign and another rational number, that is the simplification 
of the first value. In case of the first value can’t be simplified, the same value must be repeated after the ‘=’ sign.

examples:

4
1 / 2 + 3 / 4
10/8 = 5/4

1 / 2 - 3 / 4
-2/8 = -1/4

2 / 3 * 6 / 6
12/18 = 2/3

1 / 2 / 3 / 4
4/6 = 2/3

*/
#include <stdio.h>

int main(void){
	int numerator, denominator, times, i;
	int N1,N2, D1, D2, v;
	char operation;

	scanf("%d", &times);

	for(i = 0; i < times; i++){
		scanf("%d / %d %c %d / %d", &N1, &D1, &operation, &N2, &D2);
		switch(operation){
			case '+':
				numerator = (N1 * D2 + N2 * D1);
			  denominator = (D1 *  D2);
			break;
			case '-':
				numerator = (N1 * D2 - N2 * D1);
			  denominator = (D1 * D2);
			break;
			case '*':
				numerator = (N1 * N2);
			  denominator = (D1 * D2);
			break;
			case '/':
			  numerator = (N1 * D2);
			  denominator = (N2 * D1);
			break;
		}
		printf("%d/%d = ", numerator, denominator);

		numerator > denominator ? (v = numerator) : (v = denominator);
		for(; v >= 2; v--){
			if(numerator == denominator){
				numerator = 1;
				denominator = 1;
				break;
			}
			if(numerator % v == 0 && denominator % v == 0){
				numerator /= v;
				denominator /= v;
			}
		}

		printf("%d/%d\n", numerator, denominator);
	}
	
  return 0;
}