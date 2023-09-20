# 11. Write a program to search an element in the list using for loop and also demonstrate the use of "else" with for loop.

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            return True
            return False

list = [1, 2, "Mihir", 4, "Python", 6]

n = "Mihir"
if search(list, n):
    print("Found")
else:
    print("Not Found")