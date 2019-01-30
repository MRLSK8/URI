'''
Another Lottery

Even in times of an economic crisis, people in Byteland still like
to participate in lotteries. With a bit of luck, they might get rid
of all their sorrows and become rich.

The most popular lottery in Byteland consists of m rounds. In each round,
everyone can purchase as many tickets as he wishes, and among all tickets
sold in this round, one
ticket is chosen randomly, each one with the same probability. The owner
of that ticket wins the prize money of this round. Since people in Byteland
like powers of 2, the prize money for the winner of round i amounts to 2i
Bytelandian Dollars.

Can you determine for each participant in the lottery the probability that
he will win more money than anybody else?

Input
The input consists of several test cases. Each test case starts with a line
containing two integers n and m, the number of participants in the lottery
and the number of rounds in the lottery. You may assume that 1 ≤ n ≤ 10000
and 1 ≤ m ≤ 30.

The following n lines contain the description of the tickets bought by the
participant. The ith such line contains m non-negative integers c1, ..., cm,
where cj (1 ≤ j ≤ m) is the amount of tickets of round j bought by participant i.
The total number of tickets sold in each round is between 1 and 109.

The input ends with a line containing 2 zeros.

Output
For each test case, print n lines of output, where line i contains the
probability as a reduced fraction that participant i wins the most money.
See the sample output for details.
'''
def reducefraction(numerator, denominator):
    def gcd(numerator, denominator):
        while denominator != 0:
            aux = denominator
            denominator = numerator % denominator
            numerator = aux
        return numerator
    
    greatest = gcd(numerator, denominator)
    numerator /= greatest
    denominator /= greatest
    
    return int(numerator), int(denominator)
        
while True:
    participants, rounds = [int(x) for x in input().split()]
    if participants == 0 and rounds == 0:
        break
    
    listLastTicket = []
    
    for x in range(1, participants + 1):
        ticket = input().split()
        listLastTicket.append(ticket[rounds - 1])
        
    Sum = sum(int(i) for i in listLastTicket)
    
    for x in listLastTicket:
        numerator, denominator = reducefraction(int(x), Sum)
        print('{} / {}'.format(numerator, denominator))
    
