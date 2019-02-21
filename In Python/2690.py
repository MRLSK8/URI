'''
New Password RA

A new set of authentication will be implemented at the Federal
Institute of South of Minas, Muzambinho campus, so users will
not have much difficulty, plus you ... Well, the new authentication
service is safe, without bugs and headaches even though we are at
the end of the semester. It will allow your password to have spaces,
but not numbers or special characters. The update always occurs during
the vacation period, so tpdps adjustments are made and in the end please
all users. As a trainee at the school's support center, your duty is
to implement the new authentication.
For now the new standard for user names is being studied.

"GQ": 0,  "IS": 1,  "EOY": 2, "FPZ": 3, "JT": 4,
"DNX": 5, "AKU": 6, "CMW": 7, "BLV": 8, "HR": 9

"aku": 0, "blv": 1,  "cmw": 2, "dnx": 3, "eoy": 4,
"fpz": 5, "gq": 6, "hr": 7, "is": 8, "jt": 9

As we can see for each set of letters we will have a specific number.
Make a bad program to do this conversion of the letters to the numbers,
and since you will not access the passwords of the students, make an
algorithm so that the same one does the process alone using its own test cases.

Note: Your test cases can not exceed 20 character and the output, 12 digits.

Input
You will have N indicating the number of passwords that will be exchanged,
then N test cases.

Output
The output will be a list with the new, encrypted numbers of the passwords
that were typed.

'''
def main():
    n = int(input())
    
    while n > 0:
        sentence = input().split(" ")
        
        lista = []
        count = 1
        
        for x in range(len(sentence)):
            if count > 12:
                break
            for i in range(0, len(sentence[x])):
                if count > 12:
                    break
                else:
                    count += 1
                    
                if str(sentence[x][i]).isupper():
                    lista.append(upperLetter(str(sentence[x][i])))
                else:
                    lista.append(lowerLetter(str(sentence[x][i])))
                    
        lista = map(str, lista)                  
        print(''.join(lista))
                                 
        n = n - 1

def upperLetter(letter):
    dictionary = {"GQ": 0,  "IS": 1,  "EOY": 2, "FPZ": 3, "JT": 4,
                  "DNX": 5, "AKU": 6, "CMW": 7, "BLV": 8, "HR": 9}

    for keys in dictionary.keys():
            if letter in keys:
                return dictionary[keys]
                          
def lowerLetter(letter):
    dictionary = {"aku": 0, "blv": 1,  "cmw": 2, "dnx": 3, "eoy": 4,
                  "fpz": 5, "gq": 6, "hr": 7, "is": 8, "jt": 9}

    for keys in dictionary.keys():
            if letter in keys:
                return dictionary[keys]
    
main()



