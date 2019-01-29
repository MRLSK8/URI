'''
Peter is organizing an event in his University. The event will be
in April month, beginning and finishing within April month.
The problem is: Peter wants to calculate
the event duration in seconds, knowing obviously the begin
and the end time of the event.

You know that the event can take from few seconds to some days,
so, you must help Peter to compute the total time corresponding to duration of the event.

Input
The first line of the input contains information about the beginning
day of the event in the format: “Dia xx”. The next line contains the
start time of the event in the format presented in the sample input.
Follow 2 input lines with same format, corresponding to the end of the event.

Output
Your program must print the following output, one information by line,
considering that if any information is null for example, the number 0
must be printed in place of W, X, Y or Z:

W dia(s)
X hora(s)
Y minuto(s)
Z segundo(s)

Obs: Consider that the event of the test case have the minimum duration
of one minute. “dia” means day, “hora” means hour, “minuto” means minute
and “Segundo” means second in Portuguese.

'''
beginDay = input().split(' ')
beginDay = int(beginDay[1])

beginTime = input().split(' ')
beginHour = int(beginTime[0])
beginMinutes = int(beginTime[2])
beginSeconds = int(beginTime[4])

endDay = input().split(' ')
endDay = int(endDay[1])

endTime = input().split(' ')
endHour = int(endTime[0])
endMinutes = int(endTime[2])
endSeconds = int(endTime[4])

day = hour = minutes = seconds = 0

day = (endDay - beginDay) - 1

if beginSeconds > endSeconds:
    seconds = (60 - beginSeconds) + endSeconds
else:
    seconds = endSeconds - beginSeconds 
    minutes += 1

if beginMinutes >= endMinutes:
    minutes += ((60 - beginMinutes) + endMinutes) - 1
else:
    minutes += (endMinutes - beginMinutes) - 1
    hour += 1

if beginHour >= endHour:
    hour += ((24 - beginHour) + endHour) - 1
else:
    hour += (endHour - beginHour) - 1
    day += 1

if minutes == 60:
    minutes = 0
    hour += 1
if hour == 24:
    hour = 0
    day += 1
    
print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(day, hour, minutes, seconds))




