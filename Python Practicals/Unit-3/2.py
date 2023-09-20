# 2. Write a program to create Student class with a constructor having more than one parameter.

class student:
    def __init__(self, nm='.', ag=15, m=0):
        self.name = nm
        self.age = ag
        self.marks = m

# instance method
    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Marks :",self.marks)

s = student("Nisha",18,46) # Creating an object(or instance) to student class
s.display() # call to display() method
s1 = student("Sharma") # here it will take default values
s1.display()