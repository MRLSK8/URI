'''
Close the Doors!

Madam Beauvoir has a mansion where she hosts her descendants
(grandchildren and great-grandchildren) during their vacations.
Her mansion has exactly N rooms (each room is numbered from 1 to N),
and she has exactly N descendants (each descendant is also numbered from 1 to N).

Like all children, Mme. Beauvoir's descendants are really prankish.
It's always the same mess: Every day, they wake up early in the morning
before her, and meet in the garden. Then, each descendant, one at a time,
enters the mansion and switch the state of the door of the rooms whose
number is a multiple of his own number. To switch the state of a door
means to close an open door or to open a closed door. So, for example,
the descendant 15 will switch the state of the door of the rooms 15, 30, 45,
and so on.

Initially, all doors are closed (all descendants close the doors before
going to the garden). Also, each descendant enters exactly one time in
the mansion (due to the mess, however, we don't know in which order).
Which doors will be open once all descendants have entered the mansion?

Input
The input consists of several test cases. Each test case is described by
a line containing the integer N (0 ≤ N ≤ 25000000), the number of rooms
and descendants. The last test case is followed by a line containing a single 0.

Output
For each test case, print the numbers of the rooms whose door will be
open, in increasing order. Print a single space between consecutive numbers.
'''

while True:
    n = int(input())
    if n == 0:
        break

    x = 1
    y = 0
    while y + x <= n:
        y += x
        if y+x+2 > n:
            print(y)
        else:
            print(y, end=' ')
        x += 2
        

'''
 PS: This code has "Time limit Exceeded"
 ---------------------------------------
def dictTrueOrFalse(new_dict, n):
    
    for j in range(2, n+1):
        if new_dict[j] == True:
            new_dict[j] = False
        else:
            new_dict[j] = True
            
        x = 2
        while j * x <= n:
            if new_dict[j*x] == True:
                new_dict[j*x] = False
            else:
                new_dict[j*x] = True
            x += 1
         
    return new_dict

while True:
  new_dict = dict()
  n = int(input())
  
  if not n:
      break

  list_ = list(x for x in range(1, n + 1))
  new_dict = new_dict.fromkeys(list_, True)

  new_dict = dictTrueOrFalse(new_dict, n)
  
  x = 1
  for item in new_dict.values():
      if item == True:
          print(x, end=' ')
      x += 1
  print()
'''
