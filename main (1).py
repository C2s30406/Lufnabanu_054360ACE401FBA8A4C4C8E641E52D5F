#leap year.

def isLeapyear(year):
  if (year % 4==0 and year % 100 != 0)or year % 400 == 0:
     return True 
else:
     return False
  
  year =int(input("enter a year:"))

  if isLeaplear(year):
     print('{}is a leapyear.'.format(year))
  else:
     print('{} is not a leap year.'.format(year)