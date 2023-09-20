# 9. Write a program to demonstrate the use of Positional argument, keyword argument and default arguments.

# Positional arguments
def positional(Mihir, Harshil, Nishant):
    print(Mihir, Harshil, Nishant)

a = 'Mihir'
b = 'Harshil'
c = 'Nishant'

positional(a,b,c)

# Keyword Arguments
def keyword(Mihir, Harshil, Nishant):
    print(Mihir, Harshil, Nishant)

a = 'Mihir'
b = 'Harshil'
c = 'Nishant'

keyword(Mihir=a, Nishant=c, Harshil=b)

# Default argument
def keyword(Mihir, Harshil, Nishant = 'Nishant'):
    print(Mihir, Harshil, Nishant)

a = 'Mihir'
b = 'Harshil'
keyword(Mihir = a, Harshil = b)