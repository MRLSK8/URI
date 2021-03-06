/*
Flecha no Coelho

Olivera Queen is a very skilled archer. She can hit any target at long distances without much difficulty. 
This time, she wants to train with her two hunting buddies in a somewhat unusual way: the target will be 
a stuffed rabbit. The archer will choose his own posture and his distance to the tree where the rabbit will 
be positioned, and from this information, the rabbit must be positioned in a way so that the archer can straightly hit it, 
without making any further movement. 

The distance between the archer and the tree is represented by D, the height of the archer's shoulders to his 
feet is represented by A and the height at which the stuffed rabbit must be positioned so that the archer can 
hit its head is H. The angle of the tree and the angle of the archer with respect to the ground are always 90º, 
and the angle of the archer's arm with respect to his own body will be chosen by himself.

So, help Olivera Queen and her two promising hunting buddies train the way they planned: write a program that 
returns the appropriate value H so the stuffed rabbit can be hit in the head, according to the given information. 
Consider the arrow always goes straightly, regardless of its distance to the target.

Input
The input contains several test cases. Each line constains a real number A (1 ≤ A ≤ 2) indicating the height of the archer, 
a real number D (5 ≤ D ≤ 40) indicating the distance between the archer and the tree and a real number R (50 ≤ R ≤ 150) 
indicating the angle, in degrees, between the archer's arm and his body. It's guaranteed that the input is always valid and 
doesn't generate unexpected outputs. Read input until EOF.

Output
For each test case, print the value of H with accuracy of 4 decimal places.
*/
#include <stdio.h>
#include <math.h>
int main(void){
    float altura, distancia, angulo;

    while(scanf("%f %f %f", &altura, &distancia, &angulo) !=  EOF){
        if(angulo == 90){
            printf("%.4f\n", altura);
        }else if(angulo > 90){
            printf("%.4f\n", altura + (tan((angulo - 90) * 3.141592/180) * distancia));
        }else{
            printf("%.4f\n", altura - (tan((90 - angulo) * 3.141592/180) * distancia));
        }
    }

    return 0;
}