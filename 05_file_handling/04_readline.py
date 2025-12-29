g = open("myfile.txt")

line1 = g.readline()
print(line1, type(line1))

line2 = g.readline()
print(line2, type(line2))

line3 = g.readline()
print(line3, type(line3))

# since there is no 3rd line exists therefore 
# nothing will print without throwing error.

g.close