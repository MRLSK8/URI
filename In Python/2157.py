'''
Mirror Sequence

Print numbers in sequence is a relatively simple task. 
But, and when it is a sequence mirror? This is a sequence 
having a number of start and an end number and all numbers 
therebetween, including these, are arranged in an increasing 
sequence without spaces, and then this sequence is designed 
in inverted form, as a reflection in the mirror. For example, 
if the sequence is 7 to 12, the result would 789101112211101987

Write a program that, given two integers, print their mirror sequence.

Input
The input has an integer value C indicating the number of test cases. 
Then each case has two integer values ​​E and B ( 1 ≤ B ≤ E ≤ 12221 ), 
indicating the start and end of the sequence.

Output
For each test case, print the respective mirror sequence.
'''
x = int(input())

while x != 0:
    numbers = input().split(" ")
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    string = ''
    
    for i in range(num1, num2+1, 1):
        string += str(i)
    print('{}{}'.format(string, string[::-1]))
    x -= 1