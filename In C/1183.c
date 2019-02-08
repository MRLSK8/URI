/*

Above the Main Diagonal

Read an uppercase character that indicates an operation that will be performed in an array M[12][12]. Then, calculate and print the sum or 
average considering only that numbers that are above the main diagonal of the array.

Input
The first line of the input contains a single uppercase character O ('S' or 'M'), indicating the operation Sum or Average
(Média in portuguese) to be performed with the elements of the array. Follow 144 floating-point numbers of the array.

Output
Print the calculated result (sum or average), with one digit after the decimal point.Input
The first line of the input contains a single uppercase character O ('S' or 'M'), indicating the operation Sum or Average 
(Média in portuguese) to be performed with the elements of the array. Follow 144 floating-point numbers of the array.

Output
Print the calculated result (sum or average), with one digit after the decimal point.

*/
#include <stdio.h>
int main(void){
    char option;
    float M[12][12];
    int i, j;
    float sum = 0.0;
    
    scanf("%c", &option);

    for(i = 0; i < 12; i++){
        for(j = 0; j < 12; j++){
            scanf("%f", &M[i][j]);
            if(j > i){
                sum += M[i][j];
            }
        }
    }

    if(option == 'S'){
        printf("%.1f\n", sum);
    }else{
        printf("%.1f\n", sum/66);
    }

    return 0;
}