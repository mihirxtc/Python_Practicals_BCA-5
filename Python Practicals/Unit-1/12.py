# 12. Write a python program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result. (2.54 = 1 Inch).

cm = int(input("Enter length in cm : "))
if cm < 0:
    print("invalid entry")
else:
    print(cm / 2.54, "inches")