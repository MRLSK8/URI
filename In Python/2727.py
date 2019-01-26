'''
Secret Code

Joana likes to play pretending to be a secret agent with her friends Bruna, Jaqueline and Laura.
Joana and Bruna have created asecret code to communicate without their enemies discovering their
plans. The secret code works as follows:

The letter 'a' is represented by a single dot '.'
The letter 'b' is represented by two dots '..'
The letter 'c' is represented by three dots '...'
The other letters follow the previous logic, however each set of points is separated by a space
and always with a set of more points, as in the example below:
. → a
.. → b

... → c

. . → d

.. .. → e
... ... → f

. . . → g
.. .. .. → h
... ... ... → i

Your goal is to create a program that decipher the secret messages and help Jaqueline and Laura
find out what Joana and Bruna are planning.

Input
The input contains several test cases. The first line of each test should contain an integer (N ≤ 50),
which represents the number of letters to be deciphered and the next N lines contain the code for each letter.

Output
A string represented by the letter of the alphabet corresponding to the input code. Each string must
be separated from the other by a new line.

'''
listCode = [".","..","...",". .",".. ..","... ...",". . .",".. .. ..",
         "... ... ...",". . . .",".. .. .. ..","... ... ... ...", 
         ". . . . .",".. .. .. .. ..","... ... ... ... ...",
         ". . . . . .",".. .. .. .. .. ..","... ... ... ... ... ...",
         ". . . . . . .", ".. .. .. .. .. .. ..", "... ... ... ... ... ... ...",
         ". . . . . . . .",".. .. .. .. .. .. .. ..","... ... ... ... ... ... ... ...",
         ". . . . . . . . .",".. .. .. .. .. .. .. .. .."]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
            "q","r","s","t","u","v","w","x","y","z"]
while True:
    try:
        times = int(input())
        while times != 0:
            k = input()
            index = listCode.index(k)
            print(alphabet[index])
            times -= 1
    except:
        break
