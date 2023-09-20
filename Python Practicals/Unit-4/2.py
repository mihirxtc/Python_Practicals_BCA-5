# 2. Write a program to handle multiple exceptions like SyntaxError and TypeError

try:
    a = eval(input("Enter a dividend : "))
    b = eval(input("Enter a divisor : "))
    Ans = a/b
except  (TypeError, SyntaxError):
    print("Error")
else:
    print("Answer = ", Ans)