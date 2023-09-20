# 3. Write a program to demonstrate the use of instance and class/static variable.

# program demostrating use of class variable
class sample:
    var = 10 # this is a class variable
    # this is class method
    # using built-in decorator @classmethod, to mark this method as class method
    
    @classmethod
    def new_modify(cls):
        cls.var += 1

s1 = sample()
s2 = sample()

print("X in s1 ", s1.var)
print("X in s2 ", s2.var)

# modify x in s1....showing use of class variable and method

s1.new_modify()
print("X in s1 ", s1.var)
print("X in s2 ", s2.var)

# ----------------------------------------------------------------------------- #
print("------------")

# program demostrating use of instance variable
class sample:
    def __init__(self):
        self.x = 10 # this is instance variable
        # this is instance method
    
    def modify(self):
        self.x+=1

s1 = sample()
s2 = sample()

print("X in s1 ", s1.x)
print("X in s2 ", s2.x)

# modify x in s1....showing use of instance variable and method

s1.modify()
print("X in s1 ", s1.x)
print("X in s2 ", s2.x)
