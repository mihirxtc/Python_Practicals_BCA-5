# 16. Create a sample list of 7 elements and implement the List methods mentioned: append, insert, copy, extend, count, remove, pop, sort, reverse and clear.

# Creating list
list1 = [ i for i in range(1, 8)]
print(list1)

# Append
list1.append(8)
print(list1)

# Insert
list1.insert(2, 12)
print(list1)

# Copy
list2 = list1.copy()
print(list2)

# Extend
another_list = ['A', 'B', 'C']
list1.extend(another_list)
print(list1)

# Count
print(list1.count(3))

# Remove
list1.remove('C')
print(list1)

# pop
print(list1.pop())

# Sort
list2 = [4, 8, 3, 4, 6, 5, 68, 33, 46, 5, 0]
list2.sort()
print(list2)

# Reverse
list1.reverse()
print(list1)

# Clear
list2.clear()
print(list2)
