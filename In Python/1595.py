'''
You are walking in your city and you noticed that there are moments that you walk faster or slower, 
it depends on the inclination of the street.

The course made by you has S meters. We can divide the course in parts of 1 meter, 
and in the i-th part you walk with velocity Vi meters/second. With that information 
and some basic Physics you can calculate the time you need to reach the end.
Now you want to run! But you don't want to get tired, that is why you will run in at 
most C of the S parts of the course. When you run, your speed has an addition of R meters/second! 
Assume that your acceleration is instantaneous. Chossing the best running strategy, 
compute the minimum amount of time you need to reach at the end of the course.

Input
On the first line you have an integer T (T = 100) indicating the number of test cases.

On the first line of each case we have the integers S (1 ≤ S ≤ 100* or 1 ≤ S ≤ 105**), 
C (0 ≤ C ≤ N​) and R (0 ≤ R≤ 100). On the following line, S integers will follow separated 
by spaces indicating the speed in each part of the course. In all test cases, 1 ≤ Vi ≤ 100. 
We know that this speed is huge, but imagine you are a cousin of The Flash.

*for around 90% of the cases;
**for the other test cases.

Output
Print, for each test case, the minimum amount of time necessary to reach the end, in seconds, rounded to two decimal places.
'''
T = int(input())

for i in range(T):
    Options = list(map(int, input().split()))
    S, C, R = Options[0], Options[1], Options[2]

    speeds = list(map(int, list(input().split())))
    speeds.sort()

    time, x = 0, 1

    for a in range(S):
        if(x <= C):
            time += 1/(int(speeds[a]) + R)
        else:
            time += 1/int(speeds[a])
        x += 1
    print('{:.2f}'.format(time))

    