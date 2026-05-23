#calendar module

'''import calendar
year=2025
month=5
print(calendar.month(year,month))'''



'''import calendar
year=2026
print(calendar.calendar(year))'''



#task
'''import calendar
n=int(input())
m=int(input())
print(calendar.month(n,m))'''


#present time and day

'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''


#epoch time
'''import time
a=time.time()
print(a)

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")'''


#task
import random
import time
for i in range(10):
    a=random.randint(100,500)

    print(a)
    time.sleep(2)


