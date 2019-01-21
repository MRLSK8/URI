'''
Monetary Formatting

Often it is necessary to write monetary amounts in a standard format. 
We decided formatting quantities in the following way:

   1. The montande must begin with '$';
   2. The number must end with a decimal point and exactly two digits following;
   3. The digits to the left of the decimal point must separate in groups of three oir commas.

Your task in this problem is to create a program that, given two integer values ​​to dollars 
and cents return String formatted properly.

Input
The input consists of several test cases. Each test case consists of two integers, 
dollars (0 ≤ dollars ≤ 2 * 109) and cents (0 ≤ cents ≤ 99), respectively.

Output
For each test case print a string formatted according to the formatting rules.
'''

def DollarFormat(dollars):
    listFormated = []
    count = 1
    
    for i in range(len(dollars) - 1, -1, -1):
        if count % 4 == 0:
            listFormated.append(',')
            listFormated.append(dollars[i])
            count += 1
        else:
            listFormated.append(dollars[i])
        count += 1

    listFormated.reverse()
    return listFormated

while True:
    dollars = list(input())
    if not dollars:
        break
    try:
        cents = int(input())
    except:
        break

    print('${}.{:02d}'.format(''.join(DollarFormat(dollars)), cents))