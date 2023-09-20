# 1. Write a program to handle some built in exceptions like ZeroDivisionError.

a = int(input("Enter a dividend : "))
b = int(input("Enter a divisor : "))
try:
    Ans = a/b
except ZeroDivisionError:
    print("zero division error")
else:
    print("Answer = ", Ans)