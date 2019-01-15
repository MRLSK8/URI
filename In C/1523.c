/*
Linear Parking Lot

After a long time saving money, Rafael finally got to buy his own car. 
Enough of catching bus, now his life is going to be easier. At least this is what he thought, 
until he heard about the parking lot near the university where he decided to park the car every day.

The parking lot has only one corridor, with enough width to fit one car, and enough depth to fit K cars, 
one behind the other. As this parking lot has just one gate, it is only possible to the cars to enter and leave by it.

When the first car enters the parking, it occupies the last position near the wall, at the bottom of the parking lot. 
All the next cars park right behind it, forming a queue. Obviously, it is not possible that one car passes 
over the other, therefore it is only possible for a car to leave the parking lot if it is the last at the queue.

Given the expected arrival and exit time of N drivers, Rafael included, tell if it is possible that they all 
can park and remove their cars at the quote parking lot.

Input
There will be several test cases. Each test case starts with two integers N and K (3 ≤ N ≤ 10⁴, 1 ≤ K ≤ 10³), 
representing the number of drivers that are going to make use of the parking lot, and the number of cars that 
the parking lot can fit, respectively.

Following there will be N lines, each one containing two integers Ci and Si (1 ≤ Ci, Si ≤ 10⁵), representing, 
repectively, the arrival and exit time of the i-th driver (1 ≤ i ≤ N). The values of Ci are given in ascending 
order, in other words, Ci < Ci+1 for each 1 ≤ i < N.

There will be no more than one driver that arrive at the same time, and no more than one driver that leave at 
the same time. It is possible that one driver can park at the same time that other driver is leaving.

The last test case is indicated when N = K = 0, which should not be processed.

Output
For each test case print one line, containing the word “Sim”, if it is possible that all the N drivers make 
use of the parking lot, or “Nao” otherwise.

*/
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct{
	long int C;
	long int S;
}T_parking;

int main(void){
	unsigned long int N, K;
	bool isPossible, changed;
	int i, count, a, b, z;

	// Input
	while(1){
		T_parking *cars = (T_parking *)calloc(1, sizeof(T_parking));
		scanf("%ld %ld", &N, &K);
		
		if(!N && !K)break; // IF (N = 0) and (K = 0) stop the program
		cars = (T_parking *)realloc(cars, N * sizeof(T_parking));

		count = 0;
		isPossible = true;
		changed = false;
		a = 0;
		b = 0;

		for(i = 0; i < N; i++){
			scanf("%ld %ld", &cars[a].C, &cars[a].S);
			if(!isPossible)continue;
			count++;  // Counts how many cars are in the parking lot

			if(count != 1){
				// If arrived time iqual or greater than the exit of the last car
				if(cars[a].C >= cars[a-1].S){
					if(count >= 3){
						for(b = (a - 1); b >= 0; b--){
							if(cars[a].C < cars[b].S){
								if(cars[a].S < cars[b].S){
									cars[b+1] = cars[a];
									a = b + 2;
									count = b + 2;
									changed = true;
									break;
								}else{
									isPossible = false;
									break;
								}
							}else if(cars[a].C == cars[b].S){
								if(cars[a].S < cars[b-1].S){
									cars[b] = cars[a];
									a = b + 1;
									count = b + 1;
									changed = true;
									break;
								}else{
									isPossible = false;
									break;
								}
							}
						}
						if(!changed){
							cars[0] = cars[a];
							a = 1;
						}
					}else{
						cars[a-1] = cars[a];
					}
					
				}else if(cars[a].S > cars[a-1].S){
					isPossible = false;
				}else{
					a++;
				}
			}else{
				a++;
			}
			// If the parking lot is filled up
			if(a > K){
				isPossible = false;
			}
		}
    
		// Output
		if(isPossible){
			printf("Sim\n");
		}else{
			printf("Nao\n");
		}
		free(cars);
	}
  return 0;
}