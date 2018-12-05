'''
Digits
Given two integers, n and m, how many digits have nm?

Examples:

2 and 10 - 210 = 1024 - 4 digits

3 and 9 - 39 = 19683 - 5 digits

Input
The input is composed of several test cases. The first line has an integer C, representing the number of test cases.
The following C lines contain two integers N and M (1 <= N, M <= 100).

Output
For each input test case of your program, you must print an integer containing the number of digits of the
result of the calculated power in the respective test case.
'''

C = int(input())

for x in range(C):
  a = input().split(" ")
  n = int(a[0])
  m = int(a[1])

  aux = n**m
  count = 0

  while aux > 0:
    aux = aux // 10
    count = count + 1
  print(count)