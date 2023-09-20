# 15. Write a program to check the object type to know whether the method exists in the object or not.

class Dog:
    def bark(self):
        print("Bow Wow")
class Duck:
    def talk(self):
        print("Quack Quack")
class Human:
    def talk(self):
        print("Hello, Hi")

# this method accepts an object and calls talk() method
def call_talk(obj):
    if hasattr(obj, "talk"):
        obj.talk()
    elif hasattr(obj, "bark"):
        obj.bark()
    else:
        print("Wrong object passed")

x = Duck()
call_talk(x)
x = Human()
call_talk(x)
x = Dog()
call_talk(x)
