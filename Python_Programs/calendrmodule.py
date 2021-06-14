from calendar import *
from datetime import date
"""c=calendar(2021)
print(c)

c=month(2021,2)
print(c)

c=leapdays(2018,2021)
print(c)

c=monthrange(2021,2)
print(c)

c=weekday(2021,2,5)
print(c)"""

#Q.Enter your birth date and find the age of person using calender and datetime module..

y = int(input("Enter Year : "))
m = int(input("Enter Month : "))
d = int(input("Enter Date : "))

dob =date(y,m,d) 
print("Your birth date is :", dob)

today =date.today()
print("Current date & year is :", today)

age = (today- dob).days/365 #days is remove the days ex- 9980 days so it convert into only digit 9980.
print("Your age is :",age)

