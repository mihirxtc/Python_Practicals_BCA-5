# 3. Write a program to import "os" module and to print the current working directory and return a list of all module functions.

import os
# Return the absolute path
print(os.getcwd())

# Return the list of functions of OS
print(dir(os))