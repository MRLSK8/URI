'''
Problem with the Calculator

joãozinho have to help his father. One specific report are being pressed 
with unwished letters between the three existing numbers. You have to do 
a program to sum these three numbers, ignoring the letters existents. Each line have no spaces.

Input
The first line of input contains an integer N (N < 100000). Follow N lines with 
exacly 14 characters that must be read and the three number existing in this line 
must be extracted and summed.

Output
For each input, your program must print a integer representing the sum of the 3 
existent numbers of that line.
'''
x = int(input())

for i in range(x):
	string = input()
	lista = []
	tosum = []

	for a in range(len(string)):
		if string[a].isdigit():
			if len(lista) != 0:
				lista[0] = lista[0] + string[a]
			else:
				lista.append(string[a])
		else:
			if len(lista) != 0:
				tosum.append(lista[0])
				lista = []
		if len(lista) != 0 and a == (len(string) - 1) and lista[0].isdigit():
			tosum.append(lista[0])

	print(sum(list(map(int, tosum))))