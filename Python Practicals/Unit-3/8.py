# 8. Write a program to create a Emp class and make all the members of the Emp class available to another class(Myclass). [By passing members of one class to another]

class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.salary = sal
    
    def display(self):
        print("Id = ", self.id)
        print("Name = ", self.name)
        print("Salary = ", self.salary)

class myclass:
    @staticmethod
    def mymethod(e):
        e.salary += 1000 # incrementing salary by 1000
        e.display()
    
e = Emp(1001, "Jack Smith", 12000.75)
myclass.mymethod(e)