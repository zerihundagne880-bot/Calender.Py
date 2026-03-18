import calendar  

month = int(input("Please enter the month (1-12): "))
year = int(input("Please enter the year: "))


cal = calendar.month(year, month) 

print(cal)

