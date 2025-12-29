l = [3, 5, 7, 9]


index = 0
for item in l:
    print(f"Then item number at index {index} is {item}")
    index +=1


for  index, item in enumerate(l):
    print(f"Then item number at index {index} is {item}")
# The enumerate function is a built-in function in Python that adds a counter to an iterable and returns it in the form of an enumerate object.