# 3. Write a program to understand various methods of array class mentioned: append, insert, remove, pop, index, tolist and count.

list1 = [1, 2, 3, 4, 5, 6, 7]
list1.append(10)
print(list1)

list1.remove(2)
print(list1)

list1.pop()
print(list1)

print(list1.index(3))
print(list1.count(4))

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.tolist())