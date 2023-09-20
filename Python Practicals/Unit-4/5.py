# 5. Write a program to import datetime module and format the date as required. Also use the same module to calculate the difference between your birthday and today in days.

import datetime
year = int(input("Enter your birth year : "))
month = int(input("Enter your birth month : "))
day = int(input("Enter your birth date : "))
birthday = datetime.datetime.now()
Difference = now - birthday
print("Difference is ", Difference.days, "days")