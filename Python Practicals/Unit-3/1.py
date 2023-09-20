# 1. Write a program to create a Student class with name, age and marks as data members. Also create a method named display() to view the student details. Create an object to Student class and call the method using the object.

class student:
    def __init__(self):
        self.name = "Mihir"
        self.age = 19
        self.marks = 93

# instance method

    def display(self):
        print("Name :",self.name)
        print("Age :",self.age)
        print("Marks :",self.marks)

s = student() # Creating an object(or instance) to student class
s.display() # call to display() method
