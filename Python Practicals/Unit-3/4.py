# 4. Write a program to store data into instance using mutator methods and to retrieve data from the instances using accessor methods.

class student:
    #mutator method
    def setname(self, name):
        self.name = name
    
    #accessor method
    def getname(self):
        return self.name
    
    #mutator method
    def setmarks(self, marks):
        self.marks = marks

    #accessor method
    def getmarks(self):
        return self.marks
    
n = int(input("how many students ? "))
i=0
while(i<n):
    s = student()
    name = input("Enter name : ")
    s.setname(name)
    marks = int(input("Enter marks : "))
    s.setmarks(marks)
    print("HI ", s.getname())
    print("Your Marks :", s.getmarks())
    i+=1
    print("-----------------------------------------------")