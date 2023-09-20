# 13. Write a program to implement multiple inheritance using two base classes.

class Father:
    def height(self):
        print("Height is 6.0 foot")
class Mother:
    def complexion(self):
        print("Complexion is Fair")
class child(Father, Mother):
    pass
c = child()
print("Child inherited qualities :")
c.height()
c.complexion()
