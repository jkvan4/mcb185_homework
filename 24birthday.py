#list out of calendar, index
import random
import sys

cal = int(sys.argv[1]) # number of days
num = int(sys.argv[2])  # number of ppl

#make empty calendar
calendar = [0] * cal

#fill calendar w dates
for _ in range(num):
    date = random.randint(0, cal-1)
    calendar[date] += 1
print(calendar)

#check calendar for shared bdays
shared = False
for date in range(cal):
    if calendar[date] >= 2:
        shared = True
        break

if shared: print('birthday twins!')
else: print('no shared bdays')