# 5. Write a program to use class method to handle the common features of all the instance of Student class.

class student:
    marks = 10
    @classmethod
    def modify(cls, name):
        print(" {} scored {} marks".format(name, cls.marks))
student.modify("Mihir")
student.modify("Jack")