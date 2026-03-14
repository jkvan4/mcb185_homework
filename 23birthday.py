# list out of birthdays/people
import random
import sys
cal = int(sys.argv[1]) # days in year
num = int(sys.argv[2]) # number of people

shared = False
birthdays = list()
for _ in range(num):
    date = random.randint(0, cal-1)
    birthdays.append(date)
for i in range(num):
    for j in range(i+1, num):
            if birthdays[i] == birthdays[j]:
                shared = True
if shared: print('birthday twins!')
else: print('no shared bdays')