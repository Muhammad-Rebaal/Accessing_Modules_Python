import sys
location = sys.path
print(location)
for i in location:
    print(i)
    
print("")


import calendar
print("Fridays in a Calendar:",calendar.FRIDAY)
print("The number of Leap Days between two Years:",calendar.leapdays(2022, 2050))
print("Is 2023 this Year a leap Year:",calendar.isleap(2023))