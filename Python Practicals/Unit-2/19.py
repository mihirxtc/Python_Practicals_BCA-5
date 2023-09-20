# 19. Create a program to sort tuple with nested tuples.

tup = [(1, (2, 3)), (3, (2, 1)), (2, (2, 1))]
sort_tup = sorted(tup, key=lambda t: (t[1][1], t[0]))
print(sort_tup)
