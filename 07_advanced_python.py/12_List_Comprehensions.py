mylist = [1, 2, 9, 5, 3, 5]


squaredlist = []
for item in mylist:
    squaredlist.append(item**2)

print(squaredlist)

#  The same task can be done using list comprehension, which is a more concise way to create lists in Python.

squaredlist2 = [item**2 for item in mylist]
print(squaredlist2)