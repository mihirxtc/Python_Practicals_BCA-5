# 12. Create a python function to accept python function as a dictionary and display its elements.

def func(d):
    for key in d:
        print("key:", key, "Value:", d[key])
D = {'a':1, 'b':2, 'c':3}
func(D)